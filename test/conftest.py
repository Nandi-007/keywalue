import time

import pytest
from keywalue.connection_handler.connection import KVStoreClient


def pytest_addoption(parser):
    parser.addoption("--hostname", action="store", default="DESKTOP-C1OMGSH", help="Hostname for the server")
    parser.addoption("--port", action="store", default="6378", help="Port for the server")
    parser.addoption("--foreground", action="store", default="NO", help="Should the server run in foreground")


@pytest.fixture(scope='function', autouse=True)
def server_setup_teardown(request):
    hostname = request.config.getoption("--hostname")
    port = request.config.getoption("--port")
    foreground = request.config.getoption("--foreground")

    server_parameters = ""
    if port != "6378":
        server_parameters += f" -p {port}"
    if foreground == "YES":
        server_parameters += " -F"

    client = KVStoreClient(hostname, port, server_parameters)
    client.start_server(server_parameters)

    timeout = 5
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            client.login_cli()
            break
        except AssertionError:
            time.sleep(1)

    yield client
    client.stop_cli()
    client.kill_server()
