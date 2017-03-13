def function(n, s):
    numbers = range(0, n, s)
    for i in numbers:
        print ("N_%d :" %i),i
    print numbers


n = int(raw_input("input max range:"))
s = int(raw_input("input step:"))
function(n, s)


def function_2(n, s):
    i = 0
    numbers = []

    while i <= n:
        print ("item : %d" % i)
        i = i + s
        numbers.append(i)


n = int(raw_input("input max range:"))
s = int(raw_input("input step:"))

function_2(n, s)
