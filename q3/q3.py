import numpy as np
from sklearn import preprocessing,neighbors,svm
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
df =pd.read_csv('iris.data')
df.to_csv("iris.data", header=["sl", "sw", "pl","pw","class"], index=False)

f = open("input.txt", "r")
df =pd.read_csv('iris.data')
#print(df)
x=np.array(df.drop(['class'],1))
y=np.array(df['class'])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
clf =neighbors.KNeighborsClassifier()
#clf=svm.NuSVC()
clf.fit(x_train,y_train)

accuracy=clf.score(x_test,y_test)
print(accuracy)
input=[]
ele=[]
n=int(f.readline())
for i in range(n):
    ele=[]
    for j in range(4):
        k=float(f.readline())
        ele.append(k)
    input.append(ele)
"""
sepal_length=float(input("Sepal Length(cm):"))
sepal_width=float(input("Sepal wdith(cm):"))
petal_length=float(input("Petal Length(cm):"))
petal_width=float(input("Petal Width(cm):"))"""
pred=clf.predict(input)
print(pred)
f = open("output.txt", "w")
for i in pred:
    f.write(str(i))
    f.write("\n")
f.close()
