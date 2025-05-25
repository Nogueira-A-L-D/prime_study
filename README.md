# Study of Primes with Log Functions

Studying primes and trying to find a approximation using log functions with irrational base, computational tests and algebra analysis of graphs.

The first step in this search was the use of Geogebra's platform to see functions that follows the behavior of prime numbers. The tests began with the Prime Number Theorem, using:

$$ln(x) * x + \frac{1}{x} + 1$$

When checking the graph, I saw that this function could create a inferior margin. Then, I started to check other options, such as the change of $ln(x)$ to $\sqrt{x}$, but the results raises faster, however creates a superior margin:

$$\sqrt{x} * x + \frac{1}{x} + 1$$

So, I decided to test other functions that raises in log, but around $e$ value, to get a good superior margin and inferior margin, finding respectively:

$$\log_{\sqrt{5}}(x) \cdot x + \frac{1}{x} + 1$$

$$\log_{\sqrt{7}}(x) \cdot x + \frac{1}{x} + 1$$

As I got then, I needed to prove that these functions creates a small interval between them that contains all primes. For this, I created margin_check.py.

This program will get the quantity of primes you want to test and see if all of them will be inside of the margin created by these two functions. For this, it gets the list of primes and test, for each one, if the number of the function evaluated at x is greater (or less) than the prime tested ("greater" in case of the superior function, "less" in case of the inferior function). If it fails, it will be marked in log for future analysis. And to check the x margin, in order to garantee that the number will be between these functions horizontally, it gets the actual count and aplies Newton-Raphson algoritm to find the correspondent place of this prime number in that function.

    count = 1
    for i in primes:
    
      # Finding the nearest value for prime in each function
      sup_y = f_superior.on(count)
      inf_y = f_inferior.on(count)

      # Finding the position in which the prime number is, using
      # the inverse of the function by Newton-Raphson algorithm
      sup_x = f_superior.inverse(count,i)
      inf_x = f_inferior.inverse(count,i)

      # If the margin fails, mark on log and shell
      if (sup_y<i or i<inf_y or sup_x>count or inf_x<count): 
          print("Fail: margin doesn't contain the value.")
          margin_failure = "Yes"
          break
      count = count + 1

Using these margin limits in x and y, it is possible to afirm that this code can safety check, and prove, that all primes are inside of this area between these two functions (See log.txt to see the results). With this result in mind, it is not dificult to use it to find a prime function using sin's approximation or probability cases, improving the decodification of encrypted data and keeping closer to answer one of the Millennium Prize Problems.