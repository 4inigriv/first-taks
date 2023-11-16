
pesos = [0.5, 0.5, 0.5]
limiar = 0.6
taxa = 0.4
entradasClass = list(range(2))
entradasClass[1] = [[1, 1, 1],[1, 1, 0],[1, 0, 0]] #entradas para o treinamento 
entradasClass[0] = [[0, 1, 1],[0, 1, 0],[0, 0, 1]]

#função de ativação
def ativacao(soma):
    if soma >= 0:
        return 1
    else:
        return 0

#Fazendo avaliação do perceptron
def avaliar(entrada):
    somatoria = 0
    for i in range(len(entrada)):
        somatoria = somatoria + pesos[i] * entrada[i] 
    resultado = ativacao(somatoria - limiar)
    return resultado 

#treinamento árduo do neurônio
def treinar():
    global limiar 
    totalEntradas = 0
    acertos = 0
    for entradaN in range(3):
        for classeN in [1, 0]:
            valorEsperado = classeN #valores de saída esperados da classe [0] ou classe [1] 
            entrada = entradasClass[classeN][entradaN] #acessando a posição de certa entrada da classe
            resultado = avaliar(entrada)
            #calculo do erro
            erro = taxa * (valorEsperado - resultado)
            
            for i in range(len(pesos)):
            #atualizaçao dos pesos 
            #exemplo: 0,5 + 0,4(0)(0-1) = 0,5
                pesos[i] = pesos[i] + entrada[i] * erro            
            #atualizar do limiar
            limiar = limiar - erro
            totalEntradas += 1

            if erro == 0:
                acertos += 1
            #afim de debugar o código
            #print(f"{entrada}, {pesos}, {limiar:.2f}, {resultado:d}") 

    print(f"Acerto: {(acertos / totalEntradas) * 100:.2f}%") #calcula os acertos


if __name__ == "__main__":
    epocas = int(input("quantas épocas você deseja?"))
    for i in range(epocas):
        treinar()         
    #novas entradas
    novaEntrada = [0,0,0]
    classificacao = avaliar(novaEntrada)  
    print(f"{novaEntrada} pertence a classe {classificacao}") #em q classe ela pertence 
