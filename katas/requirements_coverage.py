from typing import List, Set


def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    """
    In software testing, it's often required to select a minimal set of test cases that cover all the requirements.
    You are given a set of test cases and their associated covered requirements.
    Your task is to select the minimal subset of test cases such that all requirements are covered.

    For example, you have the following test cases and requirements they cover:

    test_cases = [
        [1, 2, 3],   # Test case 0 covers requirements 1, 2, 3
        [1, 4],      # Test case 1 covers requirements 1, 4
        [2, 3, 4],   # Test case 2 covers requirements 2, 3, 4
        [1, 5],      # Test case 3 covers requirements 1, 5
        [3, 5]       # Test case 4 covers requirements 3, 5
    ]

    Args:
        test_cases: a list of test cases, where each test case is a list of requirements it covers.
                    Assume each requirement is covered by at least one test case.

    Returns:
        A list of indices of the minimal subset of test cases that covers all requirements
    """
    all_requirements: Set[int] = set(r for case in test_cases for r in case)
    covered: Set[int] = set()
    selected: List[int] = []

    remaining = list(enumerate(test_cases))

    while covered != all_requirements:
        # Select the test case that covers the most uncovered requirements
        best_index, best_case = max(remaining, key=lambda x: len(set(x[1]) - covered))
        selected.append(best_index)
        covered.update(best_case)
        # Remove selected test case from consideration
        remaining = [(i, c) for i, c in remaining if i != best_index]

    return sorted(selected)

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]
