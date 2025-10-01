import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Чтение CSV-файла в DataFrame
data = pd.read_csv('pressure.csv')
myDate = data.columns[0]       # Получаем имя первого столбца
upperPressure = data.columns[1]# Получаем имя второго столбца

#Выводим данные на экран
#for value in data[myDate]:
#    print(value)

plt.figure(figsize=(10, 5))  # Размер графика
plt.plot(data[myDate], data[upperPressure], marker='o', linestyle='-',
         color='green')

# Настройка оформления
plt.title('График верхнего давления по времени', fontsize=14)
plt.xlabel('Дата и время', fontsize=12)
plt.ylabel('Верхнее давление', fontsize=12)
plt.xticks(rotation=45)  # Поворот подписей по оси X
plt.grid(True)           # Включение сетки

# Отображение графика
plt.tight_layout()  # Автоматическая подгонка
plt.show()

print("Статистика")
print(f"Минимум: {np.min(data[upperPressure])}")
