import os
import sys
import pandas as pd
import numpy as np
import dill
from pathlib import Path
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
sys.path.append(str(Path(__file__).parent.parent))
from exception import CustomException
from logger import logging

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj,file_obj)
        logging.info("Successfully Created Pickle file")

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models,params):
    try:
        report = {}
        for model_name, model_instance in models.items():   
            param = params[model_name]
            gs = GridSearchCV(model_instance,param,cv =5)
            gs.fit(X_train,y_train)

            model_instance.set_params(**gs.best_params_)
            model_instance.fit(X_train,y_train)


            y_train_pred = model_instance.predict(X_train)
            y_test_pred = model_instance.predict(X_test)

            train_model_accuracy = r2_score(y_train, y_train_pred)
            test_model_accuracy = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_accuracy
        logging.info('Model Accuracy report Generated SUCCESSFULLY')
        return report
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file:
            return dill.load(file)

    except Exception as e:
        raise CustomException(e,sys)