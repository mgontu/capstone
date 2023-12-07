import tkinter as tk
from tkinter import simpledialog
from tkinter import font as tkFont
import webbrowser
import pandas as pd
import sqlite3
import random


def open_link(url):
    webbrowser.open_new(url)

def recommend_products(responses):
    print(responses[1])
    print(responses[2])
    print(responses[3])
    data_path = 'data.xlsx'
    df = pd.read_excel(data_path) #reads the data and converts from excel file into a dataframe df
    #defines file path for SQLite database and creates connection to database
    db_path = 'database.db'
    conn = sqlite3.connect(db_path)
    df.to_sql('data_table', conn, index=True, if_exists='replace')
    cursor = conn.cursor() #sets up cursor to fetch variables later
    table_name = 'data_table'
    quest = f'SELECT * FROM {table_name};'
    cursor.execute(quest)
    rows = cursor.fetchall()#gets all the data and creates a list called rows with each list index as a tuple
    cursor.close()
    conn.close()
    product_dict = {}
    by_number_dict = {}
    for i in range(len(rows)):
        user_list = list(rows[i])
        product_dict[f"{user_list[3]}"] = rows[i] #creates a dictionary with product name as the key and all data as value
        by_number_dict[f"{i}"]  = rows[i]

    skin_type, skin_concern, product_type = responses[1], responses[2], responses[3]
    all_three = []
    just_two = []
    just_one = []


    for i in range(len(rows)):
        attributes = by_number_dict[f"{i}"]
        price_per_oz = attributes[15] / attributes[5]
        if (skin_type or "all") in attributes[9] and skin_concern in attributes[13] and product_type in attributes[2]:
            all_three.append((attributes[3], attributes[4]))
            all_three_price_per_oz = [price_per_oz]
        elif (skin_type or "all") in attributes[9] and product_type in attributes[2] or skin_concern in attributes[13]:
            just_two.append((attributes[3], attributes[4]))
            just_two_price_per_oz = [price_per_oz]
        elif product_type in attributes[2] and (skin_type or "all") in attributes[9] or skin_concern in attributes[13]:
            just_two.append((attributes[3], attributes[4]))
            just_two_price_per_oz = [price_per_oz]
        elif skin_concern in attributes[13] and product_type in attributes[2] or (skin_type or "all") in attributes[9]:
            just_two.append((attributes[3], attributes[4]))
            just_two_price_per_oz = [price_per_oz]
        elif skin_concern in attributes[13] or product_type in attributes[2] or (skin_type or "all") in attributes[9]:
            just_one.append((attributes[3], attributes[4]))
            just_one_price_per_oz = [price_per_oz]

    random_one = random.sample(just_one, 3)
    random_two = random.sample(just_two, 3)
    return random_one, random_two, all_three


    # Example logic to recommend products
    # return [("Product 1", "http://example.com/product1"),
    #         ("Product 2", "http://example.com/product2"),
    #         ("Product 3", "http://example.com/product3"),
    #         ("Product 4", "http://example.com/product4"),
    #         ("Product 5", "http://example.com/product5")]


    # data_path = 'data.xlsx'
    # df = pd.read_excel(data_path)

    # skin_type, skin_concern, product_type = responses[1], responses[2], responses[3]  # Assuming these are the order of questions

    # # Filter the DataFrame based on responses
    # filtered_df = df[(df['suitable skin types'] == skin_type) & (df['skin concerns'] == skin_concern) & (df['product_type'] == product_type)]
    
    # # Randomly pick 3 products, or all products if there are less than 3
    # recommended = filtered_df.sample(n=3) if len(filtered_df) > 3 else filtered_df

    # # Extract product names and URLs
    # recommendations = [(row['product_name'], row['Link']) for index, row in recommended.iterrows()]

    # return recommendations

def show_question(question, options, next_function):
    question_window = tk.Toplevel(root, bg='white')
    question_window.title("Question")
    
    # Set the font to match the opening page and text color to black
    question_label = tk.Label(question_window, text=question, bg='white', fg='black', font=description_font, justify='center')
    question_label.pack(padx=10, pady=10)  # Adjust padding as needed

    answer = tk.StringVar(question_window)
    answer.set(options[0])  # Set the default value

    # Set the font for the options menu
    option_menu = tk.OptionMenu(question_window, answer, *options)
    option_menu.config(highlightthickness=0, bg='white', fg='black', font=button_font)
    option_menu.pack(padx=10, pady=10)  # Adjust padding as needed
    
    # Style the next button to match the opening page
    next_button = tk.Button(question_window, text="Next", command=lambda: handle_answer(question_window, answer, next_function))
    next_button.config(highlightthickness=0, font=button_font, bg='white', fg='green')
    next_button.pack(padx=10, pady=20)  # Adjust padding as needed

def handle_answer(window, answer, next_function):
    responses.append(answer.get())
    window.destroy()
    next_function()

def show_recommendations():
    show_question(questions[0], age_options, 
                  lambda: show_question(questions[1], skin_type_options, 
                                        lambda: show_question(questions[2], skin_concern_options, 
                                                              lambda: show_question(questions[3], product_type_options, display_recommendations))))

def display_recommendations():
    lowercase = [x.lower() for x in responses]
    random_one, random_two, all_three = recommend_products(lowercase)

    top = tk.Toplevel(root, bg='white')
    top.title("Your Recommendations")

    # Function to display products
    def display_products(products, title):
        section_title = tk.Label(top, text=title, fg="black", bg='white', font=subtitle_font)
        section_title.pack()

        for product_type, brand in products:
            product_info = f"{product_type} - {brand}"  # Adjust based on your data structure
            label = tk.Label(top, text=product_info, fg="black", cursor="hand2", bg='white')
            label.pack()

    # Display each set of products
    if random_one:
        display_products(random_one, "Category 1 Recommendations")
    if random_two:
        display_products(random_two, "Category 2 Recommendations")
    if all_three:
        display_products(all_three, "Category 3 Recommendations")
        
root = tk.Tk()
root.title("DermaDive Skin Quiz")

# Set the window size and position
window_width = 1000
window_height = 700
root.geometry(f"{window_width}x{window_height}")

# Set a background color
root.configure(bg='white')

# Customize fonts
title_font = tkFont.Font(family="Quicksand", size=30, weight="bold")
subtitle_font = tkFont.Font(family="Quicksand", size=25)
description_font = tkFont.Font(family="Quicksand", size=20, weight = "bold")
description_font_2 = tkFont.Font(family = "Quicksand", size = 17)
button_font = tkFont.Font(family="Quicksand", size=15)

# Create a frame to center the content vertically
center_frame = tk.Frame(root, bg='white')
center_frame.pack(expand=True)

# Title
title_label = tk.Label(center_frame, text="DermaDive", font=title_font, bg='white', fg='black')
title_label.pack()  # The title is centered horizontally by default

# Subtitle
subtitle_label = tk.Label(center_frame, text="Skin Quiz", font=subtitle_font, bg='white', fg='black')
subtitle_label.pack()  # The subtitle is centered horizontally by default

# Description - use wraplength to fit the text in the window
description_label = tk.Label(center_frame, text="Welcome to DermaDive!",
                             font=description_font, bg='white', fg='black', justify='center', wraplength=window_width - 100)  # Adjust wraplength as needed
description_label.pack(pady=(20, 20))

description_label_2 = tk.Label(center_frame, text="Dermadive's Skin Quiz is your gateway to bespoke skincare, offering tailored solutions that dive deep into your skin's unique needs for a glowing, healthy complexion.\n \n At the end you will receive up to 3 categories. Category 1 are products with just one of your preferences, Category 2 are products with two of your preferences, and Category 3 are products with all three of your preferences (which may or may not exist).",
                             font=description_font_2, bg='white', fg='black', justify='center', wraplength=window_width - 100)
description_label_2.pack()
# Start button
start_button = tk.Button(center_frame, text="Take the Quiz", command=show_recommendations, font=button_font, bg='white', fg='green', bd=0, highlightthickness=0)
start_button.pack(pady=(10, 20))

questions = [
    "What is your age?",
    "What is your primary skin type?",
    "What is your primary skin concern?",
    "What type of product are you looking for?",
]

age_options = ["Select an option","18-25", "26-35", "36-45", "46-55", "55+"]
skin_type_options = ["Select an option", "Normal", "Oily", "Dry", "Combination of 2 or more"]
skin_concern_options = ["Select an option", "Acne", "Wrinkles", "Dryness", "Dullness"]
product_type_options = ["Select an option", "Toner", "Moisturizer", "Suncreen", "Cleanser", "Exfoliant"]

responses = []

root.mainloop()