import os
from PIL import Image
# from PIL.ExifTags import TAGS
from datetime import datetime
import pickle
DATE_TIME = 306
# DATE_TIME_ORIGINAL = 36867
# DATE_TIME_DIGITIZED = 36868

directory_path = './pictures/'

image_file_types = [
    'png',
    'jpg',
]


def is_image_file(path):
    file_path_without_extension, file_extension = os.path.splitext(file_path)
    return file_extension.replace('.', '') in image_file_types


def get_date_time_from_file_name(path):
    file_name = path.split('/')[-1]
    print(file_name)


for file_name in os.listdir(directory_path):

    file_path = os.path.join(directory_path, file_name)

    if is_image_file(file_path):

        print(file_name, ':\n')

        try:
            with Image.open(file_path) as img:

                exif_data = img.getexif()

                if len(exif_data.items()) > 0:
                    date_time = exif_data[DATE_TIME]
                    print(img.info)
                    # date_time_digitized = exif_data[DATE_TIME_DIGITIZED]
                    # date_time_original = exif_data[DATE_TIME_ORIGINAL]

                    print('DateTime: ', date_time)
                    # print('DateTimeDigitized: ', date_time_digitized)
                    # print('DateTimeOriginal: ', date_time_original)

                else:
                    new_exif = {DATE_TIME: '2020:12:19 12:00:00'}
                    print(img.info)
                    img.info = {'exif': pickle.dumps(new_exif)}
                    img.save(file_path, exif=img.info['exif'])

                    get_date_time_from_file_name(file_path)
                    print("No EXIF data found.")

        except Exception as e:
            print(f"Error reading EXIF data: {e}")

        print()
        print()
        print()
        print()
        print()
        print()
