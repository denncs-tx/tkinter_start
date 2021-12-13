# TODO: Improve with a __main__
# TODO: Make into a class that gets instantiated
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=76210&distance=5&API_KEY=652EFF35-ABCB-41DD-B1BB-58BD1D10EFF2
# Sample Return Object
# [
# {"DateObserved":"2021-12-12 ","HourObserved":7,"LocalTimeZone":"CST","ReportingArea":"Dallas-Fort Worth","StateCode":"TX","Latitude":32.767,"Longitude":-96.783,"ParameterName":"O3","AQI":24,"Category":{"Number":1,"Name":"Good"}},
# {"DateObserved":"2021-12-12 ","HourObserved":7,"LocalTimeZone":"CST","ReportingArea":"Dallas-Fort Worth","StateCode":"TX","Latitude":32.767,"Longitude":-96.783,"ParameterName":"PM2.5","AQI":59,"Category":{"Number":2,"Name":"Moderate"}}
# ]
from tkinter import *
import requests
import json


# Create Zipcode Lookup function
def zip_lookup():
    try:
        weather_color = "#000000"
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json"
                                   "&zipCode=" + str(zipEntry.get()) + "&distance=5&API_KEY=652EFF35-ABCB-41DD-B1BB"
                                                                       "-58BD1D10EFF2")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0c0"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        my_label = Label(root, text=f"{city} Air Quality {str(quality)} {category}", font=("Consolas", 14),
                         background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        my_label = Label(root, text="Unable to retrieve information", font=("Consolas", 14), background=weather_color,
                         foreground="white")
        my_label.grid(row=1, column=0, columnspan=2)


root = Tk()
root.title("Dennis Creative Solutions")
root.iconbitmap('file.ico')
root.geometry("800x600")

zipEntry = Entry(root)
zipEntry.grid(row=0, column=0, sticky=W+N+E+S)

zipButton = Button(root, text="Lookup Zipcode", command=zip_lookup)
zipButton.grid(row=0, column=1)

root.mainloop()
