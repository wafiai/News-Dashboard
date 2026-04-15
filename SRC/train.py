import pandas as pd 
import joblib as jb 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score


df = pd.read_csv('Data/Raw/data.csv')
X = df['Title'] + "" + df['Description']
y = df['Class Index'] # Opening data csv file & mapping file colums 

X_train, X_test, y_train, y_test = train_test_split(
    X,y, random_state=20,test_size=0.2
) # spliting data for training and testing

Vectorizer = TfidfVectorizer() 
traindata = Vectorizer.fit_transform(X_train)
testdata = Vectorizer.transform(X_test)
# preparing vectorizer & transforming data
 
model = LogisticRegression()
model.fit(traindata,y_train)
predictions = model.predict(testdata)
# training and testing model
print(accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))
# testing model accuracy 

jb.dump(model,'models/model.pkl')
jb.dump(Vectorizer,'models/vectorizer.pkl')
# saving model & vectorizer
