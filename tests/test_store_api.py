import requests
from config import STORE_URL
from tests.base_classes.base_response import Response
from src.pydanic_schemas.user import User

def test_getting_user_list(get_user):
    Response(get_user).assert_status_code(200).validate(User)


def test_another():
    assert 1 == 1



# s = {'meta': {'pagination': {'total': 2944, 'pages': 295, 'page': 1, 'limit': 10, 'links': {'previous': None, 'current': 'https://gorest.co.in/public/v1/users?page=1', 'next': 'https://gorest.co.in/public/v1/users?page=2'}}}, 'data': [
# {'id': 7807526, 'name': 'Priya Nehru Sr.', 'email': 'nehru_sr_priya@kling.test', 'gender': 'male', 'status': 'inactive'}, {
# 'id': 7807513, 'name': 'Krishnadasa Kaniyar', 'email': 'kaniyar_krishnadasa@jones.example', 'gender': 'male', 'status': 'inactive'}, {'id': 7807512, 'name': 'Pran Kocchar', 'email': 'kocchar_pran@lynch-schmidt.test', 'gender': 'male', 'status': 'inactive'}, {'id': 7807511, 'name': 'Devika Varman', 'email': 'varman_devika@windler-wiza.test', 'gender': 'female', 'status': 'active'}, {'id': 7807510, 'name': 'Ekadant Varman CPA', 'email': 'cpa_ekadant_varman@upton-hermiston.test', 'gender':
# 'female', 'status': 'active'}, {'id': 7807509, 'name': 'Kashyap Mukhopadhyay', 'email': 'kashyap_mukhopadhyay@halvorson-cormier.test', 'gender': 'female', 'status': 'active'}, {'id': 7807508, 'name': 'Deb Trivedi', 'email': 'trivedi_deb@hyatt-rice.example', 'gender': 'female', 'status': 'inactive'}, {'id': 7807507, 'name': 'Harita Devar', 'email': 'devar_harita@braun.example', 'gender': 'male', 'status': 'inactive'}, {'id': 7807506, 'name': 'Oormila Bhattathiri', 'email': 'oormila_bhattathiri@kuhn.test', 'gender': 'female', 'status': 'active'}, {'id': 7807505, 'name': 'Acharyanandana Kapoor', 'email': 'acharyanandana_kapoor@ratke-collins.example', 'gender': 'male', 'status': 'inactive'}]}
