from csv import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

window=Tk()
window.title("Data Entry")
window.geometry("800x800")
window.title("LIVER CANCER PREDICTION")
lst=[]
main_lst=[]

def Add():
   lst=[Age.get(), Gender.get(), Total_Bilirubin.get(), Direct_Bilirubin.get(), Alkaline_Phosphotase.get(), Alamine_Aminotransferase.get(), Aspertate_Aminotransferase.get(),Total_Proteins.get(), Albumin.get(), Albumin_and_Globulin_Ratio.get(), Dataset.get()]
   main_lst.append(lst)
   messagebox.showinfo("Information","The data has been added successfully")

def Save():
   with open("test.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Age","Gender","Total_Bilirubin","Direct_Bilirubin","Alkaline_Phosphotase","Alamine_Aminotransferase","Aspertate_Aminotransferase","Total_Proteins","Albumin","Albumin_and_Globulin_Ratio","Dataset"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved succesfully")

def MLP():
   data = pd.read_csv(r"C:\Users\Akshata C K\Desktop\new liver cancer\datasets_2607_4342_indian_liver_patient_labelled.csv")
   data.head()

   # In[5]:

   data

   # In[6]:

   df = pd.DataFrame(data)

   # In[7]:

   for col in df.columns:
      df[col] = df[col].fillna(0)

   # In[8]:

   headers = list(df.columns)
   headers.remove('Dataset')
   # headers.remove('Gender')
   headers

   # In[9]:

   # pd.get_dummies(df['Gender'], prefix='Gender')
   df = pd.concat([df, pd.get_dummies(data['Gender'], prefix='Gender')], axis=1)
   print(df)

   # In[10]:

   headers.remove('Gender')

   # In[11]:

   X = df[headers]
   print(X)
   Y = df['Dataset']

   print(Y)

   # In[12]:

   df['Dataset'] = df['Dataset'].replace([1], 0)
   df['Dataset'] = df['Dataset'].replace([2], 1)
   print(df['Dataset'])

   # In[13]:

   scaler = StandardScaler()
   scaler.fit(X)
   print(X)
   X = scaler.transform(X)
   print(X)

   # In[14]:

   clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2,), random_state=1, max_iter=2000)
   clf.fit(X, Y)

   # In[15]:

   Y_pred = clf.predict(X)
   print(Y_pred)

   def cal_average(Y_pred):
      sum_Y_pred = 0
      for t in Y_pred:
         sum_Y_pred = sum_Y_pred + t

         avg = sum_Y_pred / len(Y_pred)
         return avg

   print("The average is :", cal_average(Y_pred))

   # In[16]:

   print("The loss is", clf.loss_)
   print("Mean accuracy is", clf.score(X, Y))

   # In[17]:

   comparison_dict = {}
   solvers = ['lbfgs', 'sgd', 'adam']
   activation_functions = ['identity', 'logistic', 'tanh', 'relu']
   hidden_layer_sizes = [(2,), (3,), (5,), (2, 2,), (3, 2,), (5, 2,)]
   # learning_rates = ['constant', 'invscaling', 'adaptive'] # only for sgd

   # In[18]:

   count = 1
   for solver in solvers:
      for ac in activation_functions:
         for hidden_layer_config in hidden_layer_sizes:
            clf = MLPClassifier(solver=solver, alpha=1e-5, hidden_layer_sizes=hidden_layer_config, random_state=1,
                                max_iter=5000, activation=ac)
            clf.fit(X, Y)
            comparison_dict[count] = {"solver": solver, "activation_function": ac, "hidden_layers": hidden_layer_config,
                                      "accuracy": clf.score(X, Y), "loss": clf.loss_}
            count += 1

   # In[19]:

   comparison_dict

   # In[21]:

   comparison_df = pd.DataFrame(comparison_dict).T
   print(comparison_df)

   # In[22]:

   comparison_df

   # In[23]:

   comparison_df['accuracy'] = pd.to_numeric(comparison_df['accuracy'])

   # In[24]:

   max_acc_index = comparison_df['accuracy'].idxmax()
   row = comparison_df.loc[max_acc_index]
   print("The best accuracy is at")
   print(row)

   # In[26]:

   data1 = pd.read_csv(r"C:\Users\Akshata C K\Desktop\new liver cancer\test.csv")
   print(data1)

   # In[27]:

   data1

   # In[28]:

   df1 = pd.DataFrame(data1)

   # In[29]:

   for col in df1.columns:
      df1[col] = df1[col].fillna(0)

   # In[30]:

   print(df1)

   # In[31]:

   df1

   # In[33]:

   df1 = pd.concat([df1, pd.get_dummies(data1['Gender'], prefix='Gender')], axis=1)
   print(df1)

   # In[43]:

   X = df1[headers]
   print(X)
   Y = df1['Dataset']
   print(Y)

   # In[44]:

   df1['Dataset'] = df1['Dataset'].replace([1], 0)
   df1['Dataset'] = df1['Dataset'].replace([2], 1)
   print(df1['Dataset'])
   df1

   # In[45]:

   scaler = StandardScaler()
   scaler.fit(X)
   X = scaler.transform(X)

   # In[46]:

   clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2,), random_state=1, max_iter=2000)
   clf.fit(X, Y)

   # In[47]:

   output_pred = clf.predict(X)

   # In[48]:

   output_pred

   avg = 0.0
   if (avg == output_pred):
      print("Cancer not detected")
      Label(window,text='CANCER NOT DETECTED',font='40').place(x=500,y=500)
   else:
      print("cancer detected")
      Label(window, text='CANCER DETECTED', font='40').place(x=500, y=500)

def Clear(Aspartate_Aminotransferase=None):
   Age.delete(0,END)
   Gender.delete(0,END)
   Total_Bilirubin.delete(0,END)
   Direct_Bilirubin.delete(0, END)
   Alkaline_Phosphotase.delete(0, END)
   Alamine_Aminotransferase.delete(0, END)
   Aspertate_Aminotransferase.delete(0, END)
   Total_Proteins.delete(0, END)
   Albumin.delete(0, END)
   Albumin_and_Globulin_Ratio.delete(0, END)
   Dataset.delete(0, END)




# 3 labels, 4 buttons,3 entry fields
label1=Label(window,text="Age: ",padx=20,pady=10)
label2=Label(window,text="Gender: ",padx=20,pady=10)
label3=Label(window,text="Total_Bilirubin: ",padx=20,pady=10)
label4=Label(window,text="Direct_Bilirubin: ",padx=20,pady=10)
label5=Label(window,text="Alkaline_Phosphotase: ",padx=20,pady=10)
label6=Label(window,text="Alamine_Aminotransferase: ",padx=20,pady=10)
label7=Label(window,text="Aspartate_Aminotransferase: ",padx=20,pady=10)
label8=Label(window,text="Total_Proteins: ",padx=20,pady=10)
label9=Label(window,text="Albumin: ",padx=20,pady=10)
label10=Label(window,text="Albumin_and_Globulin_Ratio: ",padx=20,pady=10)
label11=Label(window,text="Globulin: ",padx=20,pady=10)


Age=Entry(window,width=30,borderwidth=3)
Gender=Entry(window,width=30,borderwidth=3)
Total_Bilirubin=Entry(window,width=30,borderwidth=3)
Direct_Bilirubin=Entry(window,width=30,borderwidth=3)
Alkaline_Phosphotase=Entry(window,width=30,borderwidth=3)
Alamine_Aminotransferase=Entry(window,width=30,borderwidth=3)
Aspertate_Aminotransferase=Entry(window,width=30,borderwidth=3)
Total_Proteins=Entry(window,width=30,borderwidth=3)
Albumin=Entry(window,width=30,borderwidth=3)
Albumin_and_Globulin_Ratio=Entry(window,width=30,borderwidth=3)
Dataset=Entry(window,width=30,borderwidth=3)


save=Button(window,text="Save",padx=20,pady=10,command=Save)
add=Button(window,text="Add",padx=20,pady=10,command=Add)
submit=Button(window,text="Submit",padx=70,pady=10,command=MLP)
clear=Button(window,text="Clear",padx=18,pady=10,command=Clear)
Exit=Button(window,text="Exit",padx=20,pady=10,command=window.quit)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=4,column=0)
label6.grid(row=5,column=0)
label7.grid(row=6,column=0)
label8.grid(row=7,column=0)
label9.grid(row=8,column=0)
label10.grid(row=9,column=0)
label11.grid(row=10,column=0)



Age.grid(row=0,column=1)
Gender.grid(row=1,column=1)
Total_Bilirubin.grid(row=2,column=1)
Direct_Bilirubin.grid(row=3,column=1)
Alkaline_Phosphotase.grid(row=4,column=1)
Alamine_Aminotransferase.grid(row=5,column=1)
Aspertate_Aminotransferase.grid(row=6,column=1)
Total_Proteins.grid(row=7,column=1)
Albumin.grid(row=8,column=1)
Albumin_and_Globulin_Ratio.grid(row=9,column=1)
Dataset.grid(row=10,column=1)

save.grid(row=12,column=0,columnspan=2)
add.grid(row=11,column=0,columnspan=2)
submit.grid(row=13,column=0,columnspan=2)
clear.grid(row=14,column=0,columnspan=2)
Exit.grid(row=15,column=0,columnspan=2)

window.mainloop()
print(lst)
print(main_lst)