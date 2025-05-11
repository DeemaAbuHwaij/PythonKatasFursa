import json
from typing import Any


def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    """
    Merge multiple JSON configuration files into a single dictionary.

    You are given an unknown number of file paths pointing to JSON configuration files.
    These files should be merged in the order they are given:
    - Keys in later files override those in earlier ones.
    - Nested dictionaries must also be merged recursively.

    Example:

        File: default.json
        {
          "user": {
            "name": "John",
            "age": 30
          },
          "settings": {
            "theme": "light",
            "language": "english"
          }
        }

        File: local.json
        {
          "user": {
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

        Result:
        {
          "user": {
            "name": "John",
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "theme": "light",
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

    Args:
        *json_paths: Variable number of JSON file paths to merge.

    Returns:
        dict: The merged configuration dictionary.
    """

    def merge_dicts(a: dict, b: dict) -> dict:
        for key, value in b.items():
            if key in a and isinstance(a[key], dict) and isinstance(value, dict):
                a[key] = merge_dicts(a[key], value)
            else:
                a[key] = value
        return a

    merged_config = {}
    for path in json_paths:
        with open(path, 'r') as f:
            current_config = json.load(f)
            merged_config = merge_dicts(merged_config, current_config)
    return merged_config


if __name__ == '__main__':
    # Example usage; make sure the files exist if you run this directly.
    config = json_configs_merge('default.json', 'local.json')
    print(json.dumps(config, indent=2))