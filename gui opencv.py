from tkinter import *
import numpy as np
import cv2
import matplotlib.pyplot as  plt
from PIL import ImageTk, Image
a= "images.JPG "
win=Tk()
win.title("PHOTO EDITOR ")
win.geometry("1500x1500")
win.configure(background="black")
l=Label(win,text="SPHOTO EDITOR",height=2,font=20)
l1=Label(win,text="",height=1,bg="black")
l2=Label(win,text="",height=1,bg="black")
l3=Label(win,text="",height=1,bg="black")
l6=Label(win,text="",height=1,bg="black")
l4=Label(win,text="            ",height=10,bg="black")
l5=Label(win,text="            ",height=10,bg="black")
imgl=Label(win,text="           ",bg="white")
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
     image=cv2.imshow('win', img)
  

b=Button(win,text="INCREASE NOISE",command=salt,activebackground="pink",activeforeground="green",height=5,bg="gray")
l.grid(row=2,column=4)
l.config(width=30)
l.config(font=("Old English Text MT", 20))
l3.grid(row=3,column=2)
b.grid(row=4,column=2)
b.config(width=20)
b.config(font=("Bernard MT Condensed", 15))
l1.grid(row=5,column=2)
b1=Button(win,text="ADJUST LIGHT",command=light,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b1.grid(row=6,column=2)
b1.config(width=20)
b1.config(font=("Bernard MT Condensed", 15))
l2.grid(row=7,column=2)
b2=Button(win,text="BINARY",command=binary,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b2.grid(row=8,column=2)
b2.config(width=20)
b2.config(font=("Bernard MT Condensed", 15))
l4.grid(row=4,column=3)
b3=Button(win,text="GRAY",command=grayscale,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b3.grid(row=4,column=4)
b3.config(width=20)
b3.config(font=("Bernard MT Condensed", 15))
b4=Button(win,text="AVERAGE",command=averge,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b4.grid(row=6,column=4)
b4.config(width=20)
b4.config(font=("Bernard MT Condensed", 15))
b5=Button(win,text="ORIGNINAL",command=orignal,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b5.grid(row=8,column=4)
b5.config(width=20)
b5.config(font=("Bernard MT Condensed", 15))
l5.grid(row=4,column=5)
b6=Button(win,text="BLUR",command=blur,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b6.grid(row=4,column=6)
b6.config(width=20)
b6.config(font=("Bernard MT Condensed", 15))
b7=Button(win,text="RED",command=red,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b7.grid(row=6,column=6)
b7.config(width=20)
b7.config(font=("Bernard MT Condensed", 15))
b8=Button(win,text="GREEN",command=green,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b8.grid(row=8,column=6)
b8.config(width=20)

l6.grid(row=9,column=6)
b8.config(font=("Bernard MT Condensed", 15))
b9=Button(win,text="BLUE",command=blue,activebackground="green",activeforeground="yellow",height=5,font=20,bg="gray")
b9.grid(rows=10,column=4)
b9.config(width=20)
b9.config(font=("Bernard MT Condensed", 15))
imgl.grid(row=4,column=7)


win.mainloop()

