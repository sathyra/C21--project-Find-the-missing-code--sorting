import numpy as np
from tkinter import *
root=Tk()
root.geometry("600x400")
arr1 = np.array([3, 2, 0, 1])
arr2 = np.array(['banana', 'cherry', 'apple'])

#Defining the sorting function
def srt_ar_asc():
    #write a code to sort in ascending
    label.config(text=newarr3)

def srt_ar_dsc():
    #write a code to sort in descending
    label.config(text=newarr3)

def srt_txt_asc():
    #write a code to sort the text 
    label.config(text=newarr4)

#display the array elements
Message(root, text= arr1,bg='light blue', font = 50).pack()

#Write a code to create a ascending button

#Write a code to create a descending button

#Button and text elements
Message(root, text= arr2,bg='light blue', font = 50).pack()
Button(root, text="Sort Text", command=srt_txt_asc).pack(pady=20)

#Write a code to display the output using the label
label.pack()
root.mainloop()
