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