def read_and_write_file():
    try:
        # Prompt user for input file name
        input_file = input("Enter the name of the file to read from: ")
        
        # Attempt to open the file for reading
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify content (Example: Adding line numbers to each line)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
        
        # Prompt user for output file name
        output_file = input("Enter the name of the file to write to: ")
        
        # Write modified content to the output file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"Modified content successfully written to '{output_file}'.")
    
    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist. Please check the file name.")
    except PermissionError:
        print("Error: Permission denied. You may not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()