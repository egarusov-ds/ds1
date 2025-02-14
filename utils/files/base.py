import os.path


def get_extension(fp: str) -> str:
    try:
        *_, res = os.path.basename(fp).split('.')
        return res
    except ValueError:
        raise ValueError(f"Failed to get extension from filepath: {fp}")


def get_filepath_from_directory(directory: str, extensions: tuple) -> str:
    try:
        res, *_ = (
            os.path.join(directory, fn) for fn in os.listdir(directory)
            if any(fn.endswith(ext) for ext in extensions)
        )
        return res
    except ValueError:
        raise ValueError(f"File with any extension from {extensions} not found in {directory}")
