import re

def multiply_numbers_in_file(input_filename, output_filename, multiplier):
    """
    Reads a file, multiplies all numerical values by a given factor,
    and writes the updated content to a new file.
    """
    try:
        # Read the entire content of the input file
        with open(input_filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
        return

    # A regular expression to find integers and decimals
    # It finds sequences of digits, with an optional decimal point and digits after it
    # It also handles negative numbers
    number_pattern = re.compile(r'-?\d+\.?\d*')

    # Function to apply the multiplication to each found number
    def multiply_match(match):
        number_str = match.group(0)
        try:
            # Convert the matched string to a float, multiply it, and convert back to a string
            new_value = float(number_str) * multiplier
            return str(int(new_value))
        except (ValueError, TypeError):
            # If for some reason the conversion fails, return the original string
            return number_str

    # Use re.sub() to find all matches of the pattern and replace them
    # using the `multiply_match` function
    new_content = number_pattern.sub(multiply_match, content)

    # Write the modified content to the output file
    with open(output_filename, 'w') as file:
        file.write(new_content)
    
    print(f"Successfully multiplied numbers in '{input_filename}' by {multiplier}.")
    print(f"Result saved to '{output_filename}'.")

# --- Example Usage ---
# Define the file names and the multiplication factor
input_file = 'data.txt'
output_file = 'data_multiplied.txt'
factor = 1.77050838884

# Run the function
multiply_numbers_in_file(input_file, output_file, factor)