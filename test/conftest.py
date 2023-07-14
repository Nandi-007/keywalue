import time
import pytest
from connection_handler.connection import KVStoreClient

hostname = "DESKTOP-C1OMGSH"
port = '6378'


@pytest.fixture(scope='function', autouse=True)
def server_setup_teardown():
    client = KVStoreClient()
    client.start_server()

    # Wait for the server to start within a specified timeout
    timeout = 3  # Adjust the timeout value as needed
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            client.login_cli(hostname, port)
            break
        except AssertionError:
            time.sleep(1)  # Wait for 1 second before retrying

    yield client
    client.stop_cli()
    client.kill_server()
