import requests
from tests.base_classes.base_response import Response
from config import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
#from src.jsonschemas.post import POST_SCHEMA
from src.pydanic_schemas.post import Post


def test_getting_data_from_posts():
    r = requests.get(SERVICE_URL)
    resp = Response(r)
    resp.assert_status_code(200).validate(Post)