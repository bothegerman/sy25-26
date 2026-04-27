import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://books.toscrape.com/"

books = []

rating_map = {
    "One": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5"
}

# Conversion rate (update if needed)
GBP_TO_USD = 1.25

# Request page
response = requests.get(url)
response.encoding = 'utf-8'  # ✅ Fix encoding issue
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape books
for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    
    # Get raw price text
    price_text = book.find('p', class_='price_color').text
    
    # ✅ Clean price (removes £, Â, etc.)
    price_gbp = float(re.sub(r"[^\d.]", "", price_text))
    
    # Convert to USD
    price_usd = round(price_gbp * GBP_TO_USD, 2)

    availability = book.find('p', class_='instock availability').text.strip()
    
    rating_class = book.find('p')['class']
    rating_word = rating_class[1]
    rating = rating_map[rating_word]

    books.append({
        "title": title,
        "price_usd": f"${price_usd}",
        "availability": availability,
        "rating": rating
    })

# Save to JSON
with open("library.json", "w") as f:
    json.dump(books, f, indent=4)


# ---------------- MENU FUNCTIONS ---------------- #

def view_books():
    for b in books:
        print(f"{b['title']} | {b['price_usd']} | Rating: {b['rating']}")


def search_book():
    query = input("Enter title keyword: ").lower()
    results = [b for b in books if query in b['title'].lower()]

    if results:
        for b in results:
            print(f"{b['title']} | {b['price_usd']} | Rating: {b['rating']}")
    else:
        print("No books found.")


def filter_rating():
    rating = input("Enter rating (1-5): ").strip()

    if rating not in ["1", "2", "3", "4", "5"]:
        print("Invalid rating.")
        return

    results = [b for b in books if b['rating'] == rating]

    if results:
        for b in results:
            print(f"{b['title']} | {b['price_usd']}")
    else:
        print("No books found.")


def menu():
    while True:
        print("\n=== BOOK LIBRARY ===")
        print("1. View all books")
        print("2. Search book by title")
        print("3. Filter by rating")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            filter_rating()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


# Run program
if __name__ == "__main__":
    menu()