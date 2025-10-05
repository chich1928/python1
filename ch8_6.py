def get_discount_price(price, discount):
    discount = float(discount.rstrip('%')) / 100 if isinstance(discount, str) and discount.endswith('%') else discount
    return price - price * discount

print(get_discount_price(100, "20%"))      # 預期 80.0
print(get_discount_price(200, "50%"))      # 預期 100.0
print(get_discount_price(150, 0.1))         # 預期 135.0
print(get_discount_price(80, 0.25))         # 預期 60.0
print(get_discount_price(120, "0%"))       # 預期 120.0
print(get_discount_price(120, "100%"))     # 預期 0.0
