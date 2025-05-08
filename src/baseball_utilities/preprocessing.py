__all__ = ["remove_columns", "remove_nan"]

def remove_columns(df, columns_to_keep):
    """
    Remove certain columns from a specific DataFrame.

    Parameters:
        df (pandas.DataFrame): A DataFrame containing data.
        columns_to_keep (list of string): List of strings of columns to keep from DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame with stripped columns
    """
    missing = [col for col in columns_to_keep if col not in df.columns]
    if missing:
        print(f"Warning: These columns were not found and will be ignored: {missing}")
        
    valid_columns = [col for col in columns_to_keep if col in df.columns]
    return df[valid_columns]

def remove_nan(df, na_columns):
    """
    Remove NA values from certain columns in a specific DataFrame.

    Parameters:
        df (pandas.DataFrame): A DataFrame containing the columns to remove.
        na_columns (list of string): List of strings of columns to remove NAs from in a given DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame with NAs stripped.
    
    """
    initial_rows = df.shape[0]
    
    df = df.dropna(subset=na_columns)
    
    final_rows = df.shape[0]
    dropped_rows = initial_rows - final_rows
    
    if dropped_rows > 0:
        print(f"{dropped_rows} rows were dropped due to missing values in columns: {na_columns}")
    else:
        print("No rows dropped.")

    return df
