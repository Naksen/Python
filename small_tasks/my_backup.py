import time
import zipfile
import os


# Получения списка с абсолютными путями каждого файла (в подкаталогах в том числе)
def get_file_paths(source):
    filePaths = []
    for root, dirs, files in os.walk(source):
        for filename in files:
            fp = os.path.join(root, filename)
            filePaths.append(fp)
    return filePaths


if __name__ == '__main__':

    # Каталог, который необходимо скопировать
    source = 'D:\\Документы'

    # Именем zip-архива будет служить сегодняшняя дата
    today = time.strftime('%Y%m%d') + '.zip'

    # Получаем список файлов
    filePaths = get_file_paths(source)

    # Создаем и записываем в архив каждый файл из списка
    zip_file = zipfile.ZipFile(today, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
    with zip_file:
        for file in filePaths:
            zip_file.write(file)

    # Закрываем ахвиный файл
    zip_file.close()

    print('Резеревная копия успешно создана')
