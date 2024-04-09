from conexionBD import conexionBD
import pymysql

def insertarComponentes(nombreComponente,caracteristicas,precioUnitario,cantidad,imagen,tipo):
    conexion = conexionBD()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO componentes (nombreComponente,caracteristicas,precioUnitario,cantidad,imagen,tipo) VALUES (%s,%s,%s,%s,%s,%s)', (nombreComponente,caracteristicas, precioUnitario,cantidad,imagen,tipo))
    conexion.commit()
    conexion.close()


def obtenerComponentes():
    conexion = conexionBD()
    with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT idcomponente,nombreComponente,caracteristicas,precioUnitario,cantidad,imagen,tipo FROM componentes")
        componentes = cursor.fetchall()
    conexion.close()
    return componentes

def obteneridcomponente(idcomponente):
    conexion = conexionBD()
    with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT idcomponente,nombreComponente,caracteristicas,precioUnitario,cantidad,imagen,tipo FROM componentes WHERE idcomponente=%s", (idcomponente))
        componente = cursor.fetchone()
    conexion.close()
    return componente

def editarComponente(idcomponente,nombreComponente,caracteristicas,precioUnitario,cantidad,imagen,tipo):
    conexion = conexionBD()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE componentes SET nombreComponente=%s,caracteristicas=%s,precioUnitario=%s,cantidad=%s,imagen=%s,tipo=%s WHERE idcomponente=%s",(nombreComponente,caracteristicas,precioUnitario,cantidad,imagen,tipo,idcomponente))
    conexion.commit()
    conexion.close()

def eliminarComponente(idcomponente):
    conexion = conexionBD()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM componentes WHERE idcomponente=%s",(idcomponente))
    conexion.commit()
    conexion.close()
