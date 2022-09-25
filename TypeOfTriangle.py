def get_triangle_type(lst):

    return "not a triangle" if len(lst) > 3 or len(lst) <= 2 else "equilateral" if len(set(lst)) == 1 else "isosceles" if len(set(lst)) == 2 else "scalene"

a=get_triangle_type([4, 4, 7])
print(a)

# No sides equal: "scalene"
# Two sides equal: "isosceles"
# All sides equal: "equilateral"
# Less or more than 3 sides given: "not a triangle"