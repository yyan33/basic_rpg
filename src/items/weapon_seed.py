import csv
import sqlite3


def load_csv(data, csv_file):
    with open(csv_file) as f:
        f_reader = csv.reader(f)
        # Skip Headers
        next(f_reader)
        for row in f_reader:
            data.append(row)


def create_table(name, c):
    # # Create table if doesnt exist
    c.execute('''CREATE TABLE IF NOT EXISTS {} (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                display text NOT NULL,
                min integer NOT NULL,
                max integer NOT NULL,
                num_of_atks integer NOT NULL
                )'''.format(name))


def populate_table(name, data, c):
    c.executemany('''INSERT INTO {}(
          name,
          display,
          min,
          max,
          num_of_atks)
          VALUES (?,?,?,?,?)'''.format(name), data)


if __name__ == "__main__":
    # Settings
    csv_file = "weapons.csv"
    database_name = "weapons.db"
    table_name = "Weapons"

    # Load data from CSV
    data = []
    load_csv(data, csv_file)

    # Connect to database and create cursor
    con = sqlite3.connect(database_name)
    c = con.cursor()

    # Delete previous table
    c.execute("DROP TABLE {}".format(table_name))

    # Create table if it doesnt exist, then populate with data
    create_table(table_name, c)
    populate_table(table_name, data, c)

    # Save changes and close connection
    con.commit()
    con.close()
    print("Seeded.")
