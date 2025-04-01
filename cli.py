import subprocess

# Run a simple command
result = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)

# Print the output
print(result.stdout)
