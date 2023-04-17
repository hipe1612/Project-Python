class Person():
    def __init__(self,id,name,gend,dob,phone,email,address):
        self.__id= id
        self.__name= name
        self.__gend= gend
        self.__dob= dob
        self.__phone= phone
        self.__email= email
        self.__address= address
    
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_gend(self):
        return self.__gend
    def get_dob(self):
        return self.__dob
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def get_address(self):
        return self.__address
    
    def set_id(self,id):
        self.__id= id
    def set_name(self,name):
        self.__name= name
    def set_gend(self,gend):
        self.__gend= gend
    def set_dob(self,dob):
        self.__dob= dob
    def set_phone(self,phone):
        self.__phone= phone
    def set_email(self,email):
        self.__email= email
    def set_address(self,address):
        self.__address= address
    

class Staff(Person):
    def __init__(self,id,name,gend,dob,phone,email,address,salary,position):
        super().__init__(id,name,gend,dob,phone,email,address)
        self.__salary= salary
        self.__position= position
        self.__IsStaff = True
    
    def get_salary(self):
        return self.__salary
    def get_position(self):
        return self.__position
    
    def set_salary(self,salary):
        self.__salary= salary
    def set_position(self,position):
        self.__position= position

    def IsStaff(self):
        return self.__IsStaff

class Guests(Person):
    def __init__(self,id,name,gend,dob,phone,email,address):
        super().__init__(id,name,gend,dob,phone,email,address)
        self.__IsStaff = False
    
    def IsStaff(self):
        return self.__IsStaff