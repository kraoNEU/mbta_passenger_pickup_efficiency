import os
import pandas as pd
import matplotlib.pyplot as plt
from getAPIDataset import *

apiURL = "https://api-v3.mbta.com/trips?include=route,vehicle,service,shape,predictions,route_pattern,stops&api_key=6bdef87f76d742bdbf28f59a05dd1a6b&filter[route]=57"
file_name = "mbta_routes"

# Gets the API Data. Expects the API URL and File_Name to be Stored at file location: '../dataset/'
getAPIDataset.getAPIdata(apiURL, file_name)

mbta_Dataframe = pd.read_csv(r'../dataset/mbta_routes.csv')
