from steps.key_value_steps import KeyValueSteps


class TestList:
    key_value_steps = KeyValueSteps()

    def test_list_positive(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.list_data(client=client)
        assert "key" == response, f"Get is unsuccessful, response is:{response}"

    def test_list_positive_multiple(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.put_data(client=client, command_pair="key2=value2")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.list_data(client=client)
        assert ["key2", "key"] == response, f"Get is unsuccessful, response is:{response}"

    def test_list_no_key(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.list_data(client=client)
        assert "" == response, f"Get is successful, response is:{response}"
