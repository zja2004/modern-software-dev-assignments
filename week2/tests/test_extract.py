import os
import pytest

from ..app.services.extract import extract_action_items, extract_action_items_llm
from unittest.mock import patch, MagicMock


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items
    assert "Write tests" in items


@patch("week2.app.services.extract.genai.Client")
def test_extract_llm_bullet_lists(mock_client_class):
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    mock_response = MagicMock()
    mock_response.text = '{"items": ["Set up database", "Write tests"]}'
    mock_client.models.generate_content.return_value = mock_response

    text = """
    Notes from meeting:
    - Set up database
    - Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items_llm(text)
    assert len(items) == 2
    assert "Set up database" in items
    assert "Write tests" in items


@patch("week2.app.services.extract.genai.Client")
def test_extract_llm_empty_input(mock_client_class):
    items = extract_action_items_llm("   ")
    assert len(items) == 0
    mock_client_class.assert_not_called()


@patch("week2.app.services.extract.genai.Client")
def test_extract_llm_fallback(mock_client_class):
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    # Simulate an LLM error to trigger the fallback heuristic rules
    mock_client.models.generate_content.side_effect = Exception("API Error")

    text = """
    - Fix the login bug
    """
    items = extract_action_items_llm(text)
    assert len(items) == 1
    assert "Fix the login bug" in items
