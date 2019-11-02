"""
test lib

This file tests all the functions in the lib.py file

Created by Kevin Davis
"""

import os
import json
import pandas as pd
import scripts.DataSync as DataSync
from typing import List, Any

full_file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(full_file_path)


def test_load_config():
    config = DataSync.load_config()
    config_keys = list(config.keys())
    assert "main_token" in config_keys
    assert "test_token" in config_keys


def test_json_to_cvs():

    input = [{
        "firstname": "Adam",
        "lastname": "Johnson"
    }, {
        "firstname": "Bob",
        "lastname": "Smith"
    }]

    json_input = json.dumps(input)
    print(json_input)

    file = f'{dir_name}/temp.csv'
    output = DataSync.json_to_csv(json_input, file_name=file)
    expected = pd.DataFrame(input)

    assert expected.equals(output)


def test_download_data_df():

    expected = type(pd.DataFrame())
    observed = type(DataSync.download_data_df())

    assert expected == observed


def test_split_instrument_dataframe():

    temp_list: List[Any] = []
    df = DataSync.download_data_df()
    instrument_list = DataSync.split_instrument_dataframe(df)
    expected = type(temp_list)
    observed = type(instrument_list)
    assert observed == expected


def test_save_instrument_list():
    dir: str = DataSync.DATA_DICTIONARY_DIR

    df = DataSync.download_data_df()
    list_df = DataSync.split_instrument_dataframe(df)
    DataSync.save_instrument_lists(list_df)

    dir_all_files: List[str] = os.listdir(dir)
    dir_files: List[str] = [
            file for file in dir_all_files
            if os.path.isfile(os.path.join(dir, file))]
    dir_csv_files: List[str] = [
            file for file in dir_files
            if '.csv' in file
            ]

    expected: int = len(list_df)
    observed: int = len(dir_csv_files)

    assert expected == observed
