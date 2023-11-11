import numpy as np

# Задание 1

def ListToNumpy(list):
    list = np.array(list, dtype = float)
    return list

a = [[1, 2 ,3], [4, 5, 6]]

print(ListToNumpy(a))


# Задание 2

def ShapeSizeCalc(arr):

    shape = np.shape(arr)
    size = np.size(arr)

    return f"Ответ: shape = {shape}, size = {size}"

array = np.array([[1, 2, 3], [4, 5, 6]])

print(ShapeSizeCalc(array))

3
def ArrayIndexing(arr, rows, val):
    result = []

    for row in rows:
        selected_row = arr[row]
        selected_elements = selected_row[::val]
        result.append(selected_elements)
    result_array = np.array(result)
    return result_array

arr = np.array([[1, 2, 3, 4],
                [1, 2, 3, 4],
                [1, 2, 3, 4]])
rows= (0, 1)
val = 2
print(ArrayIndexing(arr, rows, val))

# графики
import matplotlib.pyplot as plt

# 1
x=np.linspace(0,10,100)
y=x*6-2

plt.title('график y=6x-2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x,y)
plt.show()
# 2
x=np.linspace(0,10,100)
y1=6*(x**3)-2*x+8
y2=3*x+1

plt.figure(figsize=(9,9))

plt.subplot(2,1,1)
plt.plot(x,y1, x,y2)
plt.title('графики F(x,y)=6x**3-2x+8, F(x,y)=3x+1')
plt.ylabel('y1, y2')
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(x,y2,)
plt.xlabel('x')
plt.ylabel('y2')
plt.grid(True)
plt.show()



# 3
tovars=['помидоры','огурцы','тыква','свекла','редис','картофель']
counts=[100, 65, 12, 47, 89, 256]
plt.bar(tovars,counts)
plt.title('товары')
plt.xlabel('товары')
plt.ylabel('количество')
plt.show()


модули



import calendar

# 1
print(dir(calendar))


year = 2027
is_leap = calendar.isleap(year)
print(year, " год високосный:", is_leap)


day_of_week = calendar.weekday(1995, 6, 25)
days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
print(f"25 июня 1995 года был {days[day_of_week]}")


import calendar
year = 2023
calendar_2023 = calendar.TextCalendar().formatyear(year)
print(calendar_2023)

#2
from fuzzywuzzy import fuzz
strings = [
    ('Плохой код на самом деле не плохой.', 'Его просто не так поняли.'),
    ('Работает? Не трогай.', 'Работает? Не трогай.'),
    ('Работает? Не трогай.', 'Работает? Не трогай!')
]

for str1, str2 in strings:
    print(f"Схожесть между '{str1}' и '{str2}': {fuzz.ratio(str1, str2)}%")'''