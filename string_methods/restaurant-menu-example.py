# 3 star michelin vegan menu examples
restaurant1_name = 'Eleven Madison Park (New York)'
item1 = 'Carrot tartare; clay-roasted beetroot'
price1 = '$225–365 USD (plus wine pairing)'

restaurant2_name = 'Arpège (Paris)'
item2 = 'Veg sushi; garden veg w/ truffle; risotto'
price2 = '€185 (lunch) – €600+ (dinner)'

restaurant3_name = 'L’Arpège (Paris)'
item3 = 'Garden veg w/ truffle; veggie risotto'
price3 = '€300–600+(dinner)'

dash1 = 45 - len(restaurant1_name)
dash2 = 50 - len(item1)
dash3 = 45 - len(restaurant2_name)
dash4 = 50 - len(item2)
dash5 = 45 - len(restaurant3_name)
dash6 = 50 - len(item3)

print(restaurant1_name + ('-' * dash1) + item1 + ('-' * dash2) + price1)
print(restaurant2_name + ('-' * dash3) + item2 + ('-' * dash4) + price2)
print(restaurant3_name + ('-' * dash5) + item3 + ('-' * dash6) + price3)
