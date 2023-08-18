import zipfile
import os
import pathlib
import tempfile

FILES_PATH = os.path.abspath(__file__)
ROOT_PATH = os.path.dirname(FILES_PATH)
RESOURCE_PATH = os.path.join(ROOT_PATH, 'resources')

def test_zip_file_list():
    all_files = os.listdir(RESOURCE_PATH)
    directory = pathlib.Path("resources/")
    with zipfile.ZipFile("resources.zip", mode='w') as archive:
        for file_path in directory.iterdir():
            archive.write(file_path, arcname=file_path.name)

    all_files_in_zip = archive.namelist()

    assert all_files == all_files_in_zip

