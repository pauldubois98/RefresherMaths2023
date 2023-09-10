$\newcommand{\Q}{\mathbb{Q}}$
$\newcommand{\Primes}{\mathbb{P}}$
$\newcommand{\st}{\text{ s.t. }}$
$\newcommand{\and}{\text{ and }}$
$\newcommand{\or}{\text{ or }}$

# Math Refresher 2023

## Assumed to be known

- 4 operations (+,-,\*,/)
- integer vs rational vs decimal
- what is a prime number

## Sets
  - sets of numbers ($\N$, $\Z$, $\R$, $\Q$, $\Primes$)
  - complex sets (with $\{ \}$)
  - examples (draw them):
    - $\{n \mid 4<n<10, n \in \N \}$
    - $\{2n-1 \mid 4<n<10 , n \in \N \}$
    - $\{x \mid 4<x<10, x \in \R \}$
    - $\{x \mid 4<x^2<10 \}$
    - $\{(x,y) \mid 0<x<2 , 1<y<3, x \in \R, y \in \R \}$
  - live exercises: draw set + define set from drawing
  - intervals ($\left[a,b\right]$ & $\left(a,b\right)$); example: $\left[-2, 3\right)$
  - sets unions & intersections
  - examples:
    - $\left[0,1\right) \cup \left(2,3\right]$
    - $\left(0,1\right) \cap \left[0.5,2\right]$
    - $\left[-2,5\right) \cap \N$
    - $\left[-2,5\right) \cap \Z$
  - live exercises: TODO
  - quantifiers: $\forall$, $\exists$
  - exmaple (simple):
    - $S = \{1,3,5,7,8\}$: $\forall s \in S, \st \leq 10$
    - $S = \{1,3,5,7,8\}$: $\exists s \in \S \st s \text{ is pair}$
  - example (combined): "for any number, there is a (natural) number greater" ($\forall x \in \R, \exists n \in \N s.t. n>x$)
  - live exercises: 
    - $S = \{5,6,3,1\}$ "all elements of $S$ are positive"
    - $S = \{5,6,3,1\}$ "there is an odd element in $S$"
    - $S = \{5,6,3,1\}$ "there is an even element in $S$ that is not a multiple of 4"
  - implications $\implies$, $\impliedby$, $\iff$
  - examples:
    - $x>1 \implies x \text{positive}$
    - $k \in \Z \impliedby k \in \N$
    - $k \in \Z  \and k\geq 0 \iff k \in \N$
  - live exercises:
    - "if $x$ is positive, then it is the square of another number"
    - "$n$ is pair is equivalent to $n=2m$ for some integer $m$"
  - extreme values ($\min$,$\max$ vs $\sup$,$\inf$)
  - live exercises: TODO
## Modular arithmetic
  - Euclidean division of $a$ by $b$ ($a=bk+R$ with $0 \leq r < b$)
  - example with $a=35$, $b=2,3,4,5,6,7,8$
  - modular classes ($12 \equiv 7 \equiv 22 \equiv 102 \equiv -3 \equiv -103 \mod 5$ i.e. $\{2+5k \mid k \in \Z \}$)
  - live exercises:
    - give 3 numbers that are congruent to 3 mod 7
    - give a test in terms of modular arithmetic that is equivalent to "$n$ is odd"
    - give a test in terms of modular arithmetic that is equivalent to "$n$ is a nultiple of $k$" (for $k$ a natural number greater than two)
    - what does it mean for $n$ to say that $n \equiv 5 \mod 10$?
    - find the least positive value of $x$ such that $71 \equiv x \mod 8$
  - modular operations (+,-,\* $\mod n$)
  - GCD and $\square^{-1} \mod n$
  - example:
    - compute the GCD of $270$ and $192$ (answer: $6$)
    - compute $5^{-1} \mod 11$
  - live exercises:
    - find the least positive value of $x$ such that $89 \equiv (x + 3) \mod 4$
    - what is $x \mod 10$ if $96 \equiv x / 7 \mod 5$
    - find an $x$ such that $5x \equiv 4 \mod 11$
    - if $x$ is congruent to $13 \mod 17$ then $7x - 3$ is congruent to which number $\mod 17$?
## Functions
  - functions def
  - span vs kernel
  - example: 
    $f: x \to x^2$,
    $g: x \to \sqrt{x}$, 
  - live exercises: TODO
  - typical plotting of functions: set of points $(x,y)$ s.t. $y = f(x)$
## Sequences
  - sequences def: general formula
  - example: $u_n = n^3-5n^2$
  - live exercises: TODO
  - sequences def: recursive formula
  - example: $u_0 = 5, u_{n+1} = u_n^2-u_n+2$
  - live exercises: TODO
- Essence of proofs
  - proof: assumption => conclusion
  - direct with $n \geq 0 \implies 2n \geq 4n$
  - cases split with $n \equiv n^2 \mod 2$
  - contradiction with $\sqrt{2} \not \in \Q$
  - induction with $u_0 = 2, u_{n+1} = \frac{u_n+1}{2} \implies u_n>1$
  - live exercises: TODO
## Large operators
  - $\sum$, $\prod$, $\bigcup$, $\bigcap$
  - examples:
    - "product of numbers from 10 to 20"
    - "sum of squares up to 10"
    - $\bigcup_{x \in \{1,4,10.5, 21.75\}} \left[ x-0.5, x+0.5 \right]$
    - $\bigcap_{n \in \N^*} \left[ -\frac{1}{n}, \frac{1}{n} \right]$
  - live exercises:
    - what set does the last example corresponds to?
    - define the factorial
    - give an expression for the sum of inverses from $1$ to $1000$
    - give an expression for the product of all prime numbers smaller than $10000$
    - give an expression for the sum of factorials from $100$ to $200$
  - Series: TODO
  - Partial sums: TODO


TODO:
- Graph of functions
- Complex numbers
- Affine functions
- Quadratic equations
- Vectors (concept, sum, scalar product)
- Equations for lines (2D, 3D) and planes (3D)
- Derivatives
- Integration
- Matrices (concept, sum, product)
- Mutli-dimensional functions
- Inversing matrices (+ row reduction; span)
- Linear regression
-