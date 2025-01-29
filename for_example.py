# sum the first 10 numbers
sum = 0
for num in range (1,101): # 11 is excluded so it goes from 1 to 100
    sum = sum + num
print(sum)

# re-write using while loop (for case of 100)
sum = 0
num = 0
while num < 100:
    num = num + 1
    sum += num # same thing as sum = num + 1
print(sum)


# print multiplication table
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}") # f for string, it's the formatting. i = 1, j = 2, result i*j = 1*2 =  2
    print() # to separate with a new line between blocks

# 'for' is used when number of iterations is know. 'while' is for unknown number of iterations. 'for' can be re-written with a while statement.

