import unittest
import os
import numpy as np
from pythonLib.dataset_reader import read_dataset_pandas

class TestDatasetReader(unittest.TestCase):
    def setUp(self):
        """Create a sample CSV file before each test."""
        self.sample_data = "test.csv"
        data = {
            "name": ["Alice", "Bob"],
            "age": [25, 30]
        }
        # Creating CSV file
        df = pd.DataFrame(data)
        df.to_csv(self.sample_data, index=False)

    def tearDown(self):
        """Clean up by removing the sample file after each test."""
        if os.path.exists(self.sample_data):
            os.remove(self.sample_data)

    def test_read_dataset(self):
        """Test that the CSV file is read correctly into a NumPy array."""
        numpy_array = read_dataset_pandas(self.sample_data)
        
        # Expected NumPy array
        expected_data = np.array([["Alice", 25], ["Bob", 30]])

        # Compare NumPy arrays
        np.testing.assert_array_equal(numpy_array, expected_data)

if __name__ == "__main__":
    unittest.main()
