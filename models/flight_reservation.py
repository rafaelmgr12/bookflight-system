# from models.payment import Payment

# Task 7: Create Reservation Class
import datetime
from flight import Flight


class FlightReservation:
    __reservation_number: int
    __user_id: int
    __flight: Flight
    __seat_count: int
    __creation_date: datetime.datetime
    __total_amount: float
    
    def __init__(self, reservation_number: int, user_id: int, flight: Flight, seat_count: int, creation_date: datetime.datetime, total_amount: float):
        
        self.__reservation_number = reservation_number
        self.__user_id = user_id
        self.__flight = flight  # Could be a flight object or a string representing flight details
        self.__seat_count = seat_count  # Number of seats reserved by the customer
        self.__creation_date = creation_date
        self.__total_amount = total_amount
        
        
    # Getter methods
    
     # Get reservation number
    def get_reservation_number(self):
        return self.__reservation_number

    # Get passengers/seats in the reservation
    def get_seat_count(self):
        return self.__seat_count

    # Update seat count
    def update_seat(self, new_seat_count:int):
        if self.__seat_count > 0:
            self.__seat_count = new_seat_count
            print(f"Seat count updated to {new_seat_count}.")
        else:
            print(f"Seat {new_seat_count} not available.")

    def __repr__(self):
        self.__status = None
        return (f"FlightReservation(reservation_number={self.__reservation_number}, "
                f"user_id={self.__user_id}, flight={self.__flight}, "
                f"seat_count={self.__seat_count}, status='{self.__status}', "
                f"creation_date='{self.__creation_date}', total_amount={self.__total_amount})")