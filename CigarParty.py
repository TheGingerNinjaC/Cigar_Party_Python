'''
Author: Chane van der Berg
Date: 13/05/2018

When squirrels get together for a party, they like to smoke cigars.
A squirrel party is successful when there were between 40 (inclusive)
and 60 (inclusive) cigars, unless it is weekend when there is no
upper limit on the number of cigars.

Write a function cigar_party() that determines whether the party was
successful or not. The function must receive as parameters an integer
value for the number of cigars as well as an integer value to indicate
a weekend. The function must then determine if it was a successful
party or not and return a true (1) or a false (0) value (true for
successful and false for unsuccessful) to the calling statement in the
main program.

Complete the Python program by asking the user to enter the number
of cigars and indicate whether it is weekend or not. After that, the
program must call the cigar_party() function with the values entered by
the user and display the result 

'''

def cigar_party(a,b):
    party = ''
    if b == 0:
        if a >= 40 and a <= 60:
            party = 1
        else:
            party = 0

    if b == 1:
        if a >= 40:
            party = 1
        else:
            party = 0

    if party == 1:
        return 'Yes! It was a successful cigar party!!!'
    elif party == 0:
        return 'No, it was a disappointing cigar party...'

cig = int(input("Enter the number of cigars: "))
day = int(input("Is it weekend? (1=True, 0=False) "))

print(cigar_party(cig,day))
