from tkinter import *
from tkinter import messagebox
from find_motion import find_motion
def btn_clicked():
    print("Button Clicked")
    username=entry0.get()
    password=entry1.get()
    if username == "r":
        print("username correct ")
        if password == "1":
            print(" password correct")
            window.destroy()
            page_next()
        else:
            messagebox.showerror("Data Verification", "please recheck the entered password")
    else:
        messagebox.showerror("Data Verification", "please recheck the entered username")

def page_next():
    window2 = Tk()
    window2.geometry("1500x800")
    window2.configure(bg = "#ffffff")
    canvas = Canvas(
        window2,
        bg = "#ffffff",
        height = 800,
        width = 1500,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"images\\secondpage.png")
    background = canvas.create_image(
        781.0, 400.0,
        image=background_img)

    img0 = PhotoImage(file = f"images\\img21.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = find_motion,
        relief = "flat")

    b0.place(
        x = 837, y = 431,
        width = 235,
        height = 87)

    img1 = PhotoImage(file = f"images\\img22.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = window2.destroy,
        relief = "flat")

    b1.place(
        x = 1162, y = 431,
        width = 235,
        height = 87)

    window2.resizable(True, True)
    window2.mainloop()



window= Tk()
window.geometry("1500x800")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 800,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images\\background.png")
background = canvas.create_image(
    750.0, 394.0,
    image=background_img)

entry0_img = PhotoImage(file = f"images\\img_textBox0.png")
entry0_bg = canvas.create_image(
    1170.0, 404.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f9f3f3",
    highlightthickness = 0)

entry0.place(
    x = 1045, y = 392,
    width = 250,
    height = 23)

entry1_img = PhotoImage(file = f"images\\img_textBox1.png")
entry1_bg = canvas.create_image(
    1170.0, 516.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#fffbfb",
    highlightthickness = 0)

entry1.place(
    x = 1045, y = 504,
    width = 250,
    height = 23)

img0 = PhotoImage(file = f"images\\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 1090, y = 569,
    width = 151,
    height = 43)

window.resizable(True, True)
window.mainloop()
