def calculate_experience_points(level):
    xp = 0
    i = 1
    while i < level:
        xp += i * 5
        i += 1
    return xp


xp = calculate_experience_points(2)
print(xp)
