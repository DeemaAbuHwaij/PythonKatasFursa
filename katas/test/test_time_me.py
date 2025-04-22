import unittest
from katas.time_me import measure_execution_time
from katas.time_me import sample_function
from katas.time_me import quick_function



class MyTestCase(unittest.TestCase):
    def test_sample_function_timing(self):
        self.assertTrue(
            480 <= measure_execution_time(sample_function) <= 520,
            "Expected ~500ms for sample_function"
        )
    def test_quick_function_timing(self):
        self.assertTrue(
            measure_execution_time(quick_function) < 10,
            "Expected quick_function to be under 10ms"
        )



if __name__ == '__main__':
    unittest.main()


