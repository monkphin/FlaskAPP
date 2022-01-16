from flask import Flask, render_template, request, flash
from db_routines import DbRoutines

########################################################
# TODO: Make server production grade using 'waitress'  #
########################################################

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

is_registed_user = False

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "" and request.form['repwd'] != "" and request.form['pwd'] == request.form['repwd']:
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE username = '{userName}' AND userpwd = '{userPwd}';")
        
            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:                     
                cursor.close()
                return render_template("message.html", message=f"User '{userName}' already registed.")
            else:
                cursor.execute(f"INSERT INTO `Credentials` (`username`, `userpwd`) VALUES ('{userName}','{userPwd}');")
                dbRoutines.mysql.connection.commit()
                cursor.close()
                return render_template("login.html")
        else:
            return render_template("message.html", message="Invalid input.")


    return render_template("register.html")



@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "":
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE username = '{userName}' AND userpwd = '{userPwd}';")
        
            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:                     
                cursor.close()
                return render_template("main.html")
    return render_template("login.html")


#Main page for the site - core functionality of app is here split over two frames - systems and minis, sysmes being where the game system data is, minis being where the collection data is. 
@app.route('/systems', methods=['POST'])
def systems():
    if request.method == 'POST':
        if request.form['company'] != "" and request.form['game_system'] != "" and request.form['game_faction'] != "" and request.form['project_name'] != "":
            company = request.form['company']
            game_system = request.form['game_system']
            game_faction = request.form['game_faction']
            project_name = request.form['project_name']
            mininame = request.form['mininame']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute (f"INSERT INTO `Game_System` (`Company`, `Game_System`, `Game_Faction`, `Project_Name`) VALUES ('{company}', '{game_system}', '{game_faction}', '{project_name}');")
            dbRoutines.mysql.connection.commit()                                            
            cursor.close()          
            return render_template("systems.html")

@app.route('/minis', methods=['POST'])
def main():
    if request.method == 'POST':
        if request.form['mininame'] != "" and request.form['mininum'] != "":
            mininum = request.form['mininum']
            minipoint = request.form['minipoint']
            minicost = request.form['minicost']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute (f"INSERT INTO `Mini_Collection` (`MiniName`, `MiniNum`, `MiniPoint`, `MiniCost`) VALUES ('{mininame}', '{mininum}', '{minipoint}', '{minicost}');")
            dbRoutines.mysql.connection.commit()                                            
            cursor.close()          
            return render_template("main.html")

'''

#User account settings changed here. 
@app.route('/account')
def account():
    if request.method == 'POST':
        if request.form['pwd'] != "" and request.form['repwd'] != "" and request.form['pwd'] == request.form['repwd']:
            userPwd = request.form['pwd']
            lastname = request.form['lastname']
            firstname = request.form['firstname']
            email = request.form['email']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute (f"INSERT INTO `Persons` (`LastName`, `FirstName`, `email`) VALUES ('{lastname}', '{firstname}', '{email}')")
            dbRoutines.mysql.connection.commit()                                            
            cursor.close()
            return render_template("account.html")
        else:    
            return render_template("account.html")

'''

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)