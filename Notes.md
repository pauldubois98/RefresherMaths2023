$\newcommand{\Q}{\mathbb{Q}}$
$\newcommand{\Primes}{\mathbb{P}}$
$\newcommand{\st}{\text{ s.t. }}$
$\newcommand{\and}{\text{ and }}$
$\newcommand{\or}{\text{ or }}$

# Math Refresher 2023

This course teaches basic mathematical metho dologies for proofs.
It is intended for students with a lack of mathematical background, or with a lack of confidence in mathematics.
We will try to cover most of the prerequisites of the courses in the master's, i.e. basic algebra/analysis and basic applications.

## Presentation

- Paul Dubois
- 3rd year PhD @ Centrale / TheraPanacea
- Research topic: AI applied to radiotherapy
- Email: b00795695@essec.edu (for any question)
- Course structure
  - 8*3h arranged as 1h20min lecture - 1/3h break - 1h20min lecture
  - No pb class planned, but lectures will have integrated live exercises
  - Interrupt if needed (do *not* wait for the end of the lecture)
- Examination
  - The course is pass/fail
  - Spoiler: All of you will pass
  - Home exercises, you will need 80+% to pass
  - How long do you need to complete exercises (should take 30min to 1h)?
  - How many exercises do you want? (2-4?)
  - Hand in paper of PDF? (vote)
  - In the unlikely event of not passing, you will be able to do some extra work to pass
- Course notes are still under construction (as I will adjust according to the speed of the class); I will give it to you at the end of the course.
- Final questions before we start?

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
  - live exercises:
    - compute and plot the inersection and union of $A = \left(1, 5\right)$ and $B = \left(3, 7\right]$.
    - compute and plot the inersection and union of $C = \left(-\infty, 2\right]$ and $D = \left[0, +\infty \right)$.
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
  - extreme values ($\min$,$\max$ vs $\inf$,$\sup$)
  - live exercises:
    - find the extreme values of the set $A = \{x \in \R \mid x>0\}$.
    - find the extreme values of the set $B = \{1-\frac{1}{n} \mid n\in \N\}$.
## Boolean Algebra
  - principle (only $0$ and $1$)
  - $+$ and $*$ for booleans: $\lor$ and $\land$
  - $not$ ($\lnot$)
  - tables
  - De Morgan's law ($\lnot (a \land b) = \lnot a \lor \lnot b$ and $\lnot (a \lor b) = \lnot a \land \lnot b$)
  - implications operators ($\implies, \impliedby, \iff$) & xor operator ($\veebar$)
  - live exercise:
    - express $xor$ in terms of $\lor, \land, \lnot$
    - express $\implies$ in terms of $\lor, \land, \lnot$
    - express $\land$ in terms of $\lor, \lnot$
    - express $\lor$ in terms of $\land, \lnot$
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
  - image vs pre-image
  - span vs kernel
  - examples:
    - $f: x \to 3x+1$
    - $g: x \to x^2-1$
    - $h: x \to 8$
  - live exercises:
    - compute the image of $2$ by $f(x) = \frac{(x+1)^2 - x}{x-3}$
    - compute the preimage(s) of $5$ by $f(x) = 2x-3$
    - compute the kernel of $f(x) = -3x+2$
    - compute the span of $f(x) = 5-(2x)^4$
  - typical plotting of functions: set of points $(x,y)$ s.t. $y = f(x)$
## Sequences
  - sequences def: general formula
  - example: $u_n = n^3-5n^2$
  - sequences def: recursive formula
  - example: $u_0 = 5, u_{n+1} = u_n^2-u_n+2$
  - live exercises:
    - consider the (arithmetic) sequence $\{a_n\}$ defined by $a_{n+1}=a_n+2$ and $a_0=-1$:
      - find the first five terms of the sequence
      - find the common difference between consecutive terms
      - find a formula for $a_n$ (without using $a_{n-1}$)
    - consider the (geometric) sequence $\{b_n\}$ defined by $b_n=3*2^n$
      - find the first five terms of the sequence
      - find the common ratio between consecutive terms
      - find a formula for $b_{n+1}$ (using only $b_n$, no $n$)
## Essence of proofs
  - proof: assumption => conclusion
  - direct with $n \geq 0 \implies 2n \geq 4n$
  - cases split with $n \equiv n^2 \mod 2$
  - contradiction with $\sqrt{2} \not \in \Q$
  - induction with $u_0 = 2, u_{n+1} = \frac{u_n+1}{2} \implies u_n>1$
  - live exercises:
    - prove that for all real numbers $x$, if $x$ is positive, then $x^3$ is also positive
    - prove that the square root of 3 is irrational, i.e., it cannot be expressed as a fraction of two integers.
    - prove by mathematical induction that for all non-negative integers $n$, $3^n - 1$ is divisible by $2$.
    - use mathematical induction to prove that for all positive integers $n$, the sum of the first $n$ odd integers is given by the formula: $1 + 3 + 5 + ... + (2n - 1)$ is $n^2$.
## Asymptotic analysis
  - definition ($\varepsilon, \delta$)
  - examples / live exercises:
    - prove that limit of $u_n = \frac{n^2+1}{n^2}$ as $n \to +\infty$ is $1$
    - prove that limit of $f(x) = \frac{2x-1}{x}$ as $x \to -\infty$ is $2$
    - prove that limit of $u_n = \frac{1}{\sqrt{n}}$ as $n \to +\infty$ is $0$
    - prove that $u_n = 2n^3$ diverges to $+\infty$ as $n \to +\infty$
    - prove that limit of $f(x) = \frac{1}{x^2}$ as $x \to 0$ is $+\infty$
    - prove that limit of $f(x) = \frac{1}{x}$ as $x \to 0^-$ is $-\infty$
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