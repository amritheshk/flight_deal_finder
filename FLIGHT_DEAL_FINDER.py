import requests
from data_manager import Data
from flight_data import Flight_data
from flight_search import Search_flight
from twilio.rest import Client


#TODO constants
end=False
TEQUILA_APIKEY=""
account_sid=""
auth_token=""
my_twilio_phno=""


#TODO write data to google sheet
data=Data()
data.create_data_sheet()

#TODO find the iata code and write it to google sheet
flight_data=Flight_data()
flight_data.find_iatacode()

#TODO search flight using iata code
search_flight=Search_flight()
search_flight.start_search()

#TODO compare the pricing
flight_search_data=search_flight.flight_search_data

#TODO send a mail
for i in flight_search_data:
    if i["lowest_acceptable_price"]>=i["price"]:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert!"
                 f"Only {i['price']} to fly from {i['cityFrom']}-{i['flyFrom']} to {i['cityTo']}-{i['flyTo']},from {search_flight.from_date} to {search_flight.to_date}"
            ,from_=my_twilio_phno,
            to="+919633323325"
        )

