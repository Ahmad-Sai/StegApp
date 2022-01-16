# StegApp

**_What is Steganography?_**

Steganography is a method of hiding plain messages within an image. The point of steganography is to be able to send an image to someone with a hidden message encoded in the bits. Any one that looks at the image will preceive it as a regular image, but only the person who receives it knows that there is a hidden message embedded with in.

This is a Python Steganography GUI application that uses the 2 least significant bits of a pixel to hide plain text messages within images.

  - hideSecret hides a user input string into the selected image
  - getSecret reads hidden strings placed by hideSecret

hideSecret and getSecret are wrapped with Tkinter applets. 

Dependencies:

  - Pillow
  - NumPy
  - Tkinter

To hide your own messages in an image, run the hidSecret.py, and follow the instructions displayed in the application. _**Make sure that the image you use is a .jpg or .jpeg only.**_


**hideSecret.py example**

_Instructions Window_

![image](https://user-images.githubusercontent.com/85080576/149641833-ef830912-04fe-4f1e-b4d7-8d04615925c3.png)

_Options_

![image](https://user-images.githubusercontent.com/85080576/149641850-bf1e2614-6aa4-4ee3-ba77-018ed0b00d3e.png)


_The message that will be hidden_

<img src="https://user-images.githubusercontent.com/85080576/149641869-2de28f25-639f-45d0-b717-c2ca20bdb8ed.png" width="600" height="300" />


_Comparison of the images_

![image](https://user-images.githubusercontent.com/85080576/149641878-5079262b-ee45-4ca9-ab49-8b115b973ad5.png)
  
  
**getSecret.py example**
  
  _Options_
  
![image](https://user-images.githubusercontent.com/85080576/149641902-d7af46cf-fde5-43a2-a824-ed26aefd249f.png)

_Image with hidden Message_

![image](https://user-images.githubusercontent.com/85080576/149641949-fd21548f-d81c-4958-a78f-642821c60a84.png)

_Extracted message_

<img src="https://user-images.githubusercontent.com/85080576/149641869-2de28f25-639f-45d0-b717-c2ca20bdb8ed.png" width="600" height="300" />

_If you choose to save the message, it will save it as a text file, e.g. imagename_message.txt_
