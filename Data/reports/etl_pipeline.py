import pandas as pd
import mysql.connector

print("ETL Process Started")

# ===================
# EXTRACT
# ===================

df = pd.read_csv("../sales_data.csv")

print("Data Extracted Successfully")
print(df.head())

# ===================
# TRANSFORM
# ===================

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df["Quantity"] = df["Quantity"].astype(int)

df["TotalAmount"] = df["Quantity"] * df["Price"]

print("\nTransformed Data")
print(df)

# ===================
# LOAD TO MYSQL
# ===================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laksh@24",
    database="sales_etl"
)

cursor = connection.cursor()

cursor.execute("DELETE FROM sales")

for index, row in df.iterrows():

    query = """
    INSERT INTO sales
    (order_id, customer, product, quantity, price, total_amount)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        int(row["OrderID"]),
        row["Customer"],
        row["Product"],
        int(row["Quantity"]),
        float(row["Price"]),
        float(row["TotalAmount"])
    )

    cursor.execute(query, values)

connection.commit()

print("Data Loaded Into MySQL")

# ===================
# REPORT GENERATION
# ===================

summary = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Revenue=("TotalAmount", "sum")
)

summary.to_csv("sales_summary.csv")

print("\nSales Summary")
print(summary)

print("\nETL Pipeline Completed Successfully")

cursor.close()
connection.close()