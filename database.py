# Program to display the data

import mysql.connector


class DB:
    def __init__(self) -> None:
        self.DB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user"
        )
        self.cur=self.DB.cursor()

