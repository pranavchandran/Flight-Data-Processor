# __Author__ = "Pranav Chandran"
# __Date__ = 11-03-2025
# __Time__ = 22:33
# __FileName__ = flight_data_processor.py
import datetime
from enum import Enum


class FlightStatus(Enum):
    ON_TIME = "ON_TIME"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"


class FlightDataProcessor:
    def __init__(self, flights: list):
        self.flights = []
        self.data_cleaner(flights)

    def data_cleaner(self, flights):
        for i in flights:
            if isinstance(i['departure_time'], str):
                i['departure_time'] = datetime.datetime.strptime(i['departure_time'], "%Y-%m-%d %H:%M")
            if isinstance(i['arrival_time'], str):
                i['arrival_time'] = datetime.datetime.strptime(i['arrival_time'], "%Y-%m-%d %H:%M")
            if isinstance(i['status'], str):
                i['status'] = FlightStatus(i['status'])
            duration_minutes = (i['arrival_time'] - i['departure_time']).total_seconds() / 60
            i['duration_minutes'] = duration_minutes
            self.flights.append(i)

    def add_flight(self, data: dict) -> None:
        for i in self.flights:
            if i['flight_number'] == data['flight_number']:
                return
        self.data_cleaner([data])

    def remove_flight(self, flight_number):
        i = 0
        for i in self.flights:
            if i['flight_number'] == flight_number:
                print(f"Removing flight {flight_number}")
                self.flights.remove(i)
                return

    def flights_by_status(self, status):
        return [i for i in self.flights if i['status'] == status]

    def update_flight_status(self, flight_number, new_status):
        for flight in self.flights:
            if flight['flight_number'] == flight_number:
                flight['status'] = FlightStatus(new_status)
                return
        print(f"Flight {flight_number} not found")

    def get_longest_flight(self):
        return max(self.flights, key=lambda x: x['duration_minutes'])


# flight_data = [
#     {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45",
#      "status": "ON_TIME"},
#     {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00",
#      "status": "DELAYED"},
# ]
# flight_data_processor = FlightDataProcessor(flight_data)
