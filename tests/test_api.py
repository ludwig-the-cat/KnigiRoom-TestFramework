import requests
from tests.base_classes.base_response import Response
from config import SERVICE_URL
from src.pydanic_schemas.post import Post
import pytest

@pytest.mark.skip
def test_getting_data_from_posts():
    r = requests.get(SERVICE_URL)
    resp = Response(r)
    resp.assert_status_code(200).validate(Post)