from flask import Flask, render_template, request, jsonify
from database.db import *
#from controllers.admin_s3 import *

app= Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/consult_page')
def consult_page():
    return render_template("consult.html")

@app.route('/registro', methods=['post'])
def registro():
    #get_files()
    print("error")
    data_user = request.form
    data_photo = request.files
    ID = data_user["ID"]
    NAME_USER = data_user["NAME_USER"]
    LAST_NAME = data_user["LAST_NAME"]
    BIRTHDAY = data_user["BIRTHDAY"]
    ACT_LABORAL = data_user["ACT_LABORAL"]
    #photo = data_photo["photo"]
    confirm = add_user(ID, NAME_USER, LAST_NAME, BIRTHDAY, ACT_LABORAL)
    print(confirm)
    return render_template("home.html")
    """if confirm:
        photo_path, photo_name = save_file(photo, ID)
        upload_file(photo_path, photo_name)
        return "Usuario añadido"
    else:
        return "Error creating the user"
"""

@app.route('/consult_user', methods=["post"])
def consult_user():
    id = request.get_json()
    print(id)
    result = consult(id)
    resp_data = {
        'NAME_USER':result[0][1],
        'LAST_NAME':result[0][2],
        'BIRTHDAY':result[0][3]
    }
    return jsonify(resp_data)

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = "5000"
    app.run(ip, port, debug=True)