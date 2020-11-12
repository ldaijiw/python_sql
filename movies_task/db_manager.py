import pyodbc
import csv

class MovieDBManager:
    def __init__(self):
        self.user = 'daiji'
        self.start_connection()

    
    def start_connection(self, server = "databases1.spartaglobal.academy", database = "Northwind", username = "SA", password = "Passw0rd2018"):
        try:
            print("Establishing Connection")
            # connect to server with pyodbc.connect()
            self.db_connection = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}")
            # init cursor to execute queries
            self.cursor = self.db_connection.cursor()
        except:
            print("Something went wrong")
        
        else:
            # if no errors occurs prints following message
            print("Connection Successfully Made")


    def create_table(self):
        create_from_data = True if input("\nCreate table from existing data?\n(y/n)\n") == "y" else False

        if create_from_data:
            filename = input("\nPlease enter path for file\n")
            try:
                self.table_name, self.table_data = self.data_from_file(filename)
                self.column_names = self.table_data.pop(0)

            except FileNotFoundError as errmsg:
                print(errmsg)
                print("\nSorry that's not a valid, path. Please try again.\n\n")
                self.create_table()

            else:
                print("File successfully loaded\n")
                print(f"TABLE NAME: {self.table_name}")
                print(f"COLUMN NAMES: {self.column_names}")
                print(f"{len(self.table_data)} ROWS TO BE ADDED")


        proceed = True if input("\nWould you like to proceed to table creation?\n(y/n)\n") == "y" else False
        while not proceed:
            attr_to_change = input("What would you like to change?\n(table name/column names)\n").lower().replace(' ', '_')

            if attr_to_change == 'table_name':
                self.table_name = input("\nPlease enter new table name\n")
                print(f"NEW TABLE NAME {self.table_name}")

            elif attr_to_change == 'column_names': 
                column_to_change = int(input(f"\nWhich column would you like to change?\n0 - {len(self.column_names)}\n"))

                try:
                    self.column_names[column_to_change] = input("\nPlease enter new column name\n")

                except IndexError as errmsg:
                    print(errmsg)
                    print("Column index out of range, please try again")

                else:
                    print("Column name change successful\n")
                    print(f"NEW COLUMN NAMES\n{self.column_names}")

            else:
                print("Not recognised, please try again.")
                continue
            
            proceed = True if input("\nWould you like to make any other changes?\n(y/n)\n") == "n" else False
        
        print(f"TABLE NAME: {self.table_name}")
        print(f"COLUMN NAMES: {self.column_names}")
        print(f"{len(self.table_data)} ROWS TO BE ADDED")

        




    def data_from_file(self, filename):
        with open(filename, "r") as datafile:
            if filename[-3:] == "csv":
                csvdata = list(csv.reader(datafile))
                table_name = f"{self.user}_{filename[:-4].split('/')[-1]}"
                return table_name, csvdata
                
                
                



    def table_info(self):
        pass


    def select_query(self, select_details = "*"):
        pass


    def find_movie(self, movie_title):
        pass

    
    def add_movie(self, movie_details):
        pass


def main():
    new_mdbm = MovieDBManager()
    #new_mdbm.data_from_file("movies_task/imdbtitles.csv")
    new_mdbm.create_table()

if __name__ == "__main__":
    main()
    