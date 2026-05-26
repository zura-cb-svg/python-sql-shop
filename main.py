import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()


def show_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


def show_orders():
    cursor.execute("""
    SELECT users.name, orders.total, orders.status
    FROM users
    LEFT JOIN orders ON users.id = orders.user_id
    """)
    return cursor.fetchall()


def add_user_db(user_id, name):
    cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, name))
    conn.commit()


def add_order_db(order_id, user_id, total, status):
    cursor.execute(
        "INSERT INTO orders VALUES (?, ?, ?, ?)",
        (order_id, user_id, total, status)
    )
    conn.commit()


def delete_user_db(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()