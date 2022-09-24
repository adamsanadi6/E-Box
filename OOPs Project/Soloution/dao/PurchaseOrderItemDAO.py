from bo import *
from domain import *
from utility import *
from dao import ProductDAO
class PurchaseOrderItemDAO:

    def obtain_all_purchase_order_items(self):
        purchaseOrderItemList = []
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from purchase_order_item")
        for x in mycursor:
            pdao=ProductDAO()
            purchaseOrderItemList.append(PurchaseOrderItem(x[0],pdao.obtain_product_by_id(x[1]),x[2],x[3],None))
        return purchaseOrderItemList

    def obtain_purchase_order_item_by_id(self,id):
        purchaseOrderItem = None
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from purchase_order_item where id = '"+str(id)+"'")
        for x in mycursor:
            pdao=ProductDAO()
            purchaseOrderItem =(PurchaseOrderItem(x[0],pdao.obtain_product_by_id(x[1]),x[2],x[3],None))
        return purchaseOrderItem
