"""Baseline tests (lesson 4). They import only baseline.tasks."""
import pytest

from baseline import tasks


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_first_required_item_not_present():
    assert tasks.first_missing(["a", "b", "c"], ["a", "c"]) == "b"


@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_none_when_nothing_is_missing():
    assert tasks.first_missing(["a", "b"], ["b", "a", "x"]) is None
