import hashlib
import re
from datetime import datetime

# Function to generate MD5 hash
def generate_md5(input_string):
    md5_hash = hashlib.md5(input_string.encode())
    return md5_hash.hexdigest()

def convert_to_epoch(date_str):
    try:
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        # Convert the datetime object to epoch time
        epoch_time = int(date_obj.timestamp())
        return epoch_time
    except ValueError:
        return None

def is_valid_date_format(date_str):
    # Regular expression pattern for dd/mm/yyyy
    date_pattern = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b'
    return bool(re.match(date_pattern, date_str))

def is_valid_start_and_end_date(start_date, end_date):
    if not is_valid_date_format(start_date) or not is_valid_date_format(end_date):
        return False

    start_epoch = convert_to_epoch(start_date)
    end_epoch = convert_to_epoch(end_date)
    if start_epoch is None or end_epoch is None or start_epoch > end_epoch:
        return False
    return True

# Example usage: hashing a food supply record
food_supply_record = "Item: Apples, Quantity: 100, Supplier: Farm Fresh, Date: 2025-04-09"
md5_result = generate_md5(food_supply_record)

print("MD5 Hash of Food Supply Record:", md5_result)

date_str = "15/01/2025"

if is_valid_date_format(date_str):
    print("Match found: " + date_str)
else:
    print("No match found: " + date_str)

epoch_time = convert_to_epoch(date_str)
if epoch_time is not None:
    print(f"The epoch time for {date_str} is {epoch_time}.")
else:
    print(f"Invalid date format: {date_str}")
