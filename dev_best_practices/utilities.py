import pandas as pd


def test_func():
    print('hello!')

def numbers_function():
	print('122223333')

def letters_function():
	print('abc')

def check_item_in_list(x, a_list):
    return x in a_list


def double_all_cols(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    for col in df.columns:
        df[col] = df[col] * 2
    return df
