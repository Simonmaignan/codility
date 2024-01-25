from pathlib import Path
from re import T
from typing import List, Tuple
import unittest

from trainings.CountingElements.PermCheck.solution import solution


class TestingSolution(unittest.TestCase):
    def setUp(self) -> None:
        with open(Path(__file__).parent.absolute() / 'test-input.txt', 'r') as f:
            test_inputs: List[str] = f.readlines()

        self._test_cases: List[Tuple[List[int], int]] = []
        for test_input in test_inputs:
            test_input = test_input.strip()
            translation_table = dict.fromkeys(map(ord, '[(),'), None)
            test_input = test_input.translate(translation_table)
            if test_input.startswith('#'):
                continue
            test_input = test_input.split(']')
            self._test_cases.append((
                [int(i) for i in test_input[0].split(' ')],
                int(test_input[1])
            ))
        return super().setUp()
    
    def test_solution(self):
        for test_case in self._test_cases:
            self.assertEqual(solution(test_case[0]), test_case[1])

