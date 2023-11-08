import tkinter as tk
from tkinter import *
import os
import git




			
def update():
	os.system('git config --global user.email "abdelrahmanelneshwy77@gmail.com')
	os.system('git add .')
	os.system(f'git commit -m \'{comment_Entry.get()}\' ')
	os.system('git push origin main')

	
    


# Create the main application window
iti_window =tk.Tk()
iti_window.geometry("900x480")
iti_window.title("ITI")
# ----------------------------------------------------------canves------------------------------------------------------#
canves1 =Canvas(iti_window, width=900, height=480,background="Gray")
canves1.pack()

image = PhotoImage(file=".//iti-logo.png")
desired_width = 200
desired_height = 200

# Resize the image using the subsample method
image = image.subsample(image.width() // desired_width, image.height() // desired_height)
ITI_label = tk.Label(canves1, 
     image=image
     )
ITI_label.place(x=600,y=50)
# Create and place labels and entry fields for username and password

update_button = tk.Button(canves1,
	  text="update ",
	  font=("Arial", 20, "bold"),
	  command=update,
	  background="yellow",
	  foreground="black"
	  )
update_button.place(x=200,y = 400)

comment_label = tk.Label(canves1, 
	text="comment",
	font=("Arial", 20, "bold"),
	background="Orange",
	foreground="white",
	borderwidth=10)
comment_label.place(x=80,y=200)
comment_Entry = tk.Entry(canves1,
     font=("Arial", 20, "bold")
     )
comment_Entry.place(x=250,y = 207)

# Run the main event loop
iti_window.mainloop()


