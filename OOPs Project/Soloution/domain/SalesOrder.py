#import User
import datetime
#import SalesOrderItem
class SalesOrder:
    def __init__(self, id,customer,quantity,total_price,tax_amount,sales_lead,sale_date, item_list):
         self.__id = id
         self.__customer = customer
         self.__quantity = quantity
         self.__total_price = total_price
         self.__tax_amount = tax_amount
         self.__sales_lead = sales_lead
         self.__sale_date = sale_date
         self.__item_list = item_list
         
    def get_id(self):   
        return self.__id   
      
    def set_id(self, id):   
        self.__id = id

    def get_customer(self):   
        return self.__customer   
      
    def set_customer(self, customer):   
        self.__customer = customer

    def get_quantity(self):   
        return self.__quantity   
      
    def set_quantity(self, quantity):   
        self.__quantity = quantity

    def get_total_price(self):   
        return self.__total_price  
      
    def set_total_price(self, total_price):   
        self.__total_price = total_price

    def get_tax_amount(self):   
        return self.__tax_amount  
      
    def set_tax_amount(self, tax_amount):   
        self.__tax_amount = tax_amount

    def get_sales_lead(self):   
        return self.__sales_lead  
      
    def set_sales_lead(self, sales_lead):   
        self.__sales_lead = sales_lead

    def get_sale_date(self):   
        return self.__sale_date  
      
    def set_sale_date(self, sale_date):   
        self.__sale_date = sale_date

    def get_item_list(self):   
        return self.__item_list  
      
    def set_item_list(self, item_list):   
        self.__item_list = item_list

    def __str__(self):
        return "%-20s %-20d %-20.2f %-20.2f %-20s %-20s"%(self.get_customer().get_name(),self.get_quantity(),self.get_total_price(),self.get_tax_amount(),self.get_sales_lead().get_name(), self.get_sale_date().strftime("%d/%m/%Y"))












