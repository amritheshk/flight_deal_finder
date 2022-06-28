import requests

#TODO constants
TEQUILA_APIKEY=""

#TODO endpoints
sheety_get_endpoint= "https://api.sheety.co/eb1d80cb386cef1092824698410439ad/citiesToVisit/sheet1"
sheety_put_endpoint= "https://api.sheety.co/eb1d80cb386cef1092824698410439ad/citiesToVisit/sheet1"
tequila_location_endpoint="https://tequila-api.kiwi.com/locations/query"

class Flight_data:
    def find_iatacode(self):
        # TODO acquire data from google sheet
        sheety_response1 = requests.get(url=sheety_get_endpoint)
        self.sheety_data=sheety_response1.json()

        for i in self.sheety_data["sheet1"]:
            parameter={
                "term":i["city"],
                "location_types":"airport"
            }
            headers={
            "apikey":TEQUILA_APIKEY
            }
            tequila_response2=requests.get(url=tequila_location_endpoint,params=parameter,headers=headers)
            self.tequila_data=tequila_response2.json()
            #TODO put iata code to google sheet
            self.sheety_variables = {
                "sheet1": {
                    "iataCode":self.tequila_data["locations"][0]["id"]
                }
            }
            self.row_id=self.sheety_data["sheet1"].index(i)+2
            sheety_response2=requests.put(url=f"{sheety_put_endpoint}/{self.row_id}",json=self.sheety_variables )
