
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.datasets import make_classification
from sklearn.metrics import roc_auc_score



def PlotDecisionBoundary(classifier, X_train, X_test, y_train, y_test):
    '''
    To use:
    rf = RandomForestClassifier()
    Ex: PlotDecisionBoundary(rf, X_train, X_test, y_train, y_test)
    
    '''
    X_set, y_set = X_train.values, y_train

    colors=('red', 'green')
    cmap = ListedColormap(colors)

    X1_min, X1_max = X_set[:,0].min() - 1, X_set[:,0].max() + 1
    X2_min, X2_max = X_set[:,1].min() - 1, X_set[:,1].max() + 1
    step=0.01

    X1, X2 = np.meshgrid(
        np.arange(X1_min, X1_max, step),
        np.arange(X2_min, X2_max, step)
    )


    arr = np.array([X1.ravel(), X2.ravel()])
    classifier.fit(X_train, y_train)
    Z = classifier.predict(arr.T)
    Z = Z.reshape(X1.shape)

    plt.contourf(X1, X2, Z, alpha=0.5, cmap=cmap)

    X_test = X_test.values
    for i, j in enumerate(np.unique(y_test)):

        xi = X_test[y_test == j, 0]
        yi = X_test[y_test == j, 1]

        sns.scatterplot(x=xi, y=yi, c=colors[i], label=j)


def MakeData(n_classes, weights, sep):
    '''
    To use:
    Ex: MakeData(n_classes=2, weights=[0.90], sep=2)
    
    '''
    X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_classes=n_classes, n_clusters_per_class=1, weights=weights, class_sep=sep, random_state=0)

    X = pd.DataFrame(data=X, columns=['varA', 'varB'])
    y = pd.Series(y)

    return X, y


def RunClassifier(classifier, X_train, X_test, y_train, y_test):
    '''
    Ex:

    rf = RandomForestClassifier()

    runRandomForests(rf, X_train, X_test, y_train, y_test)
    '''

    classifier.fit(X_train, y_train)

    print('Train Set')
    train_prob = classifier.predict_proba(X_train)[:,1]
    print('Train set roc-auc: {}'.format(roc_auc_score(y_train, train_prob)))

    print('Test set')
    test_prob = classifier.predict_proba(X_test)[:,1]
    print('Test set roc-auc: {}'.format(roc_auc_score(y_test, test_prob)))


def Scatterplot(data1, class1, data2, class2):
    '''
    Plot 2 Scatterplots.
    1 Row and 2 columns, given the 2 provided datasets
    Ex:

    >>>Scatterplot(X, y, X_resampled, y_resampled)


    '''
    
    plt.figure(figsize=(12,6))
    plt.subplot(121)
    sns.scatterplot(data=data1, x=data1.columns[0], y=data1.columns[1], hue=class1)

    plt.subplot(122)
    sns.scatterplot(data=data2, x=data2.columns[0], y=data2.columns[1], hue=class2)

