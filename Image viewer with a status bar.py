from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images with MGA')
root.geometry('650x520')
root.iconbitmap('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\Images\moon.ico')

my_image1 = ImageTk.PhotoImage(Image.open('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\photos\shells.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\photos\Roses.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\photos\waterfall.jpg'))
my_image4 = ImageTk.PhotoImage(Image.open('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\photos\sunset.jpg'))
my_image5 = ImageTk.PhotoImage(Image.open('D:\Python\Level 2\Codemy\Python And TKinter\PYTkinter\photos\leaf.jpg'))

images_list = [my_image1, my_image2, my_image3, my_image4, my_image5]
my_label = Label(image = my_image1)
my_label.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image = images_list[image_number-1])
    button_back = Button(root, text='back   <<', padx=30, pady=10, fg='blue', bg='yellow', command=lambda: back(image_number-1))
    button_forward = Button(root, text='>>   forward', padx=30, pady=10, fg='blue', bg='yellow', command=lambda: forward(image_number+1))
    if image_number == 5:
        button_forward = Button(root, text='>>   forward', padx=30, pady=10, fg='blue', bg='yellow', state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text=f"     Image {image_number} of {len(images_list)}     ", bd=3, relief=SUNKEN, fg='blue', bg='white', anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = Label(image=images_list[image_number - 1])

    button_back = Button(root, text='back   <<', padx=30, pady=10, fg='blue', bg='yellow', command=lambda: back(image_number - 1))
    button_forward = Button(root, text='>>   forward', padx=30, pady=10, fg='blue', bg='yellow', command=lambda: forward(image_number + 1))
    if image_number == 1:
        button_back = Button(root, text='back   <<', padx=30, pady=10, fg='blue', bg='yellow', state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text=f"     Image {image_number} of {len(images_list)}     ", bd=3, relief=SUNKEN, fg='blue', bg='white', anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

status = Label(root, text = f"     Image 1 of {len(images_list)}     ", bd = 3, relief = SUNKEN, fg = 'blue', bg = 'white', anchor = E)
status.grid(row = 2, column = 0, columnspan = 3, sticky=W+E)

exit_button = Button(root, text = 'EXIT', padx = 30, pady = 10, bg = 'yellow', fg = 'red', command = root.quit)
exit_button.grid(row = 1, column = 1, pady = 5)

button_back = Button(root, text = 'back   <<', padx = 30, pady = 10, fg = 'blue', bg = 'yellow', command = lambda: back, state = DISABLED)
button_back.grid(row = 1, column = 0)

button_forward = Button(root, text = '>>   forward', padx = 30, pady = 10, fg = 'blue', bg = 'yellow', command = lambda: forward(2))
button_forward.grid(row = 1, column = 2)

root.mainloop()