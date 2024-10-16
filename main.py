import os
import cv2
import numpy as np

# Функция для определения преобладающего цвета в изображении
def find_predominant_color(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Создаем пустой массив для подсчета количества пикселей для каждого оттенка
    hue_histogram = np.zeros(63, dtype=int)

    # Считаем количество пикселей для каждого оттенка
    for row in hsv_image:
        for pixel in row:
            if pixel[2] <= 5: # Чёрные пиксели (яркость менее 5%)
                hue_histogram[61] += 1
            elif pixel[2] >= 95 and pixel[1] <= 5: # Белые пиксели (яркость 95% и больше, насыщенность менее 5%)
                hue_histogram[62] += 1
            else:
                pixel_hue = round(pixel[0]/3)
                hue_histogram[pixel_hue] += 1

    # Находим оттенок с максимальным количеством пикселей
    predominant_hue = np.argmax(hue_histogram)

    return predominant_hue

def colour_name(hsv_color_dict, predominant_hue):
    for hue_range, color in hsv_color_dict.items():
        if hue_range[0] <= predominant_hue <= hue_range[1]:
            return color


# Папка с изображениями
input_folder = 'D:\\Pictures'
output_folder = 'D:\\Sorted_Pictures'

# Получаем список файлов в папке
image_files = os.listdir(input_folder)

# Создаем папку для результатов, если она не существует
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
i = 0

hsv_colour_dict = {
(0, 5): "red",
(6, 15): "yellow",
(16, 25): "green",
(26, 35): "cyan",
(36, 45): "blue",
(46, 55): "violet",
(56, 60): "red",
(61, 61): "black",
(62, 62): "white"
}

# Сортируем изображения по преобладающему цвету и переименовываем их
for filename in image_files:
    image_path = os.path.join(input_folder, filename)
    predominant_hue = find_predominant_color(image_path)
    colorname = colour_name(hsv_colour_dict,predominant_hue)
    if predominant_hue != (61 and 62) :
        new_filename = f"dominant colour - {6*predominant_hue} - {colorname}(picture_number - {i}).jpg"
    else: 
        new_filename = f"dominant colour - {colorname}(picture_number - {i}).jpg"
    i += 1
    new_path = os.path.join(output_folder, new_filename)
    # Переименовываем файл
    os.rename(image_path, new_path)

print("Done")
