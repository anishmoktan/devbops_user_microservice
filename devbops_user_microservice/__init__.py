from flask import Flask, request
from devbops_user_microservice.user_functions import Users
#from user_functions import Users
user = Users()
app = Flask(__name__)


@app.route('/register', methods=['POST'])
def signup():
    res = request.json
    username = res["Username"]
    password = res["Password"]
    email = res["Email"]

    firstname = res["FirstName"]
    lastname = res["LastName"]
    currentcity = res["City"]
    currentcountry = res["Country"]

    reg = user.verification(username=username, currentcity=currentcity, currentcountry=currentcountry, email=email, firstname=firstname, lastname=lastname,
                                                   password=password)
    return reg


@app.route("/login", methods=['POST'])
def login():
    res = request.json
    username = res["Username"]
    password = res["Password"]
    r = user.authincate_user(user=username, password=password)
    # return dict{}
    return r


@app.route("/delete", methods=['POST'])
def delete():
    res = request.json
    username = res["Username"]
    deleted = user.delete_account(username=username)
    return deleted



# @app.route("/update-pw", methods=['POST'])
# def updated_pw():
#     res = request.json
#     username = res["Username"]
#     password = res["Password"]
#     updated = user.update_user_pw(user=username,password=password)
#     return updated


@app.route("/update-user-info", methods=["POST"])
def update_info():
    res = request.json
    username = res["Username"]
    firstname = res["FirstName"]
    lastname = res["LastName"]
    currentcity = res["City"]
    currentcountry = res["Country"]
    password = res['Password']
    email = res['Email']
    updated_user = user.update_user(user=username, currentcity=currentcity, currentcountry=currentcountry, firstname=firstname, lastname=lastname, password=password, email=email)
    return updated_user



if __name__ == "__main__":
    app.run(debug=True)
