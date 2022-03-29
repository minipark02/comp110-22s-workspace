"""Dictionary related utility functions."""

__author__ = "730388033"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a column based table with n number of rows of data shown."""
    result: dict[str, list[str]] = {}
    for columns in data:
        i: int = 0
        values: list[str] = []
        while i < rows:
            values.append(data[columns][i])
            i += 1
        result[columns] = values
    return result


def select(data: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce column based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = data[name]
    return result


def concat(data_1: dict[str, list[str]], data_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column based table made of two column based tables combined."""
    result: dict[str, list[str]] = {}
    for column in data_1:
        result[column] = data_1[column]
    for column in data_2:
        if column in result:
            result[column] += data_2[column]
        else:
            result[column] = data_2[column]
    return result


def count(data: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in the input list."""
    result: dict[str, int] = {}
    for item in data:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def average(data: dict[str, int]) -> float:
    result: float = 0.0
    for key in data:
        result += data[key]
    result /= len(data)

    return result