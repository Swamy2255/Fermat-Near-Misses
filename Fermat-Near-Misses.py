import math

def find_near_miss(n, k):
    """
    Finds the smallest relative difference between (x^n + y^n) and z^n for given values of n and k.

    Args:
        n (int): The exponent value, where 3 <= n < 12.
        k (int): The upper limit for the values of x and y, where k > 10.

    Returns:
        tuple: The smallest relative difference, along with the best values of x, y, and z.
    """
    # Initialize the smallest relative difference with infinity
    smallest_diff = float('inf')
    # Variables to hold the best values of x, y, and z
    best_x, best_y, best_z = None, None, None

    # Iterate through all possible values of x and y within the specified range
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Calculate the sum of x^n and y^n
            xn_plus_yn = x ** n + y ** n

            # Find the nearest integer z such that z^n is just greater than or equal to x^n + y^n
            z = 10
            while z ** n < xn_plus_yn:
                z += 1

            # Calculate z^n and (z+1)^n to bracket xn_plus_yn
            zn = z ** n
            z_plus_1_n = (z + 1) ** n

            # Calculate the differences between xn_plus_yn and the closest powers of z
            diff1 = abs(xn_plus_yn - zn)
            diff2 = abs(z_plus_1_n - xn_plus_yn)

            # Find the smallest relative difference between xn_plus_yn and the two bracketing values
            relative_diff = min(diff1 / xn_plus_yn, diff2 / xn_plus_yn)

            # Update the smallest relative difference if the current one is smaller
            if relative_diff < smallest_diff:
                smallest_diff = relative_diff
                best_x, best_y, best_z = x, y, z

    # Return the smallest relative difference and the best values of x, y, and z
    return smallest_diff, best_x, best_y, best_z

if __name__ == "__main__":
    # Get user input for the exponent n and the upper limit k
    n = int(input("Enter the exponent n (between 3 and 11): "))
    k = int(input("Enter the upper limit k (greater than 10): "))

    # Find the smallest near miss for the given n and k
    smallest_diff, x, y, z = find_near_miss(n, k)

    # Print the results
    print("Smallest relative difference:", smallest_diff)
    print(f"Best values found: x = {x}, y = {y}, z = {z}")
