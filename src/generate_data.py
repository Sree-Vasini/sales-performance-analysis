import numpy as np
import pandas as pd

def generate_sales(n=5000, seed=42):
    rng = np.random.default_rng(seed)

    dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")
    regions = ["North", "South", "East", "West"]
    channels = ["Online", "Store"]
    categories = ["Electronics", "Fashion", "Home", "Beauty", "Grocery"]
    products = {
        "Electronics": ["Headphones", "Phone", "Laptop", "Speaker"],
        "Fashion": ["T-Shirt", "Jeans", "Shoes", "Jacket"],
        "Home": ["Lamp", "Chair", "Table", "Cookware"],
        "Beauty": ["Skincare", "Perfume", "Makeup", "Shampoo"],
        "Grocery": ["Snacks", "Beverages", "Cereal", "Spices"],
    }

    rows = []
    for i in range(1, n + 1):
        date = rng.choice(dates)
        region = rng.choice(regions)
        channel = rng.choice(channels)
        category = rng.choice(categories)
        product = rng.choice(products[category])

        price = rng.uniform(10, 300)
        qty = rng.integers(1, 5)
        discount = rng.uniform(0, 0.2)

        revenue = price * qty * (1 - discount)

        rows.append({
            "order_id": i,
            "order_date": date,
            "region": region,
            "channel": channel,
            "category": category,
            "product": product,
            "unit_price": round(price, 2),
            "quantity": qty,
            "discount_rate": round(discount, 2),
            "revenue": round(revenue, 2),
        })

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_sales()
    df.to_csv("data/sales.csv", index=False)
    print("Dataset generated successfully!")
