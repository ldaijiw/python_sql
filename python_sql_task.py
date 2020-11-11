import pyodbc

class SQLConnector:
    def __init__(self):
        self.start_connection()
    
    def start_connection(self, server = "databases1.spartaglobal.academy", database = "Northwind", username = "**", password = "***"):
        
        try:
            print("Establishing Connection")
            self.db_connection = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}")
        except:
            print("Something went wrong")
        
        else:
            print("Connection Successfully Made")
        

    def create_table(self, table_name, **column_info):
        cursor = self.db_connection.cursor()
        sql_query = f"CREATE TABLE {table_name}("
        


if __name__ == "__main__":
    python_sql_obj = SQLConnector()
    python_sql_obj.create_table("ldw_table", name = "VARCHAR(16)" , age = "INT", address = "VARCHAR(32)")