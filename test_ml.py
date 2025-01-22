import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from ml.model import *



# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_data_split():
    """
    # tests the test_data_split, splits the data correctly
    """
    # Your code here
    #Testing values
    testing_X = [[1, 1, 1], 
                 [1, 1, 1], 
                 [1, 1, 1], 
                 [1, 1, 1]]
    testing_y = [1,1,1,1]

    #Test
    testing_X_train, testing_X_test, testing_y_train, testing_y_test = train_test_split(testing_X, testing_y, test_size=0.25, random_state=42)
    testing_X_train_samples = len(testing_X_train)
    testing_X_test_samples = len(testing_X_test)
    testing_y_train_samples = len(testing_y_train)
    testing_y_test_samples = len(testing_y_test)

    #Results
    assert testing_X_train_samples == 3, "X_Train test did not pass"
    assert testing_X_test_samples == 1, "X_test test did not pass"
    assert testing_y_train_samples == 3, "y_Train test did not pass"
    assert testing_y_test_samples == 1, "y_test test did not pass"


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # tests compute_model_metrics from model.py returns correct precision, recalll and fbeta.  expected result is 1
    """
    # Your code here
    #Testing values
    y_true = [1,1,1,1,1,1,1,1]
    y_pred = [1,1,1,1,1,1,1,1]

    #Pass values
    test_pass_precision = 1.0
    test_pass_recall = 1.0
    test_pass_fbeta = 1.0

    #Test
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    #Results
    assert round(precision, 4) == test_pass_precision, "Precision test did not pass"
    assert round(recall, 4) == test_pass_recall, "Recall test did not pass"
    assert round(fbeta, 4) == test_pass_fbeta, "F-beta test did not pass"


# TODO: implement the third test. Change the function name and input as needed
def test_train_model():
    """
    tests to see if returns a trained randomforest model
    """
    # Your code here
    
    #Testing values
    testing_X_train = [[1, 1, 1], 
                       [1, 1, 1], 
                       [1, 1, 1], 
                       [1, 1, 1], 
                       [1, 1, 1]]
    testing_y_train = [1, 1, 1, 1, 1]

    #Test
    test_model = train_model(testing_X_train,testing_y_train)

    #Results
    assert isinstance(test_model, RandomForestClassifier), "train_model test did not pass"


