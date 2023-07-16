import time

from keywalue.steps.key_value_steps import KeyValueSteps


class TestRestart:
    key_value_steps = KeyValueSteps()

    def test_restart(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.get_count(client=client)
        assert "1" == response, f"Count is {response}"
        client.stop_cli()
        client.kill_server()
        client.start_server(client.server_parameters)
        time.sleep(5)
        client.login_cli()
        response = self.key_value_steps.get_count(client=client)
        assert "0" == response, f"Count is {response}"
