import pyodbc

class MovieDBManager:
    def __init__(self):
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


    def create_table(self, table_name, **column_details):
        pass

    
    def table_info(self):
        pass


    def select_query(self, select_details = "*"):
        pass


    def find_movie(self, movie_title):
        pass