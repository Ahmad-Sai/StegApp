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

To hide your own messages in an image, run the hidSecret.py, and follow the instructions display in the application. _**Make sure that your image is a .jpg or .jpeg only.**_

**_Hiding Text Example_**

Display Menu Options:

<img src="https://user-images.githubusercontent.com/85080576/149425451-7f3585e7-ac75-40fe-a918-329524272d2c.png" width="600" height="250" />

After embedding a message in an image:

<img src="https://user-images.githubusercontent.com/85080576/149426114-27921ff4-227a-4fe9-9ac2-ce07d78d1989.png" width="600" height="300" />

_If you choose to save the image, then your image will be save as image_msg.jpg_

Image Comparison of before and after the message was embedded in the image:

<img src="https://user-images.githubusercontent.com/85080576/149428273-d90cfbe7-e99b-4466-83af-d7792db3cf6e.png" width="600" height="250" />



**_Retreiving Text Example_**

Display Menu Options:

![image](https://user-images.githubusercontent.com/85080576/149437904-2cc15db8-0c9f-4b45-a687-8b5e10e6dca8.png)

Message and image after extraction:

<img src="https://user-images.githubusercontent.com/85080576/149426114-27921ff4-227a-4fe9-9ac2-ce07d78d1989.png" width="600" height="300" />

_If you choose to save the message, it will save it as a text file, e.g. imagename_message.txt_






















Example of hideSecret.py running

_Menu options:_

![image](https://user-images.githubusercontent.com/85080576/149641833-ef830912-04fe-4f1e-b4d7-8d04615925c3.png)

_Instructions Window:_

![image](https://user-images.githubusercontent.com/85080576/149641850-bf1e2614-6aa4-4ee3-ba77-018ed0b00d3e.png)


_The message that will be hidden:_

![image](https://user-images.githubusercontent.com/85080576/149641869-2de28f25-639f-45d0-b717-c2ca20bdb8ed.png)_


_Comparison of the images. Before and after._

![image](https://user-images.githubusercontent.com/85080576/149641878-5079262b-ee45-4ca9-ab49-8b115b973ad5.png)
  
  
  Example if getSecret.py running:
  

![image](https://user-images.githubusercontent.com/85080576/149641902-d7af46cf-fde5-43a2-a824-ed26aefd249f.png)

![image](https://user-images.githubusercontent.com/85080576/149641949-fd21548f-d81c-4958-a78f-642821c60a84.png)

![image](https://user-images.githubusercontent.com/85080576/149641869-2de28f25-639f-45d0-b717-c2ca20bdb8ed.png)
