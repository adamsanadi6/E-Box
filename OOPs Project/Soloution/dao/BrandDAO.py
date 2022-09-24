from domain import *
from utility import *
class BrandDAO:
    
    def obtain_all_brand(self):
        brand_list=[]
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from brand")
        for x in mycursor:
            brand_list.append(Brand(x[0],x[1]))
        return brand_list

    def add_brand(self,brand):
        brandList=self.obtain_all_brand()
        res=True
        for b in brandList:
            if b==brand:
                res=False
                break
        if res:
            dbObj = DBConnection()
            mydb = dbObj.get_connection()
            mycursor = mydb.cursor()
            mycursor.execute("insert into brand(name) values('"+brand.get_name()+"')")
            mydb.commit()
        return res
    
    def display_brand(self):
        brandList=self.obtain_all_brand()
        if(len(brandList)>0):
            print("%-5s %-15s\n"%("Id","Name"))
            for brand in brandList:
                print("%-5s %-15s\n"%(brand.get_id(),brand.get_name()))
        else:
            print("Brand list is empty")

    def obtain_brand_by_id(self,id):
        brand = None;
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from brand where id = '"+str(id)+"'")
        for x in mycursor:
            brand = Brand(x[0],x[1])
        return brand
