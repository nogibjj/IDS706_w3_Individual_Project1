# %% [markdown]
# # Cardio Good Fitness Case Study
# The market research team at AdRight is assigned the task to identify the profile of the typical customer for each treadmill product offered by CardioGood Fitness.
# 
# The market research team decides to investigate whether there are differences across the product lines with respect to customer characteristics.
# 
# The team decides to collect data on individuals who purchased a treadmill at a CardioGoodFitness retail store during the prior three months.
# 
# The data are stored in the CardioGoodFitness.csv file

# %%
import warnings
warnings.filterwarnings('ignore')
from mylib.lib import *

# %%
cardio_data = read_dataset(PATH)
cardio_data

# %%
general_summary(cardio_data)

# %%
plot_crosstab(cardio_data)

# %%
plot_histogram(cardio_data)

# %%
plot_boxplot(cardio_data)

# %% [markdown]
# ## EDA for pivot table

# %%
pt1 = pd.pivot_table(cardio_data, index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])
pt2 = pd.pivot_table(cardio_data,'Income', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])
pt3 = pd.pivot_table(cardio_data,'Miles', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])

# %%
pt1

# %%
pt2

# %%
pt3

# %%
# x= number of each product, hue= seperated by Gender
plot_count(cardio_data)

# %% [markdown]
# # Average of Age

# %%
cardio_data['Age'].mean()

# %%
cardio_data['Age'].std()

# %%
sns.distplot(cardio_data['Age'])

# %% [markdown]
# # Seperated data by Gender

# %%
from mylib import *

# %%
plot_income(cardio_data)

# %%
cardio_data.loc[(cardio_data['Income'] > 70000) & (cardio_data['Income'] < 100000) & (cardio_data['Gender'] == 'Female')]

# %%
plot_age(cardio_data)

# %%
plot_scatter(cardio_data)

# %% [markdown]
# From the above plots, we can conclude(infer) that TM798 is the more expensive and better one.

# %% [markdown]
# # Heatmap
# ## Overview of the correlation of the different variables
# 
# 

# %%
plot_corr(cardio_data)

# %%



