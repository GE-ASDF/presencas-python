import mysql.connector
from mysql.connector import errorcode

class connection:

    def __init__(self, host, user, password, database, port = 3306):
        try:
            self.db_connection = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
            self.db_connection
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                return None
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return None
            else:
                return error

    def selectUserOuro(self, CodigoContrato):
        cursor = self.db_connection.cursor()
        query = "SELECT NOME AS NomeAluno FROM usuarios WHERE LOGIN = %s GROUP BY LOGIN"
        cursor.execute(query, (CodigoContrato,))
        return cursor.fetchone()

    def selectUserPresenca(self, CodigoContrato, DataPresenca, HoraPresenca):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM presencas WHERE CodigoContrato = %s AND DataPresenca = %s AND HoraPresenca = %s GROUP BY CodigoContrato"
        cursor.execute(query, (CodigoContrato,DataPresenca,HoraPresenca,))
        return cursor.fetchone()
    
    def closedb(self):
        self.db_connection.close()
