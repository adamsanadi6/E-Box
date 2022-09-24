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

    def obtain_users_by_role(self, name):
        '''Fill your code here'''
        query = "select u.id, u.name, u.username, u.mobile_number, u.email, u.address from user u, role r where u.role_id = r.id and r.name = '" + name + "'"
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        customer_list = list()
        for row in result:
            customer = "%-20d %-20s %-20s %-20s %-20s %-20s"%(row[0], row[1], row[2], row[3], row[4], row[5])
            customer_list.append(customer)
        return customer_list

    def obtain_users_by_id(self,id):
        '''Fill your code here'''
        query = "select id from user where id = " + str(id)
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return result[0][0]
        