# Gerar os primeiros 1 milhão de números primos
import math, time
from sympy.sympy.ntheory.generate import primerange, nextprime

# habilitação de salvamento automático
autosave = False

# função a ser testada
class LogFunction:
    
    def __init__(self, base):
        self.base = base

    def on(self, x):
        return math.log(x, self.base) * x + (1/x) + (1)


tempo_inicial_execucao = time.time()


# Digitação da quantidade de primos a serem obtidos
primes_quantity = int(input("Qual a quantidade de primos? :> "))


# Inicialização das funções e a busca pelos primos
tempo_inicial_primos = time.time()
print("Obtendo Primos")
f_superior = LogFunction(math.sqrt(5))
primes = list(primerange(1, nextprime(1,primes_quantity)+1))  # 15485863 é o 1.000.000º primo
f_inferior = LogFunction(math.sqrt(7))
print("Primos Obtidos\n")
tempo_final_primos = time.time()


sup_list = []
inf_list = []
falhas_margem = "Nao"
count = 1

# Teste para ver se as funções servem como margem para os números primos
tempo_inicial_teste = time.time()
print("Teste iniciando...")
for i in primes:
    
    sup_y = f_superior.on(count)
    inf_y = f_inferior.on(count)

    sup_list.append(sup_y)
    inf_list.append(inf_y)

    if (sup_y<i or i<inf_y): # Caso de falha nas nas funções de margem, relatar no terminal
        print("Falha na margem")
        falhas_margem = "Sim"
        break
    count = count + 1

    percentage = (count/primes_quantity)*100
    old_percentage = ((count-1)/primes_quantity)*100
    if int(percentage) > int(old_percentage):
        print(str(int(percentage)) + "%")           # Acompanhamento por porcentagem ao usuário
tempo_final_teste = time.time()


save = 'y'
if not autosave:
    save = input("Deseja salvar?[y/n] :> ")


# Salvamento caso desejado
tempo_inicial_salvamento = time.time()
if save=='y' or autosave:
    # Salvar em um arquivo .txt separado por vírgulas
    with open("resultados/primos.txt", "w") as f:
        f.write(','.join(map(str, primes)))
    with open("resultados/superior.txt", "w") as f:
        f.write(','.join(map(str,sup_list)))
    with open("resultados/inferior.txt", "w") as f:
        f.write(','.join(map(str,inf_list)))
tempo_final_salvamento = time.time()


# Armazenamento das informações no log
with open("resultados/log.txt", "a+") as f:
    if save=='y' or autosave:
        f.write("Duracao do Programa: " + str(int(time.time()-tempo_inicial_execucao)) + " s\n Quantidade de Primos: " + str(primes_quantity) + "\n Tempo de Coleta Primos: " + str(int(tempo_final_primos - tempo_inicial_primos)) + " s\n Tempo de Teste: " + str(int(tempo_final_teste - tempo_inicial_teste)) + " s\n Tempo de Salvamento: " + str(int(tempo_final_salvamento - tempo_inicial_salvamento)) + " s\n Falhas na Margem: " + falhas_margem +"\n\n")
    else:
        f.write("Duracao do Programa: " + str(int(time.time()-tempo_inicial_execucao)) + " s\n Quantidade de Primos: " + str(primes_quantity) + "\n Tempo de Coleta Primos: " + str(int(tempo_final_primos - tempo_inicial_primos)) + " s\n Tempo de Teste: " + str(int(tempo_final_teste - tempo_inicial_teste)) + " s\n Falhas na Margem: " + falhas_margem +"\n\n")