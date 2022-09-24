from bo import *
from domain import *
from utility import *
class ProductTypeDAO:
    
    def obtain_all_product_type(self):
        product_type_list=[]
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from product_type")
        for x in mycursor:
            product_type_list.append(ProductType(x[0],x[1],x[2]))
        return product_type_list

    def add_product_type(self,product_type):
        productTypeList=self.obtain_all_product_type()
        res=True
        for p in productTypeList:
            if(p==product_type):
                res=False
                break
        if res:
            dbObj = DBConnection()
            mydb = dbObj.get_connection()
            mycursor = mydb.cursor()
            mycursor.execute("insert into product_type(name,description) values('"+product_type.get_name()+"','"+product_type.get_description()+"')")
            mydb.commit()
        return res
        
    def display_product_type(self):
        productTypeList=self.obtain_all_product_type()
        if(len(productTypeList)>0):
            print("%-5s %-15s %-15s\n"%("Id","Name","Description"))
            for productType in productTypeList:
                print("%-5s %-15s %-15s\n"%(productType.get_id(),productType.get_name(),productType.get_description()))
        else:
            print("Product type list is empty")

    def obtain_product_type_by_id(self,id):
        productType = None;
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from product_type where id = '"+str(id)+"'")
        for x in mycursor:
            productType = ProductType(x[0],x[1],x[2])
        return productType
