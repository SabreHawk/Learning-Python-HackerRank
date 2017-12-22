from Points import Points
import math

A = Points(*map(float, input().strip().split()))
B = Points(*map(float, input().strip().split()))
C = Points(*map(float, input().strip().split()))
D = Points(*map(float, input().strip().split()))
AB = B - A
BC = C - B
CD = D - C
X = AB.cross(BC)
Y = BC.cross(CD)
print ("%.2f"%degrees(acos(X.dot(Y)/X.mod()/Y.mod())))