b_yx = 4/5
b_xy = 9/20
r = (b_yx * b_xy) ** (0.5)
sd_y = b_yx * (3.0 / r)
var_y = sd_y ** 2
print(round(var_y, 1))
