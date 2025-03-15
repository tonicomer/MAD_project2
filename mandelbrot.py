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
    final = np.zeros((len(imaginary),len(real)))
    final = final + real
    imaginary = imaginary.reshape(len(imaginary),1)
    final = final + imaginary
    return final

#print(get_complex_grid(-1+1j, 1.1-1.1j, 1))


def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
    #function takes in a array of c values and the number of iterations needed it creates an array of zeros with same shape
    #while also create an array of ones except that is multiplied with max iterations + 1 we loop in range max iterations to find 
    #the escape value for each value in the array but we use numpy logical operators to stop us from going over indicies we have
    #already calculated the escape value of. IF the escape value has an absolute value greater than 2 it is added to our new escaped array 
    #if not that spot stays zero representing the color black. At the end a formula is run on the whole array to refine the numbers
    z = np.zeros_like(c_arr)
    final_escape_time = np.ones_like(c_arr, dtype=float) * (max_iterations + 1)
    total_escaped = np.zeros_like(c_arr, dtype=bool)
    for count in range(max_iterations):
        not_escaped = np.logical_not(total_escaped)
        z[not_escaped] = (z[not_escaped] **2)  + c_arr[not_escaped]
        cur_escaped = np.abs(z) > 2
        new_escaped = np.logical_not(total_escaped) & cur_escaped
        total_escaped = new_escaped | cur_escaped
        final_escape_time[new_escaped] = count
    final_escape_time = (max_iterations - final_escape_time + 1) / (max_iterations + 1)
    return final_escape_time



def get_julia_color_arr(grid: np.ndarray, rabbit_c: complex, max_iterations: int)->np.ndarray:
    #Function is very similar to the one above except while in the loop it adds our inputted complex rabbit_C
    #as opposed to looking through a passed in array, also we are looping through the values of the inputted grid
    #and performing operations on them as opposed to performing the operations continually by squaring z and continuting.
    #After this we determine if the absolute value of z is greater than 2 and if so its index is taken and that spot is now equal
    #to the count or runtime escape. This is continuted through every spot that does not escape then we run a formula on the whole
    #array at the end to refine the numbers.
    z = grid
    final_escape_time = np.ones_like(grid, dtype=float) * (max_iterations + 1)
    total_escaped = np.zeros_like(grid, dtype=bool)
    for count in range(max_iterations):
        not_escaped = np.logical_not(total_escaped)
        z[not_escaped] = (z[not_escaped] **2)  + rabbit_c
        cur_escaped = np.abs(z) > 2
        new_escaped = np.logical_not(total_escaped) & cur_escaped
        total_escaped = new_escaped | cur_escaped
        final_escape_time[new_escaped] = count
    final_escape_time = (max_iterations - final_escape_time + 1) / (max_iterations + 1)
    return final_escape_time
