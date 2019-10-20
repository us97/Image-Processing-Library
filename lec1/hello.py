import numpy
# Lab 1
# Question 1

# A Write python code using python indexing and slicing for the following output. Use only one print statement for each output.
x = [[1, 2, 3, 4, 5], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35]]
# a
a1 = x[1]
print(a1)
# b
a2 = x[0][2]
print(a2)
# c
a3 = x[2][1:3]
print(a3)
# d
a4 = x[0][0:5:2]
print(a4)
# B Declare y = [0, 0, 0], now using for loop write average of first list in list ‘x’ on first index of list y and so on. The print(y) should give the following output [3.0, 23.0, 33.0]
y = [0, 0, 0]
print("for loop start")
number = 0
for i in x:
    y[number] = sum(i[0:5:1])/5
    number = number + 1
print(y)
print("loop end ...")
# C Declare z = [0, 0, 0, 0, 0], now using for loop write average of each index of each list in ‘x’ on corresponding index of list y. The print(z) should give the following output [17.66, 18.66, 19.66, 20.66, 21.66]
print("for loop start")
z = [0, 0, 0, 0, 0]
for i in range(0, 5, 1):
    z[i] = (x[0][i] + x[1][i] + x[2][i])/3
print(z)
print("end loop ...")

# Question 2
x = [1, 3, 5, 6, 7, 8, 6, 1, 2, 3]
y = [0, 0, 0, 0, 0, 0, 0, 0]
# A Write python code using while loop that write average of first three items on first index of y and so on. The print(y) should give the following output [3.0, 4.666666666666667, 6.0, 7.0, 7.0, 5.0, 3.0, 2.0]
number = 0
while number < 8:
    y[number] = (x[number] + x[number + 1] + x[number + 2])/3
    number = number + 1
print(y)


# B Define a function that takes list as argument and returns the average of it. Then calculate the average of x and y.
def avg(li):
    return sum(li)/len(li)


print(avg(x))
print(avg(y))


# Home Task
# Write a code that takes two integers from user as input and store in x and y variables. Now generate
# a list (w) of x elements and each element contains y random integers ranging from 1 to 10 and
# display this list.

#  Now ask user to enter a number from 1 to 10 and display the number of times that
# integer occurs in the whole list (w).

#  Write a code that calculate mean, median and mode of the list (w).

#  Write a code that make another list (u) of same dimensions and compare each number
# of original list (w) with the average of it calculated in the previous part, if the number
# is less than the average, the code should place 0 on the corresponding index in newly
# created list (u) else it should place 10. Display the list (u).

x = int(input("enter input 1:  "), 10)
y = int(input("enter input 2:  "), 10)
print("The numbers you entered are.. ", x, " and ", y)
# generating array of random numbers
arr = [numpy.random.randint(0, 10, y)for i in range(x)]
print(arr)

check = int(input("Enter a number from 1 to 10 "), 10)
print("checking from the list... ")
count = 0
for i in range(x):
    count = count + numpy.sum(numpy.array(arr[i]) == check)
print(count)
#   mean is
mean = 0
for i in range(x):
    mean = mean + avg(arr[i])
mean = mean / x
print("Mean is ... ", mean)
#   median is
lis = []
for i in range(x):
    lis.extend(arr[i])
median = numpy.median(lis)
print("Median is ... ", median)
#   mode is
lis.sort()
print("Mode is ... ", lis[-1])

u = arr[:]
print(u)
for i in range(x):
    for j in range(y):
        if arr[i][j] < mean:
            u[i][j] = 0
        else:
            u[i][j] = 10
print(u)
print("END")
# import numpy $ pip3 install numpy
# source for changing input string to int: https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers
# source for counting number in list: https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
