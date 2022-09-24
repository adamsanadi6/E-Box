from bo import *
from domain import *
from utility import *
class ProductCategoryDAO:
    
    def obtain_all_product_category(self):
        '''Fill your code here'''
        return None

    def add_product_category(self,product_category):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        name = product_category.get_name()
        description = product_category.get_description()
        query = "select * from product_category where name = '" + name + "'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) != 0:
            return False
        mycursor.execute("select * from product_category")
        result = mycursor.fetchall()
        rc = len(result) + 1
        sql = "INSERT INTO product_category (id, name, description) VALUES (%s, %s, %s)"
        val = (rc, name, description)
        mycursor.execute(sql, val)
        mydb.commit()
        return True
        
    def display_product_category(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select * from product_category"
        mycursor.execute(query)
        result = mycursor.fetchall()
        print("%-5s %-30s %-15s"%("Id","Name","Description"))
        for row in result:
            print("%-5s %-30s %-15s"%(str(row[0]), row[1], row[2]))

    def obtain_product_category_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select id from product_category where id = " + str(id)
        mycursor.execute(query)
        return mycursor.fetchall()[0][0]
