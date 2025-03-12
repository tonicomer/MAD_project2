import numpy as np
def get_escape_time(c: complex, max_iterations: max) -> int | None:
    z = 0   # z always starts at 0
    for count in range(max_iterations):  # Iterating through the maximum number of iterations we can, based on the max_iterations input
        z = z * z + c  # Updates z by going through the next part of the formula; squares the previous z and adds c.
        if abs(z)>2:  # If z now has a magnitude greater than 2, we can output the number of iterations we have gone through.
            return count
    return None   # The for loop will break if it is still going but is out of the range of max_iterations.
# If the for loop breaks, the function will return None.


def get_complex_grid(top_left: complex, bottom_right: complex,step: float) -> np.ndarray:
    #function takes in the top left value and the bottom right value of the complex grid and
    #when called it takes in the values it makes two arrays one with the real numbers and one
    #with the imaginary numbers with a step size equal to the inputted step. From here we intialize
    #a 3 by 3 array of zeros and we add the complex and imaginary numbers to the zeros to give us our
    #final value. Since complex values are added horizontally we have to reshape to (3,1) instead
    # of the aranged with (1,3) dimensions. They are added together and the final array is returnedl.
    real = np.arange(top_left.real, bottom_right.real,step)
    imaginary = np.arange(top_left.imag, bottom_right.imag,-step) * 1j
    final = np.zeros((len(real),len(real)))
    imaginary = imaginary.reshape(len(imaginary),1)
    final = final + real
    final = final + imaginary
    return final

def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
    z = np.zeros_like(c_arr)
    final_escape_time = np.zeros_like(c_arr)
    for count in range(max_iterations):
        z = z * z + c_arr
        esscaped = np.abs(z) > 2
        final_escape_time = z[esscaped]
    return final_escape_time
#boolean indexing
