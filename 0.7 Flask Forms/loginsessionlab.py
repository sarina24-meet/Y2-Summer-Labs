from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session  
import random  
app = Flask(__name__, template_folder = "templates") 
app.config['SECRET_KEY'] = "Your_secret_string" 
@app.route ("/home", methods=['GET', 'POST'])   
def home (): 
	if request.method == 'GET':  
		return render_template("home.html") 
	else: 
		name = request.form['birthMN'] 
		return redirect(url_for('fortune', name=name))   

@app.route("/fortune/<name>")    
def fortune(name): 
	 possible_fortunes = ["You will get outstanding IN CS" , 
	 "You are sentenced to IASA food FOR life", "You will catch Lilach the dragon" , 
	 "You will be the best entrepreneurship instructor" , 
	 "You will get the best meet laptop", "You are the NEXT Y3 lead",  
	 "You will become a president one day", "You will own the biggest company in the world", 
	 "You will strart a non-profit organization and help save the world by planting trees", 
	 "You will have no wifi connection"]     
	 random_number = random.randint(0,9) 
	 index = len(name) 
	 if index > 10:
	 	return render_template("fortune.html", fortune = "Error, index number too high")   
	 else : 
	 	return render_template("fortune.html", fortune = possible_fortunes[index]) 


@app.route('/home') 
def home():
    if 'username' in session and 'birth_month' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/fortune')
def fortune():
    if 'username' in session and 'birth_month' in session:
        fortune = random.choice(fortunes)
        session['fortune'] = fortune
        return render_template('fortune.html', username=session['username'], fortune=fortune)
    return redirect(url_for('login')) 

# @app.route ("/name", methods = ['GET', 'POST']) 
# def name  : 
# 	if request.method == 'POST' 
# 	username = request.form['username'] 
#     if username == 'admin':
#           login_session['admin'] = True 
#        return redirect(url_for('home'))
#    return render_template("login.html") 



# @app.route ("/indecisive")
# def indecisive ():  
# 		indecisive_fortunes = ["You will get outstanding IN CS" , 
# 	 "You are sentenced to IASA food FOR life", "You will catch Lilach the dragon" , 
# 	 "You will be the best entrepreneurship instructor" , 
# 	 "You will get the best meet laptop", "You are the NEXT Y3 lead",  
# 	 "You will become a president one day", "You will own the biggest company in the world", 
# 	 "You will strart a non-profit organization and help save the world by planting trees", 
# 	 "You will have no wifi connection"] 
# 	  sample(random_number) = random.randint(0,9) 
 
# @app.route ("/design")
# def design (): 
# 	return '''<html> 
# 		<img src = "https://t3.ftcdn.net/jpg/01/09/07/98/360_F_109079871_OigjZSPKSyTu7ap2nD3no18RjkLIH4eV.jpg" width = "400"> 
# 		</html> ''' 








if __name__ == '__main__':
    app.run(debug=True)
