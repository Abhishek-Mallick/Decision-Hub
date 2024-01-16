import google.generativeai as palm
import time
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for, session
from flask import Flask
import os
import sqlite3
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'MYSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

palm.configure(api_key=os.getenv('API_KEY'))


models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]

model = models[0].name #chat-bison-001

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()
        


def generate_solution(prompt):
    completion = palm.generate_text(
        model=model,
        prompt="You are an expert at Converting the normal plain english text to Query Language.Here i will be sending a plain text convert it :"+prompt,
        temperature= 0.4,
        candidate_count=1,
        top_k= 40,
        top_p= 0.95,
        max_output_tokens= 1024
    )
    
    result = completion.result
    
    return result

def execute_query(database_file, query):
    query_results = None  # Initialize with a default value
    try:
        # Connect to the database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Execute the query
        cursor.execute(query)

        # Fetch the results if the query is a SELECT statement
        if query.strip().lower().startswith('select'):
            query_results = cursor.fetchall()
        else:
            query_results = "Query executed successfully."

    except sqlite3.Error as e:
        query_results = f"Error executing the query: {e}"

    finally:
        # Close the database connection
        if connection:
            connection.close()

    return query_results


def get_table_schema(database_file):
    table_schema = {}
    try:
        # Connect to the database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Get the table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Get the schema for each table
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            table_schema[table_name] = [{'name': column[1], 'type': column[2]} for column in columns]

    except sqlite3.Error as e:
        return f"Error fetching table schema: {e}"

    finally:
        # Close the database connection
        if connection:
            connection.close()

    return table_schema

@app.route('/',methods=['GET', 'POST'])
def index():
    username = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        username = user.username
    return render_template('index.html',username=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('texttoquery'))
    return render_template('login.html')

# @app.route('/texttoquery.html', methods=['GET', 'POST'])
# def texttoquery():
#     if 'user_id' in session:
#         user = User.query.get(session['user_id'])
#         if user:
#             query_results = None
#             table_schema = None
#             username = user.username
#             solution = None
#             if request.method == 'POST':
             
#                 uploaded_file = request.files['database_file']
#                 user_prompt = request.form.get('user_text')
                
#                 # Save the file to a temporary location
#                 database_file_path = os.path.join('uploads', uploaded_file.filename)
#                 uploaded_file.save(database_file_path)
                
                
#                 solution = generate_solution(user_prompt)
                
                
#                 query_results = execute_query(database_file_path, solution)

                
#                 table_schema = get_table_schema(database_file_path)
                
#                 # Remove the temporary file
#                 os.remove(database_file_path)
                
                
                
#             return render_template('texttoquery.html',solution=solution,username=username,query_results=query_results,table_schema=table_schema)

#     return redirect(url_for('login'))

@app.route('/texttoquery.html', methods=['GET', 'POST'])
def texttoquery():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            query_results = None
            table_schema = None
            username = user.username
            solution = None
            if request.method == 'POST':
                user_prompt = request.form.get('user_text')

                # Generate solution directly from the user prompt
                solution = generate_solution(user_prompt)

                # Execute query based on the generated solution
                # query_results = execute_query(solution)

                # Get table schema (if needed) based on the generated solution
                # table_schema = get_table_schema(solution)

            return render_template('texttoquery.html', solution=solution, username=username)

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None) 
    return redirect(url_for('index'))  

if __name__ == '__main__':
    # Create the 'uploads' folder if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    create_tables()
    app.run(debug=True)