#!/usr/bin/env python3
"""
Create a perf-optimization project scaffold.
"""

import argparse
from pathlib import Path


DOCKERFILE = """\
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-q", "tests"]
"""

DOCKER_COMPOSE = """\
services:
  app:
    build: .
    command: pytest -q tests
    volumes:
      - .:/app
"""

README = """\
# {project_name}

Starter scaffold for a performance optimization task.

## Structure
- repository_before/: baseline code (`__init__.py`)
- repository_after/: optimized code (`__init__.py`)
- tests/: test suite (`__init__.py`)
- evaluation/: evaluation scripts (`evaluation.py`)
- instances/: sample/problem instances (JSON)
- patches/: patches for diffing
- trajectory/: notes or write-up (Markdown)
"""

REQUIREMENTS = "# Add your Python dependencies here\n"

EVALUATION = """\
def main():
    # TODO: implement evaluation logic
    print("Evaluation placeholder")


if __name__ == "__main__":
    main()
"""


def write_file(path: Path, content: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Initialize project structure.")
    parser.add_argument(
        "project_name",
        nargs="?",
        help="Project root folder name; if omitted, use current directory",
    )
    args = parser.parse_args()

    if args.project_name:
        root = Path(args.project_name)
        base_name = args.project_name
    else:
        root = Path(".")
        base_name = Path.cwd().name

    # Required files/directories
    write_file(root / "repository_before" / "__init__.py", "")
    write_file(root / "repository_after" / "__init__.py", "")
    write_file(root / "tests" / "__init__.py", "")

    write_file(root / "evaluation" / "evaluation.py", EVALUATION)
    write_file(root / "instances" / f"{base_name}.json", "{}\n")
    write_file(root / "patches" / f"{base_name}.patch", "")
    write_file(root / "trajectory" / f"{base_name}.md", "# Trajectory\n\n")

    write_file(root / "Dockerfile", DOCKERFILE)
    write_file(root / "docker-compose.yml", DOCKER_COMPOSE)
    write_file(root / "README.md", README.format(project_name=args.project_name))
    write_file(root / "requirements.txt", REQUIREMENTS)

    print(f"Initialized scaffold at {root.resolve()}")


if __name__ == "__main__":
    main()
