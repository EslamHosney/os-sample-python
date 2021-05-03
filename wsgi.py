from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    #Islam start
    print ("Print to Screen Islam Awesome")
    #Islam Stop
    return "Hello World Eslam!"

if __name__ == "__main__":
    application.run()
