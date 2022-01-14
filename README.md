# StegApp

**What is Steganography?**

Steganography is a method of hiding plain messages within an image. The point of steganography is to be able to send an image to someone with a hidden message encoded in the bits. Any one that looks at the image will preceive it as a regular image, but only the person who receives it knows that there is a hidden message embedded with in.

This is a Python Steganography GUI application that uses the 2 least significant bits of a pixel to hide plain text messages within images.

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

_If you choose to save, then your image will be save as image_msg.jpg_

Image Comparison of before and after the message was embedded in the image:

![image](https://user-images.githubusercontent.com/85080576/149428273-d90cfbe7-e99b-4466-83af-d7792db3cf6e.png)
