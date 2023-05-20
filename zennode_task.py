#Product catalog
products = {  "Product A": 20,
              "Product B": 40,
              "Product C": 50  }
#Discount rules
discount_rules = {  "flat_10_discount": 10,
                    "bulk_5_discount": 5,
                     "bulk_10_discount": 10,
                     "tiered_50_discount": 50 }
#Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

#calculating discounts
def cal_disc(quantity, total_qty, total_amt):
    disc_types = {}

#rule: flat_10_discount
    if total_amt > 200:
        disc_types["flat_10_discount"] = 10

#rule: bulk_5_discount
    for prod_qty in quantity.values():
        if prod_qty > 10:
            disc_types["bulk_5_discount"] = 5
            break

#rule: bulk_10_discount
    if total_qty > 20:
        disc_types["bulk_10_discount"] = 10

#rule: tiered_50_discount
    if total_qty > 30:
        for product, prod_qty in quantity.items():
            if prod_qty > 15:
                disc_types["tiered_50_discount"] = discount_rules["tiered_50_discount"]
                break

#applying the most beneficial discount
    if disc_types:
        max_disc = max(disc_types.values())
        disc_name = [name for name, discount in disc_types.items() if discount == max_disc][0]
        disc_amt = max_disc
    else:
        disc_name = "No discount applied"
        disc_amt = 0

    return disc_name, disc_amt

#calculating total amount
def calc_total(quantity, wrapped_gifts):
    total_amt = 0
    total_qty = 0

    for product, prod_qty in quantity.items():
        price_per_unit = products[product]
        total_qty += prod_qty
        total_amt += prod_qty * price_per_unit

#adding gift wrap fee
        if wrapped_gifts.get(product):
            total_amt += wrapped_gifts[product] * gift_wrap_fee

    discount_name, discount_amount = cal_disc(quantity, total_qty, total_amt)

#calculating shipping fee
    shipping_fee = (total_qty // items_per_package) * shipping_fee_per_package
    if total_qty % items_per_package != 0:
        shipping_fee += shipping_fee_per_package

#calculating total
    total = total_amt - discount_amount + shipping_fee
    return total_amt, discount_name, discount_amount, shipping_fee, total

def main():
    quantity = {}
    wrapped_gifts = {}

    for product in products:
        quantity_input = input(f"Enter the quantity of {product}: ")
        quantity[product] = int(quantity_input)

        giftwrap = input(f"Is {product} wrapped as a gift? (yes/no): ")
        if giftwrap.lower() == "yes":
            wrapped_gifts[product] = int(quantity_input)

    total_amount, discount_name, discount_amount, shipping_fee, total = calc_total(quantity, wrapped_gifts)

#printing the details
    print("Product Details:")
    for product, product_quantity in quantity.items():
        print(f"{product} - Quantity: {product_quantity} - Total: {product_quantity * products[product]}")

    print("------------------------------")
    print("Subtotal:", total_amount)
    print("Discount Applied:",discount_name)
    print( "Amount:",discount_amount)
    print("Shipping Fee:",shipping_fee)
    print("Total:", total)


if __name__ == "__main__":
    main()
