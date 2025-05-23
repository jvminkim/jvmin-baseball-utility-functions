from sqlalchemy import create_engine
import pandas as pd
__all__ = ["get_connection", "get_pbp_data", "get_description_data", "get_table", "get_swing_data"]

def get_connection():
    """
    Get connection to local PostgreSQL server.

    Returns:
        sqlalchemy.engine.base.Engine: SQLAlchemy engine connected to the local PostgreSQL server.
    """
    engine = create_engine(
        "postgresql+psycopg2://postgres:jamin@localhost:5432/statcast"
    )
    return engine

def upload_dataframe(df, table_name):
    """
    Upload DataFrame to local PostgreSQL server.

    Parameters:
        table_name (string): Name of the table in PostgreSQL server.
        df (pandas.DataFrame): DataFrame to upload.
    Returns:
        None
    """
    engine = get_connection()
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace'
    )
    

def query_year(year, where_clause=""):
    """
    Query Statcast data for a given year.

    Parameters:
        year (int): Year to query.
        where_clause (string, optional) : Additional SQL conditions to query
    Returns:
        pandas.DataFrame: A DataFrame containing the Statcast data for the specified year.

    Examples:
        >>> query_year(2024)
        DataFrame with rows from 2024
        >>> query_year(2024, "AND swing_length IS NOT NULL AND bat_speed IS NOT NULL")
        DataFrame with rows of batter swings from 2024
    """
    conn = get_connection()
    query = f"""
        SELECT * FROM statcast_all
        WHERE game_year = {year}
        {where_clause};
    """
    df = pd.read_sql(query, conn)
    print(f"{year}: {len(df)} rows")
    return df

def get_pbp_data(years): 
    """
    Query Statcast data for multiple years.

    Parameters: 
        years (list of int): Years to query.

    Returns:
        pandas.DataFrame: A DataFrame containing the Statcast data for the specified years.

    Examples:
        >>> get_pbp_data([2023, 2024])
        DataFrame with rows from both years combined
    """
    pbp_data_list = [query_year(year) for year in years]
    pbp_data = pd.concat(pbp_data_list, ignore_index = True)
    
    return pbp_data

def get_swing_data(years):
    """
    Query Statcast data for swings.

    Parameters:
        years (list of int): Years to query.

    Returns:
        pandas.DataFrame: A DataFrame containing the Statcast data of swings for the specified years.

    Examples:
        >>> get_swing_data([2023, 2024])
        DataFrame with rows of swings from 2023 and 2024
    """
    conn = get_connection()

    swing_data_list = [query_year(year,"AND swing_length IS NOT NULL AND bat_speed IS NOT NULL") for year in years]
    swing_data = pd.concat(swing_data_list, ignore_index=True)
    
    return swing_data

def get_description_data(year):
    """
    Query events from Statcast data.

    Parameters:
        year (int): Year to query.

    Returns:
        pandas.DataFrame: A DataFrame containing the Statcast data of events for a specified year.
    """
    conn = get_connection()
    query = f"""
            SELECT * FROM statcast_all
            WHERE events IS NOT NULL
            AND game_year = {year};
            """
    df = pd.read_sql(query,conn)
    return df

def get_table(table_name):
    """
    Query a specific table from the database.

    Parameters:
        table_name (string): Name of the table to query.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the specified table.

    Examples:
        >>> get_table("fangraphs_batting_min_400_2024")
        Query the batters who have minimum 400 plate appearances in 2024
    """
    conn = get_connection()
    query = f"""
        SELECT * FROM {table_name}
    """

    df = pd.read_sql(query, conn)

    return df



