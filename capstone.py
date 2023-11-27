import tkinter as tk
from tkinter import simpledialog
import webbrowser

def open_link(url):
    webbrowser.open_new(url)

def recommend_products(responses):
    # Example logic to recommend products based on responses
    # In a real application, this should be more sophisticated
    return [("Product 1", "http://example.com/product1"),
            ("Product 2", "http://example.com/product2"),
            ("Product 3", "http://example.com/product3"),
            ("Product 4", "http://example.com/product4"),
            ("Product 5", "http://example.com/product5")]

def get_responses():
    questions = [
        "What is your age?",
        "What is your primary skin type? (Normal, Oily, Dry, Combination)",
        "What is your primary skin concern? (Acne, Wrinkles, Dryness, Sensitivity)",
        # Add more questions as needed
    ]
    responses = [simpledialog.askstring("Input", question, parent=root) for question in questions]
    return responses

def show_recommendations():
    responses = get_responses()
    recommended_products = recommend_products(responses)

    top = tk.Toplevel(root)
    top.title("Your Recommendations")
    for product_name, product_url in recommended_products:
        link = tk.Label(top, text=product_name, fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e, url=product_url: open_link(url))

root = tk.Tk()
root.title("Dermadive: Your Facial Skin Health Analyzer")

welcome_label = tk.Label(root, text="Welcome to Dermadive: Your Facial Skin Health Analyzer")
welcome_label.pack()

start_button = tk.Button(root, text="Click here to get started on your journey", command=show_recommendations)
start_button.pack()

root.mainloop()