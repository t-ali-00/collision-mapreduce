import sys
import io

def process_input_mapper_motorcycle_accidents(line):
    """
    Process a single line of text: split the line by comma and extract borough, num_killed, and num_injured
    """
    val = line.strip()
    values = val.split(',')
    if len(values) >= 11:  # Ensure there are at least 11 elements
        borough = values[1].strip()  # Index 2 for borough
        num_killed = values[11].strip()  # Index 9 for num_killed
        num_injured = values[10].strip()  # Index 10 for num_injured
        return borough, num_killed, num_injured
    else:
        return None, None, None  # Return None values if line doesn't have enough elements

def main():
    # Read from standard input with specified encoding
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
    for line in input_stream:
        # map borough, num_killed, num_injured
        borough, num_killed, num_injured = process_input_mapper_motorcycle_accidents(line)
        if borough is not None:  # Check if values are extracted successfully
            # Print the mapped values
            print(f"{borough}\t{num_killed}\t{num_injured}")
        else:
            # Print a message for improperly formatted lines
            print("Error: Improperly formatted line")

if __name__ == '__main__':
    main()
