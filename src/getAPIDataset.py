import csv
import requests
import json


class getAPIDataset:
    """
    Input:
        apiURL: Give the Complete API URL with the Key Included
        csv_file_location: Give the .CSV file name
    returns: None
    """

    def getAPIdata(apiURL, csv_file_name):

        dictionary_key = "data"
        data_attributes = "attributes"
        response_API = requests.get(apiURL)
        data = response_API.text

        parse_json = json.loads(data)

        mbta_transport_data = parse_json[dictionary_key]

        # now we will open a file for writing
        path = "../dataset/" + csv_file_name + ".csv"
        data_file = open(path, 'w')

        # create the csv writer object
        csv_writer = csv.writer(data_file)

        # Counter variable used for writing
        # headers to the CSV file
        count = 0

        for mbta_data in mbta_transport_data:
            attribute_data = mbta_data[data_attributes]
            if count == 0:
                header = attribute_data.keys()
                csv_writer.writerow(header)
                count += 1

            # Writing data of CSV file
            csv_writer.writerow(attribute_data.values())

        data_file.close()
