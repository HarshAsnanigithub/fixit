

# # ----------------------------------------------------------------

# from flask import Flask, render_template, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # MySQL connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Haru@sql2023",
#     database="fixit"
# )


# def get_cursor():
#     global db
#     try:
#         db.ping(reconnect=True, attempts=3, delay=2)
#     except mysql.connector.Error:
#         db = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Haru@sql2023",
#             database="fixit"
#         )
#     return db.cursor(buffered=True)


# @app.route('/resume')
# def resume():
#     return render_template('portfolio.html')



# # Homepage
# @app.route("/")
# def home():
#     return render_template("index.html")


# # Service Man main page (Register / Login options)
# @app.route("/serviceman")
# def serviceman():
#     return render_template("serviceman.html")


# # Service Man Register
# @app.route("/serviceman_register", methods=["GET", "POST"])
# def serviceman_register():

#     if request.method == "POST":

#         name = request.form["name"]
#         contact = request.form["contact"]
#         service_type = request.form["service_type"]
#         password = request.form["password"]

#         query = "INSERT INTO serviceman (name,contact,service_type,password) VALUES (%s,%s,%s,%s)"
#         values = (name, contact, service_type, password)

#         cursor = get_cursor()
#         cursor.execute(query, values)
#         db.commit()
#         cursor.close()

#         return render_template("register_success.html")

#     return render_template("serviceman_register.html")


# # SERVICE MAN LOGIN
# @app.route("/serviceman_login", methods=["GET", "POST"])
# def serviceman_login():

#     if request.method == "POST":

#         contact = request.form["contact"]
#         password = request.form["password"]

#         query = "SELECT * FROM serviceman WHERE contact=%s AND password=%s"
#         values = (contact, password)

#         cursor = get_cursor()
#         cursor.execute(query, values)
#         user = cursor.fetchone()
#         cursor.close()

#         if user:
#             return redirect("/serviceman_dashboard")
#         else:
#             return render_template("serviceman_login.html", error="Invalid Mobile Number or Password")

#     return render_template("serviceman_login.html")


# # SERVICEMAN DASHBOARD
# @app.route("/serviceman_dashboard")
# def serviceman_dashboard():

#     cursor = get_cursor()
#     query = "SELECT * FROM service_requests"
#     cursor.execute(query)
#     requests = cursor.fetchall()
#     cursor.close()

#     return render_template("serviceman_dashboard.html", requests=requests)


# # CUSTOMER MAIN PAGE
# @app.route("/customer")
# def customer():
#     return render_template("customer.html")


# # CUSTOMER REGISTER
# @app.route("/customer_register", methods=["GET", "POST"])
# def customer_register():

#     if request.method == "POST":

#         name = request.form["name"]
#         location = request.form["location"]
#         contact = request.form["contact"]
#         password = request.form["password"]

#         query = "INSERT INTO customer (name,location,contact,password) VALUES (%s,%s,%s,%s)"
#         values = (name, location, contact, password)

#         cursor = get_cursor()
#         cursor.execute(query, values)
#         db.commit()
#         cursor.close()

#         return render_template("cregister_success.html")

#     return render_template("customer_register.html")


# # CUSTOMER LOGIN
# @app.route("/customer_login", methods=["GET", "POST"])
# def customer_login():

#     if request.method == "POST":

#         contact = request.form["contact"]
#         password = request.form["password"]

#         query = "SELECT * FROM customer WHERE contact=%s AND password=%s"
#         values = (contact, password)

#         cursor = get_cursor()
#         cursor.execute(query, values)
#         user = cursor.fetchone()
#         cursor.close()

#         if user:
#             return redirect("/customer_dashboard")
#         else:
#             return render_template("customer_login.html", error="Invalid Credentials")

#     return render_template("customer_login.html")


# # CUSTOMER DASHBOARD
# @app.route("/customer_dashboard")
# def customer_dashboard():
#     return render_template("customer_dashboard.html")


# # POST REQUEST PAGE
# @app.route("/post_request", methods=["GET", "POST"])
# def post_request():

#     if request.method == "POST":

#         name = request.form["name"]
#         location = request.form["location"]
#         service_type = request.form["service_type"]
#         description = request.form["description"]
#         customer_contact = request.form["contact"]

#         query = """
#         INSERT INTO service_requests (name, location, service_type, description, customer_contact)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         values = (name, location, service_type, description, customer_contact)

#         cursor = get_cursor()
#         cursor.execute(query, values)
#         db.commit()
#         cursor.close()

#         return render_template("request.html")

#     return render_template("post_request.html")


# # OPEN BID PAGE
# @app.route("/apply_bid")
# def apply_bid():

#     request_id = request.args.get("request_id")
#     print("Apply Page Request ID:", request_id)

#     return render_template("apply_bid.html", request_id=request_id)


# # SUBMIT BID
# @app.route("/submit_bid", methods=["POST"])
# def submit_bid():

#     request_id = request.form.get("request_id")
#     contact = request.form.get("contact")
#     price = request.form.get("price")
#     message = request.form.get("message")

#     print("Submit Bid Request ID:", request_id)

#     if not request_id:
#         return "Error: Request ID missing"

#     query = """
#     INSERT INTO bids (serviceman_contact, request_id, price, message)
#     VALUES (%s, %s, %s, %s)
#     """
#     values = (contact, request_id, price, message)

#     cursor = get_cursor()
#     cursor.execute(query, values)
#     db.commit()
#     cursor.close()

#     return redirect("/serviceman_dashboard")


# # SHOW CUSTOMER REQUESTS
# @app.route("/my_requests", methods=["GET", "POST"])
# def my_requests():

#     if request.method == "POST":

#         contact = request.form["contact"]

#         query = "SELECT * FROM service_requests WHERE customer_contact=%s"

#         cursor = get_cursor()
#         cursor.execute(query, (contact,))
#         data = cursor.fetchall()
#         cursor.close()

#         return render_template("my_requests.html", requests=data)

#     return render_template("enter_contact.html")


# # VIEW BIDS
# @app.route("/view_bids")
# def view_bids():

#     request_id = request.args.get("request_id")

#     cursor = get_cursor()

#     cursor.execute("SELECT * FROM bids WHERE request_id=%s", (request_id,))
#     bids = cursor.fetchall()

#     cursor.execute("SELECT * FROM bids WHERE request_id=%s AND status='accepted'", (request_id,))
#     accepted_bid = cursor.fetchone()

#     cursor.close()

#     return render_template("view_bids.html", bids=bids, accepted_bid=accepted_bid)


# # ACCEPT BID
# @app.route("/accept_bid", methods=["POST"])
# def accept_bid():

#     bid_id = request.form["bid_id"]
#     request_id = request.form["request_id"]

#     cursor = get_cursor()

#     cursor.execute("UPDATE bids SET status='accepted' WHERE id=%s", (bid_id,))
#     cursor.execute("UPDATE bids SET status='rejected' WHERE request_id=%s AND id!=%s", (request_id, bid_id))
#     cursor.execute("UPDATE service_requests SET status='accepted' WHERE id=%s", (request_id,))

#     db.commit()
#     cursor.close()

#     return redirect("/customer_dashboard")


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

#          FOR DEPLOYMENT

from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from urllib.parse import urlparse

app = Flask(__name__)

# ✅ DATABASE CONNECTION (for deployment + local both)
def get_db_connection():
    db_url = os.getenv("DATABASE_URL")

    # 👉 If deployed (Railway gives DATABASE_URL)
    if db_url:
        url = urlparse(db_url)

        return mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path[1:],  # remove '/'
            port=url.port
        )

    # 👉 Local fallback (your MySQL Workbench)
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Haru@sql2023",
        database="fixit"
    )


def get_cursor():
    db = get_db_connection()
    return db, db.cursor(buffered=True)


@app.route('/resume')
def resume():
    return render_template('portfolio.html')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/serviceman")
def serviceman():
    return render_template("serviceman.html")


@app.route("/serviceman_register", methods=["GET", "POST"])
def serviceman_register():
    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["contact"]
        service_type = request.form["service_type"]
        password = request.form["password"]

        db, cursor = get_cursor()

        query = "INSERT INTO serviceman (name,contact,service_type,password) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (name, contact, service_type, password))
        db.commit()

        cursor.close()
        db.close()

        return render_template("register_success.html")

    return render_template("serviceman_register.html")


@app.route("/serviceman_login", methods=["GET", "POST"])
def serviceman_login():
    if request.method == "POST":
        contact = request.form["contact"]
        password = request.form["password"]

        db, cursor = get_cursor()

        query = "SELECT * FROM serviceman WHERE contact=%s AND password=%s"
        cursor.execute(query, (contact, password))
        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            return redirect("/serviceman_dashboard")
        else:
            return render_template("serviceman_login.html", error="Invalid Mobile Number or Password")

    return render_template("serviceman_login.html")


@app.route("/serviceman_dashboard")
def serviceman_dashboard():
    db, cursor = get_cursor()

    cursor.execute("SELECT * FROM service_requests")
    requests = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("serviceman_dashboard.html", requests=requests)


@app.route("/customer")
def customer():
    return render_template("customer.html")


@app.route("/customer_register", methods=["GET", "POST"])
def customer_register():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        contact = request.form["contact"]
        password = request.form["password"]

        db, cursor = get_cursor()

        query = "INSERT INTO customer (name,location,contact,password) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (name, location, contact, password))
        db.commit()

        cursor.close()
        db.close()

        return render_template("cregister_success.html")

    return render_template("customer_register.html")


@app.route("/customer_login", methods=["GET", "POST"])
def customer_login():
    if request.method == "POST":
        contact = request.form["contact"]
        password = request.form["password"]

        db, cursor = get_cursor()

        query = "SELECT * FROM customer WHERE contact=%s AND password=%s"
        cursor.execute(query, (contact, password))
        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user:
            return redirect("/customer_dashboard")
        else:
            return render_template("customer_login.html", error="Invalid Credentials")

    return render_template("customer_login.html")


@app.route("/customer_dashboard")
def customer_dashboard():
    return render_template("customer_dashboard.html")


@app.route("/post_request", methods=["GET", "POST"])
def post_request():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        service_type = request.form["service_type"]
        description = request.form["description"]
        customer_contact = request.form["contact"]

        db, cursor = get_cursor()

        query = """
        INSERT INTO service_requests (name, location, service_type, description, customer_contact)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, location, service_type, description, customer_contact))
        db.commit()

        cursor.close()
        db.close()

        return render_template("request.html")

    return render_template("post_request.html")


@app.route("/apply_bid")
def apply_bid():
    request_id = request.args.get("request_id")
    return render_template("apply_bid.html", request_id=request_id)


@app.route("/submit_bid", methods=["POST"])
def submit_bid():
    request_id = request.form.get("request_id")
    contact = request.form.get("contact")
    price = request.form.get("price")
    message = request.form.get("message")

    db, cursor = get_cursor()

    query = """
    INSERT INTO bids (serviceman_contact, request_id, price, message)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (contact, request_id, price, message))
    db.commit()

    cursor.close()
    db.close()

    return redirect("/serviceman_dashboard")


@app.route("/my_requests", methods=["GET", "POST"])
def my_requests():
    if request.method == "POST":
        contact = request.form["contact"]

        db, cursor = get_cursor()

        query = "SELECT * FROM service_requests WHERE customer_contact=%s"
        cursor.execute(query, (contact,))
        data = cursor.fetchall()

        cursor.close()
        db.close()

        return render_template("my_requests.html", requests=data)

    return render_template("enter_contact.html")


@app.route("/view_bids")
def view_bids():
    request_id = request.args.get("request_id")

    db, cursor = get_cursor()

    cursor.execute("SELECT * FROM bids WHERE request_id=%s", (request_id,))
    bids = cursor.fetchall()

    cursor.execute("SELECT * FROM bids WHERE request_id=%s AND status='accepted'", (request_id,))
    accepted_bid = cursor.fetchone()

    cursor.close()
    db.close()

    return render_template("view_bids.html", bids=bids, accepted_bid=accepted_bid)


@app.route("/accept_bid", methods=["POST"])
def accept_bid():
    bid_id = request.form["bid_id"]
    request_id = request.form["request_id"]

    db, cursor = get_cursor()

    cursor.execute("UPDATE bids SET status='accepted' WHERE id=%s", (bid_id,))
    cursor.execute("UPDATE bids SET status='rejected' WHERE request_id=%s AND id!=%s", (request_id, bid_id))
    cursor.execute("UPDATE service_requests SET status='accepted' WHERE id=%s", (request_id,))

    db.commit()

    cursor.close()
    db.close()

    return redirect("/customer_dashboard")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)