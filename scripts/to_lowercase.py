import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="youtube_data",
    user="postgres",
    password="postgres",
    port="15432"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

try:
    # Fetch all table names
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    table_names = [row[0] for row in cursor.fetchall()]

    # Iterate over all tables
    for table_name in table_names:
        # Fetch the table schema
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        column_names = [row[0] for row in cursor.fetchall()]

        # Change each column name to lower case and replace spaces with underscores
        for column_name in column_names:
            new_name = column_name.lower().replace(' ', '_')
            if new_name != column_name:
                cursor.execute(f'ALTER TABLE "{table_name}" RENAME COLUMN "{column_name}" TO "{new_name}"')

    # Commit the changes
    conn.commit()

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()