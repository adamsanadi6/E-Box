from domain import *
from utility import *
class BrandDAO:
    
    def obtain_all_brand(self):
        '''Fill your code here'''
        return None

    def add_brand(self,brand):
        '''Fill your code here'''
        name = brand.get_name()
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select * from brand where name = '" + name +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) != 0:
            return False
        mycursor.execute("select * from brand")
        result = mycursor.fetchall()
        rc = len(result) + 1
        sql = "INSERT INTO brand (id,name) VALUES (%s, %s)"
        val = (rc, name)
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    
    def display_brand(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from brand")
        result = mycursor.fetchall()
        print("%-5s %-15s"%("Id","Name"))
        for row in result:  
            print("%-5s %-15s"%(str(row[0]), row[1]))

    def obtain_brand_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select id from brand where id = " + str(id) 
        mycursor.execute(query)
        return mycursor.fetchall()[0][0]