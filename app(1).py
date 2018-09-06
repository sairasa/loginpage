from flask import Flask,render_template,redirect,url_for,request
#create the application object
app = Flask(__name__)

@app.route("/")
def home():
	return "  KEEP CALM AND CODE ON!!!"	#home page
@app.route('/welcome')				#welcome page
def welcome():
	return render_template('welcome.html')
		

@app.route('/login',methods=['GET','POST'])	#login page
def login():
	error=None
	if request.method=='POST':
		if request.form['username']!='user' or  request.form['password']!='user':
			error="Invalid credentials.Please try again."
		else:
			return redirect(url_for('welcome'))
	return render_template('login.html',error=error)	

if __name__ == '__main__':
	app.run(debug=True)
