import pypdf
import os
 #2TODO оформить в тест, добавить ассерты и использовать универсальный путь

FILES_PATH = os.path.abspath(__file__)
ROOT_PATH = os.path.dirname(FILES_PATH)
RESOURCE_PATH = os.path.join(ROOT_PATH, 'resources')

def test_pdf():
    reader = pypdf.PdfReader(os.path.join(RESOURCE_PATH, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    print(number_of_pages)
    print(first_page)
    print(text)
    count = 0
    for image_file in first_page.images:
        with open(os.path.join(RESOURCE_PATH, str(count) + image_file.name), 'wb') as fp:
            fp.write(image_file.data)
            count += 1

    assert number_of_pages == 412
    assert text == "pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, https://merlinux.eu/\nJul 14, 2022"
    assert count == 1
