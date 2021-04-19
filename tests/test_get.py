import pytest
import requests


@pytest.mark.parametrize('status_code, job_identifier, error_message',
                         [
                             (400, '', 'invalid syntax'),
                             (400, 'null', 'invalid syntax'),
                             (400, 'monkey', 'invalid syntax'),
                             (400, '$', 'invalid syntax'),
                             (400, '-1', 'invalid syntax'),
                             (400, '0', 'invalid syntax'),
                             (200, '1', '')
                         ]
                         )
def test_hash_get_request(status_code, job_identifier, error_message):
    response = requests.get("http://localhost:8088/hash/" + job_identifier)

    assert status_code == response.status_code, "Response status code is wrong"

    if len(error_message) > 0:
        assert len(response.text) > 0, "Response message (payload) should not be empty"
    else:
        assert error_message in response.text, "Response message (payload) is incorrect"
