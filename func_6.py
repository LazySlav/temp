def func(x, y): return (1) if (x**2+y**2 < 1) and (((y**2 < x**2)
                                                    and (abs(x)+abs(y) < 1)) or ((y**2 > x**2) and (abs(x)+abs(y) > 1))) else 0


print(func(float(input()), float(input())))
