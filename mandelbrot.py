def get_escape_time(c: complex, max_iterations: max) -> int | None:
    z = 0   # z always starts at 0
    for count in range(max_iterations):  # Iterating through the maximum number of iterations we can, based on the max_iterations input
        z = z * z + c  # Updates z by going through the next part of the formula; squares the previous z and adds c. 
        if abs(z)>2:  # If z now has a magnitude greater than 2, we can output the number of iterations we have gone through. 
            return count
    return None   # The for loop will break if it is still going but is out of the range of max_iterations.
# If the for loop breaks, the function will return None. 
