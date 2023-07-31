$\newcommand{\Q}{\mathbb{Q}}$

# Math Refresher 2023

### Assumed to be known

- 4 operations (+,-,\*,/)
- integer vs rational vs decimal

## Course Content:

- Sets
  - sets of numbers ($\N$, $\Z$, $\R$, $\Q$)
  - complex sets (with $\{ \}$)&
  - example:
    $\{n \mid 4<n<10 \}$,
    $\{2n-1 \mid 4<n<10 \}$,
    $\{x \mid 4<x<10 \}$,
    $\{x \mid 4<x^2<10 \}$,
    $\{(x,y) \mid 0<x<2 , 1<y<3\}$, 
  - extreme values ($\min$,$\max$ vs $\sup$,$\inf$)
- Modular arithmetic
  - Euclidean division of $a$ by $b$ ($a=bk+R$ with $0 \leq r < b$)
  - example with $a=35$, $b=2,3,4,5,6,7,8$
  - modular classes ($12 \equiv 7 \equiv 22 \equiv 102 \equiv -3 \equiv -103 \mod 5$ i.e. $\{2+5k \mid k \in \Z \}$)
  - modular operations (+,-,\* $\mod n$)
- Functions and Sequences
  - functions def
  - example: 
    $f: x \to x^2$,
    $g: x \to \sqrt{x}$, 
  - typical plotting of functions: set of points $(x,y)$ s.t. $y = f(x)$
  - sequences def: general formula
  - example: $u_n = n^3-5n^2$
  - sequences def: recursive formula
  - example: $u_0 = 5, u_{n+1} = u_n^2-u_n+2$
- Essence of proofs
  - proof: assumption => conclusion
  - direct with $n \geq 0 \implies 2n \geq 4n$
  - cases split with $n \equiv n^2 \mod 2$
  - contradiction with $\sqrt{2} \not \in \Q$
  - induction with $u_0 = 2, u_{n+1} = \frac{u_n+1}{2} \implies u_n>1$
