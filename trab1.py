keys=['Nome Comercial','Composto principal','Fórmula Química']
v=[0,0,0]
for i in range(1,5):
    v[i]=input('Nome Comercial? ')
    v[i]=input('Composto principal? ')
    v[i]=input('Fórmula Química? ')
    i = dict(zip(keys, v))
    print(i)