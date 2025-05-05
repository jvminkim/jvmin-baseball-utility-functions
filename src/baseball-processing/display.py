__all__ = ["set_pandas_display_all", "reset_pandas_display_options"]

def set_pandas_display_all():
    """
    Set preferred pandas display options for better readability in outputs.
    """
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

def reset_pandas_display_options():
    """
    Reset pandas display options to their default values.
    """
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.max_colwidth')
    