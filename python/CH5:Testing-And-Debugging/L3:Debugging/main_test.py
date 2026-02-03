from main import take_magic_damage

run_cases = [
    (100, 5, 2, 20, 65),
    (200, 10, 1, 25, 185),
    (0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1),
    (100, 2, 3, 1, 99),
    (2500, 3, 2, 2, 2499),
]


def test(input1, input2, input3, input4, expected):
    print("-----------------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = take_magic_damage(input1, input2, input3, input4)
    print(f"Expected: {expected}")
    print(f"Actual: {result}")
    if result == expected:
        print("Passed")
        return True
    else:
        print("Failed")
        return False


def main():
    passed = 0
    failed = 0
    for case in run_cases:
        correct = test(case[0], case[1], case[2], case[3], case[4])
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("========= PASS ==========")
    else:
        print("========= FAIL ==========")


main()
