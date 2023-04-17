import pickle
import os
import zipfile


# SAVE DATA
#def data_hotel(hotel_list):
#    with open("hotel.pkl", "wb") as f:
#        pickle.dump(hotel_list, f, pickle.HIGHEST_PROTOCOL)

def data_staffs(staff_list):
    with open("staff.pkl", "wb") as f:
        pickle.dump(staff_list, f, pickle.HIGHEST_PROTOCOL)

def data_guests(guests_list):
    with open("guests.pkl", "wb") as f:
        pickle.dump(guests_list, f, pickle.HIGHEST_PROTOCOL)

def data_room(room_list):
    with open("room.pkl", "wb") as f:
        pickle.dump(room_list, f, pickle.HIGHEST_PROTOCOL)

def data_reservation(reservation_list):
    with open("reservation.pkl", "wb") as f:
        pickle.dump(reservation_list, f, pickle.HIGHEST_PROTOCOL)

# ZIP DATA IN DATA.DAT
def zip_data():
    with zipfile.ZipFile("data.dat","w",compression=zipfile.ZIP_DEFLATED) as zip:
        #zip.write("hotel.pkl")
        zip.write("staff.pkl")
        zip.write("guests.pkl")
        zip.write("room.pkl")
        zip.write("reservation.pkl")
    #os.remove("hotel.pkl")
    os.remove("staff.pkl")
    os.remove("guests.pkl")
    os.remove("room.pkl")
    os.remove("reservation.pkl")

#==============================================================================================================#
# GET DATA
#def open_hotel():
#    hotel_list = []
#    if (os.path.exists("hotel.pkl")):
#        with open("hotel.pkl", "rb") as f:
#            hotel_list = pickle.load(f)
#    return (hotel_list)

def open_staffs():
    staff_list = []
    if (os.path.exists("staff.pkl")):
        with open("staff.pkl", "rb") as f:
            staff_list = pickle.load(f)
    return (staff_list)

def open_guests():
    guests_list = []
    if (os.path.exists("guests.pkl")):
        with open("guests.pkl", "rb") as f:
            guests_list = pickle.load(f)
    return (guests_list)

def open_room():
    room_list = []
    if (os.path.exists("room.pkl")):
        with open("room.pkl", "rb") as f:
            room_list = pickle.load(f)
    return (room_list)

def open_reservation():
    reservation_list = []
    if (os.path.exists("reservation.pkl")):
        with open("reservation.pkl", "rb") as f:
            reservation_list = pickle.load(f)
    return (reservation_list)

# UNZIP DATA.DAT
def unzip_data():
    if os.path.exists("data.dat"):
        with zipfile.ZipFile("data.dat","r") as zip:
            zip.extractall()
        os.remove("data.dat")