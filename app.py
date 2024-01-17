import google.generativeai as palm
import time
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for, session
from flask import Flask
import os
import sqlite3
import dotenv
from model import LLM

app = Flask(__name__)
app.secret_key = 'MYSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)
dotenv.load_dotenv()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()
        


def generate_solution(prompt):
    completion = LLM.generate_text(
        model=model,
        prompt="You are an expert at Converting the normal plain english text to Query Language.Here i will be sending a plain text convert it and provide the query statemnts only and no extra quotes:"+prompt,
        temperature= 0.4,
        candidate_count=1,
        top_k= 40,
        top_p= 0.95,
        max_output_tokens= 1024
    )
    
    result = completion.result
    
    return result

def generate_excel(prompt):
    completion = LLM.generate_text(
        model=model,
        prompt="You are an expert at Converting the normal plain english text to Excel function.Here i will be sending a plain text convert it and just show the excel function and no extra quotes for :"+prompt,
        temperature= 0.4,
        candidate_count=1,
        top_k= 40,
        top_p= 0.95,
        max_output_tokens= 1024
    )
    
    result = completion.result
    
    return result

def execute_query(database_file, query):
    query_results = None 
    try:
      
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

   
        cursor.execute(query)

 
        if query.strip().lower().startswith('select'):
            query_results = cursor.fetchall()
        else:
            query_results = "Query executed successfully."

    except sqlite3.Error as e:
        query_results = f"Error executing the query: {e}"

    finally:
      
        if connection:
            connection.close()

    return query_results


def get_table_schema(database_file):
    table_schema = {}
    try:
    
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

      
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            table_schema[table_name] = [{'name': column[1], 'type': column[2]} for column in columns]

    except sqlite3.Error as e:
        return f"Error fetching table schema: {e}"

    finally:
       
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
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        username = user.username
        return render_template('dashboard.html',username=username)
    return render_template('index.html')

@app.route('/querybuilder')
def querybuilder():
    username = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        username = user.username
        return render_template('querybuilder.html',username=username)
    return render_template('index.html')

@app.route('/Visualizer')
def Visualizer():
    username = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        username = user.username
        return render_template('Visualizer.html',username=username)
    return render_template('index.html')

@app.route('/logictester')
def logictester():
    username = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        username = user.username
        return render_template('logictester.html',username=username)
    return render_template('index.html')

@app.route('/texttoquery', methods=['GET', 'POST'])
def texttoquery():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            query_results = None
            table_schema = None
            username = user.username
            solution = None
            if request.method == 'POST':
             
                uploaded_file = request.files['database_file']
                user_prompt = request.form.get('user_text')
                
           
                database_file_path = os.path.join('uploads', uploaded_file.filename)
                uploaded_file.save(database_file_path)
                
                
                solution = generate_solution(user_prompt)
                
                
                query_results = execute_query(database_file_path, solution)

                
                table_schema = get_table_schema(database_file_path)
                
                os.remove(database_file_path)
                
                
                
            return render_template('texttoquery.html',solution=solution,username=username,query_results=query_results,table_schema=table_schema)

    return redirect(url_for('login'))

@app.route('/texttoexcel',methods=['GET', 'POST'])
def texttoexcel():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            username = user.username
            excel_solution = None
            if request.method == 'POST':
                user_prompt = request.form.get('user_text') 
                excel_solution = generate_excel(user_prompt)
        return render_template('texttoexcel.html',username=username,excel_solution=excel_solution)
    return render_template('index.html')

@app.route('/termsandservice',methods=['GET', 'POST'])
def termsandservice():
    return render_template('terms-and-services.html')

@app.route('/about',methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/userhistory')
def userhistory():
    username = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        username = user.username
        return render_template('user-history.html',username=username)
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None) 
    return redirect(url_for('index'))  

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    create_tables()
    app.run(debug=True)