import os
import unittest

try:
    from jm_tools.chatgpt import ChatGPTClient
except ModuleNotFoundError as exc:
    raise unittest.SkipTest(f"Optional dependency missing: {exc.name}") from exc

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise unittest.SkipTest("OPENAI_API_KEY not set")


class TestChatGPTClient(unittest.TestCase):

    def test_start_session(self):
        client = ChatGPTClient(OPENAI_API_KEY)
        client.start_session()
        assert client.session_id is not None

    def test_initialize_context(self):
        client = ChatGPTClient(OPENAI_API_KEY)
        client.start_session()
        client.initialize_context('Hello, world!')
        assert 'Hello, world!' in client.local_context

    def test_is_session_alive(self):
        client = ChatGPTClient(OPENAI_API_KEY)
        client.start_session()
        assert client.is_session_alive()

    def test_restart_session_with_context(self):
        client = ChatGPTClient(OPENAI_API_KEY)
        client.start_session()
        client.initialize_context('Hello, world!')
        old_session_id = client.session_id
        client.restart_session_with_context()
        assert old_session_id != client.session_id
        assert 'Hello, world!' in client.local_context

    def test_get_completion(self):
        client = ChatGPTClient(OPENAI_API_KEY)
        client.start_session()
        response = client.get_completion('Hello, world!')
        assert 'choices' in response


if __name__ == "__main__":
    unittest.main()
