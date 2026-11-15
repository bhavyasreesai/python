#lambda
#lambda argument:expression
add10=lambda x: x+10
print(add10(5))
#lambda functions also have multiple arguments
mult=lambda x,y:x*y
print(mult(2,7))

points2D=[(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted=sorted(points2D, key=lambda x:x[1])
print(points2D)
print(points2D_sorted)


points2D=[(1,2),(15,1),(5,-1),(10,4)]
def sort_by_y(x):
  return x[1]#sorts with y value
points2D_sorted=sorted(points2D, key=sort_by_y)
print(points2D)
print(points2D_sorted)

