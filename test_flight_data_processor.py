# __Author__ = "Pranav Chandran"
# __Date__ = 11-03-2025
# __Time__ = 23:02
# __FileName__ = test_flight_data_processor.py
import unittest
from flight_data_processor import FlightDataProcessor, FlightStatus


class TestFlightDataProcessr(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED"},
        ]
        self.processor = FlightDataProcessor(self.sample_data)

    def test_add_flight(self):
        new_flight = {"flight_number": "AZ003", "departure_time": "2025-03-01 10:00",
                      "arrival_time": "2025-03-01 15:00", "status": "ON_TIME"}
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 3)

    def test_add_duplicate_flight(self):
        new_flight = {"flight_number": "AZ002", "departure_time": "2025-03-01 10:00",
                      "arrival_time": "2025-03-01 15:00", "status": "ON_TIME"}
        self.processor.add_flight(new_flight)
        self.assertEqual(len(self.processor.flights), 2)

    def test_remove_flight(self):
        self.processor.remove_flight("AZ001")
        self.assertEqual(len(self.processor.flights), 1)

    def test_remove_non_existent_flight(self):
        self.processor.remove_flight("AZ003")
        self.assertEqual(len(self.processor.flights), 2)

    def test_flight_by_status(self):
        self.assertEqual(len(self.processor.flights_by_status(FlightStatus.ON_TIME)), 1)
        self.assertEqual(len(self.processor.flights_by_status(FlightStatus.DELAYED)), 1)

    def test_get_longest_flight(self):
        self.assertEqual(self.processor.get_longest_flight()['flight_number'], "AZ001")

    def test_update_flight_status(self):
        self.processor.update_flight_status("AZ001", FlightStatus.DELAYED)
        self.assertEqual(self.processor.flights[0]['status'], FlightStatus.DELAYED)


if __name__ == "__main__":
    unittest.main()
