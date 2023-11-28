import tkinter as tk
from tkinter import simpledialog
from tkinter import font as tkFont
import webbrowser


def open_link(url):
    webbrowser.open_new(url)

def recommend_products(responses):
    # Example logic to recommend products
    return [("Product 1", "http://example.com/product1"),
            ("Product 2", "http://example.com/product2"),
            ("Product 3", "http://example.com/product3"),
            ("Product 4", "http://example.com/product4"),
            ("Product 5", "http://example.com/product5")]

def show_question(question, options, next_function):
    question_window = tk.Toplevel(root, bg='black')
    question_window.title("Question")
    
    # Centering the question label horizontally and vertically
    question_label = tk.Label(question_window, text=question, bg='black', fg='white', justify='center')
    question_label.pack(padx=10, pady=(400, 0))  # Add horizontal and vertical padding

    answer = tk.StringVar(question_window)
    answer.set(options[0])  # default value

    option_menu = tk.OptionMenu(question_window, answer, *options)
    option_menu.config(highlightthickness=0, bg='white', fg='black')
    option_menu.pack(padx=400, pady=5)  # Add padding for better layout
    
    next_button = tk.Button(question_window, text="Next", command=lambda: handle_answer(question_window, answer, next_function))
    next_button.config(highlightthickness=0)
    next_button.pack(padx=400, pady=5)


def handle_answer(window, answer, next_function):
    responses.append(answer.get())
    window.destroy()
    next_function()

def show_recommendations():
    show_question(questions[0], age_options, lambda: show_question(questions[1], skin_type_options, lambda: show_question(questions[2], skin_concern_options, display_recommendations)))


def display_recommendations():
    recommended_products = recommend_products(responses)

    top = tk.Toplevel(root, bg='black')
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
    "What is your primary skin concern?"
]

age_options = ["18-25", "26-35", "36-45", "46-55", "55+"]  # Example age ranges
skin_type_options = ["Normal", "Oily", "Dry", "Combination of 2 or more"]
skin_concern_options = ["Acne", "Wrinkles", "Dryness", "Sensitivity"]

responses = []

root.mainloop()
