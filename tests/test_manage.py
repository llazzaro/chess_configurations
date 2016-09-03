#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from tempfile import NamedTemporaryFile

from pytest import raises
from mock import Mock, patch

from chess_configurations.scripts.manage import main
from chess_configurations.models import Queen, Board


class TestManage:
    """
        Some people could argue that I'm test the argparse lib here.
        It's true in some part, however I wan to test that the argparse configuration
        is the right one.
    """

    @patch('chess_configurations.scripts.manage.backtracking')
    def test_that_manage_calls_backtracking(self, backtracking_mock):
        testargs = 'manage.py -n 3 -m 3 --pieces=K'.split()
        with patch.object(sys, 'argv', testargs):
            main()

        assert backtracking_mock.called

    def test_that_result_is_saved_as_json(self):
        expected = [{'n': 3, 'm': 3, 'pieces': {'(0, 0)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(0, 1)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(0, 2)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(1, 0)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(1, 1)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(1, 2)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(2, 0)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(2, 1)': 'K'}}, {'n': 3, 'm': 3, 'pieces': {'(2, 2)': 'K'}}]
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


    def test_that_result_is_saved_as_text(self):
        expected = '┌──────┐\n│K _ _ │\n│_ _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ K _ │\n│_ _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ K │\n│_ _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│K _ _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ K _ │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ K │\n│_ _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ _ │\n│K _ _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ _ │\n│_ K _ │\n└──────┘\n\n\n┌──────┐\n│_ _ _ │\n│_ _ _ │\n│_ _ K │\n└──────┘\n\n\n'
        temp_file = NamedTemporaryFile()
        testargs = 'manage.py -n 3 -m 3 --pieces=K --output {0} --output_format text'.format(temp_file.name).split()
        with patch.object(sys, 'argv', testargs):
            main()

        with open(temp_file.name, 'r') as output_file:
            res = output_file.read()

        temp_file.close()
        assert res == expected
