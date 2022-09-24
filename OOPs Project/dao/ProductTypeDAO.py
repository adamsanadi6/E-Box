from bo import *
from domain import *
from utility import *
class ProductTypeDAO:
    
    def obtain_all_product_type(self):
        '''Fill your code here'''
        return None

    def add_product_type(self, product_type):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        name = product_type.get_name()
        description = product_type.get_description()
        query = "select * from product_type where name = '" + name + "'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) != 0:
            return False
        mycursor.execute("select * from product_type")
        result = mycursor.fetchall()
        rc = len(result) + 1
        sql = "INSERT INTO product_type (id, name, description) VALUES (%s, %s, %s)"
        val = (rc, name, description)
        mycursor.execute(sql, val)
        mydb.commit()
        return True
        
      
    def display_product_type(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select * from product_type"
        mycursor.execute(query)
        result = mycursor.fetchall()
        print("%-5s %-15s %-15s"%("Id","Name","Description"))
        for row in result:
            print("%-5s %-15s %-15s"%(str(row[0]), row[1], row[2]))


    def obtain_product_type_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select id from product_type where id = " + str(id)
        mycursor.execute(query)
        return mycursor.fetchall()[0][0]