# Every data is retrieved from the request object and every data is represenetd in JSON format
from flask import Flask, request, jsonify

# This code says that flask app exist in this particular file(inbuilt variable __name__ which stores the name of the current module)
app = Flask(__name__)

# greet is going to be the endpoint and we will only use it for GET & POST requests
# When a user visits /greet, the greet function will be executed (Whenever this endpoint is hit, this function will run)
@app.route("/greet", methods=["GET","POST"])
def greet():
    # I will do some processing or transformation on the data
    # First thing inside a post unction is to get the data from the user and convert it to json format
    if request.method == "GET":
        name = request.args.get("name","user")
        age = request.args.get("age",15)
    else:
        data = request.json
        name = data.get("name","user")
        age = data.get("age",15)

    # Now I will create a response message (Some Transformation/Processing)
    res = f"Hello, {name}! You are {age} years old."
    # Finally I will return the response in JSON format
    return jsonify({"message":res})

# whenever we click on run button, please run the app in debug mode
if __name__=="__main__":
    app.run(debug=True)

# Type python simple_flask_app2.py to run the app