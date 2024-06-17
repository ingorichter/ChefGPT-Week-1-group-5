import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

model = "gpt-3.5-turbo"

def query_openai(messages):
    while True:
        print("\n")
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)
        
        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )
        user_input = input()
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

def prepare_message(chef, dish):
    messages = [
        {
            "role": "system",
            # "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
            "content": chef['personality']
        }
    ]

    messages.append(
    {
        "role": "system",
        "content": "Your client is going to ask for a recipe. 1. Suggest dishes based on ingredients. 2. Provide recipes based on the dishes provided. 3. Criticizing the recipes given by the user input. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
    })

    messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    })

    return messages

def load_chefs(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data["chefs"]

def display_chefs(chefs_data):
    print("Please select a Chef:")
    for index, chef in enumerate(chefs_data, start=1):
        print(f"{index} - {chef['name']}, Country: {chef['country']}")

def get_chef_selection(num_options):
    while True:
        try:
            selection = int(input("Enter the number of your choice: "))
            if 1 <= selection <= num_options:
                return selection
            else:
                print(f"Invalid selection. Please choose a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    options = load_chefs('chefs.json')
    display_chefs(options)
    selection = get_chef_selection(len(options))
    dish = input("Type the name of the dish you want a recipe for:\n")

    message = prepare_message(options[selection - 1], dish)
    # print(f"Message: %s", message)
    # print(f"You selected: {options[selection - 1]}")
    query_openai(message)

if __name__ == "__main__":
    main()