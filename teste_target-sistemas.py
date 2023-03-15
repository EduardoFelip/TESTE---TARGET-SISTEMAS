QUESTÃO 1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);


Ao final do processamento, qual será o valor da variável SOMA?

                             RESPOSTA:
    
  No final do processamento, o valor da variável SOMA será 91.

Isso ocorre porque o código acima está calculando a soma dos números de 1 a 13, que é uma série aritmética.
A variável K é usada como contador para percorrer a série e a variável SOMA é usada para acumular o valor total da série.

O laço "enquanto" faz com que o bloco de código dentro dele seja executado repetidamente
enquanto a condição K < INDICE for verdadeira. Dentro desse bloco de código,
a variável K é incrementada em 1 a cada iteração e a variável SOMA é atualizada somando-se o valor de K.

Portanto, o valor final de SOMA será a soma dos números de 1 a 13, que é 91.


QUESTÃO 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
 Como a linguagem não foi definida pelo criador do teste vou escolher PYTHON usando, if,else, while que são estruturas de repetição.
                               RESPOSTA:
      Código
  # recebe um número do usuário
num = int(input("Digite um número: "))

# inicializa a sequência de Fibonacci com os primeiros dois números
fibonacci = [0, 1]

# calcula os próximos números da sequência até o número informado ser ultrapassado
while fibonacci[-1] < num:
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo) #usando append que adiciona um item ao fim lista.

# verifica se o número informado pertence à sequência de Fibonacci
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
    
    
    
QUESTÃO 3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, _9_

b) 2, 4, 8, 16, 32, 64, _128_

c) 0, 1, 4, 9, 16, 25, 36, _49_

d) 4, 16, 36, 64, _100_

e) 1, 1, 2, 3, 5, 8, _13_

f) 2,10, 12, 16, 17, 18, 19, _200_

QUESTÃO 4) Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h 
e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. 
Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.
b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais
para passar em cada um deles e o carro possui tag de pedágio (Sem Parar).
c) Explique como chegou no resultado.

                            RESPOSTA: #USANDO MRU, MOVIMENTO RETILÍNIO UNIFORME.
Determinamos o local de cruzamento, coloquei o ponto de referência em Ribeirão Preto, entao a equação horária
do carro é : x1 = v1.t
Como o caminhão sai de um local 100 km distante do ponto de referência e se aproxima dele, sua equação
horária é : x2 =100km - v2.t
Como o caminhão tem 2 pedágios para passar e vai perder 5 minutos em cada um deles, podemos calcular o tempo de viagem
sem os pedágios. 
 Tsp = 100KM/80KM/H = 1,25 H. #(onde Tsp = tempo sem pedágio).
Porém como perde 10 minutos ou 0,17 horas #(transformando em horas fica 0,17 horas aproximadamente arredondando, basta dividir 10/60 min)
nos pedágios, o  tempo de viagem para o caminhão será de 1,25h + 0,17h = 1,42 hr. Portanto sua velocidade média é :
v2 = 100 km/ 1,42 h = 70,6  km/h.
  Nas equações horárias, podemos igualar ambas para achar o ponto em que o carro e o caminhão se cruzam:
    t = x1/v1
    t = x2-100km/-v2
    x1 = x2 => x/v1 = x-100km/-v2 #reescrevendo
    -v2.x = v1.x-v1.100 km #reorganizando
    x = v1.100km/v1+v2 = 110km/h.100km / 110km/h + 70,6 km/h
    logo após feito os cálculos temos que  x = 60,9km

Essa é a distância da cidade de Ribeirão Preto em que o carro e o caminhão se cruzam, ambos á mesma distãncia.
    
QUESTÃO 5) Escreva um programa que inverta os caracteres de um string.

                            IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
                      
                            RESPOSTA:
      CÓDIGO em python:
# recebe uma string do usuário
string = input("Digite uma string: ")

# cria uma nova string vazia para armazenar o resultado
string_invertida = ""

# percorre a string original de trás para frente
for i in range(len(string) - 1, -1, -1):
    # adiciona cada caractere da string original na nova string
    string_invertida += string[i]

# imprime a string invertida
print("A string invertida é:", string_invertida)

     
