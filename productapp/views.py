from django.shortcuts import render

# Create your views here.
import math

# Product catalog
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.1),
    "tiered_50_discount": (30, 0.5)
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10

# Function to calculate the total amount for a product
def calculate_product_total(product_name, quantity, is_gift_wrapped):
    price = products[product_name]
    total = price * quantity
    gift_wrap_total = gift_wrap_fee * quantity if is_gift_wrapped else 0
    return total, gift_wrap_total

# Function to apply discount rules and determine the most beneficial discount
def apply_discount_rules(quantity, product_totals):
    max_discount = 0
    discount_name = "None"
    
    for rule, (rule_quantity, rule_discount) in discount_rules.items():
        if quantity >= rule_quantity:
            discount_amount = 0
            for total in product_totals:
                if total > rule_quantity:
                    discount_amount += (total - rule_quantity) * rule_discount
            if discount_amount > max_discount:
                max_discount = discount_amount
                discount_name = rule
    
    return discount_name, max_discount

# Function to calculate the total shipping fee
def calculate_shipping_fee(quantity):
    package_count = math.ceil(quantity / units_per_package)
    shipping_fee = package_count * shipping_fee_per_package
    return shipping_fee

# User input
product_quantities = {}
product_gift_wraps = {}

for product in products:
    quantity = int(input(f"Enter the quantity for {product}: "))
    is_gift_wrapped = input(f"Is {product} wrapped as a gift? (Yes/No): ").lower() == "yes"
    product_quantities[product] = quantity
    product_gift_wraps[product] = is_gift_wrapped

# Calculation
product_totals = []
quantity_total = 0

for product, quantity in product_quantities.items():
    is_gift_wrapped = product_gift_wraps[product]
    total, gift_wrap_total = calculate_product_total(product, quantity, is_gift_wrapped)
    product_totals.append(quantity)
    quantity_total += quantity
    print(f"{product}: Quantity: {quantity}, Total amount: ${total}")
    print(f"Gift wrap fee for {product}: ${gift_wrap_total}")
    print()

subtotal = sum(product_totals)
discount_name, discount_amount = apply_discount_rules(quantity_total, product_totals)
shipping_fee = calculate_shipping_fee(quantity_total)

# Output
print("Summary:")
print(f"Subtotal: ${subtotal}")
print(f"Discount applied: {discount_name}, Discount amount: ${discount_amount}")
print(f"Shipping fee: ${shipping_fee}")
print(f"Total: ${subtotal - discount_amount + shipping_fee}")

