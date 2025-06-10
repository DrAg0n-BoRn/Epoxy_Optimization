from helpers.function_map import function_map
from paths import make_directories, RAW_DATA_CSV, PREPROCESSED_DATA_CSV
import polars as pl
import os


def preprocess_data() -> None:
    """
    Preprocesses the data by applying functions from function_map
    """
    # If the data CSV file does not exist, raise IO error
    if not os.path.exists(RAW_DATA_CSV):
        raise IOError(f"Data file '{RAW_DATA_CSV}' does not exist.")
    
    # Read the data CSV file into a DataFrame
    df = pl.read_csv(RAW_DATA_CSV, infer_schema=False)
    
    # Check that column names match to function map
    for feature_name in df.columns:
        if feature_name not in function_map.keys():
            raise ValueError(f"Feature '{feature_name}' not found in function map.")
    
    # Apply the functions to the columns
    results = []
    for feature_name, function in function_map.items():
        if function is not None and callable(function):
            output = function(df[feature_name])
            # Check if the output is a Series or DataFrame
            if isinstance(output, pl.Series):
                results.append(output)
            elif isinstance(output, pl.DataFrame):
                results.extend(output.get_columns())
            else:
                raise ValueError(f"Function for '{feature_name}' did not return a Series or DataFrame.")
    
    # Special case
    # results.extend(parse_special_case(df).get_columns())
    
    if results:
        # Make a new DataFrame from the results
        results_df = pl.DataFrame(results)
        # save the results to a new CSV file
        results_df.write_csv(PREPROCESSED_DATA_CSV)
        print(f"Preprocessed data saved to '{PREPROCESSED_DATA_CSV}'")
    else:
        raise ValueError("No results. Check the function map and data.")


if __name__ == "__main__":
    make_directories()
    preprocess_data()
    