from pathlib import Path


class Paths:
    current_file = Path(__file__)
    current_file_dir = current_file.parent  # app
    templates = current_file_dir / "templates"
    static = current_file_dir / "static"
    NOT_FOUND_404 = static / "404.html"
