from datetime import datetime as dt
from pathlib import Path
import random
import re
from typing import List, Tuple
import unittest

from trainings.PrefixSums.PassingCars.solution import solution


class TestingSolution(unittest.TestCase):
    def setUp(self) -> None:
        with open(
            Path(__file__).parent.absolute() / "test-input.txt", "r", encoding="utf-8"
        ) as f:
            test_inputs: List[str] = f.readlines()

        self._validity_test_cases: List[Tuple[List[int], int]] = []
        for test_input in test_inputs:
            test_input = test_input.strip().replace(" ", "")
            if test_input.startswith("#"):
                print(f"Input line '{test_input}' is commented out.")
                continue
            re_match = re.match(r"^\(.*\[(.+)\].*(\d)\)$", test_input)
            if re_match is None:
                print(f"No Regex match found for input line '{test_input}'")
                continue
            a_regex, result_regex = re_match.groups()
            self._validity_test_cases.append(
                (
                    [int(re.sub("\u2212", "-", i)) for i in a_regex.split(",")],
                    int(result_regex),
                )
            )

        self._efficiency_test_cases: List[List[int]] = []
        n_min = 1
        n_max = 100000
        n_equivalence_classes = [n_min, random.randint(n_min, n_max - 1), n_max]

        a: List[int] = [i % 2 for i in range(n_max)]
        self._validity_test_cases.append((a, -1))

        for n in n_equivalence_classes:
            a: List[int] = [random.randint(0, 1) for _ in range(n)]
            self._efficiency_test_cases.append(a)
        return super().setUp()

    def test_solution_validity(self):
        for a, result in self._validity_test_cases:
            self.assertEqual(solution(a), result)

    def test_solution_efficiency(self):
        for test_case in self._efficiency_test_cases:
            # print(f"N = {test_case[}")
            # print(f"Size A = {len(test_case)}")
            start_test = dt.now()
            solution(test_case)
            execution_time_s = (dt.now() - start_test).total_seconds()
            # print(f"Execution time = {execution_time}")
            self.assertLess(execution_time_s, 0.03)
