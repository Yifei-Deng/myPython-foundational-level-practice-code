'''

python开发基础40-形参和实参的值传递和引用传递

'''

# Call-by-Value
# If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like call-by-value. The object reference is passed to the function parameters. They can't be changed within the function, because they can't be changed at all, i.e. they are immutable.

def change_it(s):
    s = s + ' end'
    print(s)

astr = 'Test'
change_it(astr)
print(astr)


'''
Outputs:

Test end
Test

'''




