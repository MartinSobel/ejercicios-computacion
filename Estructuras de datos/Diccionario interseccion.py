# Crear 2 conjuntos de animales. Mostrar su unión y su intersección. Mostrar si tiene como elemento “avestruz”.

animales1 = {'perro', 'gato', 'conejo', 'hamster', 'pez', 'serpiente', 'tortuga', 'pajaro', 'pez', 'serpiente', 'tortuga', 'pajaro'}
animales2 = {'gato', 'conejo', 'hamster', 'pez', 'serpiente', 'tortuga', 'pajaro', 'pez', 'serpiente', 'tortuga', 'pajaro', 'avestruz'}

todosLosAnimales = animales1 | animales2
animalesEnComun = animales1 & animales2
contieneAvestruz = 'avestruz' in todosLosAnimales

print(todosLosAnimales)
print(animalesEnComun)
print(contieneAvestruz)