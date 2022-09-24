from unittest import result
from bo import *
from domain import *
from utility import *
from dao import UserDAO,SalesOrderItemDAO

class SalesOrderDAO:
    def obtain_all_sales_order(self):
        '''Fill your code here'''
        return None
         

    def add_sales_order(self,salesOrder):
        '''Fill your code here'''
        customer = salesOrder.get_customer()
        quantity = salesOrder.get_quantity()
        total_price = salesOrder.get_total_price()
        tax_amount = salesOrder.get_tax_amount()
        sales_lead = salesOrder.get_sales_lead()
        sales_date = salesOrder.get_sale_date()
        sales_date = str(sales_date).split(" ")
        sales_date = sales_date[0]
        # item_list = salesOrder.get_item_list()
        query = "insert into sales_order (customer_id, quantity, total_price, tax_amount, sales_lead_id, sale_date) values (%s, %s, %s, %s, %s, %s)"
        args = (str(customer), str(quantity), str(total_price), str(tax_amount), str(sales_lead), sales_date)
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query, args)
        mydb.commit()
        return True
        
    def display_sales_order(self):
        '''Fill your code here'''
        print("%-20s %-20s %-20s %-20s %-20s %-20s"%("User Name", "Order Quantity","Total Price","Tax Amount","Sales Lead","Sale Date"))
        query = "select u.name, s.quantity, s.total_price, s.tax_amount, u2.name, s.sale_date from user u, user u2, sales_order s where s.customer_id = u.id and s.sales_lead_id = u2.id"
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()

        for row in result:
            year, month, day = str(row[5]).split("-")
            date = day + "/" + month + "/" + year
            print("%-20s %-20s %-20.2f %-20.2f %-20s %-20s"%(row[0], str(row[1]), row[2], row[3], row[4], date))