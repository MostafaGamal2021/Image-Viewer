from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images with MGA')
#root.geometry('650x500')
root.iconbitmap('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\Images\moon.ico')

my_image = ImageTk.PhotoImage(Image.open('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\photos\shells.jpg'))
my_label = Label(image = my_image)
my_label.pack()

exit_button = Button(root, text = 'EXIT', padx = 30, pady = 10, bg = 'yellow', fg = 'red', command = root.quit)
exit_button.pack()


root.mainloop()