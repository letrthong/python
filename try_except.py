try:
    # Code that might cause an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("You can't divide by zero!")
except Exception as e:
    # Code to handle any other exceptions
    print(f"An error occurred: {e}")
finally:
    # Code that will run no matter what
    print("Execution completed.")
