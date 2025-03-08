from dotenv import load_dotenv
import os
import random
import time
from openai import OpenAI


#Recipe Generator

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing API key. Set OPENAI_API_KEY in your environment variables.")

client = OpenAI()

def get_ingredients():
    ingredients_input = input("Enter a list of ingredients separated by commas: ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]
    return ingredients

chosen_ingredients = random.sample(get_ingredients(), 3)
print(f"Today's random ingredients are {', '.join(chosen_ingredients)}")

def countdown(seconds):
    while seconds > 0:
        print(f"Retrying in {seconds} seconds...", end="\r", flush=True)
        time.sleep(1)
        seconds -= 1
    print("Retrying now...               ")  

def promptGPT(prompt, model, system_requirements, retries=3, wait_time=30):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_requirements},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            print(f"An error occurred: {e}")
            if "insufficient_quota" in str(e) and attempt < retries - 1:
                countdown(wait_time)
            else:
                return "Failed to generate a recipe due to API limitations."

model = "gpt-3.5-turbo"
system_requirements = "You are a helpful AI designed to create recipes."
prompt = f"Create a simple and delicious recipe using the following ingredients: {', '.join(chosen_ingredients)}."

recipe = promptGPT(prompt, model, system_requirements)
print("\nHere is your recipe:")
print(recipe)
