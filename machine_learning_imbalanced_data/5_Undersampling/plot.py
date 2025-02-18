from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_decision_boundary(classifier, X_train, X_test, y_train, y_test):
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