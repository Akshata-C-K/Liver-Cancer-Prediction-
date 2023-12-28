#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import tkinter as tk
from csv import *
from PIL import ImageTk,Image
from tkinter import messagebox

base = Tk()
base.geometry('1000x1000')
base.title("LIVER CANCER PREDICTION")
img = Image.open(r"C:\Users\Akshata C K\Desktop\front\liver.png")
bg = ImageTk.PhotoImage(img)
label = Label(base,image=bg)
label.place(x=0,y=0,width=1300,height=1300)
main_lst=[]

def Save():
   with open("test.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Age","Gender","Total_Bilirubin","Direct_Bilirubin","Alkaline_Phosphotase","Alamine_Aminotransferase","Aspertate_Aminotransferase","Total Proteins","Albumin","Albumin_and_Globulin_Ratio","Globulin"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved succesfully")

labl_0 = Label(base, text="LIVER CANCER PREDICTION", width=70, font=("bold", 20))
labl_0.place(x=120, y=53)

labl_1 = Label(base, text="Age", width=20, font=("bold", 10))
labl_1.place(x=500, y=130)

entry_1 = Entry(base)
entry_1.place(x=740, y=130)

labl_2 = Label(base, text="Gender", width=20, font=("bold", 10))
labl_2.place(x=500, y=180)

entry_02 = Entry(base)
entry_02.place(x=740, y=180)

labl_3 = Label(base, text="Total_Bilirubin", width=20, font=("bold", 10))
labl_3.place(x=500, y=230)

entry_02 = Entry(base)
entry_02.place(x=740, y=230)

labl_4 = Label(base, text="Direct_Bilirubin", width=20, font=("bold", 10))
labl_4.place(x=500, y=280)

entry_02 = Entry(base)
entry_02.place(x=740, y=280)

labl_5 = Label(base, text="Alkaline_Phosphotase", width=20, font=("bold", 10))
labl_5.place(x=500, y=330)

entry_02 = Entry(base)
entry_02.place(x=740, y=330)

labl_6 = Label(base, text="Alamine_Aminotransferase", width=20, font=("bold", 10))
labl_6.place(x=500, y=380)

entry_02 = Entry(base)
entry_02.place(x=740, y=380)

labl_7 = Label(base, text="Aspertate_Aminotransferase", width=20, font=("bold", 10))
labl_7.place(x=500, y=430)

entry_02 = Entry(base)
entry_02.place(x=740, y=430)

labl_8 = Label(base, text="Total Proteins", width=20, font=("bold", 10))
labl_8.place(x=500, y=480)

entry_02 = Entry(base)
entry_02.place(x=740, y=480)

labl_9 = Label(base, text="Albumin", width=20, font=("bold", 10))
labl_9.place(x=500, y=530)

entry_02 = Entry(base)
entry_02.place(x=740, y=530)

labl_10 = Label(base, text="Albumin_and_Globulin_Ratio", width=20, font=("bold", 10))
labl_10.place(x=500, y=580)

entry_02 = Entry(base)
entry_02.place(x=740, y=580)

labl_10 = Label(base, text="Globulin", width=20, font=("bold", 10))
labl_10.place(x=500, y=630)

entry_02 = Entry(base)
entry_02.place(x=740, y=630)


Button(base, text='Save', width=20, bg='brown', fg='white').place(x=530, y=680)
entry_02 = Entry(base)
entry_02.place(x=500, y=730, width=400)
Button(base, text='Submit', width=20, bg='brown', fg='white').place(x=730, y=680)

# it will be used for displaying the registration form onto the window
entry_02 = Entry(base)
entry_02.place(x=500, y=730, width=400,height=30)
Button(base, text='Exit', width=20, bg='brown', fg='white').place(x=630, y=770)


base.mainloop()
print(main_lst)


