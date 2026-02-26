import unittest
from ex01_special_args import get_summary


class GetSummaryTests(unittest.TestCase):

    def test_get_summary_for_valid_inputs(self):
        summary = get_summary(10, 20, 30)
        self.assertTrue(isinstance(summary, dict))
        self.assertEqual(summary['count'], 3)
        self.assertEqual(summary['sum'], 60)
        self.assertEqual(summary['average'], 20)

    def test_get_summary_for_mixed_datatypes(self):
        summary = get_summary(10, 20, 'vinod', False, 30)
        self.assertTrue(isinstance(summary, dict))
        self.assertEqual(summary['count'], 3)
        self.assertEqual(summary['sum'], 60)
        self.assertEqual(summary['average'], 20)


# following helps if you are executing this script itself
if __name__ == '__main__':
    unittest.main()

# if the above is missing (unittest.main()), then
# run the following command in the CMD prompt:
# python -m unittest ex01_special_args_get_summary_tests.py