import PIL
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# create window and set title
window = Tk()

screen_width = str(window.winfo_screenwidth()//12)
screen_height = str(window.winfo_screenheight()//12)
window.geometry(f'+{screen_width}+{screen_height}')
window.resizable(width=False, height=False)

window.title('Simple Steganography App')



# global variables
path = ''
msg = ''
img = None
img_as_np_array = None
width = None
height = None
message_list = []
new_image = None
enter_message = ''
popup_window = None
popup_window2 = None

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
    clearWidgets(frame1, frame3, frame4)
    close(popup_window, popup_window2)
    
    try:
        path = filedialog.askopenfilename(initialdir='/', title='Select image:',
                                          filetype=(('png', '*.png'), ('jpg', '*.jpg'), ('jpeg', '*.jpeg')))
        img = PIL.Image.open(path)
        width, height = img.size
        img_as_np_array = np.asarray(img, dtype=np.dtype('B'))
        Label(frame1, text=f'Image Selected: {path}').grid(row=0, column=0)

    except AttributeError:
        Label(frame1, text='Select Image').grid(row=0, column=0)


def clear():
    global path, msg, img, img_as_np_array, width, height, \
        message_list, msg_in_pic, new_image, enter_message

    path = ''
    msg = ''
    img = None
    img_as_np_array = None
    width = None
    height = None
    message_list = []
    new_image = None
    enter_message = ''


# submit function submits the message entered into the entry box
def submit():
    global msg, message_list, enter_message
    close(popup_window, popup_window2)

    try:
            
        if len(entry.get()) > ((width*height*3)*2)/8:
            Label(frame3, text='Message too long').grid(row=3, column=0)
        else:
            if entry.get() != '':
                    clearWidgets(frame3)
                                        
            msg = entry.get()
            enter_message = entry.get()
            msg = f"<<<<<{msg}>>>>>"

            message_list = []
            for i in range(len(msg)):
                byte = (format(ord(msg[i]), ("08b")))
                message_list.append(int(byte[0:2], 2))
                message_list.append(int(byte[2:4], 2))
                message_list.append(int(byte[4:6], 2))
                message_list.append(int(byte[6:8], 2))

            message_list = np.array(message_list)
            rand_int2 = np.random.randint(0, 4, (width * height * 3))
            length = len(message_list)
            rand_int2[0:length] = message_list
            message_list = np.reshape(rand_int2, (height, width, 3))
            entry.delete(0, "end")
    except AttributeError:
        pass
    except TypeError:
        pass


# create and show functions makes the image with the submited message
def create_and_show():
    global new_image
    if enter_message != '':
        try:
            last_lsb = img_as_np_array % 2
            second_last_lsb = (img_as_np_array // 2) % 2

            msg_in_pic = img_as_np_array - (last_lsb + 2 * second_last_lsb) + message_list

            new_image = Image.fromarray(msg_in_pic.astype('uint8'))
            Label(frame3, text="Image Created with Message").grid(row=3, column=0)
            done = True
            image_window()
        except ValueError:
            Label(frame3, text='Submit Message First').grid(row=3, column=0)
        except AttributeError:
            Label(frame3, text='Error Occurred With Selected Image, Try Again').grid(row=3, column=0)
        except TypeError:
            Label(frame3, text='Must Select Image First').grid(row=3, column=0)
    else:
        Label(frame3, text='Submit Image then submit message').grid(row=3, column=0)

def image_window():
    global popup_window
    popup_window = Toplevel(window)
    popup_window.resizable(width=False, height=False)
    popup_window.title('Images')

    try:
        resized_im = img.resize((round(img.size[0] * 0.5), round(img.size[1] * 0.5)))
        tk_img = ImageTk.PhotoImage(resized_im)
        image = Label(popup_window, image=tk_img)
        image.image = tk_img
        Label(popup_window, text='Old Image').grid(row=0, column=0)
        image.grid(row=1, column=0)

        resized_im2 = new_image.resize((round(new_image.size[0] * 0.5), round(new_image.size[1] * 0.5)))
        tk_img2 = ImageTk.PhotoImage(resized_im2)
        image2 = Label(popup_window, image=tk_img2)
        image2.image = tk_img2
        Label(popup_window, text='New Image').grid(row=0, column=1)
        image2.grid(row=1, column=1)
    except TypeError:
        Label(frame4, text='Must Select Image First').grid(row=4, column=0)

    popup_window.mainloop()


def text_window():
    global popup_window2
    if enter_message != '':
        popup_window2 = Toplevel(window)
        popup_window2.resizable(width=False, height=False)
        popup_window2.title('Text')
        
        text_box = Text(popup_window2)
        text_box.insert(INSERT, enter_message)
        text_box.config(state=DISABLED)
        text_box.grid(row=2, column=0)
        Label(popup_window2, text='Your Message').grid(row=2, column=1)
        
        popup_window2.mainloop()

def instructions():
    popup_window = Toplevel(window)
    popup_window.resizable(width=False, height=False)
    popup_window.title('Insctructions')
    
    Label(popup_window, text="Instructions").grid(row=5, column=0, columnspan=2)
    Label(popup_window, text="1. Choose Image that you want to hide message in").grid(row=6, column=0, columnspan=2)
    Label(popup_window, text="2. Enter Message in Text Box and Submit").grid(row=7, column=0, columnspan=2)
    Label(popup_window, text="3. Press Create and Show Button to see new image").grid(row=8, column=0, columnspan=2)
    Label(popup_window, text="4. (optional) Save").grid(row=9, column=0, columnspan=2)
    
    popup_window.mainloop()

# save function saves the newly created image
def save():
    clearWidgets(frame4)
    try:
        newpath = path[:-4] + ' msg.png'
        new_image.save(newpath)
        Label(frame4, text=f'Saved at {newpath}').grid(row=4, column=0)
    except TypeError:
        Label(frame4, text='Must Select Image First').grid(row=4, column=0)
    except AttributeError:
        Label(frame4, text='No Image to Save').grid(row=4, column=0)


# widgets used in GUI

# -------------------------

frame1 = Frame(window)
frame1.grid(row=0, column=0)

Label(frame1, text=f'Select Image').grid(row=0, column=0)
browse_button = Button(window, text='Browse', command=browse)
browse_button.grid(row=0, column=1)
# ------------------------
entry = Entry(window, width=80)
entry.grid(row=1, column=0)
# ------------------------
submit_button = Button(window, text='Submit Message', command=lambda: [submit(), text_window()])
submit_button.grid(row=1, column=1)
# ------------------------
frame3 = Frame(window)
frame3.grid(row=3, column=0)

create_and_show_button = Button(window, text='Create and Show', command=create_and_show)
create_and_show_button.grid(row=3, column=1)
# ------------------------
frame4 = Frame(window)
frame4.grid(row=4, column=0)

save_button = Button(window, text='Save', command=save)
save_button.grid(row=4, column=1)

instructions()

window.mainloop()
