import requests

#TODO constants
TEQUILA_APIKEY=""
end=False

#TODO endpoints
sheety_get_endpoint= "https://api.sheety.co/eb1d80cb386cef1092824698410439ad/citiesToVisit/sheet1"
sheety_post_endpoint="https://api.sheety.co/eb1d80cb386cef1092824698410439ad/citiesToVisit/sheet1"
sheety_put_endpoint= "https://api.sheety.co/eb1d80cb386cef1092824698410439ad/citiesToVisit/sheet1"

#TODO post the variables to google sheet
class Data:
    def __init__(self):
        self.end=False
    def create_data_sheet(self):
        while self.end==False:
            sheety_variables={
            "sheet1":{
                "city":input("Enter name of the city you want to visit : "),
                "lowestPrice":input("Enter acceptable price for travel : "),
            }
            }

            sheety_response1=requests.post(url=sheety_post_endpoint,json=sheety_variables)
            self.add_another_city=input("Would you like to add another city ?y/n : ").lower()

            if self.add_another_city=="n":
                self.end=True

