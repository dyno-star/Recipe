from dotenv import load_dotenv
import os
import random
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

ingredients = ["banana", "eggs", "cheese", "honey", "bread", "tomato", "milk", "apple", "sausages"]
chosen_ingredients = random.sample(ingredients, 3)
print(f"Today's random ingredients are {', '.join(chosen_ingredients)}")