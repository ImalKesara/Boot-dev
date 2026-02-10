def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = False
    is_alphonse_edward_same = False
    is_winry_alphonse_same = False
    if edward_height == mustang_height:
        is_mustang_edward_same = True
    if alphonse_height == edward_height:
        is_alphonse_edward_same = True
    if winry_height == alphonse_height:
        is_winry_alphonse_same = True

    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same


# we can compare tuple too
print((2, 3, 1) == (2, 3, 1))
