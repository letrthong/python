
import hashlib

# Function to generate MD5 hash
def generate_md5(input_string):
    md5_hash = hashlib.md5(input_string.encode())
    return md5_hash.hexdigest()

# Example usage: hashing a food supply record
food_supply_record = "Item: Apples, Quantity: 100, Supplier: Farm Fresh, Date: 2025-04-09"
md5_result = generate_md5(food_supply_record)

print("MD5 Hash of Food Supply Record:", md5_result)
