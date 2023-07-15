from steps.key_value_steps import KeyValueSteps


class TestCount:
    key_value_steps = KeyValueSteps()

    def test_count_positive(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.get_count(client=client)
        assert "1" == response, f"Count is {response}"

    def test_count_positive_multiple(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.put_data(client=client, command_pair="key2=value2")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.get_count(client=client)
        assert "2" == response, f"Count is {response}"

    def test_count_no_key(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.get_count(client=client)
        assert "0" == response, f"Count is {response}"
