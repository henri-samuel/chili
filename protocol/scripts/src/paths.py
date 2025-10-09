"""Local paths to data and other resources used in the CHILI protocol."""

from pathlib import Path

protocol = Path(__file__).parents[2]
scripts = protocol / "scripts"
inputs = protocol / "inputs"
outputs = protocol / "outputs"
