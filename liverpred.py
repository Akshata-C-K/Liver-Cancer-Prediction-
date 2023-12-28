#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix


# In[4]:


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
hidden_layer_sizes = [(2,), (3,), (5,), (2,2,), (3,2,), (5,2,)]
# learning_rates = ['constant', 'invscaling', 'adaptive'] # only for sgd


# In[18]:



count = 1
for solver in solvers:
    for ac in activation_functions:
        for hidden_layer_config in hidden_layer_sizes:
            clf = MLPClassifier(solver=solver, alpha=1e-5, hidden_layer_sizes=hidden_layer_config, random_state=1, max_iter=5000, activation=ac)
            clf.fit(X, Y)
            comparison_dict[count] = {"solver":solver, "activation_function": ac, "hidden_layers":hidden_layer_config, "accuracy": clf.score(X,Y), "loss":clf.loss_}
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
if(avg == output_pred):
  print("Cancer not detected")
else:
  print("cancer detected")
# In[49]:


print("The loss is", clf.loss_)
print("Mean accuracy is", clf.score(X, Y))


# In[ ]:




