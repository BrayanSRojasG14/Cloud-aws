import pymysql
from keys import PUNTO_K, USER_K, PASS_K, DB_K
#intenta conectarse a la base de datos

def connectionsql():
    try:
        obj_connect = pymysql.connect(
            host=PUNTO_K,
            user=USER_K,
            password=PASS_K,
            database=DB_K
        )
        print("Conexion satisfactoria a la base de datos")
        return obj_connect
    #para generar el error en caso de que no se conecte a la base de datos
    except Exception as err:
        print("Error ", err)
        obj_connect = None

def add_user(ID, NAME_USER, LAST_NAME, BIRTHDAY, ACT_LABORAL):
    try:
        instruction_sql = "INSERT INTO users (ID, NAME_USER, LAST_NAME, BIRTHDAY, ACT_LABORAL) values ("+ID+", '"+NAME_USER+"', '"+LAST_NAME+"', '"+BIRTHDAY+"', '"+ACT_LABORAL+"')"
        obj_connect = connectionsql()
        obj_connect.cursor().execute(instruction_sql)
        obj_connect.commit()
        print("El usuario fue añadido")
        return True
    except Exception as err:
        print("Error", err)
        return False
    
def consult(id):
    try:
        instruction = "SELECT * FROM users WHERE id=" + id
        connection = connectionsql()
        cursor = connection.cursor()    
        cursor.execute(instruction)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print("Error", err)
        return None