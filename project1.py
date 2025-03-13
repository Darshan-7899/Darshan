import pandas as pd
import matplotlib.pyplot as plt

# 1. Data Loading (Replace with your actual data)
data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C'],
    'quantity': [2, 3, 1, 4, 2, 3, 1, 2, 3, 4],
    'price_per_unit': [10, 15, 10, 20, 15, 10, 20, 10, 15, 20],
    'customer_id': [101, 102, 101, 103, 102, 101, 103, 101, 102, 103]
}
df = pd.DataFrame(data)

# 2. Data Cleaning (Example: Calculate total revenue)
df['total_revenue'] = df['quantity'] * df['price_per_unit']

# 3. Exploratory Data Analysis (EDA)

# Top-selling products
top_products = df.groupby('product')['quantity'].sum().sort_values(ascending=False)
print("\nTop-Selling Products:\n", top_products)

# Calculate total revenue per product
revenue_per_product = df.groupby('product')['total_revenue'].sum().sort_values(ascending=False)
print("\nTotal Revenue per Product:\n", revenue_per_product)

# Customer spending habits
customer_spending = df.groupby('customer_id')['total_revenue'].sum().sort_values(ascending=False)
print("\nCustomer Spending:\n", customer_spending)

# Average order value
average_order_value = df['total_revenue'].mean()
print("\nAverage Order Value:", average_order_value)

# 4. Visualization (Optional)
top_products.plot(kind='bar', title='Top-Selling Products')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.show()

customer_spending.head(5).plot(kind='bar', title='Top 5 Customers by Spending')
plt.xlabel('Customer ID')
plt.ylabel('Total Revenue')
plt.show()

print("\nDataframe with total revenue column:")
print(df)