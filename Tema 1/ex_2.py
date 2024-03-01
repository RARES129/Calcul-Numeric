def ex1():
    p = 1
    while (1 + pow(10, -p)) != 1:
        p += 1
    p=p-1
    return pow(10, -p)

def main():
    u = ex1()
    x=1.0
    y=u/10
    z=u/10
    left = (x + y) + z
    right = x + (y + z)
    if left == right:
        print("left == right")
    else:
        print("left != right")

    x=0.1
    y=0.2
    z=0.3
    left = (x * y) * z
    right = x * (y * z)
    if left == right:
        print("left == right")
    else:
        print("left != right")
    

main()
