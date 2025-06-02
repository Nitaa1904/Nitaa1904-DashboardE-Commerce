import pandas as pd
import pytest
from dashboard import (
    create_daily_orders_df,
    create_customer_profile_df,
    create_top_products_df
)

# Contoh data dummy untuk testing
DUMMY_DATA = pd.DataFrame({
    "order_purchase_timestamp": ["2023-01-01", "2023-01-01", "2023-01-02"],
    "order_id": [1, 2, 3],
    "price": [100, 200, 300],
    "customer_state": ["SP", "RJ", "SP"],
    "customer_city": ["São Paulo", "Rio", "Campinas"],
    "product_category_name": ["eletrônicos", "livros", "eletrônicos"],
    "product_id": ["p1", "p2", "p3"],
    "freight_value": [10.5, 5.0, 8.0],
    "review_score": [5, 4, 3],
    "customer_id": ["c1", "c2", "c3"]
})

# Test 1: Fungsi create_daily_orders_df
def test_create_daily_orders_df():
    result = create_daily_orders_df(DUMMY_DATA)
    
    # Cek apakah kolom yang diperlukan ada
    assert "order_count" in result.columns
    assert "revenue" in result.columns
    
    # Cek hasil aggregasi
    assert result["order_count"].sum() == 3  # Total order harus 3
    assert result["revenue"].sum() == 600   # Total revenue (100+200+300)

# Test 2: Fungsi create_customer_profile_df
def test_create_customer_profile_df():
    result = create_customer_profile_df(DUMMY_DATA)
    
    # Cek struktur dataframe
    assert all(col in result.columns for col in ["customer_state", "customer_city", "customer_count"])
    
    # Cek nilai unik
    assert result["customer_state"].nunique() == 2  # SP dan RJ

# Test 3: Fungsi create_top_products_df
def test_create_top_products_df():
    result = create_top_products_df(DUMMY_DATA)
    
    # Cek kolom dan sorting
    assert "product_category_name" in result.columns
    assert result["order_id"].iloc[0] >= result["order_id"].iloc[1] 

# Test 4: Error handling (opsional)
def test_invalid_data():
    with pytest.raises(Exception):
        create_daily_orders_df(pd.DataFrame()) 

def test_missing_order_purchase_timestamp():
    invalid_data = pd.DataFrame({
        "order_id": [1, 2, 3],
        "price": [100, 200, 300]
    })

    with pytest.raises(KeyError, match="order_purchase_timestamp"):
        create_daily_orders_df(invalid_data)
