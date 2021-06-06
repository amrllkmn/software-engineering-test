import unittest
import seed
import solution


class TestSeed(unittest.TestCase):
    def test_seed_is_numeric(self):
        result = seed.result
        not_alpha = False
        for date in result:
            not_alpha = not date.isalpha()

        self.assertTrue(not_alpha)

    def test_output_is_sorted_by_length(self):
        input_timestamps = ['2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05',
                            '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05', '2021-03-18 15:13:05']
        sorted_timestamps = solution.sort_timestamps(input_timestamps)
        is_decreasing_length = all(
            sorted_timestamps[i][2] <= sorted_timestamps[i+1][2]for i in range(len(sorted_timestamps)-1))

        self.assertTrue(is_decreasing_length)

    def test_consecutive_length_should_be_one(self):
        input_timestamps = ['2021-03-13 00:00:00', '2021-03-13 23:59:59']
        sorted_timestamps = solution.sort_timestamps(input_timestamps)
        self.assertEqual(sorted_timestamps[0][2], 1)


if __name__ == '__main':
    unittest.main()
