from flask import Flask, render_template, request, flash, session
from db_routines import DbRoutines
from tables import Credentials, Persons, Game_System, Mini_Collection
from werkzeug.security import generate_password_hash, check_password_hash


#############################################################
# TODO: Make server production grade using 'waitress'       #
# TODO: Add user session control                            #
# TODO: Add full reklationship functionality                #
# TODO: Implelemnt U and D aspects of CRUD                  #
# TODO: Refactor code to break content down into logical    #
# files - eg have an init file, etc...                      #
# TODO: Make pretty                                         #
#############################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dlkhsdfhfsdf'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

is_registed_user = False


@app.route('/')
def index():
#    if 'username' in session:
#        return 'Hey, {}!'.format(escape(session['username']))  
    return render_template("login.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
#    if request.method == 'POST':
#        session['username'] = request.form['uname']
#        return render_template('index.html')
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



@app.route('/verify', methods=['POST', 'GET'])
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
@app.route('/systems', methods=['POST', 'GET'])
def systems():
    if request.method == 'POST':
        if request.method == 'GET':
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute("SELECT * FROM `Game_System`")
            rows = cursor.fetchall()
            table = Game_System(rows)
            cursor.close() 
            return render_template('main.html', table = table)
        if request.form['company'] != "" and request.form['game_system'] != "" and request.form['game_faction'] != "" and request.form['project_name'] != "":
            company = request.form['company']
            game_system = request.form['game_system']
            game_faction = request.form['game_faction']
            project_name = request.form['project_name']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Game_System` WHERE Project_Name = '{project_name}';")
            
            project_list = cursor.fetchall()
            if project_list[0]['COUNT(*)'] > 0:                     
                cursor.close()
                return render_template("message.html", message=f"A Project called '{project_name}' already exists.")
            else:    
                cursor = dbRoutines.mysql.connection.cursor()
                cursor.execute(f"use webapp_db;")
                '''
                ////                                                                                                     Start hacky code                                                                                        ////
                hacky method to get the CredID and SystemID to populate into the Mini_Collection table when adding content.. I'm certain theirs a better way, but I have no idea what it is for now and lack time to really research....
                                                                        THIS IS NOT PRODUCTION READY CODE PLEASE INVESTIGATE A BETTER AND MORE SECURE WAY TO DO THIS USING USER SESSIONS ETC 
                                                                                                                     Turns out this doesnt work. 

                ////                                                                                                                                                                                                             ////
                cursor.execute(f"SELECT (credId) FROM `Credentials`;")
                credId = cursor.fetchone()                                                                                                                       //// end hack ////
                '''
                cursor.execute (f"INSERT INTO `Game_System` (`Company`, `Game_System`, `Game_Faction`, `Project_Name`) VALUES ('{company}', '{game_system}', '{game_faction}', '{project_name}');")
                dbRoutines.mysql.connection.commit()                                            
                cursor.close()          
                return render_template("systems.html")

    return render_template("systems.html")            

@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        cursor = dbRoutines.mysql.connection.cursor()
        cursor.execute(f"use webapp_db;")
        cursor.execute("SELECT * FROM `Mini_Collection`")
        rows = cursor.fetchall()
        table = Mini_Collection(rows)
        cursor.close() 
        return render_template('main.html', table = table)
    if request.method == 'POST':
        if request.form['mininame'] != "" and request.form['minitype'] != "" and request.form['mininum'] != "":
            mininame = request.form['mininame']
            minitype = request.form['minitype']
            mininum = request.form['mininum']
            minipoint = request.form['minipoint']
            minicost = request.form['minicost']
            '''
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            ////                                                                                                     Start hacky code                                                                                        ////
            hacky method to get the CredID and SystemID to populate into the Mini_Collection table when adding content.. I'm certain theirs a better way, but I have no idea what it is for now and lack time to really research....
                                                                THIS IS NOT PRODUCTION READY CODE PLEASE INVESTIGATE A BETTER AND MORE SECURE WAY TO DO THIS USING USER SESSIONS ETC 
                                                                                                                  Turns out this doesnt work. 
            ////                                                                                                                                                                                                             ////
            cursor.execute(f"SELECT (credId) FROM `Credentials`;")
            cursor.execute(f"SELECT (SystemID) FROM `Game_System`;")
            cred = cursor.fetchone()
            system = cursor.fetchone()                                                                                                                   //// end hack ////
            '''
            cursor.execute (f"INSERT INTO `Mini_Collection` (`MiniName`, `MiniType`, `MiniNum`, `MiniPoint`, `MiniCost`) VALUES ('{mininame}', '{minitype}', '{mininum}', '{minipoint}', '{minicost}');")
            dbRoutines.mysql.connection.commit()                                            
            cursor.close()          
            return render_template("main.html")
    return render_template("main.html")    

#User account settings changed here. 
@app.route('/account', methods=['POST', 'GET'])
def account():
    if request.method == 'GET':
        cursor = dbRoutines.mysql.connection.cursor()
        cursor.execute(f"use webapp_db;")
        cursor.execute("SELECT `username` FROM `Credentials` WHERE 1;")
        output = cursor.fetchone()
        cursor.close() 
        return render_template('account.html', data = output)

    if request.form['pwd'] != "" and request.form['repwd'] != "" and request.form['pwd'] == request.form['repwd']:
        userName = request.form['uname']
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
    return render_template("account.html")


@app.route('update', methods=['POST', 'GET'])
def update():
    pass

@app.route('delete', methods=['POST', 'GET'])
def delete():
    pass


@app.route('/logout')    
def logout():
#    session.pop('uname')
    return render_template('login.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)