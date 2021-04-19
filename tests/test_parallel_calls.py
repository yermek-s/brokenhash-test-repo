import pytest
import encrypter
import requests
import random


@pytest.mark.parametrize('status_code, password',
                         [
                             (400, ''),
                             (200, 'another angrymonkey 1'),
                             (200, 'another angrymonkey 2'),
                             (200, 'another angrymonkey 3'),
                             (200, 'another angrymonkey 4'),
                             (200, 'another angrymonkey 5'),
                             (200, 'another angrymonkey 6'),
                             (200, 'another angrymonkey 7'),
                             (200, 'another angrymonkey 8'),
                             (200, 'another angrymonkey 9'),
                             (200, 'another angrymonkey 10')
                         ]
                         )
def test_hash_post_request(status_code, password):
    random_number = random.randint(1, 100)

    # randomly skipping requests with 50-50
    if random_number % 2 == 1:
        return

    # checking only POST requests in parallel execution
    payload = {"password": password}
    response = requests.post("http://localhost:8088/hash", data=payload);
    job_identifier = int(response.text)
    assert response.status_code == status_code, "Status code from POST request doesn't match, should be 400"

    assert response.elapsed.total_seconds() > 5, "Request processing took less than 5 sec"

    # checking if password encryption was done correctly
    response = requests.get("http://localhost:8088/hash/" + str(job_identifier))
    expected_encrypted_password = encrypter.encoderofstring(password)
    assert expected_encrypted_password == response.text, "encrypted password doesn't match"
