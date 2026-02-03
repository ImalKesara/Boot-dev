from main import max_players_on_server

run_cases = [(1.024e18), (1.024e19), (1.024e20)]


def test(expected1, expected2, expected3):
    print("---------------------------------")
    result = max_players_on_server()
    print(f"Expected: {(expected1, expected2, expected3)}")
    print(f"Actual:   {result}")
    if result == (expected1, expected2, expected3):
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in run_cases:
        correct = test(run_cases[0], run_cases[1], run_cases[2])
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")


main()
