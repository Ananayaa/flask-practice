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



# a = DB()
# mycursor = a.mydb.cursor()

# mycursor.execute("SELECT * FROM user1")

# # This SQL statement selects all data from the CUSTOMER table.
# result = mycursor.fetchall()


# # Printing all records or rows from the table.
# for res in result:
#     print(res)
# # It returns a result set.
