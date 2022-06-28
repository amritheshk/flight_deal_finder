import requests
from pprint import pprint

#TODO constants
TEQUILA_APIKEY="PKCPMeZU4tEXKxpIqgrkcnG0GKClxrWN"
DEPARTURE_AIRPORT_IATACODE="COK"

#TODO endpoints
tequila_endpoint="https://tequila-api.kiwi.com/v2/search"
sheety_get_endpoint= "https://api.sheety.co/eb1d80cb386cef1092824698410439ad/citiesToVisit/sheet1"


search_from = input("Search flights from (dd/mm/yyyy) : ")
search_to = input("Search flights upto (dd/mm/yyyy) : ")


class Search_flight:
    def __init__(self):
        self.flight_search_data=[]
        self.from_date=search_from
        self.to_date=search_to
    def start_search(self):
        # TODO read from google sheet
        sheety_response1 = requests.get(url=sheety_get_endpoint)
        self.sheety_response_data = sheety_response1.json()

        headers={
        "apikey":TEQUILA_APIKEY
        }

        self.flight_search_data=[]
        for i in self.sheety_response_data["sheet1"]:

            parameters={

            "fly_from":DEPARTURE_AIRPORT_IATACODE,
            "fly_to":self.sheety_response_data["sheet1"][self.sheety_response_data["sheet1"].index(i)]["iataCode"],
            "dateFrom":self.from_date,
            "dateTo":self.to_date,
            "curr":"INR"

            }
            tequila_response=requests.get(url=tequila_endpoint,params=parameters,headers=headers)
            self.tequila_response_data=tequila_response.json()
            self.flight_search_data.append({"cityFrom":self.tequila_response_data["data"][0]["cityFrom"],
                                       "cityTo":self.tequila_response_data["data"][0]["cityTo"],
                                      "flyFrom":self.tequila_response_data["data"][0]["flyFrom"],
                                      "flyTo":self.tequila_response_data["data"][0]["flyTo"],
                                      "price":self.tequila_response_data["data"][0]["price"],
                                      "lowest_acceptable_price":int(self.sheety_response_data["sheet1"][self.sheety_response_data["sheet1"].index(i)]["lowestPrice"])})
        pprint(self.flight_search_data)
# flight_test=Search_flight()
# flight_test.start_search()