import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Authenticate OpenAI using the API key
# Replace 'YOUR_API_KEY' with the actual API key
openai.api_key = api_key

# Now you can use OpenAI API for further operations
# For example:
response = (openai
                .chat
                .completions
                .create(
                        messages=[{
                                    "role": "user",
                                    "content": "Say this is a test"}
                                ],
                        model="gpt-3.5-turbo",
            )
            )



print(response.choices[0].text)