import pytest
import encrypter
import requests


@pytest.mark.parametrize('status_code, password',
                                                    [
                                                        (400, ''),
                                                        (200, 'another angrymonkey'),
                                                        (200, 'sadmonkey123'),
                                                        (200, 'madmonkey@'),
                                                        (200, 'madmonkey\"'),
                                                        (200, 'mad_monkey'),
                                                        (200, 'UGLYmonkey'),
                                                        (200, 'uglymonkey$'),
                                                        (200, 'uglymonkey%'),
                                                        (200, 'uglymonkey{}'),
                                                        (200, 'uglymonkey[]]'),
                                                        (200, 'uglymonkey<>'),
                                                        (200, 'uglymonkey£'),
                                                        (200, 'uglymonkey±'),
                                                        (200, 'uglymonkey 亂數假文產生器'),
                                                        (200, 'uglymonkey Лорем ипсум долор сит аме'),
                                                        (200, 'uglymonkey ما هو لوريم ايبسوم')
                                                    ]
                )
def test_hash_post_request(status_code, password):
    response = requests.get("http://localhost:8088/stats")
    password_requests_number = response.json()["TotalRequests"]
    origin_average_time = response.json()["AverageTime"]

    # sending password for encryption
    # and validating response time and status code
    payload = {"password": password}
    response = requests.post("http://localhost:8088/hash", data=payload);
    job_identifier = int(response.text)
    assert response.status_code == status_code, "Status code from POST request doesn't match, should be 400"

    # if job identifier is incremented with every POST request following should be uncommented
    # assert job_identifier == password_requests_number + 1, "Job identifier is wrong"

    assert response.elapsed.total_seconds() > 5, "Request processing took less than 5 sec"

    # checking if password encryption was done correctly
    response = requests.get("http://localhost:8088/hash/" + str(job_identifier))
    expected_encrypted_password = encrypter.encoderofstring(password)

    assert expected_encrypted_password == response.text, "encrypted password doesn't match"

    # checking if stats has changed
    response = requests.get("http://localhost:8088/stats")
    assert response.json()["TotalRequests"] == password_requests_number + 1, "Total requests number hasn't changed"

    # checking if average time has changed
    assert origin_average_time < response.json()["AverageTime"], "Timestamp hasn't changed after POST request"







