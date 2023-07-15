import time

import pytest

from connection_handler.connection import KVStoreClient

hostname = "DESKTOP-C1OMGSH"
port = '6378'


@pytest.fixture(scope='function', autouse=True)
def server_setup_teardown():
    client = KVStoreClient(hostname, port)
    client.start_server()

    timeout = 5
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            client.login_cli(hostname, port)
            break
        except AssertionError:
            time.sleep(1)

    yield client
    client.stop_cli()
    client.kill_server()
