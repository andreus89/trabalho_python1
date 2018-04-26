import sys
import matplotlib.pyplot as plt
import numpy as np

def isReal(txt):
    try:
        float(txt)
        return True
    except ValueError:
        return False


#dicionários
med_dic={1:{'ID':1,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
2:{'ID':2,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
3:{'ID':3,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
4:{'ID':4,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
5:{'ID':5,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
6:{'ID':6,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
7:{'ID':7,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
8:{'ID':8,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
9:{'ID':9,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}},
10:{'ID':10,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':{'A':0,'B':0,'C':0}}
}


#listas
nc_list=[]
cp_list=[]
fq_list=[]
mde_list=[]
nce_list=[]
pef_list=[]
mpef_list=[]
qcc_list=[]
dda_list=[]
rac_list=[]
mqcc_list=[]


#input
for i in range(1,11):    
    
    while True:
        med_dic[i]['Nome Comercial']=(input('Nome Comercial?'))
        nc_list.append(med_dic[i]['Nome Comercial'])
        nc=med_dic[i]['Nome Comercial']
        if nc == "exit":
            sys.exit('Parada abrupta do programa!')
        elif nc.isalpha():
            break
        print("Valor inválido!")
    
    while True:
        med_dic[i]['Composto principal']=input('Composto principal?')
        cp_list.append(med_dic[i]['Composto principal'])
        cp=med_dic[i]['Composto principal']
        if cp == "exit":
            sys.exit('Parada abrupta do programa!')
        elif cp.isalpha():
            break
        print("Valor inválido!")
    
    while True:
        med_dic[i]['Fórmula Química']=input('Fórmula Química?')
        fq_list.append(med_dic[i]['Fórmula Química'])
        fq=med_dic[i]['Fórmula Química']
        if fq == "exit":
            sys.exit('Parada abrupta do programa!')
        elif fq.isalnum():
            break
        print("Valor inválido!")
    
    while True:
        med_dic[i]['Meia-vida de eliminação']=input('Meia-vida de eliminação (horas)?')
        mde_list.append(med_dic[i]['Meia-vida de eliminação'])
        mde=med_dic[i]['Meia-vida de eliminação']
        if mde == "exit":
            sys.exit('Parada abrupta do programa!')
        elif mde.isdigit():
            break
        print("Valor inválido!")
    
    while True:    
        med_dic[i]['Número de comprimidos por embalagem']=input('Número de comprimidos por embalagem?')
        nce_list.append(med_dic[i]['Número de comprimidos por embalagem'])
        nce=med_dic[i]['Número de comprimidos por embalagem']
        if nce == "exit":
            sys.exit('Parada abrupta do programa!')
        elif nce.isdigit():
            break
        print("Valor inválido!")
    
    while True:
        try:
            med_dic[i]['Preço da embalagem em 3 fornecedores']['A']=float(input('Preço da embalagem em 3 fornecedores? Embalagem A: R$'))
            a=med_dic[i]['Preço da embalagem em 3 fornecedores']['A']
            break
        except ValueError:
            print("Valor inválido!")
            continue
        
    while True:
        try:
            med_dic[i]['Preço da embalagem em 3 fornecedores']['B']=float(input('Preço da embalagem em 3 fornecedores? Embalagem B: R$'))
            b=med_dic[i]['Preço da embalagem em 3 fornecedores']['B']
            break
        except ValueError:
            print("Valor inválido!")
            continue
        
    while True:
        try:
            med_dic[i]['Preço da embalagem em 3 fornecedores']['C']=float(input('Preço da embalagem em 3 fornecedores? Embalagem C: R$'))
            c=med_dic[i]['Preço da embalagem em 3 fornecedores']['C']
            break
        except ValueError:
            print("Valor inválido!")
            continue   
    mpef=(a+b+c)/3
    mpef_list.append(mpef)                
        
    while True:
        try:
            med_dic[i]['Quantidade do composto principal por comprimido']=float(input('Quantidade do composto principal por comprimido?(em mg)'))
            qcc_list.append(med_dic[i]['Quantidade do composto principal por comprimido'])
            qcc=med_dic[i]['Quantidade do composto principal por comprimido']
            break
        except ValueError:
            print("Valor inválido!")
            continue    
    mqcc=mpef/qcc
    mqcc_list.append(mqcc) 
        
    while True:
        med_dic[i]['Dose diária para um adulto']=input('Dose diária para um adulto?(em mg)')
        dda_list.append(med_dic[i]['Dose diária para um adulto'])
        dda=med_dic[i]['Dose diária para um adulto']
        if dda == "exit":
            sys.exit('Parada abrupta do programa!')
        elif isReal(dda):
            break
        print("Valor inválido!")
    
    while True:
        med_dic[i]['As 3 reações adversa mais comuns']['A']=input('As 3 reações adversas mais comuns? Reação A: ')
        a=med_dic[i]['As 3 reações adversa mais comuns']['A']
        if a == "exit":
            sys.exit('Parada abrupta do programa!')
        elif a.isalpha():
            break
        print("Valor inválido!")
    while True:
        med_dic[i]['As 3 reações adversa mais comuns']['B']=input('As 3 reações adversas mais comuns? Reação B: ')
        b=med_dic[i]['As 3 reações adversa mais comuns']['B']
        if b == "exit":
            sys.exit('Parada abrupta do programa!')
        elif b.isalpha():
            break
        print("Valor inválido!")
    while True:
        med_dic[i]['As 3 reações adversa mais comuns']['C']=input('As 3 reações adversas mais comuns? Reação C: ')
        c=med_dic[i]['As 3 reações adversa mais comuns']['C']
        if c == "exit":
            sys.exit('Parada abrupta do programa!')
        elif c.isalpha():
            break
        print("Valor inválido!")
    rac_list.append(med_dic[i]['As 3 reações adversa mais comuns'])
    
        
    if i==10:
        break
    else:
        continuar=input("Digite 'p' para parar: ")
        if continuar == "p":
            break

        

#gráfico 1
fig, ax = plt.subplots()
index = np.arange(i)
bar_width = 0.15
opacity = 0.8

rects1 = plt.bar(index, mpef_list, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Média de Preço')

plt.xlabel('Medicamentos')
plt.ylabel('Reais(R$)')
plt.title('Valores por Medicamento')
plt.xticks(index, (nc_list))
plt.legend()
 
plt.tight_layout()
plt.show()


#gráfico 2
fig1, ax1 = plt.subplots()
index = np.arange(i)
bar_width = 0.15
opacity = 0.8

rects1 = plt.bar(index, mqcc_list, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Média por 1 mg')

plt.xlabel('Medicamentos')
plt.ylabel('Reais(R$)')
plt.title('Média de Preço por Miligramas do Componente Principal')
plt.xticks(index, (nc_list))
plt.legend()
 
plt.tight_layout()
plt.show()
