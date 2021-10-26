from pprint import pprint

import easyocr


def text_recognition(file_path):
    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    pprint(result)

def main():
    file_path = "./photo/1.jpg"
    text_recognition(file_path=file_path)

if __name__ == '__main__':
    main()
