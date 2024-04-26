#1. Importa el paquete NUMPY bajo el nombre np.
import numpy as np

#2. Imprime la versión de NUMPY y la configuración.
print(np.version.version)

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

a = np.random.random((2,3,5))
a1 = np.random.randint(10, size=(2,3,5))

#4. Imprime a.
print(a)

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

b = np.ones((5,2,3))

#6. Imprime b.

print(b)

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

print(a.size == b.size)
# Según la función de python, sí que tendrían el mismo tamaño. Porque ambos tienen 30 de size total.

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

try:
    print(a+b)
except ValueError:
    print ("The sum could not be completed")
#No es posible sumar porque tienen la misma forma

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

c = np.transpose(b, (1,2,0))
print(c)

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

d = a+c
print(d)

#Ahora funciona porque sí que tienen la misma forma (de rows y columnas)

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

print("separation line ----")
print(a)
print("separation line ----")
print(d)
print("separation line ----")
# d es simplemente a pero con todos los números + 1

#12. Multiplica a y c. Asigna el resultado a e.

e = a*c
print(e)


#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

print(e == a)

#Lo es porque se ha multiplicado por 1

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print(d_max, d_min, d_mean)


#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

f = np.zeros((2,3,5))


"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[(d == d_mean)] = 50
f[(d == d_max)] = 100
f[(d == d_min)] = 0

print(f)
print('separation ----')
def comprobar_numeros(d, mean, max, min, f):

        for i in range(d.shape[0]):
                for j in range(d.shape[1]):
                        for l in range(d.shape[2]):
                                if l > d_min and l < d_mean:
                                        f[i,j,l] = 25
                                elif l > d_mean and l <d_max:
                                        f[i,j,l] = 75
                                elif l == d_mean:
                                        f[i,j,l] = 50
                                elif l == d_max:
                                        f[i,j,l] = 100
                                elif l == d_min:
                                        f[i,j,l] = 0
        return f
                        

result_using_forloop = comprobar_numeros(d, d_mean,d_max, d_min, f)
print(result_using_forloop)


"""
#17. Imprime d y f. ¿Tienes el f esperado?
Por ejemplo, si tu d es:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Tu f debería ser:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print(d)
print(f)
print(result_using_forloop)


"""
#18. Pregunta de bonificación: en lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena 
("A", "B", "C", "D" y "E") para etiquetar los elementos del array? Esperas el resultado sea:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
De nuevo, no necesitas Numpy en esta pregunta.
"""

# 0.75 = 'D'
# 0.25 = 'B'
# 0.5 = 'C'
# 0 = 'A'
# 1 = 'E'

new_f = np.empty((2,3,5),dtype=object)

new_f[(d > d_min) & (d < d_mean)] = 'B'
new_f[(d > d_mean) & (d < d_max)] = 'D'
new_f[(d == d_mean)] = 'C'
new_f[(d == d_max)] = 'E'
new_f[(d == d_min)] = 'A'

print(new_f)