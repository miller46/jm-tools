import requests
import openai
import tiktoken

from jm_tools.config.chatgpt import (
    DEFAULT_ENGINE_ID,
    ENGINES_COST_PER_1000_TOKENS_INPUT_MAP,
    ENGINES_COST_PER_1000_TOKENS_OUTPUT_MAP,
)


class ChatGPTClient:

    def __init__(self, api_key, engine_id=DEFAULT_ENGINE_ID):
        openai.api_key = api_key
        self.engine_id = engine_id
        self.local_context = []

    def count_tokens(self, text):
        encoding = tiktoken.encoding_for_model(self.engine_id)
        num_tokens = len(encoding.encode(text))
        return num_tokens

    def estimate_input_cost(self, text):
        tokens = self.count_tokens(text)
        cost_per_token = ENGINES_COST_PER_1000_TOKENS_INPUT_MAP[self.engine_id] / 1000
        cost = tokens * cost_per_token
        return cost

    def estimate_output_cost(self, max_output_length):
        cost_per_token = ENGINES_COST_PER_1000_TOKENS_OUTPUT_MAP[self.engine_id] / 1000
        cost = max_output_length * cost_per_token
        return cost

    def make_chat_request(self, prompt, max_tokens=1000, temperature=1,
                      top_p=1, n=1, stream=False, logprobs=None, stop="\n"):

        response = openai.Completion.create(
            model=self.engine_id,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n,
            stream=stream,
            logprobs=logprobs,
            stop=stop
        )

        return response.choices[0].text.strip()
