import sys
import os
import pytest

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def dash_app():
    return app


def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    header = dash_duo.find_element("h1")

    assert header.text == "Pink Morsel Sales Dashboard"


def test_graph_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    graph = dash_duo.find_element("#sales-chart")

    assert graph is not None


def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    radio = dash_duo.find_element("#region-filter")

    assert radio is not None