from math import pi 

def convertDegsToRads(deg):
    rad = deg * pi / 180, 2
    return rad

userDegs = int(input("Ingrese los grados a convertir"))
userRads = convertDegsToRads(userDegs)
print(f"Los {userDegs}° equivalen a {userRads}rad")
