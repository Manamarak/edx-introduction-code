def is_prime(num):
    """
    Function to check if a number is prime
    Returns True if prime, False otherwise
    """
    # Handle edge cases
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check for odd divisors from 3 to sqrt(num)
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    
    return True


def main():
    """
    Main function to get user input and check if the number is prime
    """
    try:
        num = int(input("Enter a number to check if it's prime: "))
        
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
            
    except ValueError:
        print("Please enter a valid integer.")


# Run the program
if __name__ == "__main__":
    main()