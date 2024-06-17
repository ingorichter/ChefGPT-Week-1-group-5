# Encode - AI Bootcamp - Week 1 Project

This repository contains the weekend group project for Week 1 of the Encode AI Bootcamp. It is a Python program that uses the OpenAI API to allow users to ask a chef for a recipe. The chef responds with a recipe that matches their unique personality.

## Group Members' IDs

- **HA8T5C**
- **UIPAsU**
- **JqqcqX**
- **oy04T7**
- **25K4RW**

## Chef Personalities (All Fake Names)

- **Bjorn Hansen**: A calm and methodical chef with a deep respect for nature. He strictly adheres to traditional Icelandic culinary methods and is known for his polite and reserved demeanor.
- **Sofia Gutierrez**: A passionate and lively chef who loves sharing stories over a meal. She embraces both traditional and modern Argentinian cooking styles and is friendly and engaging, though she can be very direct and outspoken.
- **Yuki Tanaka**: A precise and disciplined chef focused on perfection in every dish. He incorporates traditional Japanese ingredients to enhance dishes, follows traditional Japanese culinary techniques rigorously, and is generally respectful but can be very strict and blunt in the kitchen.
- **Amira Al-Farsi**: A warm and hospitable chef who always makes guests feel at home. She loves cooking Halal dishes and sticks to traditional Middle Eastern recipes. She is extremely polite and accommodating but not great with criticism
- **Hans Muller**: A jovial and hearty chef with a knack for bringing people together. He loves mixing traditional German cuisine with innovative twists and is usually friendly and humorous, though he can be quite direct and sometimes rude. He is also very particular about ingredient choices.

## Get Started

Please provide your OpenAI API key in a .env file. The content of the file can be found in the [`.env.example`](./.env.example) file.

### Run the Script by Cloning

Clone the repository:

```python
git clone https://github.com/ingorichter/ChefGPT-Week-1-group-5 && cd ChefGPT-Week-1-group-5
```

Install the dependencies:

```python
pip install -r requirements.txt
```

Run ChefGPT:

```python
python ChefGPT.py
```

### How to Add More Chef Personalities

The `chefs.json` file contains a list of fake names and corresponding chef personalities. To add more chefs, simply update this file and run the script again.

### Example usage

```shell
python ChefGPT.py
Please select a Chef:
1 - Bjorn Hansen, Country: Iceland
2 - Sofia Gutierrez, Country: Argentina
3 - Yuki Tanaka, Country: Japan
4 - Amira Al-Farsi, Country: Saudi Arabia
5 - Hans Muller, Country: Germany
Enter the number of your choice: 4
Type the name of the dish you want a recipe for:
fish stew
```

Sample response from Chef Amira Al-Farsi:

```console
I'm delighted to share a traditional Middle Eastern-style fish stew recipe with you. Here's a detailed recipe along with the preparation steps:

Ingredients:
- 1 lb white fish fillets (such as cod or tilapia), cut into chunks
- 1 onion, finely chopped
- 2-3 garlic cloves, minced
- 2 tomatoes, chopped
- 1 red bell pepper, sliced
- 1 yellow bell pepper, sliced
- 1 zucchini, sliced
- 4 cups fish or vegetable broth
- 2 tablespoons tomato paste
- 1 teaspoon ground cumin
- 1 teaspoon ground coriander
- 1 teaspoon paprika
- Salt and pepper to taste
- Fresh parsley, chopped (for garnish)
- Lemon wedges (for serving)

Preparation Steps:
1. In a large pot, heat some olive oil over medium heat. Add the chopped onions and cook until they are translucent.
2. Add the minced garlic and cook for another minute until fragrant.
3. Stir in the chopped tomatoes, bell peppers, and zucchini. Cook for a few minutes until the vegetables start to soften.
4. Add the tomato paste, ground cumin, coriander, paprika, salt, and pepper. Stir well to coat the vegetables with the spices.
5. Pour in the fish or vegetable broth and bring the stew to a gentle simmer.
6. Carefully add the fish chunks into the stew, making sure they are submerged. Let the stew simmer for about 10-15 minutes until the fish is cooked through.
7. Taste and adjust the seasoning if needed. Add more salt or pepper as per your preference.
8. Once the fish is fully cooked, remove the pot from the heat.
9. Serve the fish stew hot, garnished with fresh parsley and accompanied by lemon wedges on the side.
10. Enjoy your delicious and comforting fish stew with some crusty bread or over a bed of rice.

I hope you enjoy making and savoring this hearty and flavorsome fish stew! If you need any more assistance, feel free to ask.
```