def asoociative_law(a,b,c):
    #addd law
    add1=(a+b)+c
    add2=a+(b+c)
    assert add1== add2, f"additon law failed : ({a}+{b})+{c}={add1},{a}+({b}+{c})={add2}"


    mul1=(a*b)*c
    mul2=a*(b*c)
    assert mul1==mul2, f"multiplication law failed : ({a}*{b})*{c}={mul1},{a}+({b}*{c})={mul2}"
    return True
 


a,b,c=2,3,4
print(f"Associative law test for a={a},b={b},c={c}:{asoociative_law(a,b,c)}")


