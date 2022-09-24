import mysql.connector 
import configparser

class DBConnection:
    def _init_(self):
        pass
    
    def get_connection(self):
        config = configparser.RawConfigParser()
        config.read('mysql.properties')
        dburl=config.get('DatabaseSection', 'db.host');
        dbname = config.get('DatabaseSection', 'db.schema');
        username = config.get('DatabaseSection', 'db.username');
        password = config.get('DatabaseSection', 'db.password');
        port = '3306';
        self.mydb = mysql.connector.connect(host = dburl , port = port , database = dbname , user = username, password = password)
        return self.mydb