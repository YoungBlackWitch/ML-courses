#Задача 3. Минимизация негладкой функции

#Теперь рассмотрим функцию h(x) = int(f(x)) на том же отрезке [1, 30], т.е. теперь каждое значение f(x) приводится к типу int и функция 
#принимает только целые значения.

#Такая функция будет негладкой и даже разрывной, а ее график будет иметь ступенчатый вид. Убедитесь в этом, построив график h(x) 
#с помощью matplotlib.

#Попробуйте найти минимум функции h(x) с помощью BFGS, взяв в качестве начального приближения x=30. Получившееся значение функции – 
#ваш первый ответ в этой задаче.

#Теперь попробуйте найти минимум h(x) на отрезке [1, 30] с помощью дифференциальной эволюции. Значение функции h(x) в точке минимума – 
#это ваш второй ответ в этом задании. Запишите его через пробел после предыдущего.

#Обратите внимание на то, что полученные ответы различаются. Это ожидаемый результат, ведь BFGS использует градиент (в одномерном случае – 
#производную) и явно не пригоден для минимизации рассмотренной нами разрывной функции. Попробуйте понять, почему минимум, найденный BFGS, 
#именно такой (возможно в этом вам поможет выбор разных начальных приближений).

#Выполнив это задание, вы увидели на практике, чем поиск минимума функции отличается от глобальной оптимизации, и когда может быть 
#полезно применить вместо градиентного метода оптимизации метод, не использующий градиент. Кроме того, вы попрактиковались в использовании 
#библиотеки SciPy для решения оптимизационных задач, и теперь знаете, насколько это просто и удобно.


from math import *
from scipy.optimize import minimize, differential_evolution


def fun(x):
    f = sin(x/5.) * exp(x/10.) + 5 * exp(-x/2.)
    return int(f)


res1 = minimize(fun, [30], method='BFGS')
print(fun(res1.x))

res2 = differential_evolution(fun, [(1, 30)])
print(fun(res2.x))

#Ответ: -5, -11