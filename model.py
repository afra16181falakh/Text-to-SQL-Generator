import openai

class SQLConverter:
    def __init__(self, api_key):
        openai.api_key = api_key

    def convert(self, query):
        response = openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Convert the following natural language query to SQL: {query}"}
            ]
        )
        return response['choices'][0]['message']['content']
