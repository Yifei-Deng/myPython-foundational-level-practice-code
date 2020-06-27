'''

python开发基础35-for&while循环结构

'''
print("当使用break或continue时，只能作用于当前循环。如果当前循环还有父循环时，则无法从父循环中break或continue:")

for i in range(5):
    for n in range(5):
        if n == 3:
            break
        print("在内循环：n = %d,在外循环：i = %d" % (n,i))

print("\n如何通过使用FLAG,同时在父循环中break或continue:")
end = False
for a in range(5):
    for b in range(5):
        if b == 3:
            end = True
            break
        print("在内循环：b = %d,在外循环：a = %d" % (b,a))
    if end:
        break





'''
Outputs:

当使用break或continue时，只能作用于当前循环。如果当前循环还有父循环时，则无法从父循环中break或continue:
在内循环：n = 0,在外循环：i = 0
在内循环：n = 1,在外循环：i = 0
在内循环：n = 2,在外循环：i = 0
在内循环：n = 0,在外循环：i = 1
在内循环：n = 1,在外循环：i = 1
在内循环：n = 2,在外循环：i = 1
在内循环：n = 0,在外循环：i = 2
在内循环：n = 1,在外循环：i = 2
在内循环：n = 2,在外循环：i = 2
在内循环：n = 0,在外循环：i = 3
在内循环：n = 1,在外循环：i = 3
在内循环：n = 2,在外循环：i = 3
在内循环：n = 0,在外循环：i = 4
在内循环：n = 1,在外循环：i = 4
在内循环：n = 2,在外循环：i = 4

如何通过使用FLAG,同时在父循环中break或continue:
在内循环：b = 0,在外循环：a = 0
在内循环：b = 1,在外循环：a = 0
在内循环：b = 2,在外循环：a = 0

'''




