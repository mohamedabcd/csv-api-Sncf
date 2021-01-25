from sncf import Sncf

# Create an instance of the class Sncf
sncf = Sncf()

# Call the method read_json to do a get request to an determined api
url = "https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/txt/3fa48b7d-ce01-4268-8cbf-a3eecc8df7bb.txt"
# sncf.read_json(url)

# Call the display stops method to display all stops, coordinates, codes,
# and administative regions and create an stops attribute
# stops = sncf.display_stops()

# Call the method create_csv to transfer the stops attribute from the last method into a CSV dataframe
# x = sncf.create_csv(stops, "stop_areas")
# print(x)


# Get the stops from Paris GARE DE LYON to Lyon Perrache

# From  Paris - Gare de Lyon
depart = "stop_area:OCE:SA:87686006"
# To Lyon - Perrache
arrival = "stop_area:OCE:SA:87722025"
# Call the metohod and will return the new data
# my_journey = sncf.get_journey(depart, arrival)
# print(my_journey)
# post the journey into a CSV
# sncf.create_csv(my_journey, "Journey")

# Get the trains from Paris to Lyon entre 18h et 20h
sncf.get_datetime()
#sncf.get_trains_datetime(start=depart, stop=arrival)

'''
def insert_stop(key):
    # model the new data
    new_stop_area = {
        "administrative_regions": [
            {
                "coord": {
                    "lat": "50.23436",
                    "lon": "7.996379"
                },
                "id": "admin:1187560extern",
                "insee": "",
                "label": "Venezuela",
                "level": 15,
                "name": "Venezuela",
                "zip_code": "8001"
            },
            {
                "coord": {
                    "lat": "51.23436",
                    "lon": "8.996379"
                },
                "id": "admin:5432693extern",
                "insee": "",
                "label": "Bresil",
                "level": 10,
                "name": "Bresil",
                "zip_code": ""
            }
        ],
        "codes": [
            {
                "type": "VE-VB-BR",
                "value": "0080-300520-BV"
            }
        ],
        "coord": {
            "lat": "50.24065",
            "lon": "7.6990968"
        },
        "id": "stop_area:BRE:VE:90503914",
        "label": "VENEZUELA",
        "links": [],
        "name": "VENEZUELA-BR",
        "timezone": "Amerique/New-york"
    }
    with open("stop_areas.JSON", mode="r") as file:
        data = json.load(file)
        data['stop_areas'].insert(0, new_stop_area)
        manip_json(data)
        print("operation succeded")

    # Creates stop_areas.py and construct a dictionary
    # Get the format of an stop area, the first one
    # (my_data_dict[key][0])
    # print(my_data_dict[key][0].items())
    # STOP AREAS is a list of dictionaries of administrative regions
    # The keys are 'codes', 'name', 'links', 'coord', 'label', 'administrative_regions', 'timezone', 'id'
'''
