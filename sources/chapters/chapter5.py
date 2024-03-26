from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk

root=tb.Window(themename='solar')
root.title('el1')
root.geometry('1280x720')
root.resizable(False,False)

mainFrame=ScrolledFrame(root)
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

def enter(pageName):
    print('yo')

backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n2, (40, 80), n2)

tkimage = ImageTk.PhotoImage(backgroundImage)
background = tb.Label(mainFrame,image=tkimage)
background.pack()


el1=Button(mainFrame,command=lambda:enter('unit1'))
el1.place(x=20,y=40)


backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n1, (20, 40), n1)



root.mainloop()

#https://stackoverflow.com/questions/23876447/tkinter-overlay-foreground-image-on-top-of-a-background-image-with-transparency