# relation between guest and room 
class Reservation():
    def __init__(self, id, guestID, roomID, checkin, checkout):
        self.__id = id
        self.__guestID = guestID
        self.__roomID = roomID
        self.__checkin = checkin
        self.__checkout = checkout
    
    def get_id(self):
        return self.__id
    def get_guestID(self):
        return self.__guestID
    def get_RoomID(self):
        return self.__roomID
    def get_checkin(self):
        return self.__checkin
    def get_checkout(self):
        return self.__checkout

    def set_ID(self, id):
        self.__id = id
    def set_GuestID(self, guestID):
        self.__guestID = guestID
    def set_RoomID(self, roomID):
        self.__roomID = roomID
    def set_Checkin(self, checkin):
        self.__checkin = checkin
    def set_Checkout(self, checkout):
        self.__checkout = checkout
