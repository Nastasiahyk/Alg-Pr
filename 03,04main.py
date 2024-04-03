#Задание26
def generate_sequences(a, b, s, n):    
    x = [a]
    y = [b] 
n = 0
for i in range(2, n+1):       
    x_k = 0.5 * (x[i-2] + y[i-2])
    y_k = 0.5 * (x_k + y[i-2])        
    x.append(x_k)     
    y.append(y_k)
a = 10  # Значение ab = 7   # Значение b
s = 5   # Значение sn = 10  # Количество элементов для генерации
x_sequence, y_sequence = generate_sequences(a, b, s, n)
print("Последовательность x_k:", x_sequence)
print("Последовательность y_k:", y_sequence)
#Задание28
def find_average(numbers):    
    negative_sum = 0
    negative_count = 0   
    non_negative_sum = 0
    non_negative_count = 0    
    for num in numbers:       
        if num == -1000:
            break       
            if num < 0:
            negative_sum += num          
            negative_count += 1
        else:            non_negative_sum += num
            non_negative_count += 1    
    negative_average = negative_sum / negative_count if negative_count != 0 else 0    
    non_negative_average = non_negative_sum / non_negative_count if non_negative_count != 0 else 0
        return negative_average, non_negative_average
numbers = []
while True:    num = float(input("Введите число (для окончания введите -1000): "))
    if num == -1000:        break
    numbers.append(num)
neg_avg, non_neg_avg = find_average(numbers)
print("Среднее арифметическое отрицательных чисел:", neg_avg)
print("Среднее арифметическое неотрицательных чисел:", non_neg_avg
