class Room():
    def __init__(self, id, type, price, status):
        self.__id = id
        self.__type = type
        self.__price = price
        self.__status = status

    
    def get_id(self):
        return self.__id
    def get_type(self):
        return self.__type
    def get_price(self):
        return self.__price
    def get_status(self):
        return self.__status


    def set_id(self, id):
        self.__id = id
    def set_type(self, type):
        self.__type = type
    def set_price(self, price):
        self.__price = price
    def set_status(self, status):
        self.__status = status

    