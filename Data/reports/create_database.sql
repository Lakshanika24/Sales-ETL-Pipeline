CREATE DATABASE sales_etl;

USE sales_etl;

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    customer VARCHAR(100),
    product VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    total_amount DECIMAL(10,2)
);