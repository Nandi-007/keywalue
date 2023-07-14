import pytest
from connection_handler.connection import KVStoreClient

hostname = "DESKTOP-C1OMGSH"
port = '6378'


@pytest.fixture(scope='session', autouse=True)
def server_setup_teardown():
    client = KVStoreClient()
    client.start_server()
    client.login_cli(hostname, port)
    yield client
    client.stop_server()
