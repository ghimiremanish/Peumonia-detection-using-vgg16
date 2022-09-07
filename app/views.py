from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def home():
   #HANDLE POST REQ
   if request.method == 'POST':
      return "piost"
   else:
      return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')