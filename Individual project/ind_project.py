from flask import session as login_session 
from flask import Flask, render_template, request, redirect, url_for  
import pyrebase 
app = Flask(__name__, template_folder='templates', static_folder='static') 
app.config['SECRET_KEY'] = 'super-secret-key' 

firebaseConfig = {
  "apiKey": "AIzaSyCPesWVPC9JaQpLJt5UJd9shGbDOu2cAg4",
  'authDomain': "indproject-bcc4b.firebaseapp.com",
  'databaseURL': "https://indproject-bcc4b-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "indproject-bcc4b",
  'storageBucket': "indproject-bcc4b.appspot.com",
  'messagingSenderId': "793372088189",
  'appId': "1:793372088189:web:e886d5d088c8741ffe1e14",
  'measurementId': "G-XBEW0Y2DFZ"
} 


firebase = pyrebase.initialize_app(firebaseConfig)  
auth = firebase.auth()  
db =firebase.database() 


@app.route ("/", methods = ['GET', 'POST']) 
def signup (): 
  if request.method == "POST" :  
    email = request.form['email'] 
    full_name = request.form ['full_name'] 
    username = request.form ['username']
    password = request.form['password'] 
    login_session['user'] = auth.create_user_with_email_and_password(email, password) 
    user = {"full_name" : full_name, "email" : email, "username" : username}    
    UID = login_session['user']['localId']
    db.child("Users").child(UID).set(user)   
    return(redirect(url_for('home')))  
  return render_template("signup.html") 

@app.route ("/signin", methods = ['GET', 'POST'])  
def signin (): 
  if request.method == "POST" :  
    email = request.form['email'] 
    password = request.form['password']  
    
    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('home')) 
    except:
      error = "Authentication failed"
      return redirect("/error")
  else: 
    return render_template("signin.html") 


@app.route ("/signout", methods = ['GET', 'POST'])
def signout (): 
    print(login_session ['user'])  
    login_session['user'] = None 
    print(login_session ['user']) 
    return (redirect(url_for("signin")))  


@app.route("/home", methods = ['GET', 'POST']) 
def home(): 
  if request.method == 'POST':  
    return redirect(url_for('thanks')) 
  UID = login_session['user']['localId']
  print(UID)
  print(db.child("Users").child(UID).get().val())
  username = db.child("Users").child(UID).get().val()["username"]
  return render_template('home.html', username = username)  



@app.route("/history")  
def history():   
  return render_template('history.html')  


@app.route("/modernatt")  
def modernatt():   
  return render_template('modernatt.html')  


@app.route("/archit")  
def archit():   
  return render_template('archit.html')  

@app.route("/old_city")  
def old_city():   
  return render_template('old_city.html')  

@app.route("/mooli")  
def mooli():   
  return render_template('mooli.html')  


@app.route("/review" , methods = ['GET', 'POST'])   
def review():  
  if request.method == 'POST':  
    rating = request.form['rating']
    review = request.form['review']
    feedback = {"rating": rating, "review": review } 
    db.child("reviews").push(feedback)   
  return render_template('old_city.html')  



@app.route("/malls")  
def malls():   
  return render_template('malls.html')  

@app.route("/jast")  
def jast():   
  return render_template('jast.html')  


@app.route("/cityc")  
def cityc():   
  return render_template('cityc.html') 


@app.route("/mus")  
def mus():   
  return render_template('mus.html')  

@app.route("/holy")  
def holy():   
  return render_template('holy.html')  


if __name__ == '__main__':
  app.run(debug=True) 