#Use following command to run the project
# flask --app main run
# main is the file name
# It is better to rename the file "app.py"/ "wsgi.py" then you need to run following command
# flask run

# to run debigging mode use following command, it will also enable auto reload on change detection
# flask run --debug

from flask import Flask, request

app = Flask(__name__) #"__name__" is the name of file which is currently "app.py"

@app.route("/")
def index_page():
    return "<h3>Welcome! to dashboard.</h3>"

# end slash is good for urls, if not added then localhost/about/ will not work
# and you need to remove last slash
@app.route("/about/")
def about_page():
    return "<h3>About page.</h3>"


# taking paramters from urls
# parameter type are string, int, float, path, uuid
@app.route("/hello/<string:name>")
def hello_page(name):
    return f"<h3>Hello {name}.</h3>"

# post request
@app.route("/post1/", methods=["POST"])
def post1():
    return "<h3>Post1 success</h3>"


# multiple method types
@app.route("/user/", methods=["GET", "POST", "PUT", "DELETE"])
def user():
    if request.method == "GET":
        return "<h3>Get request called.</h3>"
    elif request.method == "POST":
        return "<h3>Post request called.</h3>"
    elif request.method == "PUT":
        return "<h3>PUT request called.</h3>"
    else:
        return "<h3>Delete request called.</h3>"
