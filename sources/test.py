import tkinter as tk



root = tk.Tk()

# Create a Text widget
text_widget = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_widget.insert(tk.END, "Button Clicked!\n")
text_widget.pack()

# Insert some text
text_widget.insert(tk.END, "This is some text.\n")

# Create a Button widget
button = tk.Entry(root, text="Click me!")

# Insert the Button after the text
text_widget.window_create(tk.END, window=button)

root.mainloop()
