from datetime import datetime as dt
from pathlib import Path
import random
import re
from typing import List, Tuple
import unittest

from trainings.PrefixSums.CountDiv.solution import solution


class TestingSolution(unittest.TestCase):
    def setUp(self) -> None:
        with open(
            Path(__file__).parent.absolute() / "test-input.txt", "r", encoding="utf-8"
        ) as f:
            test_inputs: List[str] = f.readlines()

        self._validity_test_cases: List[Tuple[int, ...]] = []
        for test_input in test_inputs:
            test_input = test_input.strip().replace(" ", "")
            if test_input.startswith("#"):
                print(f"Input line '{test_input}' is commented out.")
                continue
            re_match = re.match(r"^\((.+)\)$", test_input)
            if re_match is None:
                print(f"No Regex match found for input line '{test_input}'")
                continue
            input_regex = re_match.groups()[0]
            self._validity_test_cases.append((tuple(map(int, input_regex.split(",")))))

        self._efficiency_test_cases: List[Tuple[int, int, int]] = []
        k_min = 1
        k_max = int(2e9)
        k_equivalence_classes = [k_min, random.randint(k_min, k_max - 1), k_max]
        a_b_min = 0
        a_b_max = int(2e9)
        a_b_equivalence_classes = [
            a_b_min,
            random.randint(a_b_min, a_b_max - 1),
            a_b_max,
        ]

        self._validity_test_cases.append((a_b_min, a_b_max, k_min, k_max + 1))
        # self._validity_test_cases.append((1, 1, 1, 1))
        self._validity_test_cases.append((1, a_b_max, 1, k_max))

        for k in k_equivalence_classes:
            for a in a_b_equivalence_classes:
                for b in a_b_equivalence_classes:
                    self._efficiency_test_cases.append((a, b, k))

        return super().setUp()

    def test_solution_validity(self):
        for A, B, K, result in self._validity_test_cases:
            print((A, B, K, result))
            self.assertEqual(solution(A, B, K), result)

    def test_solution_efficiency(self):
        for A, B, K in self._efficiency_test_cases:
            # print(f"N = {test_case[}")
            # print(f"Size A = {len(test_case)}")
            start_test = dt.now()
            solution(A, B, K)
            execution_time_s = (dt.now() - start_test).total_seconds()
            # print(f"Execution time = {execution_time}")
            self.assertLess(execution_time_s, 0.03)
