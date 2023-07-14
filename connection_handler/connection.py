import subprocess


class KVStoreClient:
    server_process = None

    def __init__(self):
        self.server_process = None

    def start_server(self, parameters=None):
        command = ['wsl', './binary/bb-kvstore_server']
        if parameters:
            command.append(parameters)
        self.send_command(command)

    def stop_server(self):
        if self.server_process is not None:
            self.server_process.terminate()
            self.server_process = None
            print("Server stopped.")
        else:
            print("Server is not running.")

    def __read_output(self):
        response = ""
        while True:
            line = self.server_process.stdout.readline()
            response += str(line)
            if line == b'\n':
                break
        return response

    def login_cli(self, hostname, port):
        command = f'wsl ./binary/bb-kvstore_cli {hostname} {port}'
        self.send_command(command)
        response = self.__read_output()
        assert "available commands" in response and "put key=value" in response \
               and "get key" in response and "del key" in response and "list" in response and "count" in response \
               and "quit" in response, f"response is {response}"
        print(self.server_process)
        return response

    def run_cli_command(self, command):
        command = bytes(command + "\n", 'utf-8')
        self.server_process.stdin.write(command)
        self.server_process.stdin.flush()
        return self.__read_output()

    def send_command(self, command):
        self.server_process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True
        )
        return_code = self.server_process.poll()
        if return_code is not None:
            raise Exception(f'Server process exited with return code {return_code}!')
