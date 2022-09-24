from bo import *
from domain import *
from utility import *
class ProductDAO:
    def obtain_all_products(self):
        product_list=[]
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from product")
        data1=mycursor.fetchall()
        for x in data1:
            mycursor.execute("select * from brand where id='"+str(x[2])+"'")
            brand=None
            data2=mycursor
            for y in data2:
                brand=Brand(y[0],y[1])
            mycursor.execute("select * from product_type where id='"+str(x[8])+"'")
            productType = None
            data3=mycursor
            for y in data3:
                productType = ProductType(y[0],y[1],y[2])
            mycursor.execute("select * from product_category where id='"+str(x[9])+"'")
            productCategory = None
            data4=mycursor
            for y in data4:
                productCategory = ProductCategory(y[0],y[1],y[2])
            product_list.append(Product(x[0],x[1],brand,x[3],x[4],x[5],x[6],x[7],productType,productCategory))
        return product_list

    def add_product(self,product):
        productList=self.obtain_all_products()
        res=True
        for p in productList:
            if p==product:
                res=False
                break
        if res:
            dbObj = DBConnection()
            mydb = dbObj.get_connection()
            mycursor = mydb.cursor()
            mycursor.execute("insert into product(name,brand_id,product_type_id,product_category_id,color,material,active,price,quantity) values('"+product.get_name()+"','"+str(product.get_brand().get_id())+"','"+str(product.get_product_type().get_id())+"','"+str(product.get_product_category().get_id())+"','"+product.get_color()+"','"+product.get_material()+"','"+str(product.get_active())+"','"+str(int(product.get_price()))+"','"+str(product.get_quantity())+"')")
            mydb.commit()
        return res

    def display_all_products(self):
        product_list=self.obtain_all_products()
        if len(product_list)>0:
            print("Product Details:")
            print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id", "Product Name","Brand","Color","Material","Price","Available Quantity","Product Type","Product Category"))
            for product in product_list:
                print(product)
        else:
            print("Product list is empty")

    def obtain_product_by_name(self,name):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from product where name='"+name+"'")
        data1=mycursor.fetchall()
        for x in data1:
            mycursor.execute("select * from brand where id='"+str(x[2])+"'")
            brand=None
            data2=mycursor
            for y in data2:
                brand=Brand(y[0],y[1])
            mycursor.execute("select * from product_type where id='"+str(x[8])+"'")
            productType = None
            data3=mycursor
            for y in data3:
                productType = ProductType(y[0],y[1],y[2])
            mycursor.execute("select * from product_category where id='"+str(x[9])+"'")
            productCategory = None
            data4=mycursor
            for y in data4:
                productCategory = ProductCategory(y[0],y[1],y[2])
            product = Product(x[0],x[1],brand,x[3],x[4],x[5],x[6],x[7],productType,productCategory)
            return product
        return None

    def obtain_product_by_id(self,id):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from product where id='"+str(id)+"'")
        data1=mycursor.fetchall()
        for x in data1:
            mycursor.execute("select * from brand where id='"+str(x[2])+"'")
            brand=None
            data2=mycursor
            for y in data2:
                brand=Brand(y[0],y[1])
            mycursor.execute("select * from product_type where id='"+str(x[8])+"'")
            productType = None
            data3=mycursor
            for y in data3:
                productType = ProductType(y[0],y[1],y[2])
            mycursor.execute("select * from product_category where id='"+str(x[9])+"'")
            productCategory = None
            data4=mycursor
            for y in data4:
                productCategory = ProductCategory(y[0],y[1],y[2])
            product = Product(x[0],x[1],brand,x[3],x[4],x[5],x[6],x[7],productType,productCategory)
            return product
        return None

    def update_product(self, product):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("update product set name='"+product.get_name()+"',brand_id='"+str(product.get_brand().get_id())+"',color='"+product.get_color()+"',material='"+product.get_material()+"',price='"+str(product.get_price())+"', active='"+str(product.get_active())+"',quantity='"+str(product.get_quantity())+"', product_type_id='"+str(product.get_product_type().get_id())+"', product_category_id='"+str(product.get_product_category().get_id())+"' where id='"+str(product.get_id())+"'")
        mydb.commit()
        return True

    def display_product(self,product):
        print("Product Details:")
        print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id", "Product Name","Brand","Color","Material","Price","Available Quantity","Product Type","Product Category"))
        print(product)











            
    
