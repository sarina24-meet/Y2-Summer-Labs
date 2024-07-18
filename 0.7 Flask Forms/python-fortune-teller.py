from flask import Flask, render_template, request, redirect, url_for 
import random   
app = Flask(__name__, template_folder = "templates") 
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
 








if __name__ == '__main__':
    app.run(debug=True)
