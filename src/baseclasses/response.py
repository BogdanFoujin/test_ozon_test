# from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response) -> None:
        self.response = response
        self.response_jsone = response.json().get("data")
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_jsone, list):
            for item in self.response_jsone:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_jsone)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self
    
    def __str__(self) -> str:
        return \
f"""
Status code: {self.response_status}
Requested url: {self.response.url}, Response body: {self.response_jsone}
"""