#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2019
# Modified by: Layla Michel
# Modified on: May 7, 2021
# This program calculates total from subtotal and tax


# imports constant for HST
import constants


def main():
    # this function calculates total from subtotal and tax

    # asks the user for the subtotal
    sub_total = float(input("Enter the subtotal: $"))

    # calculates the tax and total
    tax = sub_total * constants.HST
    total = sub_total + tax

    # displays the tax and total price
    print("")
    print("The HST is ${0:,.2f}, and the total cost is: ${1:,.2f}\
". format(tax, total))


if __name__ == "__main__":
    main()
