import os
import pandas as pd
import matplotlib.pyplot as plt
from getAPIDataset import *


apiURL = "https://api-v3.mbta.com/routes?api_key=6bdef87f76d742bdbf28f59a05dd1a6b"
file_name = "mbta_transport_type"

# Gets the API Data. Expects the API URL and File_Name to be Stored at file location: '../dataset/'
getAPIDataset.getAPIdata(apiURL, file_name)

mbta_Dataframe = pd.read_csv(r'../dataset/mbta_transport_type.csv')

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
