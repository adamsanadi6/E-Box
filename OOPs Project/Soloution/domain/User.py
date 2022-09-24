#import Role

class User:
    def __init__(self, id,name,username,password,mobile_number,email,address,role):
         self.__id = id
         self.__name = name
         self.__username = username
         self.__password = password
         self.__mobile_number = mobile_number
         self.__email = email
         self.__address = address
         self.__role = role
         
    def get_id(self):   
        return self.__id   
      
    def set_id(self, id):   
        self.__id = id

    def get_name(self):   
        return self.__name   
      
    def set_name(self, name):   
        self.__name = name

    def get_username(self):   
        return self.__username  
      
    def set_username(self, username):   
        self.__username = username

    def get_mobile_number(self):   
        return self.__mobile_number  
      
    def set_mobile_number(self, mobile_number):   
        self.__mobile_number = mobile_number

    def get_email(self):   
        return self.__email  
      
    def set_email(self, email):   
        self.__email = email

    def get_role(self):   
        return self.__role 
      
    def set_role(self, role):   
        self.__role = role

    def get_password(self):   
        return self.__password  
      
    def set_password(self, password):   
        self.__password = password

    def get_address(self):   
        return self.__address  
      
    def set_address(self, address):   
        self.__item_list = item_list

    def __str__(self):
        return "%-20d %-20s %-20s %-20s %-20s %-20s %-20s"%(self.get_id(),self.get_name(),self.get_username(),self.get_mobile_number(),self.get_email(),self.get_address(),self.get_role().get_name())























