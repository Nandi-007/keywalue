from keywalue.steps.key_value_steps import KeyValueSteps


class TestPut:
    key_value_steps = KeyValueSteps()

    def test_put_positive(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"

    def test_put_duplicate_key(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "ERROR: key already exists" == response, f"Put is successful, response is:{response}"
