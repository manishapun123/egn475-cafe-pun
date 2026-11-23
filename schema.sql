DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS menu_items;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'customer'
);

CREATE TABLE menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
    available INTEGER NOT NULL DEFAULT 1 CHECK (available IN (0, 1))
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Pending',
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL REFERENCES orders(id),
    menu_item_id INTEGER NOT NULL REFERENCES menu_items(id),
    quantity INTEGER NOT NULL DEFAULT 1 CHECK (quantity > 0)
);

INSERT INTO menu_items (id, name, category, price_cents) VALUES
    (1, 'Café con leche', 'Drinks', 350),
    (2, 'Cuban Sandwich', 'Food', 850),
    (3, 'Guava Pastry', 'Snacks', 300),
    (4, 'Cortadito', 'Drinks', 275),
    (5, 'Empanada', 'Food', 450),
    (6, 'Tres Leches Cake', 'Desserts', 500);

INSERT INTO orders (id, customer_name, status, notes) VALUES
    (1001, 'Maria', 'Preparing', 'Pickup at 12:30 PM'),
    (1002, 'Carlos', 'Ready', 'Pickup at 1:00 PM'),
    (1003, 'Sofia', 'Completed', 'Pickup at 1:30 PM');

INSERT INTO order_items (order_id, menu_item_id, quantity) VALUES
    (1001, 1, 1),
    (1001, 2, 1),
    (1002, 3, 1),
    (1002, 4, 1),
    (1003, 5, 1),
    (1003, 6, 1);
