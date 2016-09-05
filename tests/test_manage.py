#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from tempfile import NamedTemporaryFile

from mock import patch

from chess_configurations.scripts.manage import main


@patch('chess_configurations.scripts.manage.backtracking')
def test_call_backtracking(backtracking_mock):
    """ test_that_manage_calls_backtracking"""
    testargs = 'manage.py -n 3 -m 3 --pieces=K'.split()
    with patch.object(sys, 'argv', testargs):
        main()

    assert backtracking_mock.called


def test_saved_as_json():
    """ test_that_result_is_saved_as_json """
    expected = [
        {'n': 3, 'm': 3, 'pieces': {'(0, 0)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(0, 1)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(0, 2)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(1, 0)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(1, 1)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(1, 2)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(2, 0)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(2, 1)': 'K'}},
        {'n': 3, 'm': 3, 'pieces': {'(2, 2)': 'K'}}]
    temp_file = NamedTemporaryFile()
    testargs = 'manage.py -n 3 -m 3 --pieces=K --output {0} --output_format json'.format(temp_file.name).split()
    with patch.object(sys, 'argv', testargs):
        main()

    with open(temp_file.name, 'r') as output_file:
        res = []
        for result in output_file:
            res.append(json.loads(result))
    temp_file.close()
    assert res == expected


def test_as_text():
    """ test_that_result_is_saved_as_text """
    expected = '┌──────┐\n│K _ _ │\n│_ _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ K _ │\n│_ _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ K │\n│_ _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│K _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ K _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ K │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ _ │\n│K _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ _ │\n│_ K _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ _ │\n│_ _ K │\n└──────┘\n\n\n'
    temp_file = NamedTemporaryFile()
    testargs = 'manage.py -n 3 -m 3 --pieces=K --output {0} --output_format text'.format(temp_file.name).split()
    with patch.object(sys, 'argv', testargs):
        main()

    with open(temp_file.name, 'r') as output_file:
        res = output_file.read()

    temp_file.close()
    assert res == expected
