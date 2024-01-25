from pathlib import Path
import re
from typing import List, Tuple
import unittest

from trainings.CountingElements.MaxCounter.solution import solution


class TestingSolution(unittest.TestCase):
    def setUp(self) -> None:
        with open(Path(__file__).parent.absolute() / 'test-input.txt', 'r') as f:
            test_inputs: List[str] = f.readlines()

        self._test_cases: List[Tuple[int, List[int], List[int]]] = []
        for test_input in test_inputs:
            test_input = test_input.strip().replace(' ', '')
            if test_input.startswith('#'):
                continue
            re_match= re.match(r'^\((\d).*\[(.+)\].*\[(.+)\]\)$', test_input)
            if re_match is None:
                continue
            N_regex, A_regex, result_regex =re_match.groups()
            test_input = test_input.split(']')
            self._test_cases.append((int(N_regex),
                [int(i) for i in A_regex.split(',')],
                [int(i) for i in result_regex.split(',')]
            ))
        return super().setUp()
    
    def test_solution(self):
        for test_case in self._test_cases:
            print(test_case)
            self.assertEqual(solution(test_case[0], test_case[1]), test_case[2])

