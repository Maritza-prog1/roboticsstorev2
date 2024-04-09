import pymysql

def conexionBD():
    return pymysql.connect(host='localhost', user='root',password='', db='roboticsstore')
    
