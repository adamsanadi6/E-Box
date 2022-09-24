from bo import *
from domain import *
from utility import *
class SupplierDAO:

    def obtain_all_suppliers(self):
        sList = []
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from supplier")
        for x in mycursor:
            sList.append(Supplier(x[0],x[1],x[2],x[3],x[4]))
        return sList
        
    def obtain_supplier_by_id(self,id):
        s = None
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from supplier where id='"+str(id)+"'")
        for x in mycursor:
            s=(Supplier(x[0],x[1],x[2],x[3],x[4]))
        return s
    def display_suppliers(self):
        pass
        '''sList=obtain_all_suppliers()
    print("%-20s %-20s %-20s %-20s %-20s\n","Id"%("Name","Mobile Number","Email-id","Address"))
        for s in sList:
            print(s)'''
        
