import requests
from bs4 import BeautifulSoup
import json

books = []
with open("library.json", "w") as f:
    json.dump(books, f, indent=4)
url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    
    # Rating is stored in class name (e.g. "star-rating Three")
    rating_class = book.find('p')['class']
    rating = rating_class[1]

    books.append({
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating
    })
# Menu
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
            break
        else:
            print("Invalid choice")
def view_books():
    for b in books:
        print(f"{b['title']} | {b['price']} | {b['rating']}")
def search_book():
    query = input("Enter title keyword: ").lower()
    results = [b for b in books if query in b['title'].lower()]

    for b in results:
        print(f"{b['title']} | {b['price']} | {b['rating']}")

    if not results:
        print("No books found.")
def filter_rating():
    rating = input("Enter rating (One, Two, Three, Four, Five): ")

    results = [b for b in books if b['rating'] == rating]

    for b in results:
        print(f"{b['title']} | {b['price']}")

    if not results:
        print("No books found.")
# Test output
for b in books:
    print(b)
if __name__ == "__main__":
    menu()