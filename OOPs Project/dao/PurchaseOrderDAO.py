from bo import *
from domain import *
from utility import *
class PurchaseOrderDAO:

    def add_purchase_order(self,purchaseOrder):
        '''Fill your code here'''
        supplier_id = purchaseOrder.get_supplier()
        quantity = purchaseOrder.get_quantity()
        total_price = purchaseOrder.get_total_price()
        tax_amount = purchaseOrder.get_tax_amount()
        product_lead_id = purchaseOrder.get_product_lead()
        purchased_date = (str(purchaseOrder.get_purchased_date()).split(" "))[0]
        query = "insert into purchase_order (supplier_id, quantity, total_price, tax_amount, product_lead_id, purchased_date) values (%s, %s, %s, %s, %s, %s)"
        args = (str(supplier_id), str(quantity), str(total_price), str(tax_amount), str(product_lead_id), purchased_date)
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query, args)
        mydb.commit()
        return True