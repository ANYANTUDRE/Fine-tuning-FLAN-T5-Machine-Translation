from huggingface_hub import HfApi
api = HfApi()

model_id = "anyantudre/flan-t5-ft-en2fr-gguf"

api.create_repo(model_id, exist_ok=True, repo_type="model")

api.upload_file(
    path_or_fileobj="flan-t5-ft-en2fr-gguf",
    path_in_repo="flan-t5-ft-en2fr-gguf",
    repo_id=model_id,
)