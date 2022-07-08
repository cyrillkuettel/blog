from pathlib import Path


class Paths:
    current_file = Path(__file__)
    current_file_dir = current_file.parent  # app
    templates = current_file_dir / "templates"
