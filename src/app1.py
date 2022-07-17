import os
import pandas as pd
import matplotlib.pyplot as plt

mbta_Dataframe = pd.read_csv(r'../dataset/mbta_transport_types.csv')

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
plt.title("Popular MBTA Modes of Transport")
mbta_Dataframe['description'].value_counts().plot(ax=ax, kind='bar', xlabel='Different MBTA Transport Modes',
                                                  ylabel='Number of '
                                                         'Routes')

if os.path.exists('../figures'):
    plt.savefig("../figures/mbta_modes_of_transport.png")
    plt.show()

else:
    os.makedirs('../figures')
    plt.savefig("../figures/mbta_modes_of_transport.png")
    plt.show()
