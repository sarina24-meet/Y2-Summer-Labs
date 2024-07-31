from flask import session as login_session 
from flask import Flask, render_template, request, redirect, url_for  
import pyrebase 
app = Flask(__name__, template_folder='templates', static_folder='static') 
app.config['SECRET_KEY'] = 'super-secret-key' 


firebaseConfig= {
  "apiKey": "AIzaSyBVGDLCuYYRNVlyZYz_NTJqCN8qrujwTwQ",
  "authDomain": "authlab-79d93.firebaseapp.com",
  "projectId": "authlab-79d93", 
  "storageBucket": "authlab-79d93.appspot.com",
  "messagingSenderId": "1078110054181",
  "appId": "1:1078110054181:web:54f9a6eec87bebf79fdccc",
  "measurementId": "G-60K4ZHGVYB", 
  "databaseURL":"https://indproject-bcc4b-default-rtdb.europe-west1.firebasedatabase.app/"  
}  

firebase = pyrebase.initialize_app(firebaseConfig)  
auth = firebase.auth()  
db =firebase.database() 



@app.route ("/", methods = ['GET', 'POST']) 
@app.route ("/signup", methods = ['GET', 'POST']) 
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
    #quote_text=request.form['quote_text'] 
    #said_by = request.form['said_by'] 
    quote = {"said_by": request.form['said_by'], "quote" : request.form['quote_text'], "UID" : login_session['user']['localId']}     
    login_session.modified = True 
    db.child("Quotes").push(quote) 
    # print(login_session ['quotes']) 
    return redirect(url_for('thanks')) 
  return render_template('home.html') 


@app.route("/thanks")  
def thanks(): 
  return render_template('thanks.html')  
 

@app.route ("/display") 
def display (): 
  quotes = db.child("Quotes").get().val()   
  return render_template('display.html', quotes = quotes)  


@app.route("/error")  
def error():        
  return render_template("error.html") 














if __name__ == '__main__':
  app.run(debug=True) 