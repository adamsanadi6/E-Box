from bo import *
from domain import *
from utility import *
from dao import ProductDAO

class SalesOrderItemDAO:
    def obtain_all_sales_order_items(self):
        '''Fill your code here'''
        query = "select s.id, p.name, s.quantity, s.unit_price from sales_order_item s, product p where s.product_id = p.id"
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        item_list = list()
        for row in result:
            item = "%-20d %-20s %-20d %-20.2f"%(row[0], str(row[1]), row[2], row[3])
            item_list.append(item)
        return item_list
        
    def obtain_sales_order_item_by_id(self,id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select * from sales_order_item where id = " + str(id)
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result) != 0:
            return SalesOrderItem(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])
        return None
        
        
