from tkinter import *
import numpy as np
import cv2
import matplotlib.pyplot as  plt
from PIL import ImageTk, Image
a= "images.JPG "
win=Tk()
win.title("PHOTO EDITOR ")
win.geometry("1000x1000")
win.configure(background="black")
l=Label(win,text="PHOTO EDITOR")
def adjust_light(img):
	lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
	#split channels
	l, a, b = cv2.split(lab)
	
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(3,3))
	cl = clahe.apply(l)

	limg = cv2.merge((cl,a,b))

	final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
	return final
def orignal():
                 global a
                 img = cv2.imread(a)
                 kernel = np.ones((5,5),np.float32)/25
                 dst = cv2.filter2D(img,-1,kernel)
                 plt.subplot(121),plt.imshow(img),plt.title('win')
                 plt.xticks([]), plt.yticks([])
                 plt.show("win")
def blur():
                 global a

                 img = cv2.imread(a)

                 blur = cv2.blur(img,(5,5))
                 plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
                 plt.xticks([]), plt.yticks([])
                 plt.show()
def green():
        global a
        
        image = cv2.imread(a)
        image[:,:,0:1]=0
        cv2.imshow("win",image)
def blue():
        global a
        
        image = cv2.imread(a)
        image[:,:,1:3]=0
        cv2.imshow("win",image)
                
            
def red():
        global a
        
        image = cv2.imread(a)
        image[:,:,0:2]=0
        cv2.imshow("win",image)

def averge():
                global a
                img = cv2.imread(a)
                kernel = np.ones((5,5),np.float32)/25
                dst = cv2.filter2D(img,-1,kernel)

                
                plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
                plt.xticks([]), plt.yticks([])
                plt.show("win")

        
def saltPepper(image):
	#row,col,ch = image.shape
	s_vs_p = 0.8 
	amount = 0.4
	out = np.copy(image)
	# Salt mode
	num_salt = np.ceil(amount * image.size * s_vs_p)
	coords = [np.random.randint(0, i - 1, int(num_salt))
		  for i in image.shape]
	out[coords] = 150

	# Pepper mode
	num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
	coords = [np.random.randint(0, i - 1, int(num_pepper))
		  for i in image.shape]
	out[coords] = 50
	return out

        
def binary():
         global a
         im_gray = cv2.imread(a, 0)
         (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
         thresh = 127
         im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
         cv2.imshow("win",im_bw)



def grayscale():
         global a
         im_gray=cv2.imread(a,0)
         cv2.imshow("win",im_gray)
def salt():
     global a
    
     img=cv2.imread(a,1)
     img = saltPepper(img)
     cv2.imshow('win', img)
def light():
     global a
     img=cv2.imread(a,1)
     img =adjust_light (img)
     cv2.imshow('win', img)


b=Button(win,text="increase noise on image",command=salt,activebackground="pink",activeforeground="green",height=3,font=20,bg="gray")
l.grid(rowspan=2,columnspan=2)
b.grid(rowspan=4,columnspan=2)
b1=Button(win,text="adjust lighht on image",command=light,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b1.grid(rowspan=6,columnspan=2)
b2=Button(win,text="convert to binary",command=binary,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b2.grid(rowspan=2,columnspan=3)
b3=Button(win,text="convert to gray scale",command=grayscale,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b3.grid(rowspan=4,columnspan=3)
b4=Button(win,text="Averge",command=averge,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b4.grid(rowspan=6,columnspan=3)
b5=Button(win,text="convert to original",command=orignal,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b5.grid(rowspan=2,columnspan=4)
b6=Button(win,text="blur",command=blur,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b6.grid(rowspan=4,columnspan=4)
b7=Button(win,text="red channal",command=red,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b7.grid(rowspan=6,columnspan=4)
b8=Button(win,text="green channal",command=green,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b8.grid(rowspan=2,columnspan=5)
b9=Button(win,text="blue channal",command=blue,activebackground="green",activeforeground="yellow",height=3,font=20,bg="gray")
b9.grid(rowspan=4,columnspan=5)

win.mainloop()
