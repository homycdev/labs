import pytest
from fastapi.testclient import TestClient

from moscow_time.main import app
from moscow_time.main import cwd

client = TestClient(app)


@pytest.mark.parametrize(
    "path, expected",
    [("/", 200), ("/something", 404), ("/time", 404), ("/timezone", 404)],
)
def test_get_time(path, expected):
    response = client.get(path)
    print(cwd())
    assert response.status_code == expected
