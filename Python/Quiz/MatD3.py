import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv(r"/home/elkimza/Documents/Learning/Data_Science/Python/Quiz/Standard Metropolitan Areas Data - train_data - data.csv")
# print(x)

plt.scatter(x.crime_rate, x.percent_city)
plt.title("Plot of crime_rate vs percent_city")
plt.xlabel("Percent_city")
plt.ylabel("Crime rate")
plt.show()