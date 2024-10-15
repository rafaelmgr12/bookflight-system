# To handle operations related to the FlightReservation and related tables.
import datetime
import mysql.connector
from sqlalchemy import Float
from config.database_config import get_db_connection
from ..models.auth import Account

# Task 8: Complete the implementation of the ReservationRepository class


class ReservationRepository:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def get_reservation(self, reservation_number: int):
        query = "SELECT * FROM FlightReservation WEHRE reservation_number = %s"
        self.cursor.execute(query, (reservation_number,))
        return self.cursor.fetchone()

    def get_reservation_by_userse(self, user: Account):
        username = user.username
        get_user_id_query = """
            SELECT account_id FROM Account
            WHERE username = %s
        """
        self.cursor.execute(get_user_id_query, (username,))
        user_id_result = self.cursor.fetchone()

        if user_id_result:
            user_id = user_id_result[0]

            # Get reservations from the FlightReservation table for the user ID
            query = """
                SELECT * FROM FlightReservation
                WHERE user_id = %s
            """
            self.cursor.execute(query, (user_id,))
            return self.cursor.fetchall()
        else:
            return None  # User with the given username not found

    def cancel_reservation(self, reservation_number: int):
        # Retrieve the reservation details
        get_reservation_query = """
            SELECT flight_no, seats
            FROM FlightReservation
            WHERE reservation_number = %s
        """
        self.cursor.execute(get_reservation_query, (reservation_number,))
        reservation = self.cursor.fetchone()

        if reservation:
            flight_no, seats = reservation

            # Delete the reservation entry
            delete_reservation_query = """
                DELETE FROM FlightReservation
                WHERE reservation_number = %s
            """
            self.cursor.execute(delete_reservation_query,
                                (reservation_number,))

            # Update the booked seats in the Flight table
            update_flight_query = """
                UPDATE Flight
                SET booked_seats = booked_seats - %s
                WHERE flight_no = %s
            """
            self.cursor.execute(update_flight_query, (seats, flight_no))

            # Commit the transaction to save the updates
            self.connection.commit()
            print(f"Reservation {
                  reservation_number} has been successfully canceled and deleted.")
        else:
            print(f"Reservation {reservation_number} not found.")

    def create_reservation(self, user: Account, flight_no: str, seats: int, creation_date: datetime.datetime, payment_amount: float):
        pass
