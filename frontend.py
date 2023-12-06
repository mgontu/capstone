import tkinter as tk
from tkinter import simpledialog
from tkinter import font as tkFont
import webbrowser
import pandas as pd


def open_link(url):
    webbrowser.open_new(url)

def recommend_products(responses):
    # # Example logic to recommend products
    # return [("Product 1", "http://example.com/product1"),
    #         ("Product 2", "http://example.com/product2"),
    #         ("Product 3", "http://example.com/product3"),
    #         ("Product 4", "http://example.com/product4"),
    #         ("Product 5", "http://example.com/product5")]

    data_path = 'data.xlsx'
    df = pd.read_excel(data_path)

    skin_type, skin_concern, product_type = responses[1], responses[2], responses[3]  # Assuming these are the order of questions

    # Filter the DataFrame based on responses
    filtered_df = df[(df['suitable skin types'] == skin_type) & (df['skin concerns'] == skin_concern) & (df['product_type'] == product_type)]
    
    # Randomly pick 3 products, or all products if there are less than 3
    recommended = filtered_df.sample(n=3) if len(filtered_df) > 3 else filtered_df

    # Extract product names and URLs
    recommendations = [(row['product_name'], row['Link']) for index, row in recommended.iterrows()]

    return recommendations

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
    recommended_products = recommend_products(responses)

    top = tk.Toplevel(root, bg='white')
    top.title("Your Recommendations")
    for product_name, product_url in recommended_products:
        link = tk.Label(top, text=product_name, fg="blue", cursor="hand2", bg='black')
        link.pack()
        link.bind("<Button-1>", lambda e, url=product_url: open_link(url))
        
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

description_label_2 = tk.Label(center_frame, text="Dermadive's Skin Quiz is your gateway to bespoke skincare, offering tailored solutions that dive deep into your skin's unique needs for a glowing, healthy complexion.",
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
