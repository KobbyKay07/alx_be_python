weather = input("What is the weather like today? (sunny/rainy/cold):") # Get user input for weather condition
if weather == "sunny": # Check if the weather is sunny
    print("Wear a t-shirt and sunglasses.") # Provide advice for sunny weather
elif weather == "rainy": # Check if the weather is rainy
    print("Don't forget your umbrella and a raincoat.") # Provide advice for rainy weather
elif weather == "cold": # Check if the weather is cold
    print("Make sure to wear a warm coat and a scarf.") # Provide advice for cold weather
else: # Handle unexpected input
    print("Sorry, I don't have recommendations for this weather.") # Provide a default message for unrecognized weather conditions