import unittest
import logging
import traceback
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.WARNING,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s,%(msecs)03d | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class RunnerTest(unittest.TestCase):
    def test_run(self):
        try:
            r2 = Runner(2)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            print(f"Traceback (most recent call last):")
            tb = traceback.extract_tb(e.__traceback__)
            print(f'  File "{tb[-2].filename}", line {tb[-2].lineno}, in {tb[-2].name}')
            print(f'    {tb[-2].line}')
            print('    ' + '^' * len(tb[-2].line.lstrip()))
            print(f'  File "{tb[-1].filename}", line {tb[-1].lineno}, in {tb[-1].name}')
            print(f'    {tb[-1].line}')
            print(f"TypeError: {str(e)}")

    def test_walk(self):
        try:
            r1 = Runner('Вася', -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            print(f"Traceback (most recent call last):")
            tb = traceback.extract_tb(e.__traceback__)
            print(f'  File "{tb[-2].filename}", line {tb[-2].lineno}, in {tb[-2].name}')
            print(f'    {tb[-2].line}')
            print('    ' + '^' * len(tb[-2].line.lstrip()))
            print(f'  File "{tb[-1].filename}", line {tb[-1].lineno}, in {tb[-1].name}')
            print(f'    {tb[-1].line}')
            print(f"ValueError: {str(e)}")

if __name__ == '__main__':
    unittest.main()

