import requests
import pytest

@pytest.mark.parametrize('status_code, param, error_message',
                                                    [
                                                        (200, '', ''),
                                                        (404, 'null', 'page not found'),
                                                        (404, 'monkey', 'page not found'),
                                                        (404, '$', 'page not found'),
                                                        (404, '-1', 'page not found'),
                                                        (404, '0', 'page not found'),
                                                        (404, '1', 'page not found')
                                                    ]
                )
def test_stats_get_request(status_code, param, error_message):
    if param != '':
        param = "/" + param

    response = requests.get("http://localhost:8088/stats" + param)

    assert status_code == response.status_code, "Response status code doesn't match"

    if status_code == 200:
        total_requests = response.json()["TotalRequests"]
        average_time = response.json()["AverageTime"]

        assert str(total_requests).isdigit(), "JSON format is invalid"

        assert str(average_time).isdigit(), "JSON format is invalid"
    else:
        assert error_message in response.text, "Response body message is wrong"

