import datetime

# CHECK VALIDITY OF INPUTS
def invalid_id(id, para: str):
    while True:
        try:
            id_num = int(id[-3:])
            if id[:2] != para or len(id) != 5:
                return 1
            else:
                return 0
        except ValueError:
            return 1

def invalid_reservationID(id, para: str):
    while True:
        try:
            id_num = int(id[-3:])
            if id[:3] != para or len(id) != 6:
                return 1
            else:
                return 0
        except ValueError:
            return 1
        
def invalid_gend(gend):
    if gend != "M" and gend != "F":
        return 1
    else: return 0

def invalid_dob(dob):
    while True:
        try:
            dd_check = int(dob[:2])
            mm_check = int(dob[:5][-2:])
            yyyy_check = int(dob[-4:])
            check1 = dob[:3][-1:]
            check2 = dob[:6][-1:]
            if len(dob) != 10:
                return 1
            elif check1!="/" or check2!="/":
                return 1
            elif dd_check<1 or dd_check>31:
                return 1
            elif mm_check<1 or mm_check>12:
                return 1
            else: return 0
        except ValueError:
            return 1

def invalid_phone(phone):
    while True:
        try:
            phone_check = int(phone)
            if len(phone) != 10:
                return 1
            else:
                return 0
        except ValueError:
            return 1

def invalid_salary(salary):
    while True:
        try:
            salary_check = float(salary)
            if salary_check >=0:
                return 0
            else:
                return 1
        except ValueError:
            return 1


def invalid_price(price, type):
    while True:
        try:
            price_check = float(price)
            if price_check == 1000000 and type == "Normal":
                return 0
            elif price_check == 2000000 and type == "Gold":
                return 0
            elif price_check == 3000000 and type == "Luxury":
                return 0
            else: return 1
        except ValueError:
            return 1

def invalid_type(type):
    if type != "Luxury" and type != "Gold" and type != "Normal":
        return 1
    else: return 0














# Sorting
def sort_people_list_by_column(treeview, arr, col, reverse):
    if(col == "ID"):
        arr.sort(key=lambda x: x.get_id(),reverse=reverse)
    if(col == "Name"):
        arr.sort(key=lambda x: x.get_name(),reverse=reverse)
    if(col == "Gender"):
        arr.sort(key=lambda x: x.get_gend(),reverse=reverse)
    if(col == "Date of Birth"):
        arr.sort(key=lambda x: datetime.datetime.strptime(x.get_dob(), '%d/%m/%Y'),reverse=reverse)
    if(col == "Phone"):
        arr.sort(key=lambda x: x.get_phone(),reverse=reverse)
    if(col == "Email"):
        arr.sort(key=lambda x: x.get_email(),reverse=reverse)
    if(col == "Address"):
        arr.sort(key=lambda x: x.get_address(),reverse=reverse)   
    if(col == "Salary"):
        arr.sort(key=lambda x: x.get_salary(),reverse=reverse) 
    if(col == "Position"):
        arr.sort(key=lambda x: x.get_position(),reverse=reverse)
    for i in treeview.get_children():
        treeview.delete(i)
    a_count = 0
    for element in arr:
        treeview.insert(parent='', index = 'end', iid=a_count, text='', values=(
            element.get_id(), element.get_name(), element.get_gend(), element.get_dob(), element.get_phone(), element.get_email(), element.get_address(),element.get_salary(), element.get_position()
        ))
        a_count += 1

    treeview.heading(col, text=col, command=lambda _col=col: \
                 sort_people_list_by_column(treeview, arr, _col, not reverse))

def sort_guest_list_by_column(treeview, arr, col, reverse):
    if(col == "ID"):
        arr.sort(key=lambda x: x.get_id(),reverse=reverse)
    if(col == "Name"):
        arr.sort(key=lambda x: x.get_name(),reverse=reverse)
    if(col == "Gender"):
        arr.sort(key=lambda x: x.get_gend(),reverse=reverse)
    if(col == "Date of Birth"):
        arr.sort(key=lambda x: datetime.datetime.strptime(x.get_dob(), '%d/%m/%Y'),reverse=reverse)
    if(col == "Phone"):
        arr.sort(key=lambda x: x.get_phone(),reverse=reverse)
    if(col == "Email"):
        arr.sort(key=lambda x: x.get_email(),reverse=reverse)
    if(col == "Address"):
        arr.sort(key=lambda x: x.get_address(),reverse=reverse)   
    for i in treeview.get_children():
        treeview.delete(i)
    a_count = 0
    for element in arr:
        treeview.insert(parent='', index = 'end', iid=a_count, text='', values=(
            element.get_id(), element.get_name(), element.get_gend(), element.get_dob(), element.get_phone(), element.get_email(), element.get_address()))
        a_count += 1

    treeview.heading(col, text=col, command=lambda _col=col: \
                 sort_guest_list_by_column(treeview, arr, _col, not reverse))



def sort_room_list_by_column(treeview, arr,col, reverse):
    if(col == "ID"):
        arr.sort(key=lambda x: x.get_id(),reverse=reverse)
    if(col == "Type"):
        arr.sort(key=lambda x: x.get_type(),reverse=reverse)
    if(col == "Price"):
        arr.sort(key=lambda x: x.get_price(),reverse=reverse)
    if(col == "Status"):
        arr.sort(key=lambda x: str(x.get_status()),reverse=reverse)
    for i in treeview.get_children():
        treeview.delete(i)
    a_count = 0
    for element in arr:
        treeview.insert(parent='', index = 'end', iid=a_count, text='', values=(
            element.get_id(), element.get_type(), element.get_price(), element.get_status())
        )
        a_count += 1

    treeview.heading(col, text=col, command=lambda _col=col: \
                 sort_room_list_by_column(treeview, arr, _col, not reverse))



def sort_reservation_list_by_column(treeview, arr, col, reverse):
    if (col == "ID"):
        arr.sort(key=lambda x: x.get_id(), reverse=reverse)
    if (col == "GuestID"):
        arr.sort(key=lambda x: x.get_guestID(), reverse=reverse)
    if (col == "RoomID"):
        arr.sort(key=lambda x: x.get_RoomID(), reverse=reverse)
    if (col == "Checkin"):
        arr.sort(key=lambda x: datetime.datetime.strptime(x.get_checkin(), '%d/%m/%Y'), reverse=reverse)
    if (col == "Checkout"):
        arr.sort(key=lambda x: datetime.datetime.strptime(x.get_checkout(), '%d/%m/%Y'), reverse=reverse)
    for i in treeview.get_children():
        treeview.delete(i)
    a_count = 0
    for element in arr:
        treeview.insert(parent='', index = 'end', iid=a_count, text='', values=(
            element.get_id(), element.get_guestID(), element.get_RoomID(), element.get_checkin(), element.get_checkout())
        )
        a_count += 1

    treeview.heading(col, text=col, command=lambda _col=col: \
                 sort_reservation_list_by_column(treeview, arr, _col, not reverse))

