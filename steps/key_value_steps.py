from connection_handler.connection import KVStoreClient


class KeyValueSteps:
    def __init__(self):
        self.client = KVStoreClient()

    def get_count(self, client):
        response = client.run_cli_command(command='count')
        count = response.split('\\')[0].split(' ')[-1]
        return count
