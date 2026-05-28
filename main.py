import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()


# 🟢 ADD USER
def add_user_db(user_id, name):
    cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, name))
    conn.commit()


# 🟢 ADD ORDER
def add_order_db(order_id, user_id, total, status):
    cursor.execute(
        "INSERT INTO orders VALUES (?, ?, ?, ?)",
        (order_id, user_id, total, status)
    )
    conn.commit()


# 🟢 SHOW USERS
def show_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# 🟢 SHOW ORDERS
def show_orders():
    cursor.execute("SELECT id, user_id, total, status FROM orders")
    return cursor.fetchall()


# 🟢 DELETE USER
def delete_user_db(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()


# 🟢 DELETE ORDER
def delete_order_db(order_id):
    cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
    conn.commit()


# 🟢 UPDATE USER
def update_user_db(user_id, new_name):
    cursor.execute(
        "UPDATE users SET name = ? WHERE id = ?",
        (new_name, user_id)
    )
    conn.commit()


# 🟢 SEARCH ORDERS
def search_orders_db(status):
    cursor.execute(
        "SELECT id, user_id, total, status FROM orders WHERE status = ?",
        (status,)
    )
    return cursor.fetchall()