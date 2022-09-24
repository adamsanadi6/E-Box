from bo import *
from domain import *
from utility import *
class PurchaseOrderDAO:

    def add_purchase_order(self,purchaseOrder):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("insert into purchase_order(supplier_id,quantity,total_price,tax_amount,product_lead_id,purchased_date) values('"+str(purchaseOrder.get_supplier().get_id())+"','"+str(purchaseOrder.get_quantity())+"','"+str(purchaseOrder.get_total_price())+"','"+str(purchaseOrder.get_tax_amount())+"','"+str(purchaseOrder.get_product_lead().get_id())+"','"+str(purchaseOrder.get_purchased_date())+"')")
        mydb.commit()
        mycursor.execute("select max(id) from purchase_order")
        sid=-1
        for x in mycursor:
            sid=x
        for i in purchaseOrder.get_item_list():
            mycursor.execute("update purchase_order_item set purchase_order_id='"+str(sid[0])+"' where id='"+str(i.get_id())+"'")
            mydb.commit()
        return True
        
