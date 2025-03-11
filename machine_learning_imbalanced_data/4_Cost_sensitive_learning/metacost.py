import numpy as np
import pandas as pd

from sklearn.base import clone

class MetaCost:

    def __init__(self, estimator, cost_matrix, n_estimators=50, n_samples=None, p=True, q=True):

        self.estimator = estimator
        self.cost_matrix = cost_matrix
        self.n_estimators = n_estimators
        self.n_samples = n_samples
        self.p = p
        self.q = q

    def fit(self, X,y):

        if not isinstance(X, pd.DataFrame):
            raise ValueError('S must be a DataFrame object')
        
        X = X.copy()

        #reset index, helps with resampling
        X.reset_index(inplace=True, drop=True)
        y.index = X.index

        variables = list(X.columns)

        # concatenate
        S = pd.concat([X,y], axis=1)
        S.columns=variables + ['target']

        num_class = y.nunique()

        if not self.n_samples:
            self.n_samples = len(X)

        S_ = {} #list of subdatasets
        M = [] #list of models

        