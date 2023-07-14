from steps.key_value_steps import KeyValueSteps


class TestCount:
    key_value_steps = KeyValueSteps()

    def test_count(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.get_count(client=client)
        assert "0" == response, f"Count is {response}"
