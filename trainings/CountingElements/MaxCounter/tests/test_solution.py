from datetime import datetime as dt
from pathlib import Path
import random
import re
from tkinter import N
from typing import List, Tuple
import unittest

from trainings.CountingElements.MaxCounter.solution import solution


class TestingSolution(unittest.TestCase):
    def setUp(self) -> None:
        with open(Path(__file__).parent.absolute() / 'test-input.txt', 'r') as f:
            test_inputs: List[str] = f.readlines()

        self._validity_test_cases: List[Tuple[int, List[int], List[int]]] = []
        for test_input in test_inputs:
            test_input = test_input.strip().replace(' ', '')
            if test_input.startswith('#'):
                continue
            re_match= re.match(r'^\((\d).*\[(.+)\].*\[(.+)\]\)$', test_input)
            if re_match is None:
                continue
            N_regex, A_regex, result_regex =re_match.groups()
            test_input = test_input.split(']')
            self._validity_test_cases.append((int(N_regex),
                [int(i) for i in A_regex.split(',')],
                [int(i) for i in result_regex.split(',')]
            ))

        self._efficiency_test_cases: List[Tuple[int, List[int]]] = []
        N_min = 1
        N_max = 100000
        N_equivalence_classes = [N_min, random.randint(N_min, N_max - 1), N_max]
        M_min = 1
        M_max = 100000
        M_equivalence_classes = [M_min, random.randint(M_min, M_max - 1), M_max]
        for N in N_equivalence_classes:
            for M in M_equivalence_classes:
                A: List[int] = [random.randint(1, N + 1) for _ in range(M)]
                self._efficiency_test_cases.append((N, A))
        return super().setUp()
    
    def test_solution_validity(self):
        for test_case in self._validity_test_cases:
            print("Test")
            self.assertEqual(solution(test_case[0], test_case[1]), test_case[2])

    def test_solution_efficiency(self):
        for test_case in self._efficiency_test_cases:
            # print(f"N = {test_case[0]}")
            # print(f"Size A = {len(test_case[1])}")
            start_test = dt.now()
            solution(test_case[0], test_case[1])
            execution_time_s = (dt.now() - start_test).total_seconds()
            # print(f"Execution time = {execution_time}") 
            self.assertLess(execution_time_s, 0.464)