from domain import *
from utility import *
class RoleDAO:
    def obtain_role_by_id(self,role_id):
        role = None;
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from role where id = '"+str(role_id)+"'")
        for x in mycursor:
            role = Role(x[0],x[1])
        return role
