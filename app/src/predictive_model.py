from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import xgboost as xgb

def RandomForest_train(X_train, Y_train, n_estimators=100, random_state=None, model_params=None):
    if model_params is not None: model_params = {}
    rf_params = {'n_estimators': n_estimators, 'random_state': random_state}
    rf_params.update(model_params)
    rf = RandomForestClassifier(**rf_params)
    rf.fit(X_train, Y_train)
    return rf

def LinearRegression_train(X_train, Y_train, model_params=None):
    if model_params is None: model_params = {}
    lr = LinearRegression(**model_params)
    lr.fit(X_train, Y_train)
    return lr

def LogisticRegression_train(X_train, Y_train, model_params=None):
    if model_params is None: model_params = {}
    logreg = LogisticRegression(**model_params)
    logreg.fit(X_train, Y_train)
    return logreg

def SVM_train(X_train, Y_train, model_params=None):
    if model_params is None: model_params = {}
    svm = SVC(**model_params)
    svm.fit(X_train, Y_train)
    return svm

def GradientBoosting_train(X_train, Y_train, model_params=None):
    if model_params is None: model_params = {}
    gb = GradientBoostingClassifier(**model_params)
    gb.fit(X_train, Y_train)
    return gb

def NaiveBayes_train(X_train, Y_train, model_params=None):
    if model_params is None: model_params = {}
    nb = GaussianNB(**model_params)
    nb.fit(X_train, Y_train)
    return nb

def AdaBoost_train(X_train, Y_train, model_params=None):
    if model_params is None: model_params = {}
    ab = AdaBoostClassifier(**model_params)
    ab.fit(X_train, Y_train)
    return ab

def XGBoost_train(X_train, Y_train, model_params=None):
    if model_params is None: model_params = {}
    dtrain = xgb.DMatrix(X_train, label=Y_train)
    xg = xgb.train(model_params, dtrain)
    return xg