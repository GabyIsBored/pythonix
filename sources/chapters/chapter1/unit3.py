from markdown import setTextWidget
import tkinter as tk
root=tk.Tk()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=tk.Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 34, "bold")
mainFrame.configure(bg='#D9D9D9')

unit_content1='''# Commentaires

On peut aussi mettre une phrase ne faisant pas partie du programme afin de mettre des commentaires en la commençant par #, ou en la plaçant entre trois guillemets:
'''
code_block1='''
print('Voici un message') # Ce commentaire n'affecte pas le statement
'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code')]
unit_title = 'Commentaires'

import chapters.chapter2.unit1 as nextFrame
from markdown import setTextWidget
import tkinter as tk
class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()
        self.root = master
        for block in unit_content:
            self.widget=tk.Text(master)
            setTextWidget(self.widget,block[0],block[1]) 
            self.widget.pack()   
        continuerImg=tk.PhotoImage(file='sources\assets\ElementDivers\continuer.png')
        self.nextButton = tk.Button(master,image=continuerImg,command=nextPage)
        def nextPage():
            nextFrame.Content(master)