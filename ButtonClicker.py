# import tkinter
from tkinter import *
# messagebox(showerror, showinfo etc(pop-ups))
from tkinter import messagebox
import time  # import time for the countdown
# pygame for music
import pygame

#not sure yet but give pygame the init force
pygame.init()
# assign tkinter as root
root = Tk()
root.configure(background='brown')
# set window size
root.geometry('280x150')
# set a counter for the times the button is clicked
counter = 0

# stringvar, text.set and in label textvariable, in order not to print under the text but the text changes only
text = StringVar()
text.set('Times the button is clicked will be displayed here!')
lbl = Label(root, textvariable=text, bg='aqua', fg='green').pack()


# Function to display the times the counter are pressed but only the number changes not the text
def labelShow():
    global counter
    counter += 1
    text.set(f'{counter} times clicked!')

def play():
    pygame.mixer.music.load("C:\\Users\\Noxyseras\\Desktop\\jam.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device

def stop():
    pygame.mixer.music.pause()

def startAgain():
    pygame.mixer.music.unpause()
def pop_up():
    messagebox.showerror('EROR 404', "This is an error example!")



button_user_clicks = Button(root, text=' click me!', bg='black', fg='white', command=labelShow).pack()
message = Button(root, text='Click me for an error!', command=pop_up).pack()
playy = Button(root, text='Play music!', command=play).pack()
pausee = Button(root, text='Pause.', command=stop).pack()
unpausee = Button(root, text='Unpause.', command=startAgain).pack()

root.mainloop()
