import tkinter as tk
import customtkinter as ctk
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk

# from chapter1.unit1 import mainFrame as frame_unit1
# from chapter1.unit2 import mainFrame as frame_unit2 -> not working
# from chapter1.unit3 import mainFrame as frame_unit3 -> not working


App=tk.Tk()
App.title('el1')
App.geometry('1280x720')
App.resizable(False,False)

mainFrame=ScrolledFrame(App)
mainFrame.autohide_scrollbar()
mainFrame.pack(expand=True, fill='both')

backgroundImage=Image.open('sources/assets/ChapterSelectionBackgrounds/Variables et affectations.png')
n1=Image.open('sources/assets/ChapterSelectionIcons/Niveau1.png')
n2=Image.open('sources/assets/ChapterSelectionIcons/Niveau2.png')
n3=Image.open('sources/assets/ChapterSelectionIcons/Niveau3.png')
n4=Image.open('sources/assets/ChapterSelectionIcons/Niveau4.png')
n5=Image.open('sources/assets/ChapterSelectionIcons/Niveau5.png')
quiz=Image.open('sources/assets/ChapterSelectionIcons/quiz.png')
megaQuiz=Image.open('sources/assets/ChapterSelectionIcons/Mega quiz.png')


backgroundImage.paste(n1, (20, 40), n1)
# backgroundImage.paste(n2, (40, 80), n2)

tkimage = ImageTk.PhotoImage(backgroundImage)
background = tk.Label(mainFrame,image=tkimage)
background.pack()

# BUTTONS
class snake_button(ctk.CTkButton):
    def __init__(self, master: tk.Tk, button_text = '-1', button_color = '#d9d9d9'):
        self.button = ctk.CTkButton(
            master = master, 
            text = button_text, 
            width = 150, 
            height = 160, 
            corner_radius = 100, 
            border_width = 2.5, 
            fg_color = button_color, 
            text_color = 'black', 
            border_color = 'black', 
            font = ('Calibri', 80, 'bold'), 
            hover = False,
            command=self.enter)
        
    def place(self, x: int, y: int):
        self.button.place(x=x, y=y)

    def enter(self):
        print('entering!')


button_unit1 = snake_button(mainFrame)
button_unit1.place(281, 536)

button_unit1 = snake_button(mainFrame)
button_unit1.place(390, 974)

button_unit1 = snake_button(mainFrame)
button_unit1.place(478, 1475)


backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n1, (20, 40), n1)



App.mainloop()

#https://stackoverflow.com/questions/23876447/tkinter-overlay-foreground-image-on-top-of-a-background-image-with-transparency