class ProductType:

    def __init__(self, id=None, name=None, description=None):
         self.__id = id
         self.__name = name
         self.__description = description
         
    def get_id(self):   
        return self.__id   
      
    def set_id(self, id):   
        self.__id = id

    def get_name(self):   
        return self.__name   
      
    def set_name(self, name):   
        self.__name = name

    def get_description(self):   
        return self.__description   
      
    def set_description(self, description):   
        self.__description = description

    def __eq__(self, productType):
        return self.get_name() == productType.get_name()
