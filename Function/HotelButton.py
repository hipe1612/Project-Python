from tkinter import *

from PIL import Image, ImageTk

def hotel_window(window, width, height, room_list, reservation_list):
    window = Toplevel(window)

    window.title("Hotel Information")
    window.configure(bg = "white")
    window.geometry("%dx%d+0+0" % (width, height))
    
    # Picture
    with Image.open("image/hotel_anh_doc.jpg") as image:
        resized_image = image.resize((520, 760))
        picture1 = ImageTk.PhotoImage(resized_image)
    picture_label = Label(window, image=picture1)
    picture_label.place(x=1000, y= 20)

    # Title
    text_label = Label(window, text = " ABOUT HOTEL", font = ("Montserrat Bold",80,'bold'), fg = "#5E95FF", bg = "white")
    text_label.place(x=100, y= 10)

    # Line
    canvas = Canvas(window, width = 700, height= 50, bg='white', highlightthickness=0)
    canvas.create_line(50,30,700,30,width=2,fill="#5E95FF")
    canvas.place(x=100, y= 120)

    # RoomStatus
    text_label = Label(window, text = " Room Status ", font = ("Montserrat Bold",25,'bold'), fg = "#5E95FF", bg = "white")
    text_label.place(x=30, y= 180)

    background = Canvas(window, width = 250, height= 150, bg='#efefef', highlightthickness=0)
    background.place(x=100, y= 240)
    background.create_text(10, 15, text="Total", font = ("Montserrat Bold",20,'bold'), fill="#5E95FF", anchor="nw", justify='center', tags="text")

    background = Canvas(window, width = 250, height= 150, bg='#efefef', highlightthickness=0)
    background.place(x=400, y= 240)
    background.create_text(10, 15, text="Booked", font = ("Montserrat Bold",20,'bold'), fill="#5E95FF", anchor="nw", justify='center', tags="text")

    room_count_label = Label(window, text =f'{len(room_list)}', font = ("Montserrat Bold",55,'bold'), fg = "red", bg = "#efefef")
    room_count_label.place(x=250, y= 290)

    res_room_count_label = Label(window, text=f'{len(reservation_list)}', font = ("Montserrat Bold",55,'bold'), fg = "red", bg = "#efefef")
    res_room_count_label.place(x=570, y= 290)

    # Contact
    text_label = Label(window, text = " Contact ", font = ("Montserrat Bold",25,'bold'), fg = "#5E95FF", bg = "white")
    text_label.place(x=30, y= 550)

    location_label = Label(window, text = "Location : _____Street, _____District, _____City", font = ("Montserrat Bold",20,'bold'), fg = "#5E95FF", bg = "white")
    location_label.place(x=50, y= 600)

    tele_label = Label(window, text = "Telephone : (+84)123456789", font = ("Montserrat Bold",20,'bold'), fg = "#5E95FF", bg = "white")
    tele_label.place(x=48, y= 640)

    email_label = Label(window, text = "Email : ourhotel@gmail.com", font = ("Montserrat Bold",20,'bold'), fg = "#5E95FF", bg = "white")
    email_label.place(x=50, y= 680)

    window.mainloop()