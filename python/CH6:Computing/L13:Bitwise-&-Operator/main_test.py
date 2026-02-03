from main import *

run_cases = [
    (get_create_bits, 0b1000, 0b1010, True),
    (get_review_bits, 0b0100, 0b1001, False),
    (get_delete_bits, 0b0010, 0b0110, True),
    (get_edit_bits, 0b0001, 0b1110, False),
]

submit_cases = run_cases + [
    (get_create_bits, 0b1000, 0b0111, False),
    (get_review_bits, 0b0100, 0b0110, True),
    (get_delete_bits, 0b0010, 0b1101, False),
    (get_edit_bits, 0b0001, 0b0011, True),
]


def test(func, perm_bit, user_permissions, expected_output):
    print("-----------------------------------------")
    print(f"Testing {func.__name__}")
    # 04b -> means tells python to format the variable user_permissions as a 4 digit binary number
    print(f"Inputs {user_permissions:04b}")
    print(f"Expected {expected_output}")
    # func(user_permission) === get_create_guild(user_permission)
    result = func(user_permissions) == perm_bit
    print(f"Acutal:   {result}")
    if result == expected_output:
        print("Test passed")
        return True
    print("Test failed")
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
        print("===============PASS==============")
    else:
        print("==============FAIL==============")


main()
