import csv
import requests
import json

# Future, the Version will be deprecated to allow for a generalised API Caller method.
# The Data layer and the Request layer would be separated in the future version

response_API = requests.get('https://api-v3.mbta.com/routes?api_key=6bdef87f76d742bdbf28f59a05dd1a6b')
data = response_API.text

parse_json = json.loads(data)

mbta_transport_data = parse_json["data"]

# now we will open a file for writing
data_file = open('../dataset/mbta_transport_types.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for mbta_data in mbta_transport_data:
    attribute_data = mbta_data["attributes"]
    if count == 0:
        header = attribute_data.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(attribute_data.values())

data_file.close()
