from aplicacion import app
from flask_mysqldb import MySQL
from MySQLdb.cursors import Cursor

app.config['MYSQL_HOST'] = 'containers-us-west-84.railway.app'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'C5KyMhGevnpyxrgJKdOl'
app.config['MYSQL_DB'] = 'railway'
app.config['MYSQL_PORT'] = 7103

mysql = MySQL(app)

def execute(sql:str) -> Cursor:
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    return cursor

def commit() -> None:
    mysql.connection.commit()
