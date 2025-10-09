"""Common objects and functions for the CHILI protocol scripts."""

import paths
import yaml


def load_yaml(file_path: str) -> dict:
    """Load a YAML file and return its contents as a dictionary."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


MODELS = load_yaml(paths.protocol / "models.yaml")["models"]
