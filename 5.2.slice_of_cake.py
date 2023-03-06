
def get_recipe_price(prices, optional=[], **args):
    final_price = 0
    for ingredient, price in prices.items():
        if ingredient not in optional:
            quantity = args.get(ingredient)
            ingredient_price = quantity/100 * price  # the price is according to 100 grams
            final_price += ingredient_price

    print(int(final_price))




