class Prime:
    # This program takes a number given by
    # the user and tests to see if the number
    # is prime or not

    # main method
    def main():

        # prompt for a number to evaluate
        num = int(input("Enter a number to test if it is prime: "))

        # if num is prime display the message
        if (isPrime(num)):
            print (num , " is prime!")
        # otherwise say it isn't prime
        else:
            print (num , " is not prime!")

    # method that determines if the number is prime or not
    def isPrime(n):

        prime = True

        # check all the numbers that can possibly prove it isn't prime
        for i in range(2,n):

            # if a number divides it then it isn't prime
            if (n % i == 0):
                prime = False
                
        return prime

    main()
