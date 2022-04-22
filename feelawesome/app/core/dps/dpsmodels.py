import os
from config.settings import MEDIA_ROOT
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


class PredictionDepressionModel(object):
    def __init__(self):
        self.y_test = None
        self.y_train = None
        self.x_test = None
        self.x_train = None
        self.name = ''
        # base_dir = MEDIA_ROOT
        path = os.path.join(MEDIA_ROOT, str('datasets/data_bdi.xlsx'))
        df = pd.read_excel(path)

        self.split_data(df)

    def split_data(self, df):
        x = df.loc[:, 'B1':'SCORE']
        y = df[['CLASS_D']]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def svm_classifier(self):
        self.name = 'Svm Classifier'
        classifier = SVC()
        return classifier.fit(self.x_train, self.y_train)

    def randomforest_classifier(self):
        self.name = 'Random Forest Classifier'
        classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
        return classifier.fit(self.x_train, self.y_train)

    def decisionTree_classifier(self):
        self.name = 'Decision tree Classifier'
        classifier = DecisionTreeClassifier()
        return classifier.fit(self.x_train, self.y_train)



