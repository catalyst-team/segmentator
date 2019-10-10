import os

from catalyst.utils import has_image_extension


def find_in_dir(dirname: str):
    result = [
        os.path.join(dirname, fname) for fname in sorted(os.listdir(dirname))
    ]
    return result


def find_images_in_dir(dirname: str):
    result = [
        fname for fname in find_in_dir(dirname) if has_image_extension(fname)
    ]
    return result


def id_from_fname(fname: str):
    return os.path.splitext(os.path.basename(fname))[0]
