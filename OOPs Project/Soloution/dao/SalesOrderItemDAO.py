from bo import *
from domain import *
from utility import *
from dao import ProductDAO

class SalesOrderItemDAO:
    def obtain_all_sales_order_items(self):
        salesOrderItemList = []
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from sales_order_item")
        for x in mycursor:
            productId=x[1]
            pdao=ProductDAO()
            d=(pdao.obtain_product_by_id(productId))
            salesOrderItemList.append(SalesOrderItem(x[0],d,x[2],x[3],None))
        return salesOrderItemList;
        
    def obtain_sales_order_item_by_id(self,id):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from sales_order_item where id = '"+str(id)+"'")
        for x in mycursor:
            pdao=ProductDAO()
            return SalesOrderItem(x[0],(pdao.obtain_product_by_id(x[1])),x[2],x[3],None)
        return None
        
