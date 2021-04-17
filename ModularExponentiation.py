#In pseudocode, this method can be performed the following way:

#function modular_pow(base, exponent, modulus) is
#    if modulus = 1 then
#        return 0
#    c := 1
#    for e_prime = 0 to exponent-1 do
#        c := (c * base) mod modulus
#    return c

#The following is an example in pseudocode based on Applied Cryptography by Bruce Schneier.[2]
# The inputs base, exponent, and modulus correspond to b, e, and m in the equations given above.

#function modular_pow(base, exponent, modulus) is
#    if modulus = 1 then
#        return 0
#    Assert :: (modulus - 1) * (modulus - 1) does not overflow base
#    result := 1
#    base := base mod modulus
#    while exponent > 0 do
#        if (exponent mod 2 == 1) then
#            result := (result * base) mod modulus
#        exponent := exponent >> 1
#        base := (base * base) mod modulus
#    return result


import math
def modPow(b, e, m):
  if m == 1 :
    return 0
  else:
    r = 1
    b = b % m
    while e > 0 :
        if (e % 2) == 1 :
            r = (r*b) % m
        e = math.floor(e / 2)
        b = (b**2) % m
    return(r)

print(modPow(2, 1234, 789))
