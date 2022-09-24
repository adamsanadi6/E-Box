from bo import *
from domain import *
from utility import *
class ProductDAO:
    def obtain_all_products(self):
        '''Fill your code here'''
        return None

    def add_product(self, product):
        '''Fill your code here'''
        name = product.get_name()
        brand_id = product.get_brand()
        color = product.get_color()
        material = product.get_material()
        price = product.get_price()
        active = product.get_active()
        quantity = product.get_quantity()
        product_type_id = product.get_product_type()
        product_category_id = product.get_product_category()
        query = "select * from product where name = '%s' and brand_id = %s and color = '%s' and material = '%s' and  price = %s and active = %s and product_type_id = %s and product_category_id = %s"%(name, str(brand_id), color, material, str(price), str(active), str(product_type_id), str(product_category_id))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) != 0:
            return False
        query = "Select * from product"
        mycursor.execute(query)
        result = mycursor.fetchall()
        id = len(result) + 1
        query = "insert into product (id, name, brand_id, color, material, price, active, quantity, product_type_id, product_category_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        args = (str(id), name, str(brand_id), color, material, str(price), str(active), str(quantity), str(product_type_id), str(product_category_id))
        mycursor.execute(query, args)
        mydb.commit()
        return True

    def display_all_products(self):
        '''Fill your code here'''
        print("Product Details:")
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select p.id, p.name, b.name, p.color, p.material, p.price, p.quantity, pt.name, pc.name from product p, brand b, product_type pt, product_category pc where p.brand_id = b.id and p.product_type_id = pt.id and p.product_category_id = pc.id"
        mycursor.execute(query)
        print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id", "Product Name","Brand","Color","Material","Price","Available Quantity","Product Type","Product Category"))
        result = mycursor.fetchall()
        for row in result:
            print("%-20s %-20s %-20s %-20s %-20s %-20.2f %-20s %-20s %-20s\n"%(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    def obtain_product_by_name(self,name):
        '''Fill your code here'''
        query = "select id from product where name = '" + name + "'"
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return result[0][0]

    def obtain_product_by_id(self,id):
        '''Fill your code here'''
        query = "select id from product where id = " + str(id) 
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) == 0:
            return None
        return Product(result[0][0])

    def update_product(self, product):
        '''Fill your code here'''
        name = product.get_name()
        color = product.get_color()
        material = product.get_material()
        price = product.get_price()
        active = product.get_active()
        quantity = product.get_quantity()
        id = product.get_id()
        query = "update product set name = '%s', color = '%s', material = '%s', price = %s, active = %s, quantity = '%s' where id = %s"%(name, color, material, str(price), str(active), str(quantity), str(id))
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        return True

    def display_product(self,product):
        '''Fill your code here'''
        print("Product Details:")
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select p.id, p.name, b.name, p.color, p.material, p.price, p.quantity, pt.name, pc.name from product p, brand b, product_type pt, product_category pc where p.id = " + str(product) + " and p.brand_id = b.id and p.product_type_id = pt.id and p.product_category_id = pc.id"
        mycursor.execute(query)
        print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id", "Product Name","Brand","Color","Material","Price","Available Quantity","Product Type","Product Category"))
        result = mycursor.fetchall()
        for row in result:
            print("%-20s %-20s %-20s %-20s %-20s %-20.2f %-20s %-20s %-20s\n"%(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))   