def distributive_law(a,b,c):
    left=a*(b+c)
    right=(a*b)+(a*c)

    assert left==right,"error"
    return True


a,b,c=2,3,4

print(distributive_law(a,b,c))




