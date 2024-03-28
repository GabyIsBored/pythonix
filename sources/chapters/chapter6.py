import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk

root=tk.Tk()
root.title('el1')
root.geometry('1280x720')
root.resizable(False,False)

mainFrame=ScrolledFrame(root)
mainFrame.autohide_scrollbar()
mainFrame.pack(expand=True, fill='both')

background=tk.PhotoImage(file='sources/assets/ChapterSelectionBackgrounds/Boucles.png')
n1=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau1.png')
n2=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau2.png')
n3=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau3.png')
n4=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau4.png')
n5=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau5.png')
quiz=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/quiz.png')
megaQuiz=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Mega quiz.png')



def enter(event):
    print('yo')

canvas = tk.Canvas(mainFrame,width=background.width(),height=background.height(), highlightthickness=0, bd=0)
backgroundImg = canvas.create_image(0, 0, image=background, anchor="nw")
n1Img = canvas.create_image(476, 268, image=n1, anchor="nw")
q1Img = canvas.create_image(331, 644, image=quiz, anchor="nw")
n2Img = canvas.create_image(419, 1275, image=n2, anchor="nw")
q2Img = canvas.create_image(806, 996, image=quiz, anchor="nw")
n3Img = canvas.create_image(806, 1756, image=n3, anchor="nw")
q3Img = canvas.create_image(192, 1546, image=quiz, anchor="nw")
n4Img = canvas.create_image(213, 2139, image=n4, anchor="nw")
q4Img = canvas.create_image(726, 2122, image=quiz, anchor="nw")
n5Img = canvas.create_image(737, 2503, image=n5, anchor="nw")
q5Img = canvas.create_image(429, 2715, image=quiz, anchor="nw")
mImg = canvas.create_image(549, 3102, image=megaQuiz, anchor="nw")
canvas.tag_bind(n1Img, "<Button-1>", enter)
canvas.tag_bind(q1Img, "<Button-1>", enter)
canvas.tag_bind(n2Img, "<Button-1>", enter)
canvas.tag_bind(q2Img, "<Button-1>", enter)
canvas.tag_bind(n3Img, "<Button-1>", enter)
canvas.tag_bind(q3Img, "<Button-1>", enter)
canvas.tag_bind(q4Img, "<Button-1>", enter)
canvas.tag_bind(n4Img, "<Button-1>", enter)
canvas.tag_bind(n5Img, "<Button-1>", enter)
canvas.tag_bind(q5Img, "<Button-1>", enter)

canvas.tag_bind(mImg, "<Button-1>", enter)
canvas.pack()


root.mainloop()

#https://stackoverflow.com/questions/23876447/tkinter-overlay-foreground-image-on-top-of-a-background-image-with-transparency