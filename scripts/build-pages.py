"""Build a Pages artifact without Python environments, Git metadata or HF caches."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist"
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
for name in ("models", "vendor"):
    shutil.copytree(ROOT / name, OUT / name, ignore=shutil.ignore_patterns(".cache", "__pycache__", ".gitattributes"))
whistle = OUT / "whistle"
whistle.mkdir()
for name in ("worker.js", "pack.js", "whistle.js", "backend.js", "whistle.pack"):
    shutil.copy2(ROOT / "whistle" / name, whistle / name)
shutil.copytree(ROOT / "whistle" / "onnx", whistle / "onnx")
for name in ("index.html", "jarvis.html"):
    shutil.copy2(ROOT / "jarvis.html", OUT / name)
(OUT / ".nojekyll").touch()
print(f"Built {OUT}: {sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file()) / 1e6:.1f} MB")
