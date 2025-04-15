
import example_pb2

# Create a new Person message
person = example_pb2.Person()
person.name = "John Doe"
person.id = 1234
person.email = "john.doe@example.com"

# Serialize the message to a binary string
serialized_person = person.SerializeToString()

# Deserialize the binary string back to a Person message
new_person = example_pb2.Person()
new_person.ParseFromString(serialized_person)

print(f"Name: {new_person.name}")
print(f"ID: {new_person.id}")
print(f"Email: {new_person.email}")
