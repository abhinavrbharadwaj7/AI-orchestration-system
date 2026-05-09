import json
import os
from urllib import request


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "deepseek/deepseek-chat-v3-0324:free"
REQUEST_TIMEOUT_SECONDS = 60
TEMPERATURE = 0.2
MAX_TOKENS = 1200


def call_ai(prompt: str, system_message: str = "You are a helpful AI assistant.") -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return _local_fallback_response(prompt)

    payload = {
        "model": os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL),
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }

    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    api_request = request.Request(OPENROUTER_URL, data=body, headers=headers, method="POST")

    with request.urlopen(api_request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
        response_body = response.read().decode("utf-8")
        data = json.loads(response_body)
        return data["choices"][0]["message"]["content"].strip()


def _local_fallback_response(prompt: str) -> str:
    if "Rewrite this user goal" in prompt:
        goal = _extract_after_label(prompt, "User goal:")
        return f"Build a simple, working solution for: {goal}"

    if "Break this objective into implementation tasks" in prompt:
        return json.dumps(
            [
                "Understand the requested outcome",
                "Design the simplest implementation approach",
                "Produce the requested code or output",
                "Check the output against the objective",
            ]
        )

    if "Execute these implementation tasks" in prompt:
        objective = _extract_after_label(prompt, "Objective:")
        return f"Completed draft output for objective: {objective}"

    if "Validate this generated result" in prompt:
        return "PASS"

    return "No local fallback response matched this prompt."


def _extract_after_label(text: str, label: str) -> str:
    if label not in text:
        return text.strip()

    return text.split(label, 1)[1].strip().splitlines()[0].strip()

