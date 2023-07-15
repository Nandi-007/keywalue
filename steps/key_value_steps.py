from connection_handler.connection import KVStoreClient


class KeyValueSteps:
    def __init__(self):
        self.client = KVStoreClient()

    def get_count(self, client):
        response = client.run_cli_command(command='count')
        count = response.split('\\')[0].split('> ')[-1]
        return count

    def put_data(self, client, command_pair):
        response = client.run_cli_command(command=f'put {command_pair}')
        return response.split('\\')[0].split('> ')[-1]

    def get_data(self, client, key):
        response = client.run_cli_command(command=f'get {key}')
        return response.split('\\')[0].split('> ')[-1]

    def delete_data(self, client, key):
        response = client.run_cli_command(command=f'del {key}')
        return response.split('\\')[0].split('> ')[-1]
