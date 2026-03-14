import math
from datetime import datetime
import time
import random
import string
import uuid
import file_operations

print("="*25)
print("Welcome to multi-utility toolkit")
print("="*25)

while True:
    print("\nChoose an option:")
    print("1. Datetime and time operations")
    print("2. Mathematical operations")
    print("3. Random data generation")
    print("4. Generate unique identifiers (UUID)")
    print("5. File operations (Custom module)")
    print("6. Explore module attributes (dir())")
    print("7. Exit")
    print("="*25)

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("\nDatetime and time operations:")
            print("1. Display current date and time")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown timer")
            print("6. Back to main menu")

            sub_choice = int(input("Enter your choice:"))

            if sub_choice == 1:
                dt = datetime.now()
                print("\nCurrent date and time: ",
                      dt.strftime("%Y-%m-%d %H:%M:%S"))

            elif sub_choice == 2:
                date1 = input("\nEnter the first date (YYYY-MM-DD): ")
                date2 = input("Enter the second date (YYYY-MM-DD): ")
                d1 = datetime.strptime(date1, "%Y-%m-%d")
                d2 = datetime.strptime(date2, "%Y-%m-%d")
                difference = d2 - d1
                print(f"Difference: {difference.days} days")

            elif sub_choice == 3:
                print("\nFormatted date:",
                      datetime.now().strftime("%A, %B %D, %Y"))
                print("="*25)

            elif sub_choice == 4:
                print("\nStopwatch started. Press ctrl+c to stop.")
                start_time = time.time()
                try:
                    while True:
                        elapsed = round(time.time() - start_time, 2)
                        print(f"\rElapsed time: {elapsed}s", end="")
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print("\nStopwatch stopped.")

            elif sub_choice == 5:
                sec = int(input("Enter seconds for countdown: "))
                for i in range(sec, -1, -1):
                    print(f"\rTimer:{i}s", end="")
                    time.sleep(1)
                print("\n Time's up!")

            elif sub_choice == 6:
                print("\nReturning to main menu")
                break

            else:
                print("Invalid choice")

        case 2:
            print("Mathematical operations: ")
            print("1. Calculate factorial")
            print("2. Solve compound interest")
            print("3. Trigonometric calculations")
            print("4. Area of geometric shapes")
            print("5. Back to main menu")

            sub_math = int(input("Enter your choice:"))

            if sub_math == 1:
                n = int(input("Enter a number: "))
                print(f"Factorial: {math.factorial(n)}")

            elif sub_math == 2:
                p = float(input("Enter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))

                amount = p*(pow((1+r/100), t))
                print(f"Compound interest: {amount}")

            elif sub_math == 3:
                degr = float(input("Enter angle in degree:"))
                rad = math.radians(degr)
                print(f"Sine: {math.sin(rad)}")
                print(f"Cosine: {math.cos(rad)}")

            elif sub_math == 4:
                radius = float(input("Enter radius of the circle: "))
                area = math.pi * (radius ** 2)
                print(f"Area of circle: {area}")

            elif sub_math == 5:
                print("\nBack to main menu")
                break

            else:
                print("Invalid choice")

        case 3:
            print("Random data generation:")
            print("1. Generate random number")
            print("2. Generate random list ")
            print("3. Create random password")
            print("4. Generate random otp")
            print("5. Back to main menu")

            random_choice = int(input("Enter your choice:"))

            if random_choice == 1:
                num = random.randint(1, 100)
                print("Generated random number is:", num)

            elif random_choice == 2:
                random_list = [random.randint(1, 100) for i in range(5)]
                print("Generated random list:", random_list)

            elif random_choice == 3:
                length = int(input("Enter password length:"))
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters)
                                   for i in range(length))
                print("Generated password:", password)

            elif random_choice == 4:
                otp = random.randint(1000, 9999)
                print("Random otp is:", otp)

            elif random_choice == 5:
                print("Back to main menu")
                break

            else:
                print("Invalid choice")

        case 4:
            print("1. Generate a random UUID:")
            print("2. Generate multiple UUID")
            print("3. Back to main menu")

            your_choice = int(input("Enter your choice: "))

            if your_choice == 1:
                generate = uuid.uuid4()
                print("Random UUID is:", generate)

            elif your_choice == 2:
                n = int(input("How many UUID's you want to generate:"))
                for i in range(n):
                    print(uuid.uuid4())

            elif your_choice == 3:
                print("Returning to main menu")
                break

            else:
                print("Invalid choice")

        case 5:
            print("File Operations: ")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to main menu")

            f_choice = int(input("Enter your choice:"))

            if f_choice == 1:
                filename = input("Enter file name:")
                file_operations.create_file(filename)

            elif f_choice == 2:
                filename = input("Enter file name:")
                data = input("Enter data:")
                file_operations.write_file(filename, data)

            elif f_choice == 3:
                filename = input("Enter file name:")
                file_operations.read_file(filename)

            elif f_choice == 4:
                filename = input("Enter file name:")
                data = input("Enter data:")
                file_operations.append_file(filename, data)

            elif your_choice == 5:
                print("Back to main menu")
                break

            else:
                print("Invalid choice")

        case 6:
            print("Explore module attributes:")

            module_name = input("Enter module name to explore: ")
            module = __import__(module_name)
            print(dir(module))

        case 7:
            print("="*25)
            print("Thank you for using the multi-utility toolkit!")
            print("="*25)
