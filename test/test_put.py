from keywalue.steps.key_value_steps import KeyValueSteps


class TestPut:
    key_value_steps = KeyValueSteps()

    def test_put_positive(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"

    def test_put_special_string_positive(self, server_setup_teardown):
        client = server_setup_teardown
        special_strings = ["\\0", "\\t", "\\r", "\\", "\\'", '\\"', "\\\\", "\\n", "\\x00", "\\x01", "\\x02", "\\x03",
                           "\\x04", "\\x05", "\\x06", "\\x07", "\\x08", "\\x0B", "\\x0C", "\\x0E", "\\x0F", "\\x10",
                           "\\x11", "\\x12", "\\x13", "\\x14", "\\x15", "\\x16", "\\x17", "\\x18", "\\x19", "\\x1A",
                           "\\x1B", "\\x1C", "\\x1D", "\\x1E", "\\x1F", "\\x7F", "\\x80", "\\x81", "\\x82", "\\x83",
                           "\\x84", "\\x85", "\\x86", "\\x87", "\\x88", "\\x89", "\\x8A", "\\x8B", "\\x8C", "\\x8D",
                           "\\x8E", "\\x8F"]
        for key in special_strings:
            response = self.key_value_steps.put_data(client=client, command_pair=f"{key}=value")
            assert "OK" == response, f"Put is unsuccessful, response is:{response}"
            response = self.key_value_steps.get_data(client=client, key=f"{key}")
            assert "value" == response, f"Get is unsuccessful, response is:{response}"

    def test_put_duplicate_key(self, server_setup_teardown):
        client = server_setup_teardown
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.put_data(client=client, command_pair="key=value")
        assert "ERROR: key already exists" == response, f"Put is successful, response is:{response}"

    def test_put_long_keys_positive(self, server_setup_teardown):
        client = server_setup_teardown
        key = "a" * 1000000000
        value = "b" * 1000000000
        response = self.key_value_steps.put_data(client=client, command_pair=f"{key}={value}")
        assert "OK" == response, f"Put is unsuccessful, response is:{response}"
        response = self.key_value_steps.get_data(client=client, key=key)
        assert value == response, f"Get is unsuccessful, response is:{response}"
