# Given a list of car plates
# Write a python function to sort the even and odd car plates
# and return 2 lists, as one even and one odd list

car_plate = [2341,4526,5643,4532,4826,9654,4364,3426,4331,5487]

def sort_oddeven(num):
    cp_even = []              #initialise a local empty even list
    cp_odd = []               #intiialise a local empty odd list
    for i in num:             # loop from first to last item in the list
        if i%2 == 0:          # for each item, perform a modulus of 2 and check if remainder is zero
           cp_even.append(i)  # if remainder is zero, number is even number, append item into even list
        else:                 # else item is odd number
           cp_odd.append(i)   # append item into odd list
    return cp_even,cp_odd     # return both even and odd list

car_even = []                 # initialise a new even list
car_odd = []                  # initialise a new odd list
car_even, car_odd = sort_oddeven(car_plate)  # call sort_oddeven function

# print the even and odd list
print("The list of car-plate with even numbers:")
print(car_even)
print("The list of car-plate with odd numbers:")
print(car_odd)
