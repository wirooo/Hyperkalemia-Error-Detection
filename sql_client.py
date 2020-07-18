import pyodbc
import pandas as pd
import sqlalchemy
import urllib
import os

class SqlClient:
    """
    A class that interfaces with an MS SQL Server using pyodbc and sqlalchemy
    Stores pyodbc connection, cursor, and sqlalchemy engine in self.cnxn, self.cursor, and self.engine
    """
    def __init__(self, server_name, database_name, username, password):
        self.server_name = server_name
        self.database_name = database_name
        self.username = username
        self.password = password
        params = f"Driver={{ODBC Driver 17 for SQL Server}};" \
                 f"Server={self.server_name};" \
                 f"Database={database_name};" \
                 f"UID={username};" \
                 f"PWD={password};"
        self.cnxn = pyodbc.connect(params)
        self.cursor = self.cnxn.cursor()
        self.engine = sqlalchemy.create_engine(
            f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(params)}")

    def upload_csv(self, path_to_csv, table_name):
        """
        Uploads csv to SQL server using pandas

        :param path_to_csv: string of csv file path
        :param table_name: name of table in SQL
        """
        df = pd.read_csv(path_to_csv)
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def upload_csv_directory(self, path_to_directory):
        """
        Uploads all .csv files in given directory to SQL server using pandas
        Assigns SQL name identical to file name less ".csv"

        :param path_to_directory: string of directory path
        """
        for file in os.listdir(path_to_directory):
            filename = os.fsdecode(file)
            if filename.endswith('.csv'):
                print(filename)
                self.upload_csv(os.path.join(path_to_directory, filename), filename[:-4])

    def execute(self, command, commit=True):
        """
        Execute any SQL command, set commit flag to False to avoid saving any commands

        :param command: SQL command to execute
        :param commit: whether to commit changes to SQL
        :return:
        """
        self.cursor.execute(command)
        if commit:
            self.cnxn.commit()


if __name__ == '__main__':
    server_name = "teamseven.ct4lx0aqwcg9.ca-central-1.rds.amazonaws.com"
    database_name = "demodata"
    username = "admin"
    password = "jXGiWT5FqVTyMQHXa74c"
    s = SqlClient(server_name, database_name, username, password)
    # s.upload_csv("physionet.org/files/mimiciii-demo/1.4/NOTEEVENTS.csv", "NOTEEVENTS")
    s.upload_csv_directory("physionet.org/files/mimiciii-demo/1.4/")
