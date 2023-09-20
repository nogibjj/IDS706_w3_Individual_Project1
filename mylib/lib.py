import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# PATH = "../data/CardioGoodFitness.csv"

def read_dataset(path):
    cardio_data = pd.read_csv(path)
    return cardio_data

def general_summary(cardio_data):
    print("The first five lines of the dataset\n")
    print(cardio_data.head())
    print("The descriptive statistics of the CardioGoodFitness dataset\n")
    print(cardio_data.describe().T)
    print("The info of the CardioGoodFitness dataset\n")
    print(cardio_data.info())
    print("The shape of the CardioGoodFitness dataset\n")
    print(cardio_data.shape)

# flag means whether in the python script or not
def plot_histogram(cardio_data, flag = False):
    cardio_data.hist(figsize=(15,15))
    if flag:
        plt.savefig('./results/histogram.png')

def plot_boxplot(cardio_data,flag = False):
    plt.figure()
    sns.boxenplot(x='Gender',y='Age',data=cardio_data)
    if flag:
        plt.savefig('./results/boxplot.png')


def plot_crosstab(data):
    crosstab1 = pd.crosstab(data['Product'],data['Gender'] )
    crosstab2 = pd.crosstab(data['Product'],data['Fitness'] )
    print(crosstab1)
    print(crosstab2)

def plot_count(cardio_data, flag = False):
    plt.figure()
    sns.countplot(x="Product", hue="Gender", data=cardio_data)
    if flag:
        plt.savefig('./results/count.png')


def plot_income(cardio_data, flag = False):
    plt.figure()
    cardio_data.hist(by='Gender',column = 'Income')
    if flag:       
        plt.savefig('./results/income.png')

def plot_age(cardio_data, flag = False):
    plt.figure()
    cardio_data.hist(by='Gender',column = 'Age')
    if flag:
        plt.savefig('./results/age.png')


def plot_miles(cardio_data, flag = False):
    plt.figure()
    cardio_data.hist(by='Gender',column = 'Miles')
    cardio_data.hist(by='Product',column = 'Miles')
    # plt.show()
    if flag:
        plt.savefig('./results/miles.png')

def plot_corr(cardio_data, flag = False):
    plt.figure()
    numerical_columns = cardio_data.select_dtypes(include=['float64', 'int64'])
    corr = numerical_columns.corr()
    sns.heatmap(corr, annot=True)
    # plt.show()
    if flag:
        plt.savefig('./results/corr.png')


def plot_scatter(cardio_data, flag = False):
    # sns.scatterplot(x='Age', y='Income',data=cardio_data, hue = 'Product')
    # plt.show()
    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10,10))
    sns.scatterplot(x='Age', y='Income', data=cardio_data, hue='Product', ax=ax1)
    sns.scatterplot(x='Age', y='Fitness', data=cardio_data, hue='Product', ax=ax2)
    sns.scatterplot(x='Age', y='Usage', data=cardio_data, hue='Product', ax=ax3)
    sns.scatterplot(x='Age', y='Miles', data=cardio_data, hue='Product', ax=ax4)
    ax1.set_title('Plot 1')
    ax2.set_title('Plot 2')
    ax3.set_title('Plot 3')
    ax4.set_title('Plot 4')
    plt.tight_layout()
    # plt.show()
    if flag:
        plt.savefig('./results/scatter.png')
        