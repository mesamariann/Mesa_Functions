print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Mariann S. Mesa")
def smallest_factor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def generate_prime(start, end):
    prime = []
    num = max(2, start)

    while num <= end:
        is_prime = True
        i = 2
        while i <= int(num**0.5):
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            prime.append(num)
        num += 1

    return prime

def result_prime():
    while True:
        print("Select an option you want to perform: ")
        print("(1) Find the smallest factor of n")
        print("(2) Find prime numbers in range")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Program terminated.")
            return
        elif choice == 1:
            n = int(input("Enter a number: "))
            print(f"The smallest factor of {n} is {smallest_factor(n)}")
        elif choice == 2:
            start = int(input("Enter a number [start]: "))
            end = int(input("Enter a number [end]: "))
            if start < 0 or end <= start:
                print("Invalid input. Please try again.")
                continue
            prime_numbers = generate_prime(start, end)
            print(f"Prime numbers between {start} and {end}: {prime_numbers}")
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    result_prime()
