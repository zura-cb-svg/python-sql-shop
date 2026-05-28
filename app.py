from flask import Flask, render_template, request, redirect, url_for
from main import (
    add_user_db,
    add_order_db,
    show_users,
    show_orders,
    delete_user_db,
    delete_order_db,
    update_user_db,
    search_orders_db
)

app = Flask(__name__)


# 🟢 HOME
@app.route("/")
def home():
    return render_template("index.html")


# 🟢 ADD USER
@app.route("/add_user", methods=["POST"])
def add_user():
    user_id = request.form.get("id")
    name = request.form.get("name")

    add_user_db(user_id, name)

    return redirect(url_for("home"))


# 🟢 ADD ORDER
@app.route("/add_orders", methods=["POST"])
def add_orders():
    order_id = request.form.get("order_id")
    user_id = request.form.get("user_id")
    total = request.form.get("total")
    status = request.form.get("status")

    add_order_db(order_id, user_id, total, status)

    return redirect(url_for("home"))


# 🟢 SHOW USERS
@app.route("/show_users")
def show_user():
    users = show_users()
    return render_template("users.html", users=users)


# 🟢 SHOW ORDERS
@app.route("/show_orders")
def show_order():
    orders = show_orders()
    return render_template("orders.html", orders=orders)


# 🟢 DELETE USER
@app.route("/delete_user", methods=["POST"])
def delete_user():
    user_id = request.form.get("id")

    delete_user_db(user_id)

    return redirect(url_for("show_user"))


# 🟢 DELETE ORDER
@app.route("/delete_order", methods=["POST"])
def delete_order():
    order_id = request.form.get("id")

    delete_order_db(order_id)

    return redirect(url_for("show_order"))


# 🟢 UPDATE USER
@app.route("/update_user", methods=["POST"])
def update_user():
    user_id = request.form.get("id")
    new_name = request.form.get("name")

    update_user_db(user_id, new_name)

    return redirect(url_for("show_user"))


# 🟢 SEARCH ORDERS
@app.route("/search_orders")
def search_orders():
    status = request.args.get("status")

    orders = search_orders_db(status)

    return render_template("orders.html", orders=orders)


# 🟢 RUN
app.run(debug=True)