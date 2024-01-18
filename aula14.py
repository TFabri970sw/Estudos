a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} a={nome1} b={nome2} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

nome = 'Thiago'
idade = 16
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

nome = "Thiago"
idade = 16 
formato = '{n} tem {i} anos'
print(formato.format(n=nome , i=idade))