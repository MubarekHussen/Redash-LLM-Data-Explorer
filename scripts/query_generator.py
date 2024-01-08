import os
import psycopg2
from dotenv import load_dotenv
from openai import OpenAI

def generate_sql_query(question):
    load_dotenv()

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    conn = psycopg2.connect(
        host="redash-postgres-1",
        database="youtube_data",
        user="postgres",
        password="postgres",
        port="5432"
    )

    cursor = conn.cursor()

    try:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        table_names = [row[0] for row in cursor.fetchall()]

        schemas = {}
        for table_name in table_names:
            cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
            schema_rows = cursor.fetchall()
            schemas[table_name] = {row[0]: row[1] for row in schema_rows}

        schemas_str = ', '.join(f"{table_name}: {', '.join(f'{col_name} ({col_type})' for col_name, col_type in schema.items())}" for table_name, schema in schemas.items())

        if question.lower() in ['hi', 'hello', 'hey']:
            return "Hello! I'm an AI assistant. I can help you generate SQL queries based on your questions."
        elif question.lower() == 'what is your name?':
            return "My name is Query Generator."
        elif question.lower() == 'what can you do?':
            return "I can help you generate SQL queries based on your questions."
        
        prompt = f"Retrieve data based on the question: {question}."
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant. The database has the following schemas: {schemas_str}."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        suggested_query = chat_completion.choices[0].message.content.strip()

        try:
            start_index = suggested_query.index("SELECT")
            end_index = suggested_query.index(";") + 1
        except ValueError:
            sql_query = suggested_query
        else:
            sql_query = suggested_query[start_index:end_index]

        answer = []
        answer.append(suggested_query)
        answer.append(sql_query)

        return answer

    finally:
        cursor.close()
        conn.close()


question = "how can I get the operatig system that has a maximum view ?"
sql_query = generate_sql_query(question)[1]
print(sql_query)