def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    length = min(
        len(str(x)), 
        len(str(y))
    )

    middle = int(length / 2)

    xLeft = int(str(x)[0: len(str(x)) - middle])
    xRight = int(str(x)[len(str(x)) - middle: ])
    yLeft = int(str(y)[0: len(str(y)) - middle])
    yRight = int(str(y)[len(str(y)) - middle: ])

    z0 = karatsuba (xRight, yRight)
    z1 = karatsuba (xRight + xLeft, yRight + yLeft)
    z2 = karatsuba (xLeft, yLeft)

    #print(x, y, ' --- ', xLeft, xRight, yLeft, yRight, ' --- ', z0, z1, z2, middle)

    return (z2 * 10**(middle * 2)) + ((z1 - z2 - z0) * 10**middle) + z0

print(karatsuba(
    3141592653589793238462643383279502884197169399375105820974944592, 
    2718281828459045235360287471352662497757247093699959574966967627
    )
)
