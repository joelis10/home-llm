"""Constants for the LLaMa Conversation integration."""
import types, os

DOMAIN = "llama_conversation"
CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """You are 'Al', a helpful AI Assistant that controls the devices in a house. Complete the following task ask instructed with the information provided only.
Services: {{ services }}
Devices:
{{ devices }}

Respond to the following user instruction by responding in the same format as the following examples:
{{ response_examples }}"""
ICL_NO_SYSTEM_PROMPT = """You are 'Al', a helpful AI Assistant that controls the devices in a house. Complete the following task ask instructed with the information provided only.
Services: {{ services }}
Devices:
{{ devices }}

Respond to the following user instruction by responding in the same format as the following examples:
{{ response_examples }}

User instruction:"""
NO_ICL_PROMPT = """You are 'Al', a helpful AI Assistant that controls the devices in a house. Complete the following task ask instructed with the information provided only.
Services: {{ services }}
Devices:
{{ devices }}"""
CONF_CHAT_MODEL = "huggingface_model"
DEFAULT_CHAT_MODEL = "acon96/Home-3B-v3-GGUF"
RECOMMENDED_CHAT_MODELS = [ "acon96/Home-3B-v3-GGUF", "acon96/Home-1B-v2-GGUF", "TheBloke/Mistral-7B-Instruct-v0.2-GGUF" ]
CONF_MAX_TOKENS = "max_new_tokens"
DEFAULT_MAX_TOKENS = 128
CONF_TOP_K = "top_k"
DEFAULT_TOP_K = 40
CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1
CONF_TYPICAL_P = "typical_p"
DEFAULT_TYPICAL_P = 1.0
CONF_MIN_P = "min_p"
DEFAULT_MIN_P = 0.0
CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.1
CONF_REQUEST_TIMEOUT = "request_timeout"
DEFAULT_REQUEST_TIMEOUT = 90
CONF_BACKEND_TYPE = "model_backend"
BACKEND_TYPE_LLAMA_HF = "llama_cpp_hf"
BACKEND_TYPE_LLAMA_EXISTING = "llama_cpp_existing"
BACKEND_TYPE_TEXT_GEN_WEBUI = "text-generation-webui_api"
BACKEND_TYPE_GENERIC_OPENAI = "generic_openai"
BACKEND_TYPE_LLAMA_CPP_PYTHON_SERVER = "llama_cpp_python_server"
BACKEND_TYPE_OLLAMA = "ollama"
DEFAULT_BACKEND_TYPE = BACKEND_TYPE_LLAMA_HF
CONF_DOWNLOADED_MODEL_QUANTIZATION = "downloaded_model_quantization"
CONF_DOWNLOADED_MODEL_QUANTIZATION_OPTIONS = ["F16", "Q8_0", "Q5_K_M", "Q4_K_M", "Q3_K_M"]
DEFAULT_DOWNLOADED_MODEL_QUANTIZATION = "Q4_K_M"
CONF_DOWNLOADED_MODEL_FILE = "downloaded_model_file"
DEFAULT_DOWNLOADED_MODEL_FILE = ""
DEFAULT_PORT = "5000"
DEFAULT_SSL = False
CONF_EXTRA_ATTRIBUTES_TO_EXPOSE = "extra_attributes_to_expose"
DEFAULT_EXTRA_ATTRIBUTES_TO_EXPOSE = ["rgb_color", "brightness", "temperature", "humidity", "fan_mode", "media_title", "volume_level", "item"]
CONF_ALLOWED_SERVICE_CALL_ARGUMENTS = "allowed_service_call_arguments"
DEFAULT_ALLOWED_SERVICE_CALL_ARGUMENTS = ["rgb_color", "brightness", "temperature", "humidity", "fan_mode", "hvac_mode", "preset_mode", "item", "duration"]
CONF_PROMPT_TEMPLATE = "prompt_template"
PROMPT_TEMPLATE_CHATML = "chatml"
PROMPT_TEMPLATE_ALPACA = "alpaca"
PROMPT_TEMPLATE_VICUNA = "vicuna"
PROMPT_TEMPLATE_MISTRAL = "mistral"
PROMPT_TEMPLATE_LLAMA2 = "llama2"
PROMPT_TEMPLATE_NONE = "no_prompt_template"
PROMPT_TEMPLATE_ZEPHYR = "zephyr"
DEFAULT_PROMPT_TEMPLATE = PROMPT_TEMPLATE_CHATML
PROMPT_TEMPLATE_DESCRIPTIONS = {
    PROMPT_TEMPLATE_CHATML: {
        "system": { "prefix": "<|im_start|>system\n", "suffix": "<|im_end|>" },
        "user": { "prefix": "<|im_start|>user\n", "suffix": "<|im_end|>" },
        "assistant": { "prefix": "<|im_start|>assistant\n", "suffix": "<|im_end|>" },
        "generation_prompt": "<|im_start|>assistant"
    },
    PROMPT_TEMPLATE_ALPACA: {
        "system": { "prefix": "", "suffix": "\n" },
        "user": { "prefix": "### Instruction:\n", "suffix": "\n" },
        "assistant": { "prefix": "### Response:\n", "suffix": "\n" },
        "generation_prompt": "### Response:"
    },
    PROMPT_TEMPLATE_VICUNA: {
        "system": { "prefix": "", "suffix": "\n" },
        "user": { "prefix": "USER: ", "suffix": "" },
        "assistant": { "prefix": "ASSISTANT: ", "suffix": "</s>" },
        "generation_prompt": "ASSISTANT:"
    },
    PROMPT_TEMPLATE_NONE: {
        "system": { "prefix": "", "suffix": "" },
        "user": { "prefix": "", "suffix": "" },
        "assistant": { "prefix": "", "suffix": "" },
        "generation_prompt": ""
    },
    PROMPT_TEMPLATE_MISTRAL: {
        "user": { "prefix": "<s>[INST] ", "suffix": " [/INST] " },
        "assistant": { "prefix": "", "suffix": "</s>" },
        "generation_prompt": ""
    },
    PROMPT_TEMPLATE_ZEPHYR: {
        "system": { "prefix": "<|system|>\n", "suffix": "<|endoftext|>" },
        "user": { "prefix": "<|user|>\n", "suffix": "<|endoftext|>" },
        "assistant": { "prefix": "<|assistant|>\n", "suffix": "<|endoftext|>" },
        "generation_prompt": "<|assistant|>\n"
    }
}
CONF_USE_GBNF_GRAMMAR = "gbnf_grammar"
DEFAULT_USE_GBNF_GRAMMAR = False
CONF_GBNF_GRAMMAR_FILE = "gbnf_grammar_file"
DEFAULT_GBNF_GRAMMAR_FILE = "output.gbnf"
CONF_USE_IN_CONTEXT_LEARNING_EXAMPLES = "in_context_examples"
DEFAULT_USE_IN_CONTEXT_LEARNING_EXAMPLES = True
CONF_IN_CONTEXT_EXAMPLES_FILE = "in_context_examples_file"
DEFAULT_IN_CONTEXT_EXAMPLES_FILE = "in_context_examples.csv"
CONF_NUM_IN_CONTEXT_EXAMPLES = "num_in_context_examples"
DEFAULT_NUM_IN_CONTEXT_EXAMPLES = 4
CONF_TEXT_GEN_WEBUI_PRESET = "text_generation_webui_preset"
CONF_OPENAI_API_KEY = "openai_api_key"
CONF_TEXT_GEN_WEBUI_ADMIN_KEY = "text_generation_webui_admin_key"
CONF_REFRESH_SYSTEM_PROMPT = "refresh_prompt_per_tern"
DEFAULT_REFRESH_SYSTEM_PROMPT = True
CONF_REMEMBER_CONVERSATION = "remember_conversation"
DEFAULT_REMEMBER_CONVERSATION = True
CONF_REMEMBER_NUM_INTERACTIONS = "remember_num_interactions"
DEFAULT_REMEMBER_NUM_INTERACTIONS = 5
CONF_PROMPT_CACHING_ENABLED = "prompt_caching"
DEFAULT_PROMPT_CACHING_ENABLED = False
CONF_PROMPT_CACHING_INTERVAL = "prompt_caching_interval"
DEFAULT_PROMPT_CACHING_INTERVAL = 30
CONF_SERVICE_CALL_REGEX = "service_call_regex"
DEFAULT_SERVICE_CALL_REGEX = r"({[\S \t]*?})"
FINE_TUNED_SERVICE_CALL_REGEX = r"```homeassistant\n([\S \t\n]*?)```"
CONF_REMOTE_USE_CHAT_ENDPOINT = "remote_use_chat_endpoint"
DEFAULT_REMOTE_USE_CHAT_ENDPOINT = False
CONF_TEXT_GEN_WEBUI_CHAT_MODE = "text_generation_webui_chat_mode"
TEXT_GEN_WEBUI_CHAT_MODE_CHAT = "chat"
TEXT_GEN_WEBUI_CHAT_MODE_INSTRUCT = "instruct"
TEXT_GEN_WEBUI_CHAT_MODE_CHAT_INSTRUCT = "chat-instruct"
DEFAULT_TEXT_GEN_WEBUI_CHAT_MODE = TEXT_GEN_WEBUI_CHAT_MODE_CHAT
CONF_OLLAMA_KEEP_ALIVE_MIN = "ollama_keep_alive"
DEFAULT_OLLAMA_KEEP_ALIVE_MIN = 30
CONF_OLLAMA_JSON_MODE = "ollama_json_mode"
DEFAULT_OLLAMA_JSON_MODE = False

CONF_CONTEXT_LENGTH = "context_length"
DEFAULT_CONTEXT_LENGTH = 2048
CONF_BATCH_SIZE = "batch_size"
DEFAULT_BATCH_SIZE = 512
CONF_THREAD_COUNT = "n_threads"
DEFAULT_THREAD_COUNT = os.cpu_count()
CONF_BATCH_THREAD_COUNT = "n_batch_threads"
DEFAULT_BATCH_THREAD_COUNT = os.cpu_count()

DEFAULT_OPTIONS = types.MappingProxyType(
    {
        CONF_PROMPT: DEFAULT_PROMPT,
        CONF_MAX_TOKENS: DEFAULT_MAX_TOKENS,
        CONF_TOP_K: DEFAULT_TOP_K,
        CONF_TOP_P: DEFAULT_TOP_P,
        CONF_MIN_P: DEFAULT_MIN_P,
        CONF_TYPICAL_P: DEFAULT_TYPICAL_P,
        CONF_TEMPERATURE: DEFAULT_TEMPERATURE,
        CONF_REQUEST_TIMEOUT: DEFAULT_REQUEST_TIMEOUT,
        CONF_PROMPT_TEMPLATE: DEFAULT_PROMPT_TEMPLATE,
        CONF_USE_GBNF_GRAMMAR: DEFAULT_USE_GBNF_GRAMMAR,
        CONF_EXTRA_ATTRIBUTES_TO_EXPOSE: DEFAULT_EXTRA_ATTRIBUTES_TO_EXPOSE,
        CONF_ALLOWED_SERVICE_CALL_ARGUMENTS: DEFAULT_ALLOWED_SERVICE_CALL_ARGUMENTS,
        CONF_REFRESH_SYSTEM_PROMPT: DEFAULT_REFRESH_SYSTEM_PROMPT,
        CONF_REMEMBER_CONVERSATION: DEFAULT_REMEMBER_CONVERSATION,
        CONF_REMEMBER_NUM_INTERACTIONS: DEFAULT_REMEMBER_NUM_INTERACTIONS,
        CONF_SERVICE_CALL_REGEX: DEFAULT_SERVICE_CALL_REGEX,
        CONF_REMOTE_USE_CHAT_ENDPOINT: DEFAULT_REMOTE_USE_CHAT_ENDPOINT,
        CONF_USE_IN_CONTEXT_LEARNING_EXAMPLES: DEFAULT_USE_IN_CONTEXT_LEARNING_EXAMPLES,
        CONF_IN_CONTEXT_EXAMPLES_FILE: DEFAULT_IN_CONTEXT_EXAMPLES_FILE,
        CONF_NUM_IN_CONTEXT_EXAMPLES: DEFAULT_NUM_IN_CONTEXT_EXAMPLES,
        CONF_CONTEXT_LENGTH: DEFAULT_CONTEXT_LENGTH,
        CONF_BATCH_SIZE: DEFAULT_BATCH_SIZE,
        CONF_THREAD_COUNT: DEFAULT_THREAD_COUNT,
        CONF_BATCH_THREAD_COUNT: DEFAULT_BATCH_THREAD_COUNT,
        CONF_PROMPT_CACHING_ENABLED: DEFAULT_PROMPT_CACHING_ENABLED,
        CONF_OLLAMA_KEEP_ALIVE_MIN: DEFAULT_OLLAMA_KEEP_ALIVE_MIN,
        CONF_OLLAMA_JSON_MODE: DEFAULT_OLLAMA_JSON_MODE,
        CONF_TEXT_GEN_WEBUI_CHAT_MODE: DEFAULT_TEXT_GEN_WEBUI_CHAT_MODE,
        CONF_TEXT_GEN_WEBUI_PRESET: ""
    }
)

OPTIONS_OVERRIDES = {
    "home-3b-v3": {
        CONF_PROMPT: NO_ICL_PROMPT,
        CONF_PROMPT_TEMPLATE: PROMPT_TEMPLATE_ZEPHYR,
        CONF_USE_IN_CONTEXT_LEARNING_EXAMPLES: False,
        CONF_SERVICE_CALL_REGEX: FINE_TUNED_SERVICE_CALL_REGEX,
        CONF_USE_GBNF_GRAMMAR: True,
    },
    "home-3b-v2": {
        CONF_PROMPT: NO_ICL_PROMPT,
        CONF_USE_IN_CONTEXT_LEARNING_EXAMPLES: False,
        CONF_SERVICE_CALL_REGEX: FINE_TUNED_SERVICE_CALL_REGEX,
        CONF_USE_GBNF_GRAMMAR: True,
    },
    "home-3b-v1": {
        CONF_PROMPT: NO_ICL_PROMPT,
        CONF_USE_IN_CONTEXT_LEARNING_EXAMPLES: False,
        CONF_SERVICE_CALL_REGEX: FINE_TUNED_SERVICE_CALL_REGEX,
    },
    "home-1b-v2": {
        CONF_PROMPT: NO_ICL_PROMPT,
        CONF_USE_IN_CONTEXT_LEARNING_EXAMPLES: False,
        CONF_SERVICE_CALL_REGEX: FINE_TUNED_SERVICE_CALL_REGEX,
    },
    "home-1b-v1": {
        CONF_PROMPT: NO_ICL_PROMPT,
        CONF_USE_IN_CONTEXT_LEARNING_EXAMPLES: False,
        CONF_SERVICE_CALL_REGEX: FINE_TUNED_SERVICE_CALL_REGEX,
    },
    "mistral": {
        CONF_PROMPT: ICL_NO_SYSTEM_PROMPT,
        CONF_PROMPT_TEMPLATE: PROMPT_TEMPLATE_MISTRAL,
    },
    "mixtral": {
        CONF_PROMPT: ICL_NO_SYSTEM_PROMPT,
        CONF_PROMPT_TEMPLATE: PROMPT_TEMPLATE_MISTRAL,
    },
    "llama-2": {
        CONF_PROMPT_TEMPLATE: PROMPT_TEMPLATE_LLAMA2,
    },
    "zephyr": {
        CONF_PROMPT_TEMPLATE: PROMPT_TEMPLATE_ZEPHYR,
    }
}

INTEGRATION_VERSION = "0.2.12"
EMBEDDED_LLAMA_CPP_PYTHON_VERSION = "0.2.60"