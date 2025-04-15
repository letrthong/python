
try:
    new_example.ParseFromString(corrupted_data)
except Exception as e:
    print(f"Failed to parse message: {e}")
