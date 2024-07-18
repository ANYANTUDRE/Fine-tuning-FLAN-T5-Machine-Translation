from huggingface_hub import snapshot_download


model_id="anyantudre/flan-t5-ft-en2fr"

snapshot_download(repo_id=model_id, local_dir="flan-t5-hf",
                  local_dir_use_symlinks=False, revision="main")