import matplotlib.pyplot as plt


def display(books):
    if not books:
        print("\nСписок книг порожній.")
        return
    table = [[i + 1, book['Назва книги'], book['Автор'], book['Рік видання'], book['Жанр'], book['Кількість примірників']] for i, book in enumerate(books)]
    headers = ["#", "Назва книги", "Автор", "Рік видання", "Жанр", "Кількість примірників"]
    print("\nСписок книг:")
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print()

def add(books):
    print("\nДодавання нової книги:")
    title = input("Назва книги: ")
    author = input("Автор: ")
    year = int(input("Рік видання: "))
    genre = input("Жанр: ")
    copies = int(input("Кількість примірників: "))
    books.append({
        "Назва книги": title,
        "Автор": author,
        "Рік видання": year,
        "Жанр": genre,
        "Кількість примірників": copies,
    })
    print("Книга успішно додана!")

def edit(books):
    title = input("\nВведіть назву книги, яку хочете редагувати: ")
    for book in books:
        if book["Назва книги"].lower() == title.lower():
            print("\nРедагування книги:")
            book["Назва книги"] = input(f"Нова назва книги ({book['Назва книги']}): ") or book["Назва книги"]
            book["Автор"] = input(f"Новий автор ({book['Автор']}): ") or book["Автор"]
            book["Рік видання"] = int(input(f"Новий рік видання ({book['Рік видання']}): ") or book["Рік видання"])
            book["Жанр"] = input(f"Новий жанр ({book['Жанр']}): ") or book["Жанр"]
            book["Кількість примірників"] = int(input(f"Нова кількість примірників ({book['Кількість примірників']}): ") or book["Кількість примірників"])
            print("Інформація про книгу успішно оновлена!")
            return
    print("Книгу не знайдено.")

def delete(books):
    title = input("\nВведіть назву книги, яку хочете видалити: ")
    for book in books:
        if book["Назва книги"].lower() == title.lower():
            books.remove(book)
            print("Книга успішно видалена!")
            return
    print("Книгу не знайдено")
def save(filename, books):
    with open(filename, mode='w', encoding='utf-8') as file:
        for book in books:
            file.write(f"{book['Назва книги']}|{book['Автор']}|{book['Рік видання']}|{book['Жанр']}|{book['Кількість примірників']}\n")
    print(f"Дані збережено у файл {filename}.")

def load(filename):
    books = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                title, author, year, genre, copies = line.strip().split('|')
                books.append({
                    "Назва книги": title,
                    "Автор": author,
                    "Рік видання": int(year),
                    "Жанр": genre,
                    "Кількість примірників": int(copies),
                })
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Починаємо з порожнього списку.")
    return books

def total_books(books):
    total = sum(book["Кількість примірників"] for book in books)
    print(f"\nЗагальна кількість книг у бібліотеці: {total}")

def popular_genres(books):
    genres = {}
    for book in books:
        genres[book["Жанр"]] = genres.get(book["Жанр"], 0) + book["Кількість примірників"]
    sorted_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)
    print("\nНайпопулярніші жанри:")
    for genre, count in sorted_genres:
        print(f"{genre}: {count} примірників")

def search_books(books):
    print("\nПошук книг:")
    print("1. Пошук за автором")
    print("2. Пошук за роком видання")
    choice = input("Ваш вибір: ")
    if choice == "1":
        author = input("Введіть ім'я автора: ")
        found = [book for book in books if author.lower() in book["Автор"].lower()]
    elif choice == "2":
        year = int(input("Введіть рік видання: "))
        found = [book for book in books if book["Рік видання"] == year]
    else:
        print("Невірний вибір.")
        return
    if found:
        display(found)
    else:
        print("Книги не знайдено.")

def plot_genres(books):
    genres = {}
    for book in books:
        genres[book["Жанр"]] = genres.get(book["Жанр"], 0) + book["Кількість примірників"]
    
    if not genres:
        print("Немає даних для побудови кругової діаграми.")
        return
    
    plt.figure(figsize=(8, 8))
    plt.pie(genres.values(), labels=genres.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Розподіл книг за жанрами")
    plt.show()
def plot_years(books):
    years = {}
    for book in books:
        years[book["Рік видання"]] = years.get(book["Рік видання"], 0) + book["Кількість примірників"]

    if not years:
        print("Немає даних для побудови гістограми.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(years.keys(), years.values(), color='skyblue', edgecolor='black')
    plt.xlabel("Роки видання")
    plt.ylabel("Кількість книг")
    plt.title("Кількість книг за роками видання")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    filename = "books.txt"
    books = load(filename)

    while True:
        print("\nМеню:")
        print("1. Показати список книг")
        print("2. Додати книгу")
        print("3. Редагувати книгу")
        print("4. Видалити книгу")
        print("5. Порахувати загальну кількість книг")
        print("6. Показати найпопулярніші жанри")
        print("7. Пошук книг")
        print("8. Побудувати кругову діаграму розподілу жанрів")
        print("9. Побудувати гістограму кількості книг за роками видання")
        print("10. Зберегти і вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            display(books)
        elif choice == "2":
            add(books)
        elif choice == "3":
            edit(books)
        elif choice == "4":
            delete(books)
        elif choice == "5":
            total_books(books)
        elif choice == "6":
            popular_genres(books)
        elif choice == "7":
            search_books(books)
        elif choice == "8":
            plot_genres(books)
        elif choice == "9":
            plot_years(books)
        elif choice == "10":
            save(filename, books)
            print("Дані збережено. Вихід.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
