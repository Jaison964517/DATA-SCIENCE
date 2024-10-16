import numpy as np
import  matplotlib.pyplot as plt
import pandas as pd
from IPython.core.release import classifiers

dataset= pd.read_csv('iriss.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values
from sklearn.model_selection import train_test_split
x_train,x_text,y_train,y_text=train_test_split(x,y,test_size=0.20)
from sklearn.neighbors import KNeighborsClassifier
classifiers=KNeighborsClassifier(n_neighbors=5)
classifiers.fit(x_train,y_train)
y_pred=classifiers.predict(x_text)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_text,y_pred))
