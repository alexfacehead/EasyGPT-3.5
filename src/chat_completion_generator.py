from openai import OpenAI
from termcolor import colored
from typing import List, Optional
from src.utils.helpers import sum_content_length
from src.utils.logging import Logger

logger = Logger().get_logger()


class ChatCompletionGenerator:
    def __init__(self, api_key: str, model: str, temperature: float = 0.33, top_p: float = 0.5):
        """
        Wrapper around OpenAI's Chat Completions API.

        Args:
            api_key: OpenAI API key.
            model: The model to use (e.g. "gpt-4").
            temperature: Sampling temperature (0.0-2.0).
            top_p: Nucleus sampling parameter (0.0-1.0).
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.top_p = top_p

    def generate_completion(self, messages: List[dict], model: Optional[str] = None,
                            temperature: Optional[float] = None, top_p: Optional[float] = None) -> str:
        """
        Generates a chat completion.

        Args:
            messages: List of message dicts with 'role' and 'content' keys.
            model: Override the default model for this call.
            temperature: Override the default temperature for this call.
            top_p: Override the default top_p for this call.

        Returns:
            The content of the model's response.
        """
        model = model or self.model
        temperature = temperature if temperature is not None else self.temperature
        top_p = top_p if top_p is not None else self.top_p

        logger.info(f"MODEL: {model}")
        print(colored(f"\nGenerating completion... (context length: {sum_content_length(messages)})\n", 'magenta'))

        # Models that don't support temperature/top_p/max_tokens
        NO_SAMPLING_PREFIXES = ("o1", "o3", "o4", "gpt-5")
        is_reasoning_model = any(model.startswith(p) for p in NO_SAMPLING_PREFIXES)
        params = dict(model=model, messages=messages)
        if is_reasoning_model:
            params["max_completion_tokens"] = 4096
        else:
            params["max_tokens"] = 4096
            params["temperature"] = temperature
            params["top_p"] = top_p

        response = self.client.chat.completions.create(**params)

        print(colored("--Successfully completed last API call--\n", 'blue'))
        return response.choices[0].message.content
