# By Andre Luis Dias Nogueira

# Download VS Code and Python 3.13.3 (or a Python IDE)
# Use "pip install virtualenv" and create a virtual enviroment with "python -m venv venv"
# Use "venv/Scripts/activate.ps1" and "pip install -r requirements.txt" to be able to continue
import time, math
from sympy.ntheory.generate import primerange, nextprime

# Mathematical function to be used to create a margin area that always have primes
class LogFunction:
    
    def __init__(self, base):
        self.base = base

    def on(self, x):
        return math.log(x, self.base) * x + (1/x) + (1)

# Enable/disable autosave
autosave = False

# Counting the time of the program
initial_program_time = time.time()


# Get amount of primes that will be used to work
primes_quantity = int(input("How much prime numbers? :> "))


# Inicializing functions and the prime list
initial_primes_time = time.time()
print("Getting Primes")
f_superior = LogFunction(math.sqrt(5))
primes = list(primerange(1, nextprime(1,primes_quantity)+1))
f_inferior = LogFunction(math.sqrt(7))
print("Primes Obtained\n")
final_primes_time = time.time()

# Creating lists to save data and find failures
sup_list = []
inf_list = []
margin_failure = "No"
count = 1

# Test to check if these functions are able to create a margin around the area of prime numbers distribution
initial_test_time = time.time()
print("Beggining test...")
for i in primes:
    
    sup_y = f_superior.on(count)
    inf_y = f_inferior.on(count)

    sup_list.append(sup_y)
    inf_list.append(inf_y)

    if (sup_y<i or i<inf_y): # If the margin fails, mark on log or shell
        print("Fail: margin doesn't contain the value.")
        margin_failure = "Yes"
        break
    count = count + 1

    percentage = (count/primes_quantity)*100
    old_percentage = ((count-1)/primes_quantity)*100
    if int(percentage) > int(old_percentage):
        print(str(int(percentage)) + "%")           # Users can see the progress with this percentage
final_test_time = time.time()


save = 'y'
if not autosave:
    save = input("Do you want to save changes?[y/n] :> ")


# Saving if enabled
initial_save_time = time.time()
if save=='y' or autosave:
    # Save informations in a .txt archive separated by commas
    with open("results/primes.txt", "w") as f:
        f.write(','.join(map(str, primes)))
    with open("results/superior.txt", "w") as f:
        f.write(','.join(map(str,sup_list)))
    with open("results/inferior.txt", "w") as f:
        f.write(','.join(map(str,inf_list)))
final_save_time = time.time()


# Storing informations on log
with open("results/log.txt", "a+") as f:
    if save=='y' or autosave:
        f.write("Program Duration: " + str(int(time.time()-initial_program_time)) + " s\n Quantity of Primes: " + str(primes_quantity) + "\n Time to Get Primes: " + str(int(final_primes_time - initial_primes_time)) + " s\n Time to Test Margin: " + str(int(final_test_time - initial_test_time)) + " s\n Time to Save: " + str(int(final_save_time - initial_save_time)) + " s\n Fails in Margin: " + margin_failure +"\n\n")
    else:
        f.write("Program Duration: " + str(int(time.time()-initial_program_time)) + " s\n Quantity of Primes: " + str(primes_quantity) + "\n Time to Get Primes: " + str(int(final_primes_time - initial_primes_time)) + " s\n Time to Test Margin: " + str(int(final_test_time - initial_test_time)) + " s\n Fails in Margin: " + margin_failure +"\n\n")

# Conclusion:
# Until now, all prime values are inside the margin, being necessary to create the inverse of this function to check if all x positions
# are inside the limits of these functions, confirming that we can find a function that should approximate the prime distribution and,
# furthemore, could be used to find the function that describe primes, being usefull to improve the decodification of encrypted data.