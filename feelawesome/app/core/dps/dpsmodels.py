from models import BDI
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


class PredictionBDIModel(object):
    def __init__(self):
        self.name = ''
        bdis = BDI.objects.all()
        df = bdis[['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
                 'q17', 'q18', 'q19', 'q20', 'q21', 'class_dep']]

        # Handling Missing Data
        df['q1'] = df['q1'].fillna(df['q1'].mode()[0])
        df['q2'] = df['q2'].fillna(df['q2'].mode()[0])
        df['q3'] = df['q3'].fillna(df['q3'].mode()[0])
        df['q4'] = df['q4'].fillna(df['q4'].mode()[0])
        df['q5'] = df['q5'].fillna(df['q5'].mode()[0])
        df['q6'] = df['q6'].fillna(df['q6'].mode()[0])
        df['q7'] = df['q7'].fillna(df['q7'].mode()[0])
        df['q8'] = df['q8'].fillna(df['q8'].mode()[0])
        df['q9'] = df['q9'].fillna(df['q9'].mode()[0])
        df['q10'] = df['q10'].fillna(df['q10'].mode()[0])
        df['q11'] = df['q11'].fillna(df['q11'].mode()[0])
        df['q12'] = df['q12'].fillna(df['q12'].mode()[0])
        df['q13'] = df['q13'].fillna(df['q13'].mode()[0])
        df['q14'] = df['q14'].fillna(df['q14'].mode()[0])
        df['q15'] = df['q15'].fillna(df['q15'].mode()[0])
        df['q16'] = df['q16'].fillna(df['q16'].mode()[0])
        df['q17'] = df['q17'].fillna(df['q17'].mode()[0])
        df['q18'] = df['q18'].fillna(df['q18'].mode()[0])
        df['q19'] = df['q19'].fillna(df['q19'].mode()[0])
        df['q20'] = df['q20'].fillna(df['q20'].mode()[0])
        df['q21'] = df['q21'].fillna(df['q21'].mode()[0])
        df['class_dep'] = df['class_dep'].fillna(df['class_dep'].mode()[0])

    def split_data(self, df):
        X = df.iloc[:, -1].values
        y = df.iloc[:, 22].values
        # imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose=0)
        # imputer = imputer.fit(X[:, 1:3])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def svm_classifier(self):
        self.name = 'Svm Classifier'
        classifier = SVC()
        return classifier.fit(self.x_train, self.y_train)

    def decisionTree_classifier(self):
        self.name = 'Decision tree Classifier'
        classifier = DecisionTreeClassifier()
        return classifier.fit(self.x_train, self.y_train)

    def randomforest_classifier(self):
        self.name = 'Random Forest Classifier'
        classifier = RandomForestClassifier()
        return classifier.fit(self.x_train, self.y_train)

    def naiveBayes_classifier(self):
        self.name = 'Naive Bayes Classifier'
        classifier = GaussianNB()
        return classifier.fit(self.x_train, self.y_train)

    def knn_classifier(self):
        self.name = 'Knn Classifier'
        classifier = KNeighborsClassifier()
        return classifier.fit(self.x_train, self.y_train)

    def accuracy(self, model):
        predictions = model.predict(self.x_test)
        cm = confusion_matrix(self.y_test, predictions)
        accuracy = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1])
        print(f"{self.name} has accuracy of {accuracy * 100} % ")
