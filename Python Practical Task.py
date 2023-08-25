# 1. Write a Python program to calculate the factorial of a given name..

# num = int(input("Enter the number: "))
# factorial = 1

# if (num<0 or num==1):
#     print("1")
# else:
#     for i in range(1, num+1):
#         factorial = factorial * i

# print("The factorial is: ", factorial)

# 2. Create a function that takes a list of integers and returns the sum of all even numbers in the list..

list = [1,2,3,4,5,6,7,8]

def Even(numbers):
    return [num for num in numbers if not num % 2]

# 3. Write a Python program to check if a string is a palindrome..

def Palindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]



# 4. Implement a Python function that finds and prints all prime numbers between 1 and a given number..

def Prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True       
    
def Find_Prime(l):
    p = [2,3]
    for num in range(5, l + 1, 6):
        if Prime(num):
            p.append(num)
        if Prime(num + 2) and num + 2 <= l:
            p.append(num + 2)
        return p
    
# up = int(input("Enter a number: "))
# pl = Find_Prime(up)
# print("Prime numbers between 1 and", up, "are:", pl)

# 5. Create a simple test-based calculator that can perform addition, subtraction, multiplication, and division..

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero" 

# print("Select operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     print(num1, "+", num2, "=", add(num1, num2))
# elif choice == '2':
#     print(num1, "-", num2, "=", subtract(num1, num2))
# elif choice == '3':
#     print(num1, "*", num2, "=", multiply(num1, num2))
# elif choice == '4':
#     print(num1, "/", num2, "=", divide(num1, num2))
# else:
#     print("invalid input")

# 6. Write a program that takes a list of words as input and returns a new list containing only the words longer than a specified length..

def filter_long_words(word_list, length):
    return [word for word in word_list if len(word) > length]

# word_list = input("Enter a list of words separated by spaces: ").split()
# length = int(input("Enter the minimum word length: "))

# long_words = filter_long_words(word_list, length)
# print("Words longer than", length, "characters:", long_words)

# 7. Implement a function that generates a random password of a specified length containing letters, digits and special characters..

import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# password_length = int(input("Enter the desired password length: "))

# random_password = generate_random_password(password_length)
# print("Generated random password: ", random_password)  

# 8. Create a Python script to read data from a CSV file and calculate the average, maximum, and minimum of a specific column..

import csv

def analyze_csv_column(filename, column_name):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        column_values = [float(row[column_name]) for row in reader]
    
    if not column_values:
        return None, None, None
    
    average = sum(column_values) / len(column_values)
    maximum = max(column_values)
    minimum = min(column_values)

    return average, maximum, minimum

# csv_filename = input("Enter the CSV file name: ")
# target_column = input("Enter the column name for analysis: ")

# avg, max_val, min_val = analyze_csv_column(csv_filename, target_column)
# if avg is None:
#     print("Column not found")
# else:
#     print(f"Average of '{target_column}': {avg:.2f}")
#     print(f"Maximum of '{target_column}': {max_val:.2f}")
#     print(f"Minimun of '{target_column}': {min_val:.2f}")

# 9. Build a program that simulates a basic quiz with multiple-choice questions and calculates the final score..

class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.text)
        for i, choice in enumerate(question.choices, start=1):
            print(f"{i}. {choice}")
        user_choice = int(input("Enter your choice (1, 2, 3, ...): ")) - 1
        if user_choice == question.correct_choice:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question.correct_choice + 1}.\n")
    return score

# question1 = Question("What is the Capital France?", ["Paris", "London", "Berlin"], 0)
# question2 = Question("Which planet is known as the 'Red Planet'?", ["Venus", "Mars", "Jupiter"], 1)
# question3 = Question("What is 4 * 7?", ["21", "28", "35"], 1)

# questions = [question1, question2, question3]

# print("Welcome to the Quiz!\n")
# total_score = run_quiz(questions)
# print(f"Your final score: {total_score}/{len(questions)}")

# 10. Write a Python script to download all images from a specific URL and save them to a local folder..

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve

def download_images(url, folder_path):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the URL: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_url = urljoin(url, img_tag['src'])
        img_name = os.path.basename(img_url)
        img_path = os.path.join(folder_path, img_name)

        try:
            urlretrieve(img_url, img_path)
            print(f"Downloaded: {img_name}")
        except Exception as e:
            print(f"Failed to download {img_name}: {e}")

# target_url = 'https://marvel.com'
# save_folder = 'Python'

# if not os.path.exists(save_folder):
#     os.makedirs(save_folder)

# download_images(target_url, save_folder)

# 11. Write a Python script to count the frequency of words in a given text file and display the top N most frequent words..

import re
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\w+', text.lower())
    word_count = Counter(words)
    return word_count

def display_top_words(word_count, top_n):
    top_words = word_count.most_common(top_n)
    print(f"Top {top_n} most frequent words: ")
    for word, frequency in top_words:
        print(f"{word}: {frequency}")

# file_path = 'sample.txt'
# top_n = 10

# word_count = count_words(file_path)
# display_top_words(word_count, top_n)

# 12. Implement a function that takes a list of numbers as input and finds the second-largest and second-smallest numbers in the list..

def find_second_largest_smallest(numbers):
    if len(numbers) < 2:
        return None, None
    
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[1]
    second_largest = sorted_numbers[-2]

    return second_smallest, second_largest

# number_list = [10, 5, 8, 3, 15, 2, 12]
# second_smallest, second_largest =  find_second_largest_smallest(number_list)

# if second_smallest is not None and second_largest is not None:
#     print(f"Second Smallest: {second_smallest}")
#     print(f"Second Largest: {second_largest}")
# else:
#     print("List should contain at least two numbers.")

# 13. Create a program that generates a random list of integers and then sorts it in ascending order using the Bubble Sort algorithm..

import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# list_length = 10
# random_list = [random.randint(1, 100) for _ in range(list_length)]

# print("Original List:", random_list)

# bubble_sort(random_list)

# print("Sorted List: ", random_list)

# 14. Write a Python function to find and print all prime factors of a given number..

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

# number = int(input("Enter a number: "))
# factors = prime_factors(number)

# print("Prime factors of", number, "are:", factors)

# 15. Build a simple web scraper using Python's BeautifulSoup library to extract data from a website and save it to a CSV file..

import requests
from bs4 import BeautifulSoup
import csv

# url = 'http://quotes.toscrape.com'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')

# quote_blocks = soup.find_all('div', class_='quote')

# csv_filename = 'quotes.csv'
# with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(['Quote', 'Author'])

#     for block in quote_blocks:
#         quote_text = block.find('span', class_= 'text').get_text()
#         author = block.find('small', class_='author').get_text()
#         csv_writer.writerow([quote_text, author])

# print(f"Data scraper and saved to {csv_filename}")

# 16. implement a basic Tic-Tac-Toe game where two players can take turns to play until there is a winner or a draw..

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)) or all(board [i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

#     while True:
#         print_board(board)
#         row  = int(input(f"Player {current_player}, enter row(0-2): "))
#         col = int(input(f"Player {current_player}, enter column (0-2): "))
        
#         if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
#             board[row][col] = current_player

#             if check_winner(board, current_player):
#                 print_board(board)
#                 print(f"Player {current_player} wins!")
#                 break
#             elif is_full(board):
#                 print_board(board)
#                 print("It's a draw!")
#                 break
            
#             current_player = "0" if current_player == "X" else "x"
#         else: 
#             print("Invalid move. Try again.")

# if __name__ == "__main__":
#     play_game()

# 17. Create a program that converts temperatures between Celsius and Fahrenheit based on user input..

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")
    else: 
        print("Invalid choice")

# if __name__ == "__main__":
#     main()

# 18. Write a Python function that checks if a given string is an anagram of another string..

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# if is_anagram(string1, string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

# 19. Implement a program that stimulates a dice rolling game, allow the user to roll the dice until they choose to stop..

import random 

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")

    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# if __name__ == "__main__":
#     main()

# 20. Build a script that reads a JSON file containing a list of products and their prices, then calculates the total price of a shopping cart..
   
import json

def calculate_total(cart, products):
    total = 0
    for item in cart:
        if item['product_id'] in products:
            price = products[item['product_id']]
            total += price * item['quantity']
    return total
        
def main():
    with open('products.json', 'r') as file:
        products_data = json.load(file)

    products = {}
    for product in products_data:
        products[product['id']] = product['price']

    cart = []
    while True:
        product_id = input("Enter product ID (or 'done' to finish): ")
        if product_id == 'done':
            break

        try:
            quantity = int(input("Enter quantity: "))
            cart.append({'product_id': product_id, 'quantity': quantity})
        except ValueError:
            print("Invalid input. Quantity should be an integer.")
    
    total_price = calculate_total(cart, products)
    print(f"Total price of the shopping cart: ${total_price:.2f}")

# if __name__ == "__main__":
#     main()













































































