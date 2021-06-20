product_links = open('Data Acquisition/product_links.txt', 'r')

products = []

for line in product_links:
    split = line.split(': ')
    products.append((split[0], split[1][:-1]))