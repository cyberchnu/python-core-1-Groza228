def tri_area(base, height):
    area = (base * height) / 2
    return area


base = int(input("Enter base: "))
height = int(input("Enter height:"))
print(tri_area(base, height))
