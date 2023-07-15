class KeyValueSteps:

    def quit_cli(self, client):
        client.run_cli_command(command='quit')

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

    def list_data(self, client):
        response = client.run_cli_command(command='list')
        key_lines = response.split("\\n'b'")
        if len(key_lines) > 2:
            keys = [key_lines[0].split(' > ')[1]]
            keys.extend([key.split('\\x00')[0] for key in key_lines[1:len(key_lines) - 1]])
        else:
            keys = key_lines[0].split(' > ')[1].split('\\x00')[0]
        return keys
