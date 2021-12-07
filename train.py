import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
data = pd.read_csv('pong_data_backup3.csv').dropna()

X=data.iloc[:,:4]
y = data.iloc[:,5]

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=0)
model = LinearRegression()

model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)


from joblib import dump, load 
dump(model, 'mymodel.joblib')
