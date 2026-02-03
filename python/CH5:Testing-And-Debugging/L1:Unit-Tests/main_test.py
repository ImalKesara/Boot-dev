from main import total_xp

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]


def test(input1, input2, expected):
    print("-------------------------------")
    print(f"Inputs {input1} , {input2}")
    print(f"Excepted {expected}")
    result = total_xp(input1, input2)
    print(f"Actual: {result}")
    if result == expected:
        print("test passed")
        return True
    print("Test failed")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in run_cases:
        #         this is equal to (*test_case)
        correct = test(test_case[0], test_case[1], test_case[2])
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("======== Pass =========")
    else:
        print("======== Fail =========")


main()
