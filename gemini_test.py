from dotenv import load_dotenv
from google import genai
import os
import time

print("STEP 1: Loading .env")
load_dotenv()

key = os.getenv("GEMINI_API_KEY")
print("STEP 2: Key loaded =", bool(key))

print("STEP 3: Creating Gemini client")
client = genai.Client(api_key=key)

print("STEP 4: Sending request")
start = time.time()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What is a neural network in one sentence?"
)

print(f"STEP 5: Response received after {time.time()-start:.1f} seconds")
print(response.text)