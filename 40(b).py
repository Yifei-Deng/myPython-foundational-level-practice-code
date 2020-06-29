'''

python开发基础40-形参和实参的值传递和引用传递

'''

# Call by Reference
# If you pass mutable arguments like dictionaries, sets or lists to a function, the function gets an implicit reference to the argument, rather than a copy of its value. As a consequence, the function can modify the argument, i.e. the value of the variable in the caller's scope can be changed.

def change_it(l):
    l.append(4)
    print(l)

alist = [1,2,3]
change_it(alist)
print(alist)


'''
Outputs:

[1, 2, 3, 4]
[1, 2, 3, 4]

'''


