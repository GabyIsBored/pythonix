import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk

from chapter3.unit1 import mainFrame as frame_unit1
from chapter3.unit2 import mainFrame as frame_unit2
from chapter3.unit3 import mainFrame as frame_unit3
from chapter3.unit4 import mainFrame as frame_unit4
from chapter3.quiz1 import mainFrame as frame_quiz1
# from chapter3.quiz2 import mainFrame as frame_quiz2
# from chapter3.quiz3 import mainFrame as frame_quiz3
# from chapter3.quiz4 import mainFrame as frame_quiz4
# from chapter3.megaquiz import mainFrame as frame_megaquiz

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

def enter(pageName):
    print('yo')

backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n2, (40, 80), n2)

tkimage = ImageTk.PhotoImage(backgroundImage)
background = tk.Label(mainFrame,image=tkimage)
background.pack()


el1=tk.Button(mainFrame,command=lambda:enter('unit1'))
el1.place(x=20,y=40)


backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n1, (20, 40), n1)
backgroundImage.paste(n1, (20, 40), n1)



App.mainloop()

#https://stackoverflow.com/questions/23876447/tkinter-overlay-foreground-image-on-top-of-a-background-image-with-transparency