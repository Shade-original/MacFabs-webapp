from flask import * #pip/3 install flask
import flask_login #pip/3 install flask-login
#from flask_sqlalchemy import SQLAlchemy #pip/3 install flask-sqlaclchemy

#initialising app
app = Flask(__name__)

#Activating virtual environment - source env/bin/activate
#1. home page
@app.route("/")
def index():
    return render_template("index.html")

#subpages of the wesite

#2. products or services render by the owners of the respective brands
@app.route("/Products&Services/")
def servprod():
    return render_template("ServProd.html")

#3. the event of the related brand
@app.route("/Events/")
def events():
    return render_template("Events.html")

#4. contact info for either the page owner or the owners of the respective brands
@app.route("/Contacts/")
def contacts():
    return render_template("Contacts.html")

#5. nebw and info related to the brand
@app.route("/Blog/")
def blog():
    return render_template("Blog.html")

#6. frequently asked question by page visitor and the brand related community
@app.route("/FAQ/")
def faq():
    return render_template("FAQ.html")

#Extras such as the easter eggs and login for the relative users
@app.route("/Games/")
def games():
    return render_template("Games.html")


@app.route("/Resources/")
def resources():
    return render_template("Resources.html")

@app.route("/Hi/")
def hi():
    return """
        Hello world<br>
        welcome to this beautiful site where 
        all your dreams come true.<br>
        You can return to the main page for <a href="/">here</a>
        """

@app.route("/AdLogin/")
def adlogin():
    return """<h2>Hello there fellow Admin</h2>
            <h3>Login</h3>
        <p color="blue"><i>This page is still under construction</i></p>
        Return to <a href="/">main page</a>
    """

if __name__ == "__main__":
    app.run(debug=True)