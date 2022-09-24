from domain import *
from utility import *
from dao import RoleDAO

class UserDAO:
    def validate_login(self,username,password):
        user =None
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        s="select * from user where username = '"+username+"' and password = '"+password+"'"
        mycursor.execute(s)
        roleDAO = RoleDAO()
        for x in mycursor:
            role = roleDAO.obtain_role_by_id(x[7])
            user=User(x[0],x[1],x[2],x[3],x[4],x[5],x[6],role)
        return user

    def obtain_users_by_role(self,name):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from role where name = '"+name+"'")
        role=None
        for x in mycursor:
            role=Role(x[0],x[1])
        uList=[]
        mycursor.execute("select * from user where role_id='"+str(role.get_id())+"'")
        roleDAO = RoleDAO()
        for x in mycursor:
            role=roleDAO.obtain_role_by_id(x[7])
            uList.append(User(x[0],x[1],x[2],x[3],x[4],x[5],x[6],role))
        return uList

    def obtain_users_by_id(self,id):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from user where id='"+str(id)+"'")
        roleDAO = RoleDAO()
        for x in mycursor:
            role = roleDAO.obtain_role_by_id(x[7])
            return User(x[0],x[1],x[2],x[3],x[4],x[5],x[6],role)
