from domain import *
from utility import *
class RoleDAO:
    def obtain_role_by_id(self,role_id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "SELECT name FROM role WHERE id= " + str(role_id)
        mycursor.execute(query)
        return mycursor.fetchall()[0][0]