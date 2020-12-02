import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
df =pd.read_csv('hour.csv')
#print(df.head())
f = open("input.txt", "r")

df=df.drop(['instant','dteday','casual','registered'],1)
#print(df.head())
x=np.array(df.drop(['cnt'],1))
y=np.array(df['cnt'])
#print(y)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
#clf= AR(train_data)
#clf = LinearRegression()
clf=RandomForestRegressor(n_estimators = 100, random_state = 1337)
#clf=svm.NuSVC()
#clf=PassiveAggressiveRegressor(C=1.0,fit_intercept=True,max_iter=1000,tol=0.001,early_stopping=False,validation_fraction=0.1,n_iter_no_change=5,shuffle=True,verbose=0,loss='epsilon_insensitive',epsilon=0.1,random_state=None,warm_start=False,average=False)
#clf =neighbors.KNeighborsClassifier(n_neighbors=1)
clf.fit(x_train,y_train)
accuracy=clf.score(x_test,y_test)
print(accuracy)
#season,hr,holiday,workingday,weathersit,temp,atemp,hum,windspeed
input=[]
ele=[]
n=int(f.readline())
for i in range(n):
    ele=[]
    for j in range(12):
        k=float(f.readline())
        ele.append(k)
    input.append(ele)
"""
season=float(f.readline())
yr=float(f.readline())
month=float(f.readline())
hr=float(f.readline())
holiday=float(f.readline())
weekday=float(f.readline())
workingday=float(f.readline())
weathersit=float(f.readline())
temp=float(f.readline())
atemp=float(f.readline())
hum=float(f.readline())
windspeed=float(f.readline())"""
pred=clf.predict(input)
print(pred)
f = open("output.txt", "w")
for i in pred:
    f.write(str(int(i)))
    f.write("\n")
f.close()
