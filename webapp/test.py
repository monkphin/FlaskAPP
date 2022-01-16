from flask import Flask, render_template, request
from db_routines import DbRoutines

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

cursor = dbRoutines.mysql.connection.cursor()
cursor.execute(f"INSERT INTO `Credentials` (`username`, `userpwd`) VALUES ('siamak','siamak');")
cursor.close()
