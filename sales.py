import pandas as pd

# this code reads a CSV file named "ecommerce_sales_analysis.csv"
#  located in the "data" directory and stores it in a DataFrame called "sales".
sales = pd.read_csv("data/ecommerce_sales_analysis.csv")
#sales.head()
#print(sales)

# this code reads the same CSV file again and stores it in a 
# new DataFrame called "df".
df = pd.read_csv("data/ecommerce_sales_analysis.csv")
#print(df[df["category"].isin(["Home & Kitchen", "Toys & Games","Books","Electronics"])])
#print(df.columns)


# This created a new column called "total_sales" that sums up the sales for each month across all 12 months for each product. The sum is calculated row-wise (axis=1)
#  to get the total sales for each product.
df["quantities_sold"] = df[['sales_month_1', 'sales_month_2', 'sales_month_3',
     'sales_month_4', 'sales_month_5', 'sales_month_6',
     'sales_month_7', 'sales_month_8', 'sales_month_9',
     'sales_month_10', 'sales_month_11', 'sales_month_12']
].sum(axis=1)

# This code creates a new column called "total_amount_per_category" by
#  multiplying the "price" column with the "total_sales" column.
df["total_sales"]= df["price"] * df["quantities_sold"]

# This returns a Series where the index is the category and the value
#  is the index of the row with the highest total sales for that category.
total_per_category = df.loc[df.groupby("category")["quantities_sold"].idxmax()]

# Sort by quantities sold in descending order
total_per_category.sort_values(by= "quantities_sold", ascending=False, inplace=True)
print(total_per_category)
