from main import calculate_experience_points

run_cases = [
    (2, 5),
    (3, 15),
    (4, 30),
]

submit_cases = run_cases + [
    (1, 0),
    (5, 50),
    (7, 105),
    (10, 225),
    (15, 525),
    (20, 950),
]


def test(input1, expected_output):
    print("---------------------------------")
    result = calculate_experience_points(input1)
    print(f"Input:     {input1}")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")


test_cases = submit_cases


main()
