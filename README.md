# Dermadive Capstone Project for MAD2502


## Goal

The primary goal of the project is to develop a skincare recommendation system, offering personalized product suggestions based on individual preferences and needs. The system aims to streamline the decision-making process for users by providing relevant recommendations from a database, for the user to make informed decisions.



## Motivation

The motivation behind this project comes from the observance of the overwhelming market of skincare products. With this masy options, consumers have difficulty selecting products that align with their preferences. The existing skincare industry lacks a personalized and unbiased approach. By creating this program, we aim to empower users to make informed choices, ultimately contributing to a more positive skincare experience, with less wastage. 

## Details

### Methods

#### Imports
- import tkinter as tk
- from tkinter import simpledialog
- from tkinter import font as tkFont
- import webbrowser
- import pandas as pd
- import sqlite3
- import random
#### Database Creation
- Database has 200 products, each cataloged with 18 detailed attributes.

#### User Input
- Users input  their age, primary skin type, skin concerns, and the type of skincare product they are seeking.

#### Recommendation Logic
-  Function takes the data and returns the key and a list of each attribute of the data as the definition.
  
#### Application of Mathematical Concepts
-  Algorithm  calculates how many matches each product has with the user input by adding up each instance with the count variable and sorting it into lists based on that count variable
- Calculating and displaying the price per ounce of each product that’s selected.
  
### Inputs and outputs

- Input: User's age, primary skin type, and primary skin concern and the type of product they wanted a recommendation for.
- Output: Top 3 recommendations, according to category of how many requirements are matched, and a graphs for comparison.


### Results

The  project has designed a program to offer personalized skincare recommendations to users based on their individual preferences, fulfilling its intended purpose. The program efficiently categorizes suggestions into three distinct groups, accommodating various combinations of user preferences. The program also calculates and displays the price per ounce of each product that’s selected to  display these results in a bar graph. This bar graph then appears in the final pop-up window of the quiz, so users can immediately compare skin products as they assess their options. 




## Running instructions
### Dependencies

- Jupyter Notebook. [Installation Guide](https://jupyter.org/install).

### Associated files
- Download data.xslx, and save with the same title

### Instructions
- Open Jupyter Notebook.
- Upload the capstone.ipynb file.
- Upload the data.xslx file.
- Click `shift` and `enter` to run.




### Repository structure

```txt
├── README.md
├── data
├── capstone
└── gen
    ├── video
    └── paper
```

## More Resources

Reed, Alia. "My Skincare Spreadsheet." The Acid Queen, 2015, https://theacidqueenblog.com/my-skincare-spreadsheet/


Cernansky, Rachel. "Beauty has a waste problem, and it’s not packaging." Vogue Business, 2021, https://www.voguebusiness.com/sustainability/beauty-has-a-waste-problem-and-its-not-packaging 


## About

Each group member contribued:  Megan Enochs led database creation, Meghana Gontu lead developed the code , Eleanor Riggs was the database specialist, and Zan Valere edited gen files.
