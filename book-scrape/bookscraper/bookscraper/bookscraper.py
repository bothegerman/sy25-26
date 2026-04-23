import requests
from bs4 import BeautifulSoup
import json

url = "https://books.toscrape.com/"

# Store books here
books = []

# Rating conversion
rating_map = {
    "One": "1",
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5"
}

# Scrape data
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    
    rating_class = book.find('p')['class']
    rating_word = rating_class[1]
    rating = rating_map[rating_word]

    books.append({
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating
    })

# Save to JSON AFTER scraping
with open("library.json", "w") as f:
    json.dump(books, f, indent=4)


# ---------------- MENU FUNCTIONS ---------------- #

def view_books():
    for b in books:
        print(f"{b['title']} | {b['price']} | Rating: {b['rating']}")


def search_book():
    query = input("Enter title keyword: ").lower()
    results = [b for b in books if query in b['title'].lower()]

    if results:
        for b in results:
            print(f"{b['title']} | {b['price']} | Rating: {b['rating']}")
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
            print(f"{b['title']} | {b['price']}")
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