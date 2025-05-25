# By Andre Luis Dias Nogueira

# Download VS Code and Python 3.13.3 (or a Python IDE)
# Use "pip install virtualenv" and create a virtual enviroment with "python -m venv venv"
# Use "venv/Scripts/activate.ps1" and "pip install -r requirements.txt" to be able to continue
import time, math
from sympy.ntheory.generate import primerange, nextprime

# Mathematical function to be used to create a margin area that always have primes
class LogFunction:

    e=2.718281828459045235360 # Euler's number
    max_iteration=10 # Limit of iterations in Newton-Raphson algorithm

    def __init__(self, base):
        self.base = base

    def ln(self,x):
        return math.log(x,self.e)

    def on(self, x):
        return math.log(x, math.sqrt(self.base)) * x + (1/x) + (1)
    
    def derivate(self, x):
        return (2*self.ln(x)+2)/self.ln(self.base) - (1/x**2)
    
    def inverse(self, count, prime):
        x = count
        for i in range(self.max_iteration):
            x = x-(self.on(x) - prime)/self.derivate(x)
        return x  

# Enable/disable autosave
autosave = False

# Counting the time of the program
initial_program_time = time.time()


# Get amount of primes that will be used to work
primes_quantity = int(input("How much prime numbers? :> "))


# Initializing functions and the prime list
initial_primes_time = time.time()
print("Getting Primes")

f_superior = LogFunction(5)
primes = list(primerange(1, nextprime(1,primes_quantity)+1))
f_inferior = LogFunction(7)

print("Primes Obtained\n")
final_primes_time = time.time()

# Creating lists to save data and find failures
sup_list_y = []
inf_list_y = []

sup_list_x = []
inf_list_x = []

margin_failure = "No"
count = 1

# Test to check if these functions are able to create a margin around the area of prime numbers distribution
initial_test_time = time.time()
print("Beggining test...")
for i in primes:
    
    # Finding the nearest value for prime in each function
    sup_y = f_superior.on(count)
    inf_y = f_inferior.on(count)

    sup_list_y.append(sup_y)
    inf_list_y.append(inf_y)

    # Finding the position in which the prime number is, using
    # the inverse of the function by Newton-Raphson algorithm
    sup_x = f_superior.inverse(count,i)
    inf_x = f_inferior.inverse(count,i)

    sup_list_x.append(sup_x)
    inf_list_x.append(inf_x)

    if (sup_y<i or i<inf_y or sup_x>count or inf_x<count): # If the margin fails, mark on log and shell
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
    
    with open("results/superior_primes.txt", "w") as f:
        f.write(','.join(map(str,sup_list_y)))
    
    with open("results/superior_count.txt", "w") as f:
        f.write(','.join(map(str,sup_list_x)))
    
    with open("results/inferior_primes.txt", "w") as f:
        f.write(','.join(map(str,inf_list_y)))
    
    with open("results/inferior_count.txt", "w") as f:
        f.write(','.join(map(str,inf_list_x)))
final_save_time = time.time()


# Storing informations on log
with open("results/log.txt", "a+") as f:
    if save=='y' or autosave:
        f.write("Program Duration: " + str(int(time.time()-initial_program_time)) + " s\n Quantity of Primes: " + str(primes_quantity) + "\n Time to Get Primes: " + str(int(final_primes_time - initial_primes_time)) + " s\n Time to Test Margin: " + str(int(final_test_time - initial_test_time)) + " s\n Time to Save: " + str(int(final_save_time - initial_save_time)) + " s\n Fails in Margin: " + margin_failure +"\n\n")
    else:
        f.write("Program Duration: " + str(int(time.time()-initial_program_time)) + " s\n Quantity of Primes: " + str(primes_quantity) + "\n Time to Get Primes: " + str(int(final_primes_time - initial_primes_time)) + " s\n Time to Test Margin: " + str(int(final_test_time - initial_test_time)) + " s\n Fails in Margin: " + margin_failure +"\n\n")

# To close the virtual enviroment, just use "deactivate"

# Conclusion:
# Until now, all prime values are inside the margin x and y of the functions, showing that these two functions can create a margin where
# all primes are inside, confirming we can find a function that should approximate a prime distribution and could be used to find a
# function that describe primes, being usefull to improve the decodification of encrypted data.