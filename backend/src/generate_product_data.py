import sqlite3
import random
import json
import os
from faker import Faker

# --- Configuration ---
DATABASE_PATH = '/home/ubuntu/cosmetic_ingredient_system/backend/src/database/app.db'
TARGET_PRODUCTS_PER_INGREDIENT = 10
MAX_PRICE = 500
MIN_PRICE = 50

# Initialize Faker for generating fake product names and brands
fake = Faker('zh_CN')

def get_ingredient_ids(conn):
    """Retrieves all ingredient IDs from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM ingredients")
    return cursor.fetchall()

def get_skin_type_ids(conn):
    """Retrieves all skin type IDs from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM skin_types")
    return [row[0] for row in cursor.fetchall()]

def generate_products(ingredient_id, ingredient_name, skin_type_ids):
    """Generates a list of fake products for a given ingredient."""
    products = []
    
    # Generate more products than the target to ensure variety
    num_products = TARGET_PRODUCTS_PER_INGREDIENT + random.randint(0, 5)
    
    concentration_levels = ['High', 'Medium', 'Low']
    
    for i in range(num_products):
        # Product details
        product_name = f"{fake.word()} {ingredient_name} 精华" if i < 5 else f"{fake.word()} {ingredient_name} 面霜"
        brand = fake.company()
        price = round(random.uniform(MIN_PRICE, MAX_PRICE), 2)
        purchase_link = f"https://example.com/product/{random.randint(1000, 9999)}"
        
        # Ingredient concentration level (randomly assigned for variety)
        concentration_level = random.choice(concentration_levels)
        
        # Skin type association (1 to 3 random skin types)
        num_skin_types = random.randint(1, 3)
        associated_skin_types = random.sample(skin_type_ids, num_skin_types)
        
        products.append({
            'name': product_name,
            'brand': brand,
            'price': price,
            'concentration_level': concentration_level,
            'purchase_link': purchase_link,
            'ingredient_id': ingredient_id,
            'skin_type_ids': associated_skin_types
        })
        
    return products

def insert_products(conn, products):
    """Inserts generated products and their associations into the database."""
    cursor = conn.cursor()
    
    # Insert product
    product_data = (products['name'], products['brand'], products['price'], products['concentration_level'], products['purchase_link'])
    cursor.execute(
        "INSERT INTO products (name, brand, price, concentration_level, purchase_link) VALUES (?, ?, ?, ?, ?)",
        product_data
    )
    product_id = cursor.lastrowid
    
    # Insert ingredient-product association
    cursor.execute(
        "INSERT INTO ingredient_product (ingredient_id, product_id, concentration_level) VALUES (?, ?, ?)",
        (products['ingredient_id'], product_id, products['concentration_level'])
    )
    
    # Insert product-skin_type association
    for skin_type_id in products['skin_type_ids']:
        cursor.execute(
            "INSERT INTO product_skintype (product_id, skintype_id) VALUES (?, ?)",
            (product_id, skin_type_id)
        )

def main():
    print("--- Starting Massive Product Data Generation ---")
    
    # Connect to the database
    try:
        conn = sqlite3.connect(DATABASE_PATH)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return

    ingredient_list = get_ingredient_ids(conn)
    skin_type_ids = get_skin_type_ids(conn)
    
    if not ingredient_list or not skin_type_ids:
        print("Error: Ingredient or Skin Type data not found. Please run init_data.py first.")
        conn.close()
        return
        
    print(f"Found {len(ingredient_list)} ingredients and {len(skin_type_ids)} skin types.")
    
    total_products_generated = 0
    
    # Clear existing product data to avoid duplicates/conflicts
    print("Clearing existing product data...")
    conn.execute("DELETE FROM ingredient_product")
    conn.execute("DELETE FROM product_skintype")
    conn.execute("DELETE FROM products")
    conn.commit()

    for ingredient_id, ingredient_name in ingredient_list:
        products_to_insert = generate_products(ingredient_id, ingredient_name, skin_type_ids)
        
        for product in products_to_insert:
            insert_products(conn, product)
            total_products_generated += 1
            
        print(f"Generated {len(products_to_insert)} products for ingredient: {ingredient_name} (ID: {ingredient_id})")

    conn.commit()
    conn.close()
    
    print(f"--- Finished. Total products generated: {total_products_generated} ---")

if __name__ == "__main__":
    # Ensure the database directory exists
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    # Need to ensure init_data.py is run first to create tables and base data
    print("WARNING: Ensure init_data.py has been run to create the database schema and ingredients.")
    main()
