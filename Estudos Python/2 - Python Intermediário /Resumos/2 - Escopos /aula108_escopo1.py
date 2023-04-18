def escopo():
    x = 2
    print('Este é o escopo segundário {0}'.format(x))
    def escopo_2():
        global x
        x = 3
        print('Este é o escopo terciario {0}'.format(x))
    escopo_2()

x = 1
print('Este é o x global sem ser mudado {0}'.format(x))
escopo()
print('Este é o x global mudado {0}'.format(x))

#acessando escopo global:
def mudar_x_global():
    global x
    x = 23

mudar_x_global()
print(x)