import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="youtube_data",
    user="postgres",
    password="postgres",
    port="15432"
)

cursor = conn.cursor()

try:
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    table_names = [row[0] for row in cursor.fetchall()]

    for table_name in table_names:
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        column_names = [row[0] for row in cursor.fetchall()]

        for column_name in column_names:
            new_name = column_name.lower().replace(' ', '_')
            if new_name != column_name:
                cursor.execute(f'ALTER TABLE "{table_name}" RENAME COLUMN "{column_name}" TO "{new_name}"')

    conn.commit()

finally:
    cursor.close()
    conn.close()
