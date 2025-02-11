from dotenv import load_dotenv
import os
import random
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# Select random ingredients
ingredients = ["banana", "eggs", "cheese", "honey", "bread", "tomato", "milk", "apple", "sausages"]
chosen_ingredients = random.sample(ingredients, 3)
print(f"Today's random ingredients are {', '.join(chosen_ingredients)}")

# Function to send prompt to GPT
def promptGPT(prompt, model, system_requirements):
    try:
        response = client.chat.completions.create(
            model= model,
            messages=[
                {"role": "system", "content": system_requirements},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

model =  "gpt-3.5-turbo"
system_requirements = "You are a helpful AI designed to create recipes"

prompt = f"Create a simple and delicious recipe usong the following ingredients {', '.join(chosen_ingredients)}"

recipe = promptGPT(prompt, model, system_requirements)
print("\nHere is your recipe:")
print(recipe)