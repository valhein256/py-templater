"""conftest.py"""

import os
import sys

# For Development
WORKSPACE = os.getenv('WORKSPACE', '/opt/dev')
CONFIG_PATH = os.path.join(WORKSPACE, 'config/env')
APP_PATH = os.path.join(WORKSPACE, 'app')

sys.path.append(APP_PATH)

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client
