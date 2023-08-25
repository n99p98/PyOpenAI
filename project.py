import openai
import configparser

# Read the config file//
config = configparser.ConfigParser()
config.read('config.ini')

# Get the API key and other values
openai.api_key = config.get('OpenAI', 'piyush_api_key')
max_tokens = config.getint('OpenAI', 'max_tokens')
avg_token_length = config.getint('OpenAI', 'avg_token_length')

prompt = """
Task: Create a sample list of students which returns in following JSON structure:
{
    "students": [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "age": 20,
            "grade": "Sophomore"
        },
        {
            "id": 2,
            "first_name": "Jane",
            "last_name": "Smith",
            "age": 19,
            "grade": "Freshman"
        },
        ...etc
    ]
}

"""
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
temperature=0,
top_p=0,
frequency_penalty=0.0,
presence_penalty=0.0
)
print("\n ========== OpenAI PROMPT ============ \n")
print(prompt)
print("\n ========== ENDS ============ \n")
print("\n ========== OpenAI RESPONSE ============ \n")
print(response)
print("\n ========== ENDS ============ \n")
json_text = response['choices'][0]['message']['content']
print("\n ========== JSON RESPONSE ============ \n")
print(json_text)
print("\n ========== ENDS ============ \n")
