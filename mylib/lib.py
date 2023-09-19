import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


PATH = "data/CardioGoodFitness.csv"

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

def plot_histogram(cardio_data):
    cardio_data.hist(figsize=(15,15))
    plt.show()

def plot_boxplot(cardio_data):
    # sns.boxplot(x="Gender", y="Age", data=data)
    sns.boxenplot(x='Gender',y='Age',data=cardio_data)
    plt.show()

def plot_crosstab(data):
    crosstab1 = pd.crosstab(data['Product'],data['Gender'] )
    crosstab2 = pd.crosstab(data['Product'],data['Fitness'] )
    print(crosstab1)
    print(crosstab2)
    # crosstab = pd.crosstab(data.Gender, data.Age)
    # sns.heatmap(crosstab1, annot=True)
    # sns.heatmap(crosstab2, annot=True)
    # plt.show()

def plot_count(cardio_data):
    sns.countplot(x="Product", hue="Gender", data=cardio_data)

def plot_income(cardio_data):
    # bins = np.arange(cardio_data['Income'].min(), cardio_data['Income'].max() + 10000, 5000)
    # cardio_data.hist(by='Gender',column = 'Income', bins = bins)
    cardio_data.hist(by='Gender',column = 'Income')
    # tick_interval = 10000
    # plt.xticks(np.arange(cardio_data['Income'].min(), cardio_data['Income'].max()+tick_interval, tick_interval))
    # plt.show()


def plot_age(cardio_data):
    # bins = np.arange(cardio_data['Age'].min(), cardio_data['Age'].max() + 10, 5)
    # cardio_data.hist(by='Gender',column = 'Age', bins = bins)
    cardio_data.hist(by='Gender',column = 'Age')
    # tick_interval = 10
    # plt.xticks(np.arange(cardio_data['Income'].min(), cardio_data['Income'].max()+tick_interval, tick_interval))
    # plt.show()

def plot_miles(cardio_data):
    cardio_data.hist(by='Gender',column = 'Miles')
    cardio_data.hist(by='Product',column = 'Miles')

def plot_corr(cardio_data):
    numerical_columns = cardio_data.select_dtypes(include=['float64', 'int64'])
    corr = numerical_columns.corr()
    sns.heatmap(corr, annot=True)
    plt.show()

def plot_scatter(cardio_data):
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
    plt.show()