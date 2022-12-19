import sqlite3
import pandas as pd

# Connecting to the database
conn = sqlite3.connect('attr_data.db')
cur = conn.cursor()

# Extracting data from a database
read = cur.execute("SELECT * FROM attrition_records")
col = [i[0] for i in cur.description]

# Creating a dataframe from the extracted data
info = pd.DataFrame(read, columns=col, index=None)

# Saving it as a .csv file
info.to_csv("attr.csv", index=False)


# Reading the entire file in the dataframe
def read_csv():
    return info.to_markdown(index=False)

