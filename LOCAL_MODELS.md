# Local speech models

Serve this directory over HTTP on localhost (not `file://`) and open `jarvis.html`.
The default `phonon-tts` setting uses local Phonon 31m English weights and a vendored
Phonon runtime. The voice selector reads the local catalog and local voice files.
Whistle always uses `whistle/worker.js` and its adjacent weights; `?local` is no longer needed.

## Restore downloads

The existing `.venv-hf` contains Hugging Face Hub. These downloads are public and
require no token. From the project directory:

```sh
.venv-hf/bin/python -c 'from huggingface_hub import snapshot_download; snapshot_download("gradium/phonon-31m-en",revision="92741c5b07d085ff840e26fea8ce43110b87852f",allow_patterns=["config.json","tokenizer.json","model.q8.gguf","default-voice.safetensors"],local_dir="models/phonon-31m-en-local-snapshot-92741c5b07d085ff840e26fea8ce43110b87852f"); snapshot_download("gradium/phonon-voices",allow_patterns=["voices.jsonl","voices/*"],local_dir="models/phonon-voices-local")'
```

The runtime in `vendor/phonon-tts/` is the contents of the npm package
`phonon-tts@0.6.0` (with the tarball's `package/` prefix removed).
Its license files are included. Phonon 31m weights are Apache 2.0;
consult upstream licenses before redistributing voice assets.

## What still uses the network

- LLM requests go to the configured endpoint.
- Pixi and Whistle's ONNX Runtime JavaScript/WASM still load from jsDelivr.
  Models are local, but a completely disconnected first page load needs those
  runtime dependencies vendored too.
- Browser speech recognition may use the browser vendor's remote service.
  Choose Whistle for local recognition.
- Entering a custom `hf://...` TTS model explicitly opts back into Hub loading.

The browser still reads weights from the local server when initializing a model;
this is not a fresh internet download. Phonon also retains its browser cache.
Existing browser settings are preserved; choose a valid voice in Settings if an
old saved voice such as `jarvis-like` is no longer available.
