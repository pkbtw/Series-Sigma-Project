import math


bottom_sigma_value = input("What is your first sigma value? ")
top_sigma_value = input("What is your top sigma value? ")
arith_or_geo = input("Is your series an arithmetic or geometric series? ")
t1 = input("what is t1, or your starting value? ")
t1 = float(t1)
arith_series = 3
sigma_total = 0
if arith_or_geo == "arithmetic":
    arith_series = 1
if arith_or_geo == "geometric":
    arith_series = 2
if arith_series == 1:
    difference_value = input("What is your difference value? ")
    difference_value = float(difference_value)
    sigma_total = sigma_total
    bottom_sigma_value = int(bottom_sigma_value)
    top_sigma_value = int(top_sigma_value)
    sigma_array = []
    for i in range((bottom_sigma_value), (top_sigma_value + 1)):
        sigma_array.append(i)
    for k in sigma_array:
        sigma_adder = (difference_value * (k - 1))
        sigma_total = sigma_adder + sigma_total
        sigma_arith_t1_total = t1 * k
    sigma_total = sigma_total + sigma_arith_t1_total

    print(sigma_total)
if arith_series == 2:
    r_value = input("What is your R value, or the multiplier each time? ")
    r_value = float(r_value)
    sigma_total = sigma_total
    bottom_sigma_value = int(bottom_sigma_value)
    top_sigma_value = int(top_sigma_value)
    sigma_array = []
    for i in range((bottom_sigma_value), (top_sigma_value + 1)):
        sigma_array.append(i)
    for k in sigma_array:
        sigma_total = (t1) * ((1.0-(r_value)**k)/(1.0-r_value))
    print(sigma_total)
