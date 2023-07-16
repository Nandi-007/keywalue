from keywalue.steps.key_value_steps import KeyValueSteps


class TestDelete:
    key_value_steps = KeyValueSteps()

    def test_delete_positive(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.delete_data(client=client, key="key")
        assert "OK" == response, f"Get is unsuccessful, response is:{response}"

    def test_delete_missing_key(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.delete_data(client=client, key="key")
        assert "ERROR: key not found" == response, f"Get is successful, response is:{response}"
