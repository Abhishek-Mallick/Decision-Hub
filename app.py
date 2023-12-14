import google.generativeai as palm
import time
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for, session
from flask import Flask

app = Flask(__name__)
app.secret_key = 'MYSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

palm.configure(api_key='AIzaSyB5v4JcdsO0gLlgPhSkPD6CZYefcWY7aHk')


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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        # email = request.form['email']
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

@app.route('/texttoquery.html', methods=['GET', 'POST'])
def texttoquery():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            username = user.username
            solution = None
            if request.method == 'POST':
                user_prompt = request.form.get('user_text')
                solution = generate_solution(user_prompt)
            return render_template('texttoquery.html',solution=solution,username=username)

    return redirect(url_for('login'))

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None) 
    return redirect(url_for('index'))  

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)