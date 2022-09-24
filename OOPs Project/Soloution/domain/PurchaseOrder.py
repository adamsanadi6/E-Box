import datetime
class PurchaseOrder:
    def __init__(self, id, supplier, quantity, total_price, tax_amount, product_lead, purchased_date, item_list):
         self.__id = id
         self.__supplier = supplier
         self.__quantity = quantity
         self.__total_price = total_price
         self.__tax_amount = tax_amount
         self.__product_lead = product_lead
         self.__purchased_date = purchased_date
         self.__item_list = item_list
         
    def get_id(self):   
        return self.__id   
      
    def set_id(self, id):   
        self.__id = id

    def get_supplier(self):   
        return self.__supplier   
      
    def set_supplier(self, supplier):   
        self.__supplier = supplier

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

    def get_product_lead(self):   
        return self.__product_lead  
      
    def set_product_lead(self, product_lead):   
        self.__product_lead = product_lead

    def get_purchased_date(self):   
        return self.__purchased_date  
      
    def set_purchased_date(self, purchased_date):   
        self.__purchased_date = purchased_date

    def get_item_list(self):   
        return self.__item_list  
      
    def set_item_list(self, item_list):   
        self.__item_list = item_list

    def __str__(self):
        return "%-20d %-20.2f %-20.2f %-20s %-20s %-20s"%(self.get_quantity(),self.get_totalPrice,self.get_tax_amount(),self.get_product_lead().get_name(),self.get_purchased_date().strftime("%d/%m/%Y"),self.get_supplier().get_name())












    

