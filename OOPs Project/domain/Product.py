#import Brand,ProductType,ProductCategory

class Product:

    def __init__(self, id=None, name=None, brand=None, color=None, material=None, price=None, active=None, quantity=None, product_type=None, product_category=None):
         self.__id = id
         self.__name = name
         self.__brand = brand
         self.__color = color
         self.__material = material
         self.__price = price
         self.__active = active
         self.__quantity = quantity
         self.__product_type = product_type
         self.__product_category = product_category
         
    def get_id(self):   
        return self.__id   
      
    def set_id(self, id):   
        self.__id = id

    def get_name(self):   
        return self.__name   
      
    def set_name(self, name):   
        self.__name = name

    def get_brand(self):   
        return self.__brand   
      
    def set_brand(self, brand):   
        self.__brand = brand

    def get_color(self):   
        return self.__color  
      
    def set_color(self, color):   
        self.__color = color

    def get_material(self):   
        return self.__material  
      
    def set_material(self, material):   
        self.__material = material

    def get_price(self):   
        return self.__price  
      
    def set_price(self, price):   
        self.__price = price

    def get_active(self):   
        return self.__active  
      
    def set_active(self, active):   
        self.__active = active

    def get_quantity(self):   
        return self.__quantity  
      
    def set_quantity(self, quantity):   
        self.__quantity = quantity

    def get_product_type(self):   
        return self.__product_type  
      
    def set_product_type(self, product_type):   
        self.__product_type = product_type

    def get_product_category(self):   
        return self.__product_category  
      
    def set_product_category(self, product_category):   
        self.__product_category = product_category

    def __eq__(self, product):
        if product!=None:
            return self.get_name() == product.get_name() and self.get_brand().get_name()==product.get_brand().get_name() and self.get_color()==product.get_color() and self.get_material()==product.get_material()
        else:
            return None

    def __str__(self):
        return "%-20d %-20s %-20s %-20s %-20s %-20.2f %-20d %-20s %-20s"%(self.get_id(), self.get_name(), self.get_brand().get_name(), self.get_color(),self.get_material(),self.get_price(),self.get_quantity(),self.get_product_type().get_name(),self.get_product_category().get_name())

















    
