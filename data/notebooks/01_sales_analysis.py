import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales.csv")

print("Dataset Preview:")
print(df.head())

# Basic KPIs
total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
avg_order_value = total_revenue / total_orders

print("\nKPI Summary")
print("Total Revenue:", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Average Order Value:", round(avg_order_value, 2))

# Monthly Revenue Trend
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M")

monthly = df.groupby("month")["revenue"].sum()

plt.figure(figsize=(8, 4))
monthly.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/monthly_revenue_trend.png")

# Revenue by Category
category = df.groupby("category")["revenue"].sum()

plt.figure(figsize=(8, 4))
category.plot(kind="bar")
plt.title("Revenue by Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_by_category.png")

print("\nAnalysis complete. Charts saved to outputs folder.")
