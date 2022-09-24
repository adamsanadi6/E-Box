from bo import *
from domain import *
from utility import *
class ProductCategoryDAO:
    
    def obtain_all_product_category(self):
        product_category_list=[]
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from product_category")
        for x in mycursor:
            product_category_list.append(ProductCategory(x[0],x[1],x[2]))
        return product_category_list

    def add_product_category(self,product_category):
        productCategoryList=self.obtain_all_product_category()
        res=True
        for p in productCategoryList:
            if p==product_category:
                res=False
                break
        if res:
            dbObj = DBConnection()
            mydb = dbObj.get_connection()
            mycursor = mydb.cursor()
            mycursor.execute("insert into product_category(name,description) values('"+product_category.get_name()+"','"+product_category.get_description()+"')")
            mydb.commit()
        return res
    def display_product_category(self):
        productcategoryList=self.obtain_all_product_category()
        if(len(productcategoryList)>0):
            print("%-5s %-30s %-15s\n"%("Id","Name","Description"))
            for productcategory in productcategoryList:
                print("%-5s %-30s %-15s\n"%(productcategory.get_id(),productcategory.get_name(),productcategory.get_description()))
        else:
            print("Product type list is empty")

    def obtain_product_category_by_id(self,id):
        productCategory = None;
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from product_category where id = '"+str(id)+"'")
        for x in mycursor:
            productCategory = ProductCategory(x[0],x[1],x[2])
        return productCategory
