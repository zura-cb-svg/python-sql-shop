DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS orders;

CREATE TABLE users (
    id INTEGER,
    name TEXT
);

CREATE TABLE orders (
    id INTEGER,
    user_id INTEGER,
    total INTEGER,
    status TEXT
);

INSERT INTO users VALUES
(1, 'Luka'),
(2, 'Nino'),
(3, 'Nika'),
(4, 'Gio');

INSERT INTO orders VALUES
(1, 1, 100, 'Shipped'),
(2, 2, 200, 'Pending'),
(3, 1, 50, 'Shipped'),
(4, 4, 500, 'Shipped');