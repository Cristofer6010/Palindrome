lis = []
try:
    print("\n\t\t\t\t\tTHIS PALINDROME FUNCTION IS ONLY FOR NUMBERS\n")
    manyTimes = int(input("How many Palindrome you want to test : "))
    for i in range(1,manyTimes+1):
        a = int(input(f"\nEnter the {i} number whose palindrome you want to test : "))

        def is_palindrome(a):
            if str(a) == str(a)[::-1]:
                print(f"Your number {a} is also a palindrome\n")

        def next_palindrome(b):
            while b is not is_palindrome(b):
                lis.append(b)
                int(b)
                b = b + 1
                if str(b) == str(b)[::-1]:
                    print(f'You given number palindrome is {b}\n')
                    break

        if str(a) == str(a)[::-1]:
            is_palindrome(a)
        else:
            next_palindrome(a)

except Exception as e:
    print(e)
    print("\n\t\t\t\t\tTry again ")
