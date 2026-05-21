import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()



def add_user():
    try:
        user_id = int(input("Enter user id: "))
        name = input("Enter name: ")

        cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, name))
        conn.commit()

        print("User added!\n")

    except:
        print("Invalid input! Try again.\n")


def show_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print("\n=== USERS ===")

    if not users:
        print("No users found.\n")
        return

    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}")
    print()


def add_order():
    try:
        order_id = int(input("Enter order id: "))
        user_id = int(input("Enter user id: "))
        total = int(input("Enter total: "))
        status = input("Enter status: ")

        cursor.execute(
            "INSERT INTO orders VALUES (?, ?, ?, ?)",
            (order_id, user_id, total, status)
        )
        conn.commit()

        print("Order added!\n")

    except:
        print("Invalid input! Try again.\n")



def show_orders():
    cursor.execute("""
    SELECT users.name, orders.total, orders.status
    FROM users
    LEFT JOIN orders ON users.id = orders.user_id
    """)

    orders = cursor.fetchall()

    print("\n=== ORDERS ===")

    if not orders:
        print("No orders found.\n")
        return

    for order in orders:
        print(f"User: {order[0]}, Total: {order[1]}, Status: {order[2]}")
    print()


def total_spent():
    cursor.execute("""
    SELECT users.name, SUM(orders.total)
    FROM users
    LEFT JOIN orders ON users.id = orders.user_id
    GROUP BY users.name
    """)

    results = cursor.fetchall()

    print("\n=== TOTAL SPENT ===")

    for row in results:
        total = row[1] if row[1] else 0
        print(f"{row[0]}: {total}")
    print()


def order_count():
    cursor.execute("""
    SELECT users.name, COUNT(orders.id)
    FROM users
    LEFT JOIN orders ON users.id = orders.user_id
    GROUP BY users.name
    """)

    results = cursor.fetchall()

    print("\n=== ORDER COUNT ===")

    for row in results:
        print(f"{row[0]}: {row[1]} orders")
    print()


def main():
    while True:
        print("=== ONLINE SHOP MENU ===")
        print("1. Add User")
        print("2. Add Order")
        print("3. Show Users")
        print("4. Show Orders")
        print("5. Total Spent")
        print("6. Order Count")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_order()
        elif choice == "3":
            show_users()
        elif choice == "4":
            show_orders()
        elif choice == "5":
            total_spent()
        elif choice == "6":
            order_count()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")


main()
conn.close()