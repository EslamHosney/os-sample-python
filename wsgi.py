from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    #Islam start
    #input ("Enter any char")
    #while True:
    #    print ("Print to Screen Islam Awesome")
    #Islam Stop
    return "Hello World Eslam Added!"

if __name__ == "__main__":
    application.run()
