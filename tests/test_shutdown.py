import pytest
import requests

@pytest.mark.parametrize('status_code, command, error_message',
                         [
                             (404, 'shut', 'not found'),
                             (404, 'down', 'not found'),
                             (404, '', ''),
                             (200, 'shutdown', 'not found')
                         ]
                         )
def test_shutdown_request(status_code, command, error_message):
    response = requests.post("http://localhost:8088", data=command)

    assert response.status_code == status_code, "Status code from POST request doesn't match, should be 400"

    if status_code != 200:
        assert error_message in response.text, "Error message is incorrect"

    if status_code == 200:
        # checking if it accepts call after shutdown
        response = requests.post("http://localhost:8088/hash", data={"password": "random monkey"})
        assert response.status_code >= 400, "Hash app is still accepting post requests, while shutting down"
