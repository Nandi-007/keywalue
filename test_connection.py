from connection import KVStoreClient


def test_put(server_setup_teardown):
    client = server_setup_teardown
    response = client.run_cli_command(command='count')
    assert "$ bb-kvstore_cli > 0\\x00\\n" in response, f"response is {response}"
