from mylib.lib import *

def main_func(PATH, flag):
    cardio_data = read_dataset(PATH)
    general_summary(cardio_data)
    # plot_crosstab(cardio_data)
    plot_histogram(cardio_data, flag)
    # plot_boxplot(cardio_data)
    # plot_age(cardio_data)
    plot_count(cardio_data, flag)
    # plot_income(cardio_data)
    plot_scatter(cardio_data, flag)
    # plot_corr(cardio_data)
    # plot_miles(cardio_data)
    print("Use funcitions from lib.py to show the plots. They are in the folder results")
    return True

# if __name__ == "__main__":
#     PATH = "../data/CardioGoodFitness.csv"
#     main1(PATH, True)