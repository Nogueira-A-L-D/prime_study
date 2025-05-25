# Study of Primes with Log Functions
<p>
  Studying primes and trying to find a approximation using log functions with irrational base, computacional tests and algebra analysis of graphics.
</p>
<p>
  The first step in this search was the use of Geogebra's plataform to see functions that follows the behavior of prime numbers. The tests began with the Prime Number Theorem, using:
</p>
<p>
  $$ln(x) * x + \frac{1}{x} + 1$$
</p>
<p>
  When checking the graphic, i saw that this function could create a inferior margin. Then, i started to check other options, such as the change of $ln(x)$ to $\sqrt{x}$, but the results raises faster, however creates a superior margin:
<p>
  $$\sqrt{x} * x + \frac{1}{x} + 1$$
</p>
<p>
  So, I decided to test other functions that raises in log, but around $e$ value, to find a good superior margin and inferior margin, finding:
</p>
<p>
  $$log_\sqrt{5}(x) * x + \frac{1}{x} + 1$$
  $$log_\sqrt{7}(x) * x + \frac{1}{x} + 1$$
</p>
<p>
  As I got then, I needed to prove that these functions creates a small interval between them that contains all primes. For this, I created margin_check.py.
</p>
