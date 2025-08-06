def read_and_modify_file():
    # Ask user for the input file name
    input_filename = input("Enter the name of the file to read from: ")

    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()

        # Define the output filename
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ File successfully modified and saved as '{output_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_filename}' not found.")
    except IOError:
        print(f"❌ Error: Could not read or write to the file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Run the program
read_and_modify_file()
