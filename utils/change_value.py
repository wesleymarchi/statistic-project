import pandas as pd


def remove_char(df, column):
    """
    Remove a char of a column

    :param df: The dataframe
    :param column: The name of the column
    :return: The dataframe
    """

    # Remover o caractere "º" da coluna especificada
    df[column] = df[column].str.replace('º', '', regex=False)

    return df


def change_value(df, column):
    """
    Remove a char of a column

    :param df: The dataframe
    :param column: The name of the column
    :return: The dataframe
    """

    # Remover o caractere "º" da coluna especificada
    df[column] = df[column].str.replace('Interfere muito positivamente', 'Interfere positivamente', regex=False)
    df[column] = df[column].str.replace('Interfere muito negativamente', 'Interfere negativamente', regex=False)

    return df
