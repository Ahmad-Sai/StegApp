# StegApp

What is Steganography?

Steganography is a method of hiding plain messages within an image. The point of steganography is to be able to send an image to someone with a hidden message encoded in the bits. Any one that looks at the image will preceive it as a regular image, but only the person who receives it knows that there is a hidden message embedded with in.

A Python Steganography GUI application that uses 2 least significant bits to hide messages in images.

  - hideSecret hides a user input string into the selected image
  - getSecret reads hidden strings placed by hideSecret

hideSecret and getSecret are wrapped with Tkinter applets. 

Dependencies:

  - Pillow
  - NumPy
  - Tkinter

To hide your own messages in an image, run the hidSecret.py, and follow the instructions display in the application. Make sure that your image is a .jpg or .jpeg

Display Menu Options:

![image](https://user-images.githubusercontent.com/85080576/149425451-7f3585e7-ac75-40fe-a918-329524272d2c.png)

After embedding a message in an image:

![image](https://user-images.githubusercontent.com/85080576/149426114-27921ff4-227a-4fe9-9ac2-ce07d78d1989.png)

