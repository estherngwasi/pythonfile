# File Creation
try:
    # Open file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write new content to the file
        file.write("This is a new line 1.\n")
        file.write("23456\n")  # Writing numbers as well
        file.write("Another line with a mix of strings and numbers.\n")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation completed.")

# File Reading and Display
try:
    # Open file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display contents of the file
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("The file 'my_file.txt' was not found.")
except PermissionError:
    print("You don't have permission to read the file.")
except Exception as e:
    print("An error occurred:", e)

# File Appending (optional, keeping previous content intact)
# No need to modify the appending part if you want to keep the previous content

# Error Handling (unchanged)
try:
    # Attempting to open a non-existent file to trigger FileNotFoundError
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file 'non_existent_file.txt' was not found.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Error handling completed.")
