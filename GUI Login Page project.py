# importing required modules

import tkinter 
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("system")     # it can set light or dark
customtkinter.set_default_color_theme("green")  #themes : blue, dark-blue or green

app=customtkinter.CTk()                 #creating custom tkinter window
app.geometry("600x440")
app.title('Login')




img1=ImageTk.PhotoImage(Image.open("IMG_0294.jpg"))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=50)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


l2=customtkinter.CTkLabel(master=frame, text="Login to your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="username")
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="password")
entry2.place(x=50, y=165)

l2=customtkinter.CTkLabel(master=frame, text="Forget password", font=('Century Gothic', 12))
l2.place(x=165, y=200)

button1=customtkinter.CTkButton(master=frame, width=220,text="Login", corner_radius=6)
button1.place(x=50,y=240)

app.mainloop()