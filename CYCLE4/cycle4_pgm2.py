import numpy as np
import  matplotlib .pyplot as plt
import pandas as pd

from cycle4_pgm1 import x_train, x_text, y_train, y_text, classifiers, y_pred

data=pd.read_csv('Blood Transfusion.csv ')
x=data.iloc[:,:-1].values
y=data.iloc[:,4].values
from sklearn.model_selection import train_test_split
x_train,x_text,y_train,y_test=train_test_split(x,y,test_size=0.20)
from sklearn.neighbors import KNeighborsClassifier
classifiers =KNeighborsClassifier(n_neighbors=5)
classifiers.fit(x_train,y_train)
y_pred=classifiers.predict(x_text)
from  sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_pred))