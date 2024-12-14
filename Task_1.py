PATH = r"C:\Users\redko\OneDrive\Рабочий стол\Химия\Задания_амины.docx"

def file_info(path: str) -> tuple:
    a = path.split("\\")
    b = a[len(a) - 1].split('.')
    return path, b[0], b[1]

print(file_info(PATH))