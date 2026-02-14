import pandas as pd
import matplotlib.pyplot as plot

# this code reads a CSV file named "ecommerce_sales_analysis.csv"
#  located in the "data" directory and stores it in a DataFrame called "sales".
sales = pd.read_csv("data/ecommerce_sales_analysis.csv")
#sales.head()
#print(sales)

# this code reads the same CSV file again and stores it in a 
# new DataFrame called "df".
df = pd.read_csv("data/ecommerce_sales_analysis.csv")
print(df[df["category"].isin(["Home & Kitchen", "Toys & Games","Books","Electronics"])])
print(df.columns)


# This created a new column called "quantities_sold" that sums up the sales for each month across all 12 months for each product. The sum is calculated row-wise (axis=1)
#  to get the total sales for each product.
df["quantities_sold"] = df[['sales_month_1', 'sales_month_2', 'sales_month_3',
     'sales_month_4', 'sales_month_5', 'sales_month_6',
     'sales_month_7', 'sales_month_8', 'sales_month_9',
     'sales_month_10', 'sales_month_11', 'sales_month_12']
].sum(axis=1)

# This code creates a new column called "total_sales" by
#  multiplying the "price" column with the "total_sales" column.
df["total_sales"]= df["price"] * df["quantities_sold"]

# This returns a Series where the index is the category and the value
#  is the index of the row with the highest total sales for that category.
total_per_category = df.loc[df.groupby("category")["quantities_sold"].idxmax()]

# Sort by quantities sold in descending order
total_per_category.sort_values(by= "quantities_sold", ascending=False, inplace=True)
print(total_per_category)

#Graphs 

total_per_category.plot(kind="bar", x="category", y="quantities_sold")
plot.title("Highest Sale per Category")
plot.ylabel("Total Sale Amount")
plot.show()

#df["category"].value_counts().plot.bar()
#df["quantities_sold"].value_counts().plot.bar()

#This graph shows the total sales for each category
#  by summing up the "total_sales" for each category
#  and then plotting it as a bar chart. The x-axis 
# represents the categories, and the y-axis represents
#  the total sales for each category. The title of the graph
#  is set to "Total Sales by Category". Finally, the graph 
# is displayed using plot.show().

quantities_graph = (
    df[df["category"].isin(["Electronics","Books", "Clothing", "Health","Sports","Toys"])]
    .groupby("category")["quantities_sold"].sum()  
)
quantities_graph.plot(kind="bar")
plot.title("Quantities sold by category")
plot.show()