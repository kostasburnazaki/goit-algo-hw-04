import argparse
import shutil
from pathlib import Path


def copy_file(file_path: Path, dest_dir: Path):
    try:
        ext = file_path.suffix[1:] or "no_extension"
        target_dir = dest_dir / ext
        target_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy2(file_path, target_dir / file_path.name)

    except Exception as e:
        print(f"Помилка при копіюванні {file_path}: {e}")


def read_folder(source: Path, dest: Path):
    try:
        for item in source.iterdir():
            if item.is_dir():
                read_folder(item, dest)  # рекурсія
            else:
                copy_file(item, dest)

    except Exception as e:
        print(f"Помилка доступу до {source}: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("dest", nargs="?", default="dist")

    args = parser.parse_args()

    source_path = Path(args.source)
    dest_path = Path(args.dest)

    dest_path.mkdir(parents=True, exist_ok=True)

    read_folder(source_path, dest_path)


if __name__ == "__main__":
    main()