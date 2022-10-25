"""Dictionary related utility functions."""

__author__ = "730320104"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Created a function that read an entire CSV of data into a list of rows."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Created a function that produces a list of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Created a function that transforms a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Created a function that produces a new column-based table with only the first 'N' rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        empty: list[str] = []
        i: int = 0
        if len(table[column]) < n:
            result[column] = table[column]
        else:
            while i < n:
                empty.append(table[column][i])
                i += 1
            result[column] = empty
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Created a function that produces a new column-based table with only a specfic subset of the original columns."""
    z: dict[str, list[str]] = {}
    for column in names:
        z[column] = table[column]
    return z


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Created a function that produces a new column-based table by combining two existing column-based tables."""
    result: dict[str, list[str]] = {}
    for column in dict_1:
        result[column] = dict_1[column]
    for column in dict_2:
        if column in result:
            for item in range(len(dict_2[column])):
                result[column].append(dict_2[column][item])
        else:
            result[column] = dict_2[column]
    return result


def count(x: list[str]) -> dict[str, int]:
    """Created a function that counts the number of times a value appears in an input list."""
    result: dict[str, int] = {}
    for item in x:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result