import sqlite3
# class for Database with basic sqlite CRUD operations

class DatabaseHandler:

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
      try:
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        return self.cursor
      except Exception as e:
        print("Database Connection Error.")

    def create_table(self, table_name: str, columns: list) -> None:
        """
        Create a table in the database

        :param table_name (str): name of the table
        :param columns (list): list dictionary of columns and its types
        :return: None
        """

        columns_str = ""
        attrs = []

        # unpack columns metadata
        for column in columns:
            # Set attributes
            if len(column) > 2:
              attrs = column[2]
            else:
              attrs = ""
            #Set column details (name, type, other attributes)  
            columns_str += column[0] + " " + column[1] + " " + " ".join(attrs) + ", "

         # Remove extra comma and a space at the end   
        columns_str = columns_str[:-2]

        # Create Table Final query
        query = "CREATE TABLE  IF NOT EXISTS " + table_name + " (" + columns_str + ")"

        try:
          self.cursor.execute(query)
          self.conn.commit()
        except Exception as e:
          print("Invalid CREATE TABLE Query.", e )

    def insert(self, table_name: str, values, columns= []) -> None:
        """
        Insert a row into the table

        :param table_name (str): name of the table
        :param columns (list): list of columns
        :param values (list): list of values
        :return: None
        """
        columns_str = ""
        if columns != []:
          for column in columns:
              columns_str += str(column) + ", "
          columns_str = " (" + columns_str[:-2] + ")"

        values_str = ""
        for value in values:
            values_str += "\"" + str(value) + "\", "
        values_str = values_str[:-2]

        query = "INSERT INTO " + table_name  + columns_str + " VALUES (" + values_str + ")"
        print(query)

        try:
          self.cursor.execute(query)
          self.conn.commit()
        except Exception as e:
          print("Invalid INSERT Query: ", e)

    def select(self, table_name: str, columns: list, where = "", attrs = "") -> list:
        """
        Select rows from the table

        :param table_name (str): name of the table
        :param columns (list): list of columns
        :param where (str): where clause
        :param attrs (str): Other attributes
        :return (list): list of rows
        """
        columns_str = ""
        for column in columns:
            columns_str += column + ", "
        columns_str = columns_str[:-2]

        query = "SELECT " + columns_str + " FROM " + table_name

        if where:
           query += " WHERE " + where

        if attrs:
          query += " " + attrs
        print(query)

        try:
          self.cursor.execute(query)
          return self.cursor.fetchall()
        except Exception as e:
          print("error: ", e)

    def update(self, table_name, columns, values, where) -> None:
        """
        Update rows in the table

        :param table_name (str): name of the table
        :param columns (list): list of columns
        :param values (list): list of values
        :param where (str): where clause
        :return: None
        """

        query = "UPDATE " + table_name + " SET "

        columns_str = ""
        for column in columns:
            columns_str += column + " = '" + values[columns.index(column)] + "', "
        columns_str = columns_str[:-2]
        query += columns_str

        try:
          if where != "" or where:
            query += " WHERE " + where
          else:
            raise Exception("Unsafe Update Query without WHERE clause.")

          self.cursor.execute(query)
          self.conn.commit()
        except Exception as e:
          print(e)

    def delete(self, table_name, where):
        """
        Delete rows from the table

        :param table_name (str): name of the table
        :param where (str): where clause
        :return: None
        """
        query = "DELETE FROM " + table_name

        try:

          if where != "" or where:
            query += " WHERE " + where
          else:
            raise Exception("Unsafe DELETE Query without WHERE clause.")

          self.cursor.execute(query)
          self.conn.commit()

        except Exception as e:
          print(e)

    def close(self):
        """
        Close the database connection
        
        :return: None
        """
        self.conn.close()

    def __exit__(self, exec_type, exec_value, traceback):
        """
        Destructor
        :return: None
        """
        self.conn.close()