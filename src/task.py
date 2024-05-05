def circle_area(r: int) -> int:
    PI = 3.14
    area = PI * r ** 2
    return area

def format_description(r, area):
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))

def get_info(r: float):
    area = circle_area(r)
    description = format_description(r, area)
    print(description)

radius = int(input("Enter circle radius (int): "))
get_info(radius)
