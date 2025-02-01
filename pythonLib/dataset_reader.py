import pandas as pd

def read_dataset_pandas(filename):
    """Reads a CSV file into a Pandas DataFrame and converts it to a NumPy array."""
    df = pd.read_csv(filename)
    
    # Convert the DataFrame to a NumPy array
    numpy_array = df.to_numpy()
    
    return numpy_array
