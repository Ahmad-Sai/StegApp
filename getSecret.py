import _tkinter
import PIL
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# global variables
path = ''
message = ''
img = None
img_as_np_array = None
width = None
height = None
popup_window = None
popup_window2 = None

# create window and set title
window = Tk()
window.title('Simple Steganography App')

def close(*args):
    for popup in args:
        if popup != None:
            popup.destroy()

# browse function looks for image on your computer
def clearWidgets(*args):
    for frame in args:
        for widget in frame.winfo_children():
            widget.destroy()

def browse():
    global path, img, img_as_np_array, width, height
    clear()
    close(popup_window, popup_window2)
    clearWidgets(frame1, frame2, frame3)
    
    try:
        path = filedialog.askopenfilename(initialdir='/', title='Select image:',
                                          filetype=(('png', '*.png'), ('jpg', '*.jpg'), ('jpeg', '*.jpeg')))
        img = PIL.Image.open(path)
        width, height = img.size
        img_as_np_array = np.asarray(img, dtype=np.dtype('B'))
        Label(frame1, text=f'Image Selected: {path}').grid(row=0, column=0)

    except AttributeError:
        Label(frame1, text='Select Image').grid(row=0, column=0)

def get_message():
    global message
    if img:
        clearWidgets(frame3)
        last_lsb = img_as_np_array % 2
        second_last_lsb = (img_as_np_array // 2) % 2

        stacked_array = np.stack((second_last_lsb, last_lsb), axis=3)
        flat_array = np.ndarray.flatten(stacked_array)
        bytes_array = flat_array.reshape((width * height * 2 * 3 // 8, 8))
        integer_array = np.packbits(bytes_array, bitorder='big')
        entire_img = ''
        message = ''
        reading_message = False
        indicator_start = '<<<<<'
        indicator_end = '>>>>>'
        for i in integer_array:
            if len(entire_img) >= 5:
                if entire_img[-5:] == indicator_start:
                    reading_message = True
                if reading_message:
                    message += chr(i)
                    if entire_img[-5:] == indicator_end:
                        reading_message = False
                        message = message[:-6]
                        break

            entire_img += chr(i)
        text_window()

def clear():
    global path, message, img, img_as_np_array, width, height

    path = ''
    message = ''
    img = None
    img_as_np_array = None
    width = None
    height = None

def image_window():
    global popup_window
    if img != None:
        popup_window = Toplevel(window)
        popup_window.title('Images')

        resized_im = img.resize((round(img.size[0] * 0.5), round(img.size[1] * 0.5)))
        tk_img = ImageTk.PhotoImage(resized_im)
        image = Label(popup_window, image=tk_img)
        image.image = tk_img
        Label(popup_window, text='Image').grid(row=0, column=0)
        image.grid(row=1, column=0)

        popup_window.mainloop()

def text_window():
    global popup_window2
    try:
        if message != '':
            close(popup_window2)
            popup_window2 = Toplevel(window)
            popup_window2.title('Text')

            text_box = Text(popup_window2)
            text_box.insert(INSERT, message)
            text_box.config(state=DISABLED)
            text_box.grid(row=2, column=0)
            Label(popup_window2, text='Your Message').grid(row=2, column=1)
            Label(frame2, text='Message displayed').grid(row=1, column=0)
           
            popup_window2.mainloop()
        elif img and message == '':
            Label(frame2, text='No Message Found in this image').grid(row=1, column=0)
        else:
            Label(frame2, text='Submit your image first').grid(row=1, column=0)
    except _tkinter.TclError:
        pass

def save():
    if message != '':
        clearWidgets(frame3)
        file_name = path[:-4] + ' message.txt'
        with open(file_name, 'w') as f:
            f.write(message)
        Label(frame3, text=f'Message saved at {file_name}').grid(row=2, column=0)
    elif message=='':
        Label(frame3, text='Show Message First').grid(row=2, column=0)
# widgets used in GUI

# -------------------------
frame1 = Frame(window)
frame1.grid(row=0, column=0)

Label(frame1, text=f'Select Image').grid(row=0, column=0)
browse_button = Button(window, text='Browse',command=lambda: [browse(), image_window()])
browse_button.grid(row=0, column=1)
# ------------------------
frame2 = Frame(window)

frame2.grid(row=1, column=0)

submit_button = Button(window, text='Show Message', command=lambda: [get_message(), text_window()])
submit_button.grid(row=1, column=1)
# ------------------------
frame3 = Frame(window)
frame3.grid(row=2, column=0)

save_button = Button(window, text='Save', command=save)
save_button.grid(row=2, column=1)

window.mainloop()
