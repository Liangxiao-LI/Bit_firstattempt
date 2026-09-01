"""I/O utilities."""

from pathlib import Path
import json
import yaml


def load_config(config_path: Path) -> dict:
    """Load YAML configuration file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def save_config(config: dict, config_path: Path) -> None:
    """Save configuration to YAML file."""
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)


def load_json(json_path: Path) -> dict:
    """Load JSON file."""
    with open(json_path, 'r') as f:
        return json.load(f)


def save_json(data: dict, json_path: Path) -> None:
    """Save data to JSON file."""
    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
