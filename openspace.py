
# Importing class Table from table.py file


from utils.table import Table, Seat
from utils.file_utils import name_list
import random
import pandas as pd

class Openspace:
    """
    Class defined as Openspace.
    """

    def __init__(self, number_of_tables: int = 6, number_of_seats: int = 4):
        """
        Function to initialize the argument of the Class "Openspace", And import the "table","seat" from table.py and "name" from file_utils.py as list.

        :number_of_tables: An int that define the range of table .
        :number_of_seats:An int that define the range of seats.
        """

        self.number_of_tables = number_of_tables

        self.tables = []
        for i in range(number_of_tables):
            self.tables.append(Table())

        self.seats = []
        for i in range(number_of_seats):
            self.seats.append(Seat())

        self.dictionary = {}
        for x in range(number_of_tables):
            key_name = F"Table {x+1}"
            self.dictionary[key_name] = []

    def organize(self, names: list = name_list):
        """
        Function to asign a name in every "seat" of every "table" in a random way.

        :names: A list of name who will be assign to the seats.
        :return: a random name from the list in each seat of each table if the seat is free.
        """

        temp_names = names

        for ind, table in enumerate(self.tables):
            
            key_name = F"Table {ind + 1}"

            for i, seat in enumerate(self.seats):
                
                if len(temp_names) > 0:
                    random_name = random.choice(temp_names)
                    table.assign_seat(random_name)
                    temp_names.remove(random_name)
                    self.dictionary[key_name].append(random_name)
                else: 
                    table.assign_seat('Free Spot')
                    self.dictionary[key_name].append(f'Free Spot {i}')
            
                

    def display(self):
        """
        Function displaying the tables. Each containing seats and every seat containing a name as a dataframe.

        :return: a pandas dataframe containing the tables. The seats for each table and a name for each seat.
        """

        print(pd.DataFrame(self.dictionary))

        if self.dictionary:
            return pd.DataFrame(self.dictionary)
        else:
            return pd.DataFrame()

    def store(self, filename):
        """
        Function that create a filename with a path on your computer containing the tables,seat,name of the openspace.

        :filename: dict containing the information of names,seats,tables.
        :return: A xlsx file containing the organization on the tables, seats and names.
        """
        df = pd.DataFrame(self.dictionary)
        df.to_excel(filename, index=False)
        




