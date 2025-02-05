import json
from unittest import TestCase

from zoltpy.csv_io import csv_rows_from_json_io_dict


class CsvIOTestCase(TestCase):
    """
    """


    def test_csv_rows_from_json_io_dict(self):
        # invalid prediction class. ok: forecast-repository.utils.forecast.PREDICTION_CLASS_TO_JSON_IO_DICT_CLASS
        with self.assertRaises(RuntimeError) as context:
            json_io_dict = {'meta': {'targets': []},
                            'predictions': [{'class': 'InvalidClass'}]}
            csv_rows_from_json_io_dict(json_io_dict)
        self.assertIn('invalid prediction_dict class', str(context.exception))

        # blue sky. note that we hard-code the rows here instead of loading from an expected csv file b/c the latter
        # reads all values as strings, which means we'd have to cast types based on target. it became too painful :-)
        exp_rows = [
            ['unit', 'target', 'class', 'value', 'cat', 'prob', 'sample', 'quantile', 'family', 'param1', 'param2',
             'param3'],
            ['loc1', 'pct next week', 'point', 2.1, '', '', '', '', '', '', '', ''],
            ['loc1', 'pct next week', 'named', '', '', '', '', '', 'norm', 1.1, 2.2, ''],
            ['loc2', 'pct next week', 'point', 2.0, '', '', '', '', '', '', '', ''],
            ['loc2', 'pct next week', 'bin', '', 1.1, 0.3, '', '', '', '', '', ''],
            ['loc2', 'pct next week', 'bin', '', 2.2, 0.2, '', '', '', '', '', ''],
            ['loc2', 'pct next week', 'bin', '', 3.3, 0.5, '', '', '', '', '', ''],
            ['loc2', 'pct next week', 'quantile', 1.0, '', '', '', 0.025, '', '', '', ''],
            ['loc2', 'pct next week', 'quantile', 2.2, '', '', '', 0.25, '', '', '', ''],
            ['loc2', 'pct next week', 'quantile', 2.2, '', '', '', 0.5, '', '', '', ''],
            ['loc2', 'pct next week', 'quantile', 5.0, '', '', '', 0.75, '', '', '', ''],
            ['loc2', 'pct next week', 'quantile', 50.0, '', '', '', 0.975, '', '', '', ''],
            ['loc3', 'pct next week', 'point', 3.567, '', '', '', '', '', '', '', ''],
            ['loc3', 'pct next week', 'sample', '', '', '', 2.3, '', '', '', '', ''],
            ['loc3', 'pct next week', 'sample', '', '', '', 6.5, '', '', '', '', ''],
            ['loc3', 'pct next week', 'sample', '', '', '', 0.0, '', '', '', '', ''],
            ['loc3', 'pct next week', 'sample', '', '', '', 10.0234, '', '', '', '', ''],
            ['loc3', 'pct next week', 'sample', '', '', '', 0.0001, '', '', '', '', ''],
            ['loc1', 'cases next week', 'named', '', '', '', '', '', 'pois', 1.1, '', ''],
            ['loc2', 'cases next week', 'point', 5, '', '', '', '', '', '', '', ''],
            ['loc2', 'cases next week', 'sample', '', '', '', 0, '', '', '', '', ''],
            ['loc2', 'cases next week', 'sample', '', '', '', 2, '', '', '', '', ''],
            ['loc2', 'cases next week', 'sample', '', '', '', 5, '', '', '', '', ''],
            ['loc3', 'cases next week', 'point', 10, '', '', '', '', '', '', '', ''],
            ['loc3', 'cases next week', 'bin', '', 0, 0.0, '', '', '', '', '', ''],
            ['loc3', 'cases next week', 'bin', '', 2, 0.1, '', '', '', '', '', ''],
            ['loc3', 'cases next week', 'bin', '', 50, 0.9, '', '', '', '', '', ''],
            ['loc3', 'cases next week', 'quantile', 0, '', '', '', 0.25, '', '', '', ''],
            ['loc3', 'cases next week', 'quantile', 50, '', '', '', 0.75, '', '', '', ''],
            ['loc1', 'season severity', 'point', 'mild', '', '', '', '', '', '', '', ''],
            ['loc1', 'season severity', 'bin', '', 'mild', 0.0, '', '', '', '', '', ''],
            ['loc1', 'season severity', 'bin', '', 'moderate', 0.1, '', '', '', '', '', ''],
            ['loc1', 'season severity', 'bin', '', 'severe', 0.9, '', '', '', '', '', ''],
            ['loc2', 'season severity', 'point', 'moderate', '', '', '', '', '', '', '', ''],
            ['loc2', 'season severity', 'sample', '', '', '', 'moderate', '', '', '', '', ''],
            ['loc2', 'season severity', 'sample', '', '', '', 'severe', '', '', '', '', ''],
            ['loc2', 'season severity', 'sample', '', '', '', 'high', '', '', '', '', ''],
            ['loc2', 'season severity', 'sample', '', '', '', 'moderate', '', '', '', '', ''],
            ['loc2', 'season severity', 'sample', '', '', '', 'mild', '', '', '', '', ''],
            ['loc1', 'above baseline', 'point', True, '', '', '', '', '', '', '', ''],
            ['loc2', 'above baseline', 'bin', '', True, 0.9, '', '', '', '', '', ''],
            ['loc2', 'above baseline', 'bin', '', False, 0.1, '', '', '', '', '', ''],
            ['loc2', 'above baseline', 'sample', '', '', '', True, '', '', '', '', ''],
            ['loc2', 'above baseline', 'sample', '', '', '', False, '', '', '', '', ''],
            ['loc2', 'above baseline', 'sample', '', '', '', True, '', '', '', '', ''],
            ['loc3', 'above baseline', 'sample', '', '', '', False, '', '', '', '', ''],
            ['loc3', 'above baseline', 'sample', '', '', '', True, '', '', '', '', ''],
            ['loc3', 'above baseline', 'sample', '', '', '', True, '', '', '', '', ''],
            ['loc1', 'Season peak week', 'point', '2019-12-22', '', '', '', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'bin', '', '2019-12-15', 0.01, '', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'bin', '', '2019-12-22', 0.1, '', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'bin', '', '2019-12-29', 0.89, '', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'sample', '', '', '', '2020-01-05', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'sample', '', '', '', '2019-12-15', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'point', '2020-01-05', '', '', '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'bin', '', '2019-12-15', 0.01, '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'bin', '', '2019-12-22', 0.05, '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'bin', '', '2019-12-29', 0.05, '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'bin', '', '2020-01-05', 0.89, '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'quantile', '2019-12-22', '', '', '', 0.5, '', '', '', ''],
            ['loc2', 'Season peak week', 'quantile', '2019-12-29', '', '', '', 0.75, '', '', '', ''],
            ['loc2', 'Season peak week', 'quantile', '2020-01-05', '', '', '', 0.975, '', '', '', ''],
            ['loc3', 'Season peak week', 'point', '2019-12-29', '', '', '', '', '', '', '', ''],
            ['loc3', 'Season peak week', 'sample', '', '', '', '2020-01-06', '', '', '', '', ''],
            ['loc3', 'Season peak week', 'sample', '', '', '', '2019-12-16', '', '', '', '', '']]
        with open('tests/docs-predictions.json') as fp:
            json_io_dict = json.load(fp)
            act_rows = csv_rows_from_json_io_dict(json_io_dict)
        self.assertEqual(exp_rows, act_rows)


    def test_csv_rows_from_json_io_dict_retractions(self):
        with open('tests/retractions/docs-predictions-with-retractions.json') as fp:
            json_io_dict = json.load(fp)
        exp_rows = [
            ['unit', 'target', 'class', 'value', 'cat', 'prob', 'sample', 'quantile', 'family', 'param1', 'param2',
             'param3'],
            ['loc1', 'pct next week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'pct next week', 'named', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'pct next week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'pct next week', 'bin', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'pct next week', 'quantile', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'pct next week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'pct next week', 'sample', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'cases next week', 'named', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'cases next week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'cases next week', 'sample', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'cases next week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'cases next week', 'bin', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'cases next week', 'quantile', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'season severity', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'season severity', 'bin', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'season severity', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'season severity', 'sample', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'above baseline', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'above baseline', 'bin', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'above baseline', 'sample', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'above baseline', 'sample', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'bin', '', '', '', '', '', '', '', '', ''],
            ['loc1', 'Season peak week', 'sample', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'bin', '', '', '', '', '', '', '', '', ''],
            ['loc2', 'Season peak week', 'quantile', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'Season peak week', 'point', '', '', '', '', '', '', '', '', ''],
            ['loc3', 'Season peak week', 'sample', '', '', '', '', '', '', '', '', '']]
        act_rows = csv_rows_from_json_io_dict(json_io_dict)
        self.assertEqual(30, len(act_rows))  # 29 predictions retracted + header
        self.assertEqual(exp_rows, act_rows)  # todo xx
