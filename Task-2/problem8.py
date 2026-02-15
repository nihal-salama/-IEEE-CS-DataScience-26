import math 

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

def vector(p1 , p2):
    p1p2 = []
    for i in range(3):
        p1p2.append(p2[i] - p1[i])
    return p1p2

def dot_product(X, Y):
    X_dot_Y = 0
    for i in range(3):
        X_dot_Y += X[i] * Y[i]
    return X_dot_Y

def cross_product(X,Y):
    X_cross_Y = [(X[1]*Y[2] - X[2]*Y[1]),(X[0]*Y[2] - X[2]*Y[0]),(X[0]*Y[1] - X[1]*Y[0])]
    return X_cross_Y

def magnitude(R):
    return math.sqrt(pow(R[0],2) + pow(R[1],2) + pow(R[2],2))

AB = vector(A,B)
BC = vector(B,C)
CD = vector(C,D)

X = cross_product(AB,BC)
Y = cross_product(BC,CD)

mag_x = magnitude(X)
mag_y = magnitude(Y)
if mag_x == 0 or mag_y == 0:
    print(0.00)

else :
    Cos_phi = (dot_product(X,Y)) / (mag_x * mag_y)
    Cos_phi = max(-1, min(1, Cos_phi))

    phi = math.degrees(math.acos(Cos_phi))
    print(f"{phi:.2f}")

