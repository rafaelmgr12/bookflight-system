
# Task 14: Import the Amadeus components


# Task 3: Define the Flight class
import datetime
from turtle import distance


class Flight:
    __flight_no: int
    __airline_code: str
    __distance_km: float
    __dep_time: datetime.datetime
    __arri_time: datetime.datetime
    __dep_port: str
    __arri_port: str
    __booked_seats: int
    __total_seats: int

    def __init__(self, flight_no: int, airline_code: str, distance_km: float, dep_time: datetime.datetime, arri_time: datetime.datetime, dep_port: str, arri_port: str, booked_seats: int = 0):
        self.__flight_no = flight_no
        self.__airline_code = airline_code
        self.__distance_km = distance_km
        self.__dep_time = dep_time
        self.__arri_time = arri_time
        self.__dep_port = dep_port
        self.__arri_port = arri_port
        self.__total_seats = 50  # Set total seats to 50
        self.__booked_seats = booked_seats  # Initialize booked seats to 0

    # Getters
    def get_flight_no(self):
        return self.__flight_no

    def get_airline_code(self):
        return self.__airline_code

    def get_distance_km(self):
        return self.__distance_km

    def get_dep_time(self):
        return self.__dep_time

    def get_arri_time(self):
        return self.__arri_time

    def get_dep_port(self):
        return self.__dep_port

    def get_arri_port(self):
        return self.__arri_port

    # Method to get the number of available seats
    def get_available_seats(self):
        return self.__total_seats - self.__booked_seats
    # Setters
    def set_flight_no(self, flight_no: int):
        self.__flight_no = flight_no

    def set_airline_code(self, airline_code: str):
        self.__airline_code = airline_code

    def set_dep_time(self, dep_time: datetime.datetime):
        self.__dep_time = dep_time

    def set_arri_time(self, arri_time: datetime.datetime):
        self.__arri_time = arri_time

    def set_dep_port(self, dep_port: str):
        self.__dep_port = dep_port

    def set_arri_port(self, arri_port: str):
        self.__arri_port = arri_port

    # Book seats
    def book_seats(self, num_seats: int):
        if num_seats <= self.get_available_seats():
            self.__booked_seats += num_seats
            print(f"{num_seats} seat(s) successfully booked.")
        else:
            print(f"Not enough seats available. Only {
                  self.get_available_seats()} left.")

    # Seat availability
    def get_total_seats(self):
        return self.__total_seats

    # String representation
    def __repr__(self):
        return (f"Flight No: {self.__flight_no}, Airline Code: {self.__airline_code}, "
                f"Departure from: {self.__dep_port} at {self.__dep_time}, "
                f"Arrival at: {self.__arri_port} at {self.__arri_time}")

    # Task 14: Implement the get_ticket_price() function
