"""
test_parser — unit tests for telemetry/parser.py.
"""

import json

import pytest
from pydantic import ValidationError
from telemetry.parser import parse_line, parse_lines
from telemetry.schema import TelemetryRecord

_VALID_LINE = '{"algo":"QuickSort","n":1000,"comparisons":12345,"swaps":6789,"elapsedMs":42}'


class TestParseLine:
    def test_valid_line(self):
        record = parse_line(_VALID_LINE)
        assert isinstance(record, TelemetryRecord)
        assert record.algo == "QuickSort"
        assert record.n == 1000
        assert record.comparisons == 12345
        assert record.swaps == 6789
        assert record.elapsedMs == 42

    def test_malformed_json_raises(self):
        with pytest.raises(json.JSONDecodeError):
            parse_line("{not json}")

    def test_missing_field_raises(self):
        with pytest.raises((ValidationError, ValueError)):
            parse_line('{"algo":"Test","n":100}')


class TestParseLines:
    def test_mixed_valid_and_malformed(self):
        lines = [
            _VALID_LINE,
            "",
            "{bad}",
            '{"algo":"MergeSort","n":500,"comparisons":5000,"swaps":2500,"elapsedMs":15}',
        ]
        records = parse_lines(lines)
        assert len(records) == 2
        assert records[0].algo == "QuickSort"
        assert records[1].algo == "MergeSort"

    def test_empty_list(self):
        assert parse_lines([]) == []

    def test_all_malformed(self):
        lines = ["{bad}", "", "not json"]
        assert parse_lines(lines) == []
