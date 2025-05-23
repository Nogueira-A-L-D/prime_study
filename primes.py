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
primes_quantity = int(input("How much prime numbers? :> "))


# Inicialização das funções e a busca pelos primos
tempo_inicial_primos = time.time()
print("Getting Primes")
f_superior = LogFunction(math.sqrt(5))
primes = list(primerange(1, nextprime(1,primes_quantity)+1))  # 15485863 é o 1.000.000º primo
f_inferior = LogFunction(math.sqrt(7))
print("Primes Obtained\n")
tempo_final_primos = time.time()


sup_list = []
inf_list = []
falhas_margem = "No"
count = 1

# Teste para ver se as funções servem como margem para os números primos
tempo_inicial_teste = time.time()
print("Beggining test...")
for i in primes:
    
    sup_y = f_superior.on(count)
    inf_y = f_inferior.on(count)

    sup_list.append(sup_y)
    inf_list.append(inf_y)

    if (sup_y<i or i<inf_y): # Caso de falha nas nas funções de margem, relatar no terminal
        print("Fail: margin doesn't contain the value.")
        falhas_margem = "Yes"
        break
    count = count + 1

    percentage = (count/primes_quantity)*100
    old_percentage = ((count-1)/primes_quantity)*100
    if int(percentage) > int(old_percentage):
        print(str(int(percentage)) + "%")           # Acompanhamento por porcentagem ao usuário
tempo_final_teste = time.time()


save = 'y'
if not autosave:
    save = input("Do you want to save changes?[y/n] :> ")


# Salvamento caso desejado
tempo_inicial_salvamento = time.time()
if save=='y' or autosave:
    # Salvar em um arquivo .txt separado por vírgulas
    with open("results/primes.txt", "w") as f:
        f.write(','.join(map(str, primes)))
    with open("results/superior.txt", "w") as f:
        f.write(','.join(map(str,sup_list)))
    with open("results/inferior.txt", "w") as f:
        f.write(','.join(map(str,inf_list)))
tempo_final_salvamento = time.time()


# Armazenamento das informações no log
with open("results/log.txt", "a+") as f:
    if save=='y' or autosave:
        f.write("Program Duration: " + str(int(time.time()-tempo_inicial_execucao)) + " s\n Quantity of Primes: " + str(primes_quantity) + "\n Time to Get Primes: " + str(int(tempo_final_primos - tempo_inicial_primos)) + " s\n Time to Test Margin: " + str(int(tempo_final_teste - tempo_inicial_teste)) + " s\n Time to Save: " + str(int(tempo_final_salvamento - tempo_inicial_salvamento)) + " s\n Fails in Margin: " + falhas_margem +"\n\n")
    else:
        f.write("Programa Duration: " + str(int(time.time()-tempo_inicial_execucao)) + " s\n Quantity of Primes: " + str(primes_quantity) + "\n Time to Get Primes: " + str(int(tempo_final_primos - tempo_inicial_primos)) + " s\n Time to Test Margin: " + str(int(tempo_final_teste - tempo_inicial_teste)) + " s\n Fails in Margin: " + falhas_margem +"\n\n")