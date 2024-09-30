import pandas as pd


def get_groups(df):
    """
    Create groups

    :param df: The dataframe to get columns
    :return: List of groups
    """

    positive_group = df[df["Você acredita que jogar interfere positivamente ou negativamente nas suas atividades diárias, como estudo, trabalho ou sono?"] == "Interfere positivamente"]["Quantas horas você joga por dia? (Nos dias que joga)"]
    negative_group = df[df["Você acredita que jogar interfere positivamente ou negativamente nas suas atividades diárias, como estudo, trabalho ou sono?"] == "Interfere negativamente"]["Quantas horas você joga por dia? (Nos dias que joga)"]

    return [positive_group, negative_group]
