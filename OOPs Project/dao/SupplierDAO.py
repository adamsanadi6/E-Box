from bo import *
from domain import *
from utility import *
class SupplierDAO:

    def obtain_all_suppliers(self):
        '''Fill your code here'''
        query = "select * from supplier"
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        resultSet = mycursor.fetchall()
        supplier_list = list()
        for row in resultSet:
            supplier = "%-20d %-20s %-20s %-20s %-20s"%(row[0], row[1], row[2], row[3], row[4])
            supplier_list.append(supplier)
        return supplier_list
        
    def obtain_supplier_by_id(self,id):
        '''Fill your code here'''
        query = "select id from supplier where id = " + str(id)
        dbObj = DBConnection() 
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        resultSet = mycursor.fetchall()
        if len(resultSet) == 0:
            return None
        return resultSet[0][0]

    def display_suppliers(self):
        '''Fill your code here'''
        return None