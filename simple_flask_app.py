from flask import Flask

# This code says that flask app exist in this particular file(inbuilt variable __name__ which stores the name of the current module)
app = Flask(__name__)

# hello is going to be the endpoint and we will only use it for GET requests
# When a user visits /hello, the hello function will be executed (Whenever this endpoint is hit, this function will run)
@app.route("/hello", methods=["GET"])
def hello():
    return "Welcome to this Flask app!"

# whenever we click on run button, please run the app in debug mode
if __name__=="__main__":
    app.run(debug=True)

# Type python simple_flask_app.py to run the app