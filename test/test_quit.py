from steps.key_value_steps import KeyValueSteps


class TestQuit:
    key_value_steps = KeyValueSteps()

    def test_quit_positive(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.list_data(client=client)
        assert "key" == response, f"Get is unsuccessful, response is:{response}"
        self.key_value_steps.quit_cli(client=client)
        client.login_cli(client.hostname, client.port)
        response = self.key_value_steps.list_data(client=client)
        assert "key" == response, f"Get is unsuccessful, response is:{response}"
