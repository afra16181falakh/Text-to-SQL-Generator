import openai
from model import SQLConverter  # Importing SQLConverter class

async def main():
    api_key = "YOUR_API_KEY"  # Set your OpenAI API key here
    converter = SQLConverter(api_key)  # Create an instance of SQLConverter
    user_query = input("Enter your natural language query: ")
    sql_command = await converter.convert(user_query)  # Convert the natural language query to SQL
    print(f"Generated SQL Command: {sql_command}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
