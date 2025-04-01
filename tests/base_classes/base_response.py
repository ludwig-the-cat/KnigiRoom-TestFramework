

from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        data = self.response_json
        # достаем список постов из "products", если он там есть
        if isinstance(data, dict) and 'products' in data:
            items = data['products']
        else:
            items = data
        if isinstance(items, list):
            for item in items:
                schema(**item)  # <- здесь и сработает твой валидатор по id
        else:
            schema(**items)
        return self


    def assert_status_code(self, status_code):
        if isinstance(self.response_status, list):
            assert  self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    # Опишем красиво ошибки
    def __str__(self):
        return f"""
        Status code {self.response_status}'
        Requests url {self.response.url}
        f'"""
