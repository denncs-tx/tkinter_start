from denncs import DennCSApp, tk, ttk
import json
import requests


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        self._api_key = "API KEY"
        self._base_url = "https://www.airnowapi.org/aq/observation/zipCode/current/"
        self._zip_entry = ttk.Entry(self)
        self._aq_label = ttk.Label(self, text=f"Please search for a zip code...", font=("Consolas", 14))
        self._zip_entry.grid(row=0, column=0, sticky=tk.W + tk.N + tk.E + tk.W)
        self._aq_label.grid(row=1, column=0, columnspan=2)
        ttk.Button(self, text="Lookup Zipcode", command=self._zip_lookup).grid(row=0, column=1)

    def _zip_lookup(self):
        weather_color = "#000000"
        try:
            zip_code = str(self._zip_entry.get())
            api_request = requests.get(f"{self._base_url}?format=application/json&zipCode={zip_code}&"
                                       f"distance=5&API_KEY={self._api_key}")
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

            self.configure(background=weather_color)
            self._aq_label.configure(text=f"{city} Air Quality {str(quality)} {category}", background=weather_color)
        except IndexError as ie:
            self.configure(background=weather_color)
            self._aq_label.configure(text="Information Unavailable", background=weather_color, foreground="white")
        except json.decoder.JSONDecodeError as jde:
            self.configure(background=weather_color)
            self._aq_label.configure(text=repr(jde), background=weather_color, foreground="white")


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
