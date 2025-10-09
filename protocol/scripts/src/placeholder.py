"""Placeholder script for the CHILI protocol."""

import paths
from common import MODELS

for model in MODELS:
    print(f"Model: {model['title']:<15} | type: {model.get('type', 'N/A')}")

for model in MODELS:
    model_dir = paths.outputs / model["name"]
    model_dir.mkdir(parents=True, exist_ok=True)
    with (model_dir / "README.md").open("w") as f:
        f.write(f"Results from the {model['title']} model.\n")
