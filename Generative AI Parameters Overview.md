_____________
# 📘 OpenAi ChatGpt (Generative AI) Parameters – Reference Table
_______________
<br>

| **Parameter**       | **Description**                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `model`             | Specifies the model to use (e.g., `"gpt-4o"`, `"gpt-4"`, `"gpt-3.5-turbo"`). Determines the capability and cost.             |
| `temperature`       | Controls randomness in output. Range: `0.0` (deterministic) to `2.0` (more creative). Typical values are `0.7` or `0.9`.     |
| `max_tokens`        | Sets the **maximum number of tokens** the AI can generate in a response. Limits length of the output.                        |
| `top_p`             | An alternative to `temperature`, it uses **nucleus sampling**. Range: `0.0`–`1.0`. Lower values = more focused output.       |
| `frequency_penalty` | Penalizes repeated phrases or tokens. Range: `-2.0` to `2.0`. Positive values discourage repetition.                         |
| `presence_penalty`  | Encourages the model to talk about new topics. Range: `-2.0` to `2.0`. Positive values promote diversity in content.         |
| `stop`              | Defines **stop sequences** (string or list of strings) that halt generation once encountered. Useful for structured outputs. |
| `stream`            | If `True`, the response is sent as a stream of tokens (token-by-token), ideal for real-time interfaces.                      |
| `n`                 | Number of completions to generate per prompt. Defaults to `1`. Useful for sampling multiple outputs.                         |
| `logprobs`          | If set, includes the log probabilities of output tokens. Helps for interpretability and debugging.                           |
| `user`              | An optional user ID or label that can help OpenAI monitor and detect abuse. Also useful in audit trails.                     |
| `seed`              | (Only supported in some models) Sets a random seed for deterministic outputs — ensures reproducibility.                      |
| `tools`             | Allows registering function calls or tools for function-calling models (`gpt-4` and `gpt-4o`).                               |
| `tool_choice`       | Specifies which tool to invoke if multiple are defined. Can be `"auto"`, `"none"`, or the name of a tool.                    |
| `functions`         | **Deprecated**. Former way of defining function signatures before `tools` was introduced.                                    |
| `function_call`     | **Deprecated**. Specifies which function to call. Replaced by `tool_choice` and `tools`.                                     |
| `response_format`   | For models like `gpt-4o` and `gpt-4-turbo`, allows responses in `"text"` or `"json"` format.                                 |
| `timeout`           | Specifies timeout duration in seconds for the request to complete.                                                           |
| `retry`             | (In wrappers like LangChain/OpenAI SDK) Determines retry behavior on timeouts or server errors.                              |

<br>
<br>

# 📘 Anthropic (Claude) API Parameters – Reference Table
| **Parameter**              | **Description**                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `model`                    | The Claude model to use, e.g. `"claude-3-opus-20240229"`, `"claude-3-sonnet-20240229"`, `"claude-3-haiku-20240307"`.      |
| `max_tokens`               | Sets the **maximum number of tokens** in the model’s **response only**. Does **not** include input tokens.                |
| `temperature`              | Controls randomness in output. Range: `0.0` (deterministic) to `1.0`. Typical value is `0.7`.                             |
| `top_k`                    | Limits sampling to the `k` most likely next tokens. Works like a sharp cutoff. Optional, advanced control.                |
| `top_p`                    | Enables **nucleus sampling** — only considers tokens with cumulative probability up to `top_p`. Usually `1` by default.   |
| `stop_sequences`           | A list of sequences where the model should stop generating further tokens. Works like `stop` in OpenAI.                   |
| `system`                   | Provides **system-level instructions** for the assistant’s behavior. Similar to OpenAI's `system` message.                |
| `messages`                 | An array of message objects for multi-turn conversations. Each object has a `role` (`user` or `assistant`) and `content`. |
| `stream`                   | If `true`, streams output tokens in real-time for better UX.                                                              |
| `metadata`                 | Optional key-value pairs to tag requests for analytics or abuse tracking.                                                 |
| `tools`                    | Allows defining **function-calling tools** (available in Claude 3). Similar to OpenAI’s tool use.                         |
| `tool_choice`              | Explicitly specifies which tool (function) the model should call. `"auto"` lets the model decide.                         |
| `temperature_sampling`     | Internally used to balance sampling randomness; handled automatically unless manually adjusted.                           |
| `stop_reason`              | Returned in the output — explains why generation stopped (`stop_sequence`, `max_tokens`, etc.).                           |
| `prompt` (Claude 1/2 only) | Previously used with Claude 1 and 2 — **deprecated** in Claude 3 which uses structured messages instead.                  |
<br>
<br>

# 📘 Meta (LLaMA) API & Inference Parameters – Reference Table
<br>
<br>

| **Parameter**                 | **Description**                                                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                       | The LLaMA model to use, such as `"meta-llama/Meta-Llama-3-70B-Instruct"` or `"llama2-13b-chat"` (depends on provider – e.g., Hugging Face, Replicate, Together AI). |
| `max_new_tokens`              | Maximum number of tokens to **generate**. Equivalent to `max_tokens` in OpenAI. Does **not** count input tokens.                                                    |
| `temperature`                 | Controls randomness. Lower values make output more deterministic; typical range is `0.0` to `1.0`.                                                                  |
| `top_p`                       | Nucleus sampling — limits generation to tokens with cumulative probability ≤ `top_p`.                                                                               |
| `top_k`                       | Only samples from the `k` most probable tokens. Used to filter token choices more strictly.                                                                         |
| `repetition_penalty`          | Discourages repeating the same phrases or words. Values >1.0 penalize repetition (e.g. `1.1`–`1.5`).                                                                |
| `stop` / `stop_sequences`     | One or more strings to stop text generation once encountered in output.                                                                                             |
| `do_sample`                   | Boolean. If `True`, enables sampling (used with `top_p`, `top_k`, `temperature`). Set to `False` for greedy decoding.                                               |
| `return_full_text`            | If `False`, returns only the newly generated tokens (without echoing input). Defaults to `True`.                                                                    |
| `stream`                      | Streams tokens one-by-one in real time (if supported by the backend/provider).                                                                                      |
| `prompt`                      | The full input text passed to the model, including instructions and chat history.                                                                                   |
| `messages` (chat models only) | In instruction-tuned or chat variants (like LLaMA 2/3 Instruct), a structured array of messages (`user`, `system`, `assistant`).                                    |
| `seed`                        | Optional. For reproducible outputs, sets the random seed for the model’s sampling.                                                                                  |
| `eos_token_id`                | Token ID to indicate end-of-sequence. Can be specified to stop generation cleanly.                                                                                  |
<br>

# 📘 Google Gemini (Generative AI) Parameters – Reference Table
<br>
<br>

| **Parameter**        | **Description**                                                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`              | Model name, e.g. `"gemini-1.5-pro"` or `"gemini-pro"`. Gemini 1.5 models support large context windows (up to 1M tokens).                                |
| `temperature`        | Controls randomness of the output. Range: `0.0` (deterministic) to `1.0` (very creative). Common value: `0.7`.                                           |
| `top_p`              | Enables nucleus sampling. Considers only tokens with cumulative probability up to `top_p`.                                                               |
| `top_k`              | Restricts sampling to the top `k` most probable tokens. Often used together with `top_p`.                                                                |
| `max_output_tokens`  | Maximum number of **tokens to generate** in the response. Similar to `max_tokens` in OpenAI.                                                             |
| `candidate_count`    | Number of response candidates to generate. Useful for getting multiple completions at once.                                                              |
| `stop_sequences`     | List of strings to stop the generation if any are encountered. Useful for structured outputs.                                                            |
| `context`            | Textual context for the model to consider (optional). Typically used alongside `messages`.                                                               |
| `messages`           | Chat format structure with roles: `"user"`, `"model"` (analogous to OpenAI’s `messages`).                                                                |
| `tools`              | Function-calling capability (as of Gemini 1.5). Define tool names, descriptions, and parameter schemas.                                                  |
| `tool_config`        | Specifies execution preferences for tools, like `"auto"` or `"manual"` (similar to `tool_choice`).                                                       |
| `safety_settings`    | Allows customizing model behavior for categories like violence, hate, harassment. Values range: `BLOCK_LOW`, `BLOCK_MEDIUM`, `BLOCK_HIGH`, `BLOCK_NONE`. |
| `system_instruction` | Optional system prompt to guide the assistant’s behavior (similar to OpenAI’s `system`).                                                                 |
| `stream`             | Enables token-by-token streaming (currently supported in SDK and Vertex AI, but not all client platforms).                                               |
| `response_mime_type` | Format of the returned response (e.g., `application/json`, `text/plain`, `text/html` for web tools).                                                     |
| `tools_execution`    | Optional config to define execution instructions for external tools (function-calling context).                                                          |
<br>

# 📘 xAI Grok Parameters (Inferred / Emerging)
<br>

<br>

| **Parameter**        | **Description**                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| `model`              | Name of the Grok variant, e.g., `"grok-1"`, `"grok-1.5"`, `"grok-1.5V"` (V = vision multimodal model). |
| `prompt`             | Full input prompt, typically including instructions, chat history, or task description.                |
| `max_tokens`         | Maximum number of tokens in the **response**. Prevents overly long generations.                        |
| `temperature`        | Controls randomness in output. Lower values = more deterministic. Typical: `0.7`.                      |
| `top_p`              | Nucleus sampling — restricts generation to top-probability mass ≤ `top_p`.                             |
| `top_k`              | Only sample from top `k` most likely tokens. Further restricts the model’s choices.                    |
| `stop`               | List of strings to stop generation early if matched in output.                                         |
| `do_sample`          | Boolean. If `True`, enables sampling via `top_p`, `top_k`, etc. If `False`, uses greedy decoding.      |
| `repetition_penalty` | Discourages repeated phrases/tokens. Values >1.0 = more penalty.                                       |
| `messages`           | For chat-style interfaces, models like `grok-1.5` support `messages` with roles (`user`, `assistant`). |
| `system`             | Optional system-level instructions to govern assistant behavior. Similar to OpenAI’s system prompt.    |
| `tools`              | xAI Grok 1.5 supports tool use (function-calling), though full schema is not public yet.               |
| `stream`             | If `true`, returns token-by-token streamed response.                                                   |
| `vision_input`       | In `grok-1.5V`, allows passing image + text multimodal inputs (likely via base64 or URLs).             |
| `seed`               | Optional. Fixes the randomness for reproducible outputs.                                               |
| `tool_choice`        | Allows choosing specific tools when multiple are available. `"auto"` lets model choose.                |
<br>

<br>
<br>

# 📘 DeepSeek Parameters – Reference Table  

| **Parameter**             | **Description**                                                                                                                                           |             |                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------- |
| `model`                   | The model name, e.g.: <br>• `deepseek-coder-6.7b-instruct`<br>• `deepseek-llm-7b-instruct`<br>• `deepseek-vl-1.3b` (vision-language)                      |             |                               |
| `prompt`                  | The full instruction or input string (used in base models or instruction-tuned variants).                                                                 |             |                               |
| `messages`                | For chat models: list of \`{role: "user"                                                                                                                  | "assistant" | "system", content: "..."} \`. |
| `temperature`             | Controls randomness. Range: `0.0` (deterministic) to `1.0+` (more diverse output). Typical: `0.7`.                                                        |             |                               |
| `top_p`                   | Enables nucleus sampling — only tokens within top-p cumulative probability are considered.                                                                |             |                               |
| `top_k`                   | Restricts sampling to top-k most likely tokens. Often used with `top_p`.                                                                                  |             |                               |
| `max_new_tokens`          | Maximum number of **output tokens**. Does not count input tokens.                                                                                         |             |                               |
| `stop` / `stop_sequences` | Optional list of strings where the generation should stop. Useful for formatting or safety.                                                               |             |                               |
| `do_sample`               | Boolean. If `true`, uses `top_k`, `top_p`, and `temperature` for sampling. `False` = greedy decoding.                                                     |             |                               |
| `repetition_penalty`      | Penalizes token repetition to improve output quality. Values >1.0 reduce repeated text.                                                                   |             |                               |
| `stream`                  | If `true`, streams output token-by-token (if supported by the API layer).                                                                                 |             |                               |
| `context_length`          | Model-specific context limit:<br>• `DeepSeek-Coder`: up to 16k tokens<br>• `DeepSeek-VL`: supports images + long text<br>• `DeepSeek LLM 7B`: 32k context |             |                               |
| `vision_input`            | (Only for `deepseek-vl`) Allows image input as base64 or URL in a multimodal prompt.                                                                      |             |                               |
| `seed`                    | Optional. Ensures deterministic outputs for reproducibility.                                                                                              |             |                               |

