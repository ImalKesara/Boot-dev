from main import update_player_score

run_cases = [
    (0, 100, 100),
    (100, 200, 300),
]

submit_cases = run_cases + [
    (300, 300, 600),
    (600, 50, 650),
    (0, 0, 0),
    (1, 1, 2),
    (100, -50, 50),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = update_player_score(input1, input2)
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
    for test_case in submit_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")


main()
