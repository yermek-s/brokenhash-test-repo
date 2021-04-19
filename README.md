# brokenhash-test-repo

This project uses python3, requests, pytest, pytest-xdist

For parallel tesing launch pytest -n 3 test_parallel_calls.py. Instead of 3 you can put any number you like to run the tests in parallel.

For functional smoke tests use pytest file_name. file_name could be test_get.py, test_post.py, test_shutdown.py, test_stats.py
