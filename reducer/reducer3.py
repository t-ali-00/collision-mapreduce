import sys

def reducer_average_killed():
    # Initialize variables to keep track of the current borough, total killed, total injured, and count
    (last_key, total_killed, total_injured, count) = (None, 0, 0, 0)
    
    # Read input from sys.stdin
    for line in sys.stdin:
        # Split the input line into borough, killed, and injured
        (key, num_killed, num_injured) = line.strip().split("\t")
        
        # If the borough changes or it's the first line
        if last_key != key:
            # If it's not the first line, print the average for the previous borough
            if last_key:
                avg_killed = total_killed / float(count) if count > 0 else 0  # Ensure floating-point division and handle division by zero
                avg_injured = total_injured / float(count) if count > 0 else 0  # Ensure floating-point division and handle division by zero
                print("%s\t%.2f\t%.2f" % (last_key, avg_killed, avg_injured))
            
            # Reset variables for the new borough
            (last_key, total_killed, total_injured, count) = (key, int(num_killed), int(num_injured), 1)
        else:
            # Aggregate the killed and injured counts for the current borough
            total_killed += int(num_killed)
            total_injured += int(num_injured)
            count += 1
    
    # Print the average for the last borough encountered
    if last_key:
        avg_killed = total_killed / float(count) if count > 0 else 0  # Ensure floating-point division and handle division by zero
        avg_injured = total_injured / float(count) if count > 0 else 0  # Ensure floating-point division and handle division by zero
        print("%s\t%.2f\t%.2f" % (last_key, avg_killed, avg_injured))

# Call the reducer function to execute the logic
reducer_average_killed()
