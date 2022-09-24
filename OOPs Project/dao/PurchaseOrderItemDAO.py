from bo import *
from domain import *
from utility import *
from dao import ProductDAO
class PurchaseOrderItemDAO:

    def obtain_all_purchase_order_items(self):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select poi.id, p.name, poi.quantity, poi.unit_price from purchase_order_item poi, product p where p.id = poi.product_id"
        mycursor.execute(query)
        resultSet = mycursor.fetchall()
        purchase_order_items_list = list()
        for row in resultSet:
            item = "%-20d %-20s %-20d %-20.2f"%(row[0], row[1], row[2], row[3])
            purchase_order_items_list.append(item)
        return purchase_order_items_list

    def obtain_purchase_order_item_by_id(self, id):
        '''Fill your code here'''
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        query = "select * from purchase_order_item where id = " + str(id)
        mycursor.execute(query)
        resultSet = mycursor.fetchall()
        if len(resultSet) == 0:
            return None
        return PurchaseOrderItem(resultSet[0][0], resultSet[0][1], resultSet[0][2], resultSet[0][3], resultSet[0][4])
