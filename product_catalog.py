from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.
print("Sample products:")
for product in products[:3]:
    print(product)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()


# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    updated_product = product.copy()
    updated_product["tags"] = set(product["tags"])
    converted_products.append(updated_product)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    recommendations.sort(key=lambda x: x["matches"], reverse=True)
    return recommendations


# TODO: Step 7 - Call your function and print the results
results = recommend_products(converted_products, customer_preferences)

print("\nRecommended Products:")
for product in results:
    print(f"{product['name']} - {product['matches']} matches")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#    This program uses loops to collect customer preferences and iterate
#    through the product catalog. Sets are used to store both customer
#    preferences and product tags because they remove duplicates and allow
#    for fast comparisons. Set intersection is used to efficiently count
#    how many tags match between a product and the customer.
#
# 2. How might this code change if you had 1000+ products?
#    With a much larger product catalog, the same logic would still work,
#    but performance optimizations could be added. Product tags could be
#    preprocessed once instead of repeatedly, and results could be sorted
#    or limited to top matches. For very large datasets, storing products
#    in a database or using indexing would improve efficiency.
git add .
git commit -m "Debugged final output issues"
git push
