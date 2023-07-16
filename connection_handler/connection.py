import subprocess

import psutil


class KVStoreClient:
    server_process = None

    def __init__(self, hostname, port, server_parameters):
        self.hostname = hostname
        self.port = port
        self.server_parameters = server_parameters
        self.server_process = None

    def start_server(self, parameters=""):
        command = f'wsl ../binary/bb-kvstore_server{parameters}'
        self.send_command(command)

    def stop_cli(self):
        self.run_cli_command('quit')

    def kill_server(self):
        if self.server_process is not None:
            pid = self.server_process.pid
            self.server_process.terminate()
            self.server_process.wait()
            self.__kill_pid()
            if psutil.pid_exists(pid):
                self.__kill_process_tree(pid)
            self.server_process = None
            print("Server stopped.")
        else:
            print("Server is not running.")

    def __kill_process_tree(self, pid):
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()

    def __kill_pid(self):
        command = ['wsl', 'pkill', '-f', 'bb-kvstore_server']
        self.send_command(command)

    def __read_output(self):
        response = ""
        while True:
            line = self.server_process.stdout.readline()
            response += str(line)
            if line in [b'\n', b'']:
                break
        return response

    def login_cli(self):
        command = f'wsl ../binary/bb-kvstore_cli {self.hostname} {self.port}'
        self.send_command(command)
        response = self.__read_output()
        assert "available commands" in response and "put key=value" in response \
               and "get key" in response and "del key" in response and "list" in response and "count" in response \
               and "quit" in response, f"response is {response}"
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
