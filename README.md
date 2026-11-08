# JARVIS

A browser-based voice assistant with a holographic visualization, streaming AI responses, and locally hosted speech models.

**[Launch JARVIS →](https://amirrezasalimi.github.io/jarvis/)**

## Features

- **Voice input:** browser speech recognition by default, with optional local Whistle WebGPU/WASM recognition.
- **Local speech synthesis:** Phonon TTS, with a selectable English voice catalog and short voice previews in Settings.
- **Streaming responses:** connects to an OpenAI-compatible chat completions endpoint.
- **Separate visual signals:** the sphere reacts to AI activity; the surrounding floor bars and pulses react to microphone input.
- **Floor transcript:** stacked conversation text with fading older messages.
- **Cancellation:** press **Escape** to cancel the current turn and return to listening.

## Getting started

1. Open the [live app](https://amirrezasalimi.github.io/jarvis/).
2. Open **Settings** using the gear button.
3. Configure your OpenAI-compatible endpoint, API key, and model. The endpoint should be the API base URL, such as `https://api.openai.com/v1`; the app appends `/chat/completions`.
4. Choose an STT engine and TTS voice, then **Save**.
5. Tap the sphere and allow microphone access.

Voice previews automatically pause the microphone and restore its previous state afterward. Wait for an active AI response to finish before testing a voice.

Browser speech recognition support varies by browser. Choose Whistle if the browser engine is unavailable. WebGPU is used where supported, with CPU/WASM fallback for local speech models.

## Controls

| Control | Action |
| --- | --- |
| Tap the sphere | Start or stop listening |
| `M` | Mute or unmute the microphone (outside text fields) |
| `Escape` | Cancel the current turn, stop speech, and ignore late results |
| Drag | Rotate the scene |
| Shift-drag or right-drag | Pan |
| Scroll or pinch | Zoom |
| Double-click | Toggle fullscreen |

## Models and network access

Phonon 31m English weights, the voice catalog, and Whistle weights are bundled with the site. They load from the same host, not from Hugging Face on every visit. Each browser must still download model assets on first use; browser caches can reuse them afterward. Cache eviction or clearing site data can require another download.

This is **not a fully offline app**:

- AI requests go to your configured LLM endpoint.
- Browser speech recognition may use a browser vendor's remote service.
- Pixi and Whistle's ONNX Runtime dependencies currently load from jsDelivr.
- Entering a custom `hf://...` TTS model opts into Hugging Face loading.

See [LOCAL_MODELS.md](LOCAL_MODELS.md) for model download and restore instructions.

## Run locally

Use Python 3 to serve the project directory:

```sh
python3 -m http.server 8000
```

Open **http://localhost:8000/jarvis.html**. Use HTTP on localhost rather than opening the HTML file directly; module workers and microphone access need a supported origin.

## Deploy to GitHub Pages

The workflow in [`.github/workflows/pages.yml`](.github/workflows/pages.yml) deploys pushes to `main`.

```sh
python3 scripts/build-pages.py
```

The build creates `dist/`, uses `jarvis.html` as the site's `index.html`, and copies model/runtime assets while excluding Python environments and download caches. Configure the repository's **Settings → Pages → Source** as **GitHub Actions**.

## Privacy and API keys

Settings, including your API key, are stored in this browser's `localStorage`. There is no application backend or server-side secret storage. Use your own restricted key, avoid shared devices, and never commit credentials. Your configured endpoint must allow requests from the app's origin through CORS.

Speech sent through browser recognition is subject to the browser provider's policies. Whistle processes speech locally; LLM prompts and conversation messages are sent to your configured endpoint.

## Third-party software and models

This project uses [PixiJS](https://pixijs.com/), [Phonon TTS](https://github.com/gradium-ai/xn-ptts/tree/main/ptts-wasm), [Whistle WebGPU](https://huggingface.co/spaces/mrfakename/whistle-webgpu), and [ONNX Runtime](https://onnxruntime.ai/).

Phonon 31m model weights are Apache 2.0. Vendored Phonon runtime license notices are included in `vendor/phonon-tts/`. Consult upstream licenses for the voice catalog and other bundled assets before redistributing them.
