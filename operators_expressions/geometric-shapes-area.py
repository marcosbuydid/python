import math

# rectangle
r_length = 4
r_width = 6
r_area = r_length * r_width
print('rectangle area is:', r_area)

# triangle
t_base = 8
t_height = 10
t_area = t_base * t_height / 2
print('triangle area is:', t_area)

# trapezium
tr_minor_base = 7
tr_major_base = 8
tr_height = 4
tr_area = (tr_minor_base + tr_major_base) * tr_height / 2
print('trapezium area is:', tr_area)

# circle
c_radius = 4
c_area = math.pi * c_radius * c_radius
print('circle area is:', c_area)

# cuboid
# a cuboid has 6 faces, 3 faces repeated twice (front,bottom,side)
cb_front_length = 8
cb_front_height = 2
cb_bottom_width = 4
cb_area = (2 * (cb_front_length * cb_front_height) +
           2 * (cb_front_length * cb_bottom_width) +
           2 * (cb_bottom_width * cb_front_height))
print('cuboid area is:', cb_area)
