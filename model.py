from llama_cpp import Llama

MODEL_PATH = "models/Llama-3-8B-Instruct.Q4_K_M.gguf"
llm = Llama(model_path=MODEL_PATH)

def get_reply(prompt: str) -> str:
    full_prompt = f"Q: {prompt}\nA:"
    output = llm(
        prompt=full_prompt,
        max_tokens=40,
        stop=["Q:", "\n", "</s>"]
    )
    return output["choices"][0]["text"].strip()

