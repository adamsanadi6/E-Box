#import Product,SalesOrder

class SalesOrderItem:
    def __init__(self, id,product,quantity,unit_price,sales_order):
         self.__id = id
         self.__product = product
         self.__quantity = quantity
         self.__unit_price = unit_price
         self.__sales_order = sales_order
         
    def get_id(self):   
        return self.__id   
      
    def set_id(self, id):   
        self.__id = id

    def get_product(self):   
        return self.__product   
      
    def set_product(self,product):   
        self.__product = product

    def get_quantity(self):   
        return self.__quantity   
      
    def set_quantity(self, quantity):   
        self.__quantity = quantity

    def get_unit_price(self):   
        return self.__unit_price  
      
    def set_unit_price(self, unit_price):   
        self.__unit_price = unit_price

    def get_sales_order(self):   
        return self.__sales_order  
      
    def set_sales_order(self, sales_order):   
        self.__sales_order = sales_order


    def __str__(self):
        return "%-20d %-20s %-20d %-20.2f"%(self.get_id(),self.get_product().get_name(),self.get_quantity(),self.get_unit_price())















