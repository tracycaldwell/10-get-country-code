def get_country_codes(prices):
    
    price_final = []
    separated_prices = prices.split(', ')
    for i in separated_prices:
        short_list = i.split('$')
        price_final.append(short_list[0])
    return ', '.join(price_final)
