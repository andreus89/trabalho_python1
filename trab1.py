#dicionários
med_dic={1:{'ID':1,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reação adversa mais comuns':0},
2:{'ID':2,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
3:{'ID':3,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
4:{'ID':4,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
5:{'ID':5,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
6:{'ID':6,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
7:{'ID':7,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
8:{'ID':8,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
9:{'ID':9,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0},
10:{'ID':10,'Nome Comercial':0,'Composto principal':0,'Fórmula Química':0,'Meia-vida de eliminação':0,'Número de comprimidos por embalagem':0,'Preço da embalagem em 3 fornecedores':{'A':0,'B':0,'C':0},'Quantidade do composto principal por comprimido':0,'Dose diária para um adulto':0,'As 3 reações adversa mais comuns':0}
}


#listas
nc_list=[]
cp_list=[]
fq_list=[]
mde_list=[]
nce_list=[]
pef_list=[]
apef_list=[]
bpef_list=[]
cpef_list=[]
qcc_list=[]
dda_list=[]
rac_list=[]


#input
for i in range(1,11):    
    
    med_dic[i]['Nome Comercial']=input('Nome Comercial?')
    nc_list.append(med_dic[i]['Nome Comercial'])
    
    med_dic[i]['Composto principal']=input('Composto principal?')
    cp_list.append(med_dic[i]['Composto principal'])
    
    med_dic[i]['Fórmula Química']=input('Fórmula Química?')
    fq_list.append(med_dic[i]['Fórmula Química'])
    
    med_dic[i]['Meia-vida de eliminação']=input('Meia-vida de eliminação?')
    mde_list.append(med_dic[i]['Meia-vida de eliminação'])
    
    med_dic[i]['Número de comprimidos por embalagem']=int(input('Número de comprimidos por embalagem?'))
    nce_list.append(med_dic[i]['Número de comprimidos por embalagem'])
    nce=med_dic[i]['Número de comprimidos por embalagem']
    
    med_dic[i]['Preço da embalagem em 3 fornecedores']['A']=float(input('Preço da embalagem em 3 fornecedores? Embalagem A: R$'))
    apef_list.append(med_dic[i]['Preço da embalagem em 3 fornecedores']['A'])
    med_dic[i]['Preço da embalagem em 3 fornecedores']['B']=float(input('Preço da embalagem em 3 fornecedores? Embalagem B: R$'))
    bpef_list.append(med_dic[i]['Preço da embalagem em 3 fornecedores']['B'])
    med_dic[i]['Preço da embalagem em 3 fornecedores']['C']=float(input('Preço da embalagem em 3 fornecedores? Embalagem C: R$'))
    cpef_list.append(med_dic[i]['Preço da embalagem em 3 fornecedores']['C'])
    pef_list.append(med_dic[i]['Preço da embalagem em 3 fornecedores'])

    
    med_dic[i]['Quantidade do composto principal por comprimido']=input('Quantidade do composto principal por comprimido?')
    qcc_list.append(med_dic[i]['Quantidade do composto principal por comprimido'])
    
    med_dic[i]['Dose diária para um adulto']=input('Dose diária para um adulto?')
    dda_list.append(med_dic[i]['Dose diária para um adulto'])
    
    med_dic[i]['As 3 reações adversa mais comuns']=input('As 3 reações adversa mais comuns?')
    rac_list.append(med_dic[i]['As 3 reações adversa mais comuns'])
    
        
    if i==10:
        break
    else:
        continuar=input("Digite 'p' para parar: ")
        if continuar == "p":
            break

        

#gráficos
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
index = np.arange(i)
bar_width = 0.15
opacity = 0.8

rects1 = plt.bar(index, apef_list, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Embalagem A')
 
rects2 = plt.bar(index + bar_width, bpef_list, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Embalagem B')

rects3 = plt.bar(index + bar_width + bar_width, cpef_list, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Embalagem C')

plt.xlabel('Medicamentos')
plt.ylabel('Reais')
plt.title('Valores por Medicamento')
plt.xticks(index + bar_width, (nc_list))
plt.legend()
 
plt.tight_layout()
plt.show()
