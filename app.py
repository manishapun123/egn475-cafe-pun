from flask import Flask, render_template, abort
app = Flask(__name__)



# Sample menu data for Café Calle Ocho
SAMPLE_ITEMS = [
    {
        "id": 1,
        "name": "Café con leche",
        "category": "Drinks",
        "price_cents": 350,
        "description": "Traditional Cuban coffee with steamed milk."
    },
    {
        "id": 2,
        "name": "Cuban Sandwich",
        "category": "Food",
        "price_cents": 850,
        "description": "A delicious Cuban sandwich with ham and cheese."
    },
    {
        "id": 3,
        "name": "Guava Pastry",
        "category": "Snacks",
        "price_cents": 300,
        "description": "Sweet pastry filled with guava."
    },
    {
        "id": 4,
        "name": "Cortadito",
        "category": "Drinks",
        "price_cents": 275,
        "description": "Strong Cuban espresso with a little steamed milk."
    },
    {
        "id": 5,
        "name": "Empanada",
        "category": "Food",
        "price_cents": 450,
        "description": "A tasty pastry with a savory filling."
    },
    {
        "id": 6,
        "name": "Tres Leches Cake",
        "category": "Desserts",
        "price_cents": 500,
        "description": "A soft cake made with three kinds of milk."
    }
]

# Sample orders for the kitchen board and order history
SAMPLE_ORDERS = [
    {
        "id": 1001,
        "customer": "Maria",
        "items": "Café con leche, Cuban Sandwich",
        "pickup_time": "12:30 PM",
        "status": "Preparing",
        "total_cents": 1200
    },
    {
        "id": 1002,
        "customer": "Carlos",
        "items": "Guava Pastry, Cortadito",
        "pickup_time": "1:00 PM",
        "status": "Ready",
        "total_cents": 575
    },
    {
        "id": 1003,
        "customer": "Sofia",
        "items": "Empanada, Tres Leches Cake",
        "pickup_time": "1:30 PM",
        "status": "Completed",
        "total_cents": 950
    }
]


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Menu page showing all menu items
@app.route("/menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)


# Details page for one menu item
@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    item = next(
        (item for item in SAMPLE_ITEMS if item["id"] == item_id),
        None
    )

    if item is None:
        abort(404)

    return render_template("item.html", item=item)


# Place an order page
@app.route("/order/new")
def new_order():
    return render_template("order_new.html", items=SAMPLE_ITEMS)


# Kitchen staff board
@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html", orders=SAMPLE_ORDERS)


# Order history page
@app.route("/orders")
def orders():
    return render_template("orders.html", orders=SAMPLE_ORDERS)


# Original Week 1 about page
@app.route("/about")
def about():
    return "Welcome to Café Calle Ocho in Little Havana!"


if __name__ == "__main__":
    app.run(debug=True)
