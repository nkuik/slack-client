import os
import mock
import unittest

import config.configuration as config

class ConfigTests(unittest.TestCase):

    @mock.patch.dict(os.environ,
        {'DANISH_AMAZON_CONFIG': os.path.join(os.getcwd(), 'config/test.yml')})
    def test_config_load(self):
        configuration = config.load_config()
        assert configuration['twilio']['api-key'] == 'twilio-api-key'

