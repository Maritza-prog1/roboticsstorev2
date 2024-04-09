from conexionBD import conexionBD
import pymysql

def insertarUsuario(nomUser,password,privilegios):
    conexion = conexionBD()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO usuario (nomUser,password,privilegios) VALUES (%s,%s,%s)', (nomUser,password, privilegios))
    conexion.commit()
    conexion.close()

def obtenerUsuario():
    conexion = conexionBD()

    with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT idUser, nomUser, password,privilegios FROM usuario")
        cs = cursor.fetchall()
    conexion.close()
    return cs

def eliminarUsuario(idUser):
    conexion = conexionBD()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE idUser=%s",(idUser))
    conexion.commit()
    conexion.close()

def obteneridUser(idUser):
    conexion = conexionBD()
    with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT idUser, nomUser, password, privilegios FROM usuario WHERE idUser=%s", (idUser))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def editarUser(idUser,nomUser,password,privilegios):
    conexion = conexionBD()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET nomUser=%s,password=%s,privilegios=%s WHERE idUser=%s",(nomUser,password,privilegios,idUser))
    conexion.commit()
    conexion.close()

