'''This module builds a base class for classification problems, such as logistic
regression or k-nearest neighbors classification. 
The preprocessing (if applicable) is done at this class level.

'''

import numpy as np
from preprocessing import train_test_split, scale_and_center
from evaluation_metrics import evaluate_accuracy

class Classification:
    """
    A class used to represent a classification algorithm.

    Parameters
    -----------
    features : numpy.ndarray
        Design matrix of explanatory variables.
    output : numpy.ndarray
        Labels of data corresponding to feature matrix.
    split_proportion : float
        Proportion of data to use for training; between 0 and 1.
    number_labels : int
        The number of labels present in the data.
    standardized : bool
        Whether to center/scale the data (train/test done separately).
        True by default.

    Attributes
    -----------
    number_labels : int
        The number of labels present in existing and future data.
    sample_size : int
        The sample size of all given data (train and test).
    train_size : int
        The sample size of the training data.
    test_size : int
        The sample size of the test data.
    train_rows : numpy.ndarray
        The list of indices for the train split.
    test_rows : numpy.ndarray
        The list of indices for the test split.
    train_features : numpy.ndarray
        The train design matrix.
    test_features : numpy.ndarray
        The test design matrix.
    train_output : numpy.ndarray
        The train output data.
    test_output : numpy.ndarray
        The test output data.
    dimension : int
        The number of dimensions of the data, or columns of design matrix.
        Does not include output.

    """
    def __init__(self, features, output, split_proportion, number_labels=None, 
                 standardized=True):
        # Default procedure is to assume all labels appear in output
        # If labels are missing in data, specify number_labels manually
        if number_labels is None:  
            self.number_labels = len(np.unique(output)) 
        else: 
            self.number_labels = number_labels
        self.sample_size, 
        self.train_size, 
        self.test_size, 
        self.train_rows, 
        self.test_rows, 
        self.train_features, 
        self.test_features, 
        self.train_output, 
        self.test_output = train_test_split(features, output, split_proportion)
        self.dimension = self.train_rows.shape[1]
        if standardized:
            self.standardize()

    def standardize(self):
        '''
        Separately scale/center the train and test data so each feature
        (column of observations) has 0 mean and unit variance.
        '''
        self.train_features = scale_and_center(self.train_features)
        self.test_features = scale_and_center(self.test_features)
