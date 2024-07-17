from flask import Flask, render_template
import random   
app = Flask(__name__, template_folder = "templates") 
@app.route ("/home")  
def home (): 
	return render_template("home.html") 

@app.route ("/fortune") 
def fortune (): 
	 possible_fortunes = ["You will get outstanding IN CS" , 
	 "You are sentenced to IASA food FOR life", "You will catch Lilach the dragon" , 
	 "You will be the best entrepreneurship instructor" , 
	 "You will get the best meet laptop", "You are the NEXT Y3 lead", 
	 "You will become a president one day", "You will own the biggest company", 
	 "You will strart a non-profit organization and help save the world by planting trees", 
	 "You will have no wifi connection"]     
	 random_number = random.randint(0,9) 
	 return render_template("fortune.html", fortune = possible_fortunes[random_number])   





if __name__== '__main__': 
	app.run(debug=True) 



