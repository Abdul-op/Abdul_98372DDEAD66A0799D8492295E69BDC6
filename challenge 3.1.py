"""
 Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
  """

  # Initialize an empty list to store the indices of the target product.
def linear_search_product(productlist, targetProduct):
    indices = []

  # Iterate over the list of products.
    for index, product in enumerate(productlist):
    # Check if the current product is the target product.
       if product == targetProduct:
      # Add the index of the current product to the list of indices.
         indices.append(index)

  # Return the list of indices of the target product.
    return indices

# Example usage:
products = ["laptop","mobile","laptop","keyboard","laptop"]
target = "laptop"
result = linear_search_product(products, target)
print(result)
#an empty list if the product is not found.
target2 = "airpods"
result = linear_search_product(products, target2)
print(result)
