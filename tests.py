import pytest
import requests
import hashlib


class TestClass:
    def test_validate_api_call(self):
        response_api = requests.get('https://restcountries.com/v3.1/capital/lima')
        country = response_api.json()
        language_hash = hashlib.sha1(list(country[0]['languages'].values())[0].encode('utf-8')).digest() if 'languages' in country[0].keys() else None
        hash_lima_lang = b'\xb9+f\xb3\x8e\xfc\xef\xc6F\xb9\xb2\x98\xd3C\x8ak\xadT\xde5'
        assert response_api.status_code == 200
        assert language_hash == hash_lima_lang 