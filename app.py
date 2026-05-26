from flask import Flask, request, render_template, redirect, url_for
from main import show_users, show_orders, add_user_db, add_order_db, delete_user_db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/users")
def users():
    return render_template("users.html", users=show_users())


@app.route("/orders")
def orders():
    return render_template("orders.html", orders=show_orders())


@app.route("/add_user", methods=["POST"])
def add_user():
    user_id = request.form.get("id")
    name = request.form.get("name")

    if not user_id or not name:
        return "Fill all fields!"

    add_user_db(user_id, name)
    return redirect(url_for("users"))


@app.route("/add_order", methods=["POST"])
def add_order():
    order_id = request.form.get("order_id")
    user_id = request.form.get("user_id")
    total = request.form.get("total")
    status = request.form.get("status")

    if not order_id or not user_id or not total or not status:
        return "Fill all fields!"

    add_order_db(order_id, user_id, total, status)
    return redirect(url_for("orders"))


@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    delete_user_db(user_id)
    return redirect(url_for("users"))


app.run(debug=True)