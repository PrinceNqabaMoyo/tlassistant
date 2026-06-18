# Term 2

## Differential Calculus

### Limits

Consider the function: y = (x^2+4x−12) / x+6

The numerator of the function can be factorised as: y =

(x+6)(x−2)/ x+6 .

Then we can cancel the x + 6 from numerator and denominator and we are left with: y = x − 2.

However, we are only able to cancel the x + 6 term if x 6= −6. If x = −6, then the denominator becomes 0 and the function is not defined. This means that the domain of the function does not include x = −6. But we can examine what happens to the values for y as x gets closer to −6. The list of values shows that as x gets closer to −6,y gets closer and closer to −8.

|  x      |y =(x+6)(x−2)/x+6|

| −9    |            −11            |

| −8    |            −10            |

| −7    |              −9            |

|−6,5  |           −8,5            |

|−6,4  |           −8,4            |

|−6,3  |           −8,3            |

|−6,2  |           −8,2            |

|−6,1  |           −8,1            |

|−6,09|          −8,09           |

|−6,08|          −8,08           |

|−6,01|          −8,01           |

|−5,9  |           −7,9            |

|−5,8  |           −7,8            |

|−5,7  |           −7,7            |

|−5,6  |           −7,6            |

|−5,5  |           −7,5            |

|−5     |             −7             |

|−4     |             −6             |

|−3     |             −5             |

DIAGRAM REQUIRED. \[The graph is a straight line with slope 1 and y-intercept −2, but with a hole at x = −6.]

As x approaches −6 from the left, the y-value approaches −8 and as x approaches −6 from the right, the y-value approaches −8. Since the function approaches the same y-value from the left and from the right, the limit exists.

 For the function y ==(x+6)(x−2)/x+6, we can write:

lim\_{x→-6}\[(x+6)(x−2)/x+6] = -8

This is read: the limit of(x+6)(x−2)/x+6 as x tends to −6 (from both the left and the right) is equal to −8.

We can also have the situation where a function tends to a different limit depending on whether x approaches from the left or the right.

The limit for x approaching 0 from the left is:

lim\_{x→0^-}f(x) = −2

The limit for x approaching 0 from the left is:

lim\_{x→0^+}f(x) = 2

where 0^− means x approaches zero from the left and 0^+ means x approaches zero from the right.

Therefore, since f(x) does not approach the same value from both sides, we can conclude that the limit as x tends to zero does not exist

##### Example

Determine:

a. lim\_{x→1} (10)

b. lim\_{x→2} (x+4)

Illustrate answers graphically.

SOLUTION

Step 1: Simplify the expression and cancel all common terms

We cannot simplify further and there are no terms to cancel.

Step 2: Calculate the limit

a. lim\_{x→1} (10) = 10 DIAGRAM: Cartesian axes. Straight horizontal line at y = 10 and dots from x = 1 to the line.

b. lim\_{x→2} (x+4) = 6 DIAGRAM: Cartesian axes. Straight line passing through (0;4) and the solid black-filled hole at  (2;6). dots connect point (2;6) with the corresponding coordinate value in the y and x axes.

2\. Determine the following and illustrate the answer graphically: lim\_{x→10} \[(x^2 -100) / x-10]

SOLUTION

Step 1: Simplify the expression

Factorise the numerator:

(x^2 -100) / x-10 = (x+10)(x-10) / x-10

As x → 10, the denominator (x − 10) → 0, therefore the expression is not defined for x = 10 since division by zero is not permitted.

Step 2: Cancel all common terms

(x+10)(x-10) / x-10 = x+10

Step 3: Calculate the limit

lim\_{x→10} \[(x^2 -100) / x-10] = lim\_{x→10} (x+10)

= 10 + 10 = 20

Step 4: Draw the graph

DIAGRAM: \[Cartesian axes. Straight line passing through (0;10) and the empty white hole at (10;20)]

#### Questions

1\. Determine the following limits and draw a rough sketch to illustrate:

a) lim\_{x→3} \[(x^2 -9) / x+3]

b) lim\_{x→3} \[(x+3) / x^2 +3x]

2\. Determine the following limits (if they exist):

a) lim\_{x→2} \[(3x^2 -4x) / 3-x]

b) lim\_{x→4} \[(x^2 -x-12) / x-4]

c) lim\_{x→2} (3x + 1/3x)

d) lim\_{x→0} 1/x

e) lim\_{y→1} \[(y-1) / y+1]

f) lim\_{y→1} \[(y+1) / y-1]

g) lim\_{h→0} \[(3h + h^2) / h]S

h) lim\_{h→1} \[(h^3 -1) / h-1]

i) lim\_{x→3} \[(√x -√3) / x-3]

### From average gradient to gradient at a point using limits

DIAGRAMS: for illustrations required for the whole heading.

In Grade 11 we learnt that the average gradient between any two points on a curve is given by the gradient of the straight line that passes through both points. We also looked at the gradient at a single point on a curve and saw that it was the gradient of the tangent to the curve at the given point. In this section we learn how to determine the gradient of the tangent.

Let us consider finding the gradient of a tangent t to a curve with equation y = f (x) at a given point P. We know how to calculate the average gradient between two points on a curve, but we need two points. The problem now is that we only have one point, namely P. To get around the problem we first consider a secant (a straight line that intersects a curve at two or more points) to the curve that passes through point P (xP ; yP ) and another point on the curve Q (xQ; yQ), where Q is an arbitrary distance from P.

We can determine the average gradient of the curve between the two points:

                m = (y\_Q - y\_P) / (x\_Q - x\_P)

If we let the x-coordinate of P be a, then the y-coordinate is f (a). Similarly, if the x-coordinate of Q is (a + h), then the y-coordinate is f (a + h). We can now calculate the average gradient as:

(y\_Q - y\_P) / (x\_Q - x\_P) = f (a + h) − f (a) / (a + h) − a

= \[f (a + h) − f (a)]/h

* Imagine that Q moves along the curve, getting closer and closer to P. The secant line approaches the tangent line as its limiting position. This means that the average gradient of the secant approaches the gradient of the tangent to the curve at P.
* We see that as point Q approaches point P, h gets closer to 0. If point Q lies on point P, then h = 0 and the formula for average gradient is undefined. We use our knowledge of limits to let h tend towards 0 to determine the gradient of the tangent to the curve at point P:

               Gradient at point P = lim{h→0}\[f(a + h)−f (a) /h]

##### Examples

1. Problem: Given g (x) = 3x^2, determine the gradient of the curve at the point x = -1.

SOLUTION

Step 1: Write down the formula for the gradient at a point

Gradient at a point = lim{h→0}\[g(a + h)−g(a) /h]

Step 2: Determine g (a + h) and g(a)

We need to find the gradient of the curve at x = −1, therefore we let a = -1:

g(x) = 3x^2

g(a) = g(−1)

= 3(−1)^2

= 3

g (a + h) = g (−1 + h)

= 3(−1 + h)^2

= 3(1 -2h + h^2)

= 3 -6h + 3h^2

Step 3: Substitute into the formula and simplify

lim{h→0}\[g(a + h)−g(a) /h] = lim{h→0}\[g(-1 + h)−g(-1) /h]

= lim{h→0}\[(3 -6h + 3h^2)−3 /h]

= lim{h→0}\[-6h + 3h^2 /h]

= lim{h→0}\[h(-6 + 3h) /h]

= lim{h→0}\[-6 + 3h]

= -6

Step 4: Write the final answer

The gradient of the curve g (x) = 3x^2

at x = −1 is −6.

2\. Problem: Given the function f (x) = 2x^2−5x, determine the gradient of the tangent to the curve at the point x = 2.

SOLUTION

Step 1: Write down the formula for the gradient at a point

Gradient at a point = lim{h→0} \[f (a + h) − f (a)]/h

Step 2: Determine f (a + h) and f(a)

We need to find the gradient of the tangent to the curve at x = 2, therefore we let

a = 2:

f(x) = 2x^2 − 5x

f(a) = f(2)

= 2(2)^2 − 5(2)

= 8 − 10

= −2

f (a + h) = f (2 + h)

= 2(2 + h)^2 − 5 (2 + h)

= 2(2^2 + 4h + h^2) - 10 - 5h

= 8 + 8h + 2h^2 - 10 - 5h

-2 + 3h + 2h^2

Step 3: Substitute into the formula and simplify

lim{h→0} \[f (a + h) − f (a)]/h = lim{h→0} \[f (2+ h) − f (2)]/h

= lim{h→0} \[ (-2 + 3h + 2h^2) − (-2)]/h

= lim{h→0} \[3h+2h^2 /h]

= lim{h→0} \[h(3+2h) /h]

= lim{h→0} \[3+2h]

= 3

Step 4: Write the final answer

The gradient of the tangent to the curve f (x) = 2x^2 − 5x at x = 2 is 3.

3\. Problem: Determine the gradient of k(x) = −x^3 + 2x + 1 at the point x = 1.

SOLUTION

Step 1: Write down the formula for the gradient at a point

Gradient at a point = lim{h→0}\[k(a + h)−k(a) /h]

Step 2: Determine k (a + h) and k(a)

Let a = 1:

k(x) = −x^3 + 2x + 1

k(a) = k(1)

= −(1)^3 + 2(1) + 1

= −1 + 2 + 1

= 2

k (a + h) = k (1 + h)

= −(1 + h)^3 + 2 (1 + h) + 1

= −(1 + 3h + 3h^2 + h^3) + 2 + 2h + 1

= -1 - 3h - 3h^2 - h^3 + 2 + 2h + 1

= 2 - h - 3h^2 - h^3

Step 3: Substitute into the formula and simplify

lim{h→0}\[k(a + h)−k(a) /h] = lim{h→0}\[k(1 + h)−k(1) /h]

= lim{h→0} \[(2 - h - 3h^2 - h^3)-2 /h]

= lim{h→0} \[(-h - 3h^2 - h^3)/h]

= lim{h→0} \[h(-1 - 3h - h^2) /h]

= lim{h→0} \[-1 - 3 - h^2]

= -1

Step 4: Write the final answer

The gradient of k(x) = −x^3 + 2x + 1 at x = 1 is −1.

#### Questions

1\. Given: f(x) = −x^2 + 7

a)  Find the average gradient of function f, between x = −1 and x = 3.

b) Illustrate this with a graph.

c) Find the gradient of f at the point x = 3 and illustrate this on your graph.

2\. Determine the gradient of the tangent to g if g(x) = 3/x (x ≠ 0) at x = a.

3\. Determine the equation of the tangent to H(x) = x^2 + 3x at x = −1.

### Differentiation from first principles

We know that the gradient of the tangent to a curve with equation y = f(x) at x = a can be determine using the formula:

Gradient at a point lim{h→0} \[f (a + h) − f (a)]/h

We can use this formula to determine an expression that describes the gradient of the graph (or the gradient of the tangent to the graph) at any point on the graph. This expression (or gradient function) is called the derivative.

DEFINITION: Derivative

The derivative of a function f (*x*) is written as *f*′(*x*) and is defined by:

*f*′ (*x*) = lim{h→0} \[f (*x* + h) − f (*x*)]/h

DEFINITION: Differentiation

The process of determining the derivative of a given function.

This method is called differentiation from first principles or using the definition.

* There are a few different notations used to refer to derivatives. It is very important that you learn to identify these different ways of denoting the derivative and that you are consistent in your usage of them when answering questions.
* If we use the common notation y = f (x), where the dependent variable is y and the independent variable is x, then some alternative notations for the derivative are as follows:

        *f*′ (*x*) = *y*′ = *dy*/*dx* = *df*/*dx* = *d*/*dx* \[*f* (*x*)] = D *f* (*x*) = D*ₓy*

The symbols D and d/dx are called differential operators because they indicate the operation of differentiation.

*dy*/*dx* means y differentiated with respect to x. Similarly, *dp*/*dx* means p differentiated with respect to *x*.

Important: *dy*/*dx* is not a fraction and does not mean *dy* ÷ *dx*.

##### Examples

1. Problem: Calculate the derivative of g (x) = 2x − 3 from first principles.

SOLUTION

Step 1: Write down the formula for finding the derivative using first principles

*g*′ (*x*) = lim{h→0} \[g (*x* + h) − g (*x*)]/h

Step 2: Determine g (x + h)

g(x) = 2x − 3

g (x + h) = 2 (x + h) − 3

= 2x + 2h − 3

Step 3: Substitute into the formula and simplify

*g*′ (*x*) = lim{h→0} \[2x + 2h − 3 − (2x − 3)]/h

= lim{h→0} 2h/h

= lim{h→0} 2

= 2

Step 4: Write the final answer

The derivative *g*′ (*x*) = 2.

2\. Problem:

a. Find the derivative of  *f*′ (*x*) = 4x^3 from first principles.

b. Determine *f*′(0,5) and interpret the answer.

SOLUTION

Step 1: Write down the formula for finding the derivative from first principles

*f*′ (*x*) = lim{h→0} \[f (*x* + h) − f (*x*)]/h

Step 2: Substitute into the formula and simplify

*f*′ (*x*) = lim{h→0} \[4 (*x* + h)^3 − 4*x*^3]/h

= lim{h→0} \[4 (*x*^3 + 3x^2h + 3xh^2 + h^3) − 4*x*^3]/h

= lim{h→0} \[4*x*^3 + 12x^2h + 12xh^2 + 4h^3 − 4*x*^3]/h

= lim{h→0} \[12x^2h + 12xh^2 + 4h^3]/h

= lim{h→0} \[12x^2 + 12xh + 4h^2]

= 12x^2

Step 3: Calculate *f*′(0,5) and interpret the answer

*f*′ (*x*) = 12x^2

∴ *f*′ (0,5) = 12(0,5)^2

= 12(1/4)

= 3

• The derivative of f(x) at x = 0,5 is 3.

• The gradient of the function f at x = 0,5 is equal to 3.

• The gradient of the tangent to f(x) at x = 0,5 is equal to 3.

3\. Problem: Calculate *dp*/*dx* from first principles if *p*(*x*) = -2/*x*.

SOLUTION

Step 1: Write down the formula for finding the derivative using first principles

*dp*/*dx* = lim{h→0} \[p (*x* + h) − p (*x*)]/h

Step 2: Substitute into the formula and simplify

*dp*/*dx* = lim{h→0} \[-2/x+h − (-2/x)]/h

It is sometimes easier to write the right-hand side of the equation as: *dp*/*dx* = lim{h→0} 1/h\[-2/x+h + 2/x]

= lim{h→0} 1/h \[ (−2x + 2(x + h)) / x(x+h) ]

= lim{h→0} 1/h \[ (−2x + 2x + 2h) / x(x+h) ]

= lim{h→0} 1/h \[2h /(x^2 + xh)]

= lim{h→0}  2/(x^2 + xh)

= 2/x^2

Notice: even though h remains in the denominator, we can take the limit since it does not result in division by 0.

Step 3: Write the final answer

*dp*/*dx* = 2/x^2

3\. Problem: Differentiate g (x) = 1/4 from first principles and interpret the answer.

SOLUTION

Step 1: Write down the formula for finding the derivative from first principles

*g*′ (*x*) = lim{h→0} \[g (*x* + h) − g (*x*)]/h

Step 2: Substitute into the formula and simplify

*g*′ (*x*) = lim{h→0} \[1/4 − 1/4]/h

= lim{h→0} 0/h

=lim{h→0} 0

= 0

Step 3: Interpret the answer

The gradient of g(x) is equal to 0 at any point on the graph. The derivative of this constant function is equal to 0.

#### Questions

1\. Given: g (x) = −x^2

a) Determine \[g (*x* + h) − g (*x*)]/h

b) Hence, determine lim{h→0} \[g (*x* + h) − g (*x*)]/h

c) Explain the meaning of your answer in (b).

2\. Find the derivative of f (x) = −2x^2 + 3x + 1 using first principles.

3\. Determine the derivative of f (x) = 1/x−2 using first principles.

4\. Determine g′(3) from first principles if g (x) = −5x^2.

5\. If p (x) = 4x(x − 1), determine p′(x) using first principles.

6\. Find the derivative of k(x) = 10x^3 using first principles.

7\. Differentiate f(x) = x^n using first principles.

(Hint: Use Pascal’s triangle)

### Rules for differentiation

Determining the derivative of a function from first principles requires a long calculation and it is easy to make mistakes. However, we can use this method of finding the derivative from first principles to obtain rules which make finding the derivative of a function much simpler.

• General rule for differentiation: *d*/*dx* \[*x*^*n*] = *nx*^(*n-1*), where *n* ∈ ℝ and *n* ≠ 0.

• The derivative of a constant is equal to zero: *d*/*dx* \[*k*] = 0.

• The derivative of a constant multiplied by a function is equal to the constant multiplied by the derivative of the function.

*d*/*dx* \[*k*·*f*(*x*)] = *k d*/*dx* \[*f*(*x*)]

• The derivative of a sum is equal to the sum of the derivatives.

*d*/*dx* \[*f*(*x*) + *g*(*x*)] = *d*/*dx* \[*f*(*x*)] + *d*/*dx* \[*g*(*x*)]

• The derivative of a difference is equal to the difference of the derivatives.

*d*/*dx* \[*f*(*x*) - *g*(*x*)] = *d*/*dx* \[*f*(*x*)] - *d*/*dx* \[*g*(*x*)]

When to use the rules for differentiation:

• If the question does not specify how we must determine the derivative, then we use the rules for differentiation.

When to differentiate using first principles:

• If the question specifically states to use first principles.

• If we are required to differentiate using the definition of a derivative, then we use first principles.

##### Examples

1. Use the rules of differentiation to find the derivative of each of the following:

a. y = 3x^5

b. p =1/4 q^2

c. f(x) = 60

d. y = 12x^3 + 7x

e. m = 3/2 n^4 -1

SOLUTION

Step 1: Apply the appropriate rules to determine the derivative

a\*. dy\*/*dx* = 3(5x^4) = 15x^4

b\*. dp\*/*dx* = 1/4 (2q) = 1/2 q

c. f′(x) = 0

d. *dy*/*dx* = 12(3x^2) + 7 = 36x^2 + 7

e. *dm*/*dx* = 3/2 (4n^3) - 0 = 6n^3

2\. Differentiate the following with respect to t:

a. g(t) = 4 (t + 1)^2 (t − 3)

b. k(t) = (t+2)^3 /√t

SOLUTION

a) Step 1: Expand the expression and apply the rules of differentiation

We have not learnt a rule for differentiating a product, therefore we must expand the brackets and simplify before we can determine the derivative:

g(t) = 4 (t + 1)^2 (t − 3)

= 4(t^2 + 2t + 1) (t-3)

= 4(t^3 + 2t^2 + t - 3t^2 - 6t - 3)

= 4(t^3 - t^2 - 5t - 3)

= 4t^3 - 4t^2 - 20t -12

∴g′(t) = 4(3t^2) - 4(2t) - 20 - 0

= 12t^2 - 8t - 20

b) We have not learnt a rule for differentiating a quotient, therefore we must first simplify the expression and then we can differentiate:

k(t) = (t+2)^3 /√t

= (t+2)(t^2 + 4t + 4) /√t

= (t^3 + 6t^2 + 12t + 8)/ t^(1/2)

=t^-(1/2) (t^3 + 6t^2 + 12t + 8)

=t^(5/2) + 6t^(3/2) + 12t^(1/2) + 8t^(-1/2)

∴g′(t) = 5/2 t^(3/2) + 6(3/2 t^1/2) + 12(1/2 t^-1/2) + 8(-1/2t^-3/2)

= 5/2 t^(3/2) + 9t^1/2 + 6t^-1/2 - 4t^-3/2

Important: always write the final answer with positive exponents.

g′(t) = 5/2 t^(3/2) + 9t^1/2 + 6t^-1/2 - 4t^-3/2

#### Questions

1\. Differentiate the following:

a) y = 3x^2

b) f(x) = 25x

c) k(x) = −30

d) y = −4x^5 + 2

e) g(x) = 16x^−2

f) y = 10(7 − 3)

g) q(x) = x^4 − 6x^2 − 1

h) y = x^2 + x + 4

i) f(x) = 1/3 x^3 − x^2 + 2/5

j) y = 3x^3/2 − 4x + 20

k) g(x) = x(x + 2) + 5x

l) p(x) = 200\[x^3 −1/2 x^2 + 1/5 x − 40]

m) y = 14(x − 1) \[1/2 + x^2]

2\. Find *f′*(*x*) if *f* (*x*) = (x^2 - 5x + 6)/ x-2

3\. Find *f′*(*y*) if *f* (*y*) = √*y*

4\. Find *f′*(*z*) if *f* (*z*) = (z-1)(z+1)

5\. Determine *dy*/*dx* if y = (x^3 +2√ -3)/x

6\. Determine the derivative of y = √x^3 + 1/(3x^3)

7\. Find Dₓ\[x^(3/2) - 3/(x^ 1/2)]^2

8\. Find *dy*/*dx* if x = 2y + 3.

9\. Determine *f′*(θ) if *f*(θ) = 2(θ^ 3/2 -3θ^ -1/2)^2

10\. Find *dp*/*dt* if p(t) = (t+1)^3 /√t

### Equation of a tangent to a curve

* At a given point on a curve, the gradient of the curve is equal to the gradient of the tangent to the curve.
* The derivative (or gradient function) describes the gradient of a curve at any point on the curve. Similarly, it also describes the gradient of a tangent to a curve at any point on the curve.

To determine the equation of a tangent to a curve:

1\. Find the derivative using the rules of differentiation.

2\. Substitute the x-coordinate of the given point into the derivative to calculate the

gradient of the tangent.

3\. Substitute the gradient of the tangent and the coordinates of the given point into

an appropriate form of the straight line equation.

4\. Make y the subject of the formula.

The normal to a curve is the line perpendicular to the tangent to the curve at a given

point.

m\_tangent × m\_normal = −1

##### Examples

1. Problem: Find the equation of the tangent to the curve y = 3x^2 at the point (1; 3). Sketch the curve and the tangent.

SOLUTION

Step 1: Find the derivative

Use the rules of differentiation: y = 3x^2

∴ *dy*/*dx* = 3(2x) = 6x.

Step 2: Calculate the gradient of the tangent

To determine the gradient of the tangent at the point (1; 3), we substitute the x-value into the equation for the derivative.

*dy*/*dx*  = 6x

∴ m = 6(1) = 6

Step 3: Determine the equation of the tangent

Substitute the gradient of the tangent and the coordinates of the given point into the gradient-point form of the straight line equation.

y − y\_1 = m (x − x\_1)

y − 3 = 6 (x − 1)

y = 6x − 6 + 3

y = 6x − 3

Step 4: Sketch the curve and the tangent

DIAGRAM REQUIRE: graph of y = 3x^2 with tangent at (1;3) with label y = 6x-3. x-axis starts from -4 ends at 4. y-axis starts at -4 ends at 6.

2\. Problem: Given g(x) = (x + 2)(2x + 1)^2, determine the equation of the tangent to the curve at x = −1 .

SOLUTION

Step 1: Determine the y-coordinate of the point

g(x) = (x + 2)(2x + 1)^2

g(−1) = (−1 + 2)\[2(−1) + 1]^2

= (1)(−1)^2

= 1

Therefore the tangent to the curve passes through the point (−1; 1).

Step 2: Expand and simplify the given function

g(x) = (x + 2)(2x + 1)^2

= (x + 2)(4x^2 + 4x + 1)

= 4x^3 + 4x^2 + x + 8x^2 + 8x + 2

= 4x^3 + 12x^2 + 9x + 2

Step 3: Find the derivative

g′(x) = 4(3x^2) + 12(2x) + 9 + 0

= 12x^2 + 24x + 9

Step 4: Calculate the gradient of the tangent

Substitute x = −1 into the equation for g′(x):

g′(−1) = 12(−1)2 + 24(−1) + 9

∴ m = 12 − 24 + 9

= −3

Step 5: Determine the equation of the tangent

Substitute the gradient of the tangent and the coordinates of the point into the gradient-point form of the straight line equation.

y − y1 = m (x − x\_1)

y − 1 = −3 (x − (−1))

y = −3x − 3 + 1

y = −3x − 2

3\. Problem:

a. Determine the equation of the normal to the curve xy = −4 at (−1; 4).

b. Draw a rough sketch.

SOLUTION

Step 1: Find the derivative

Make y the subject of the formula and differentiate with respect to x:

y = −4/x

= −4x^-1

∴ *dy*/*dx* = = −4(-1x^-2)

= 4x^-2

= 4/x^2

Step 2: Calculate the gradient of the normal at (−1; 4)

First determine the gradient of the tangent at the given point:

*dy*/*dx* = 4/(-1)^2

∴m = 4

Use the gradient of the tangent to calculate the gradient of the normal:

m\_tangent × m\_normal = −1

4 × m\_normal = −1

∴ m\_normal = - 1/4

Step 3: Find the equation of the normal

Substitute the gradient of the normal and the coordinates of the given point into the gradient-point form of the straight line equation.

y − y\_1 = m (x − x\_1)

y − 4 = −1/4(x − (−1))

y = −1/4x −1/4 + 4

y = −1/4x +15/4

Step 4: Draw a rough sketch

DIAGRAM REQUIRED: Graph of y = 4/x , the tangent line at (-1;4) labelled and the normal at (-1;4) labelled y = −1/4x +15/4.

#### Questions

1\. Determine the equation of the tangent to the curve defined by F(x) = x^3+2x^2−7x + 1 at x = 2.

2\. Determine the point where the gradient of the tangent to the curve:

a) f(x) = 1 − 3x^2 is equal to 5.

b) g(x) = 1/3 x^2 + 2x + 1 is equal to 0.

3\. Determine the point(s) on the curve f(x) = (2x − 1)2 where the tangent is:

a) parallel to the line y = 4x − 2.

b) perpendicular to the line 2y + x − 4 = 0.

4\. Given the function f: y = −x^2 + 4x − 3.

a) Draw a graph of f, indicating all intercepts and turning points.

b) Find the equations of the tangents to *f* at:

i. the y-intercept of *f*.

ii. the turning point of *f*.

iii. the point where x = 4,25.

c) Draw the three tangents above on your graph of *f*.

d) Write down all observations about the three tangents to *f*.

### Second derivative

The second derivative of a function is the derivative of the first derivative and it indicates the change in gradient of the original function. The sign of the second derivative tells us if the gradient of the original function is increasing, decreasing or remaining constant.

To determine the second derivative of the function *f*(x), we differentiate *f*′(x) using the rules for differentiation.

*f*′′(x) = *d*/*dx* \[*f*′(x)]

We also use the following notation for determining the second derivative of y:

*y*′′(x) = *d*/*dx*\[*dy*/*dx*] = *d^2y*/*dx^2*

##### Example

Calculate the second derivative for each of the following:

a) k(x) = 2x^3 − 4x^2 + 9

b) y = 3/x

SOLUTION

a) k′(x) = 2(3x^2) − 4(2x) + 0

= 6x^2 - 8x

k′′(x) = 6(2x) - 8

= 12x - 8

b) y = 3x^-1

*dy*/*dx* = 3(-1x^-2)

= -3x^-2

= -3/ x^2

*d^2y*/*dx^2 =* -3(-2x^-3)

= 6/x^3

#### Questions

1\. Calculate the second derivative for each of the following:

a) g(x) = 5x^2

b) y = 8x^3 − 7x

c) f(x) = x(x − 6) + 10

d) y = x^5 − x^3 + x − 1

e) k(x) = (x^2 + 1)(x − 1)

f) p(x) = −10/ x^2

g) q(x) = √x + 5x^2

2\. Find the first and second derivatives of f(x) = 5x(2x + 3).

3\. Find *d^2*/*dx^2* \[6 {3}√(x^2)]

4\. Given the function g : y = (1 − 2x)^3.

a) Determine g′ and g′′.

b) What type of function is:

i. g′

ii. g′′

c) Find the value of g′′(1/2)

d) What do you observe about the degree (highest power) of each of the derived functions?

### The effect of a and finding intercepts on functions of the form: y = ax^3 + bx^2 + cx + d

* If y = ax^3 + bx^2 + cx + d, changing the sign of a to positive or negative reflects the curve on the x-axis. VISUAL TOOL MUST BE AVAILABLE.
* When a>0 then the gradients of the curve change from positive (+) to 0 to negative (- to) to 0 and to positive again along the positive direction of the x-axis: ∕⁻∖\_∕
* When a<0 then the gradients of the curve change from - to 0 to + to 0 to - along the positive direction of the x-axis: ∖\_∕⁻∖
* The y-intercept if found by finding f(0).
* The x-intercepts are obtained by solving for f(x) = 0

##### Example

1. Problem: Given f (x) = −x^3 + 4x^2 + x − 4, find the x- and y-intercepts.

SOLUTION

Step 1: Determine the y-intercept

The y-intercept is obtained by letting x = 0:

y = −(0)^3 + 4(0)^2 + (0) − 4

= −4

This gives the point (0; −4).

Step 2: Use the factor theorem to factorise the expression

We use the factor theorem to find a factor of f(x) by trial and error:

f(x) = −x^3 + 4x^2 + x − 4

f(1) = −(1)3 + 4(1)2 + (1) − 4

= 0

∴ (x − 1) is a factor of f(x)

Factorise further by inspection:

f(x) = (x − 1)(−x^2 + 3x + 4)

= −(x − 1)(x^2 − 3x − 4)

= −(x − 1)(x + 1)(x − 4)

The x-intercepts are obtained by letting f(x) = 0:

0 = −(x − 1)(x + 1)(x − 4)

∴ x = −1, x = 1 or x = 4

This gives the points (−1; 0), (1; 0) and (4; 0).

#### Questions

1\. Given the function f(x) = x^3 + x^2 − 10x + 8.

a) Determine the x- and y-intercepts of f(x).

b) Draw a rough sketch of the graph.

c) Is the function increasing or decreasing at x = −5?

2\. Determine the x- and y-intercepts for each of the following:

a) y = −x^3 − 5x^2 + 9x + 45

b) y = x^3 −5/4 x^2 −7/4 x +1/2

c) y = x^3 − x^2 − 12x + 12

d) y = x^3 − 16x

e) y = x^3 − 5x^2 + 6

3\. Determine all intercepts for g(x) = x^3 + 3x^2 − 10x and draw a rough sketch of the graph.

### Finding the stationary points (local minima and maxima) of functions of the form y = ax^3 + bx^2 + cx + d

To determine the coordinates of the stationary point(s) of f(x):

• Determine the derivative f′(x).

• Let f′(x) = 0 and solve for the x-coordinate(s) of the stationary point(s).

• Substitute value(s) of x into f(x) to calculate the y-coordinate(s) of the stationary point(s).

* We have seen that the graph of a quadratic function can have either a minimum turning point (“smile”) or a maximum turning point (“frown”). For cubic functions, we refer to the turning (or stationary) points of the graph as local minimum or local maximum (relative minimum and maximum) turning points because there are other points on the graph with lower and higher function values.

##### Example

Calculate the stationary points of the graph of p (x) = x^3 − 6x^2 + 9x − 4.

Step 1: Determine the derivative of p (x)

Using the rules of differentiation we get:

p′(x) = 3x^2 − 12x + 9

Step 2: Let p′(x) = 0 and solve for x

3x^2 − 12x + 9 = 0

x^2 − 4x + 3 = 0

(x − 3) (x − 1) = 0

∴ x = 1 or x = 3

Therefore, the x-coordinates of the turning points are x = 1 and x = 3.

Step 3: Substitute the x-values into p (x)

We use the x-coordinates to calculate the corresponding y coordinates of the stationary points.

p (1) = (1)3 − 6(1)2 + 9 (1) − 4

= 1 − 6 + 9 − 4

= 0

p (3) = (3)3 − 6(3)2 + 9 (3) − 4

= 27 − 54 + 27 − 4

= −4

Step 4: Write final answer

The turning points of the graph of p (x) = x^3 − 6x^2 + 9x − 4 are (1; 0) and (3; −4).

#### Questions

1\. Use differentiation to determine the stationary point(s) for g(x) = −x^2 + 5x − 6.

2\. Determine the x-values of the stationary points for f(x) = -1/3 x^3 +1/2 x^2 +6x+ 5.

3\. Find the coordinates of the stationary points of the following functions using the rules of differentiation:

a) y = (x − 1)^3

b) y = x^3 − 5x^2 + 1

c) y + 7x = 1

### General method for sketching cubic graphs

1\. Consider the sign of a and determine the general shape of the graph.

2\. Determine the y-intercept by letting x = 0.

3\. Determine the x-intercepts by factorising ax^3 + bx^2 + cx + d = 0 and solving for x.

4\. Find the x-coordinates of the turning points of the function by letting f′(x) = 0 and solving for x.

5\. Determine the y-coordinates of the turning points by substituting the x-values into f (x).

6\. Plot the points and draw a smooth curve.

##### Example

Problem: Sketch the graph of g (x) = x^3 − 3x^2 − 4x.

SOLUTION

Step 1: Determine the shape of the graph

The coefficient of the x^3 term is greater than zero, therefore the graph will have the following shape: ∕⁻∖\_∕

Step 2: Determine the intercepts

The y-intercept is obtained by letting x = 0:

g (0) = (0)^3 − 3 (0)^2 − 4 (0)

= 0

This gives the point (0; 0).

The x-intercept is obtained by letting g(x) = 0 and solving for x:

0 = x^3 − 3x^2 − 4x

= x(x^2 − 3x − 4)

= x(x − 4)(x + 1)

∴ x = −1, x = 0 or x = 4

This gives the points (−1; 0), (0; 0) and (4; 0).

Step 3: Calculate the stationary points

Find the x-coordinates of the stationary points by setting g′(x) = 0:

g′(x) = 3x^2 − 6x − 4

0 = 3x^2 − 6x − 4

Using the quadratic formula x = \[-(-6) ± √\[(-6)^2 - 4(3)(-4)]]/ (2\*3) = \[6 ± √(36 + 48)]/6

∴ x = 2,53 or x = −0,53

Substitute these x-coordinates into g(x) to determine the corresponding y-coordinates:

g (x) = (2,53)^3 − 3 (2,53)^2 − 4 (2,53)

= −13,13

g (x) = (−0,53)^3 − 3 (−0,53)^2 − 4 (−0,53)

= 1,13

Therefore, the stationary points are (2,53; −13,13) and (−0,53; 1,13).

Step 4: Draw a neat sketch

### Concavity and point of inflection

Concavity indicates whether the gradient of a curve is increasing, decreasing or stationary.

• Concave up: the gradient of the curve increases as x increases.

• Concave down: the gradient of the curve decreases as x increases.

• Zero concavity: the gradient of the curve is constant.

VISUAL TOOL: Able to render function graphs on the same set of cartesian axes.

The diagram shows the graph of the cubic function k(x) = x^3. The first derivative of k(x) is a quadratic function, k′(x) = 3x^2

and the second derivative is a linear function, k′′(x) = 6x.

Notice the following:

• k′′(x) > 0, the graph is concave up.

• k′′(x) < 0, the graph is concave down.

• k′′(x) = 0, change in concavity (point of inflection).

Points of inflection (DIAGRAM REQUIRED)

* This is the point where the concavity of a curve changes, as shown in the diagram below. If a < 0, then the concavity changes from concave up (purple) to concave down (grey) and if a > 0, concavity changes from concave down (blue) to concave up (green). Unlike a turning point, the gradient of the curve on the left-hand side of an inflection point (P and Q) has the same sign as the gradient of the curve on the right-hand side.
* A graph has a horizontal point of inflection where the derivative is zero but the sign of  the gradient of the curve does not change. That means the graph (shown below) will continue to increase or decrease after the stationary point.
* In the example of k(x) = x^3, the equation k′(x) = 3x^2 indicates that the gradient of this curve will always be positive (except where x = 0). Therefore, the stationary point is a point of inflection.

 

Generally: The turning points of a cubic function f will correspond to the x-intercepts of the first derivative function f′. A point of inflection in a cubic function will correspond to the turning point of the first derivative function f′ and the x intercept of the second derivative function f′′.

#### Questions

Complete the following for each function:

• Determine and discuss the change in gradient of the function.

• Determine the concavity of the graph.

• Find the inflection point.

• Draw a sketch of the graph.

1\. f : y = −2x^3

2\. g(x) = 1/8 x^3 + 1

3\. h : x → (x − 2)^3

### Interpreting graphs

##### Example

DIAGRAM: Cartesian axes.  Curve with  a single turning point, a minimum. y-intercept shown at (0;-6) and 2 x-intercepts at (1;0) and (-2;0). Curve is labelled g′.

Consider the graph of the derivative of g(x).

1\. For which values of x is g(x) decreasing?

2\. Determine the x-coordinate(s) of the turning point(s) of g(x).

3\. Given that g(x) = ax^3 + bx^2 + cx, calculate a, b and c.

SOLUTION

Step 1: Examine the parabolic graph and interpret the given information

We know that g′(x) describes the gradient of g(x). To determine where the cubic function is decreasing, we must find the values of x for which g′(x) < 0 i.e below the x-axis:

Diagrammatic visual required.

{x : −2 < x < 1; x ∈ ℝ} or we can write x ∈ (−2; 1)

Step 2: Determine the x-coordinate(s) of the turning point(s)

To determine the turning points of a cubic function, we let g′x) = 0 and solve for the x-values. These x-values are the x-intercepts of the parabola and are indicated on the given graph:

x = −2 or x = 1

Step 3: Determine the equation of g(x)

g(x) = ax^3 + bx^2 + cx

g′(x) = 3ax^2 + 2bx + c

From the graph, we see that the y-intercept of g′(x) is −6.

∴ c = −6

g′(x) = 3ax2 + 2bx − 6

Substitute x = −2 : g′(−2) = 3a(−2)2 + 2b(−2) − 6

0 = 12a − 4b − 6 . . . . . .(1)

Substitute x = 1 : g′(1) = 3a(1)2 + 2b(1) − 6

0 = 3a + 2b − 6 . . . . . .(2)

Eqn. (1) − 4 Eqn. (2) : 0 = 0 − 12b + 18

∴ b = 3/2

And 0 = 3a + 2(3/2) - 6

0 = 3a - 3

∴a = 1

g(x) = x^3 + 3/2 x^2 - 6x

Diagrammatic visual: g(x) and g′(x) drawn on the same set of cartesian axes.

#### Questions

1\. Given f (x) = x^3 + x^2 − 5x + 3.

a) Show that (x − 1) is a factor of f (x) and hence factorise f (x).

b) Determine the coordinates of the intercepts and the turning points.

c) Sketch the graph.

2\. a) Sketch the graph of f (x) = −x^3 + 4x^2 + 11x − 30. Show all the turning points and intercepts with the axes.

b) Given g(x) = x^3 −4x^2 −11x+ 30, sketch the graph of g without any further calculations. Describe the method for drawing the graph.

3\. DIAGRAM REQUIRED: Cubic function of the form ∕⁻∖\_∕. The local minimum turning point is labelled A.

The sketch shows the graph of a cubic function, f, with a turning point at (2; 0), going through (5; 0) and (0; −20).

a) Find the equation of f.

b) Find the coordinates of turning point A.

4\. a) Find the intercepts and stationary point(s) of

f(x) = −1/3 x^3 + 2 and draw a sketch of the graph.

b) For which values of x will:

i. f(x) < 0

ii. f′(x) < 0

iii. f′′(x) < 0

Motivate each answer.

5\. Use the information below to sketch a graph of each cubic function (do not find

the equations of the functions).

a)

g(−6) = g(−1,5) = g(2) = 0

g′(−4) = g′(1) = 0

g′(x) > 0 for x < −4 or x > 1

g′(x) < 0 for − 4 < x < 1

b)

h(−3) = 0

h(0) = 4

h(−1) = 3

h′(−1) = 0

h′′(−1) = 0

h′(x) > 0 for all x values except x = −1

6\. DIAGRAM: Cubic curve of the form ∖\_∕⁻∖

The point labelled A  shares a y-coordinate with the local maximum turning point (labelled F). The smallest value x intercept is labelled B, the local minimum turning point is labelled C, the y- intercept is labelled D, the middle value x-intercept is labelled E, the local maximum turning point is labelled F, and the positive most x-intercept is labelled G. The function is labelled f.

6\. The sketch below shows the curve of f(x) = −(x+ 2)(x−1)(x−6) with turning points at C and F. AF is parallel to the x-axis.

Determine the following:

a) length OB

b) length OE

c) length EG

d) length OD

e) coordinates of C and F

f) length AF

g) average gradient between E and F

h) the equation of the tangent to the graph at E

7\. DIAGRAM: on cartesian axes, curve with no turning points but and inflection between 2 negative gradient phases. Point (3;2) is labelled at the inflection region.

Given the graph of a cubic function with the stationary point (3; 2), sketch the graph of the derivative function if it is also given that the gradient of the graph is −5 at x = 0.

8\. DIAGRAM: On cartesian axes, Curve of the form ∕⁻∖ is labelled h′. x intercepts are shown as -5 and 1.

The sketch shows the graph of h′(x) with x-intercepts at −5 and 1.

Draw a sketch graph of h(x) if h(−5) = 2 and h(1) = 6.

### Applications of differential calculus  to optimisation problems

We have seen that differential calculus can be used to determine the stationary points of functions, in order to sketch their graphs. Calculating stationary points also lends itself to the solving of problems that require some variable to be maximised or minimised. These are referred to as optimisation problems.

Finding the optimum point:

Let f′(x) = 0 and solve for x to find the optimum point.

To check whether the optimum point at x = a is a local minimum or a local maximum,

we find f′′(x):

• If f′′(a) < 0, then the point is a local maximum.

• If f′′(a) > 0, then the point is a local minimum.

Important note:

The quantity that is to be minimised or maximised must be expressed in terms of only one variable. To find the optimised solution we need to determine the derivative and we only know how to differentiate with respect to one variable (more complex rules for differentiation are studied at university level).

##### Examples

1. Problem: The fuel used by a car is defined by
   f (v) = 3/80 v^2 − 6v + 245, where v is the travelling speed in km/h. What is the most economical speed of the car?

Solution:

* In other words, determine the speed of the car which uses the least amount of fuel.
* If we draw the graph of this function we find that the graph has a minimum. The speed at the minimum would then give the most economical speed.
* We have seen that the coordinates of the turning point can be calculated by differentiating the function and finding the x-coordinate (speed in the case of the example) for which the derivative is 0.

  f′(v) = 3/40 v − 6

If we set f′(v) = 0 we can calculate the speed that corresponds to the turning point:

f′(v) = 3/40 v − 6

0 = 3/40 v − 6

v = (6\*40)/3

= 80

This means that the most economical speed is 80 km/h.

2\. Problem: The sum of two positive numbers is 10. One of the numbers is multiplied by the square of the other. If each number is greater than 0, find the numbers that make this product a maximum.

Draw a graph to illustrate the answer.

SOLUTION

Step 1: Analyse the problem and formulate the equations that are required

Let the two numbers be a and b and the product be P.

a + b = 10 . . . . . .(1)

P = a × b^2. . . . . .(2)

Make b the subject of equation (1) and substitute into equation (2):

P = a (10 − a)^2

= a(100 - 20a + a^2)

∴ P(a) = 100a − 20a^2 + a^3

Step 2: Differentiate with respect to a

P′(a) = 100 − 40a + 3a^2

Step 3: Determine the stationary points by letting P′(a) = 0

We find the value of a which makes P a maximum:

P′(a) = 3a^2 − 40a + 100

0 = (3a − 10)(a − 10)

∴ a = 10 or a = 10/3

Substitute into the equation (1) to solve for b:

If a = 10 : b = 10 − 10

= 0 (but b > 0)

∴ no solution

If a = 10/3: b = 10 - 10/3

= 20/3

Step 4: Determine the second derivative P′′(a)

We check that the point (10/3 ; 20/3) is a local maximum by showing that P′′(10/3)<0:

P′′(a) = 6a - 40

∴ P′′(10/3) = 6(10/3) - 40

= 20 - 40

= -20

Step 5: Write the final answer

The product is maximised when the two numbers are 10/3 and 20/3.

Step 6: Draw a graph

To draw a rough sketch of the graph we need to calculate where the graph intersects with the axes and the maximum and minimum function values of the turning points:

Intercepts:

P(a) = a^3 − 20a^2 + 100a

= a(a − 10)^2

Let P(a) = 0 : (0; 0) and (10; 0)

Turning points:

P′(a) = 0

∴ a = 10/3 or a = 10

Maximum and minimum function values:

Substitute (10/3 ; 20/3) : P =ab^2

= (10/3)(20/3)^2

= 4000/27

≈ 148

(A maximum turning point)

Substitute (0; 10) : P = ab^2

= (10)(0)^2

= 0

(A minimum turning point)

DIAGRAM REQUIRED

3\. Problem

Michael wants to start a vegetable garden, which he decides to fence off in the shape of a rectangle from the rest of the garden. Michael has only 160 m of fencing, so he decides to use a wall as one border of the vegetable garden. Calculate the width and length of the garden that corresponds to the largest possible area that Michael can fence off.

SOLUTION

Step 1: Examine the problem and formulate the equations that are required

The important pieces of information given are related to the area and modified perimeter of the garden. We know that the area of the garden is given by the formula:

Area = w × l

The fencing is only required for 3 sides and the three sides must add up to 160 m.

160 = w + l + l

Rearrange the formula to make w the subject of the formula:

w = 160 − 2l

Substitute the expression for w into the formula for the area of the garden. Notice that this formula now contains only one unknown variable.

Area = l(160 − 2l)

= 160l − 2l^2

Step 2: Differentiate with respect to l

We are interested in maximising the area of the garden, so we differentiate to get the following:

dA/dl = A′ = 160 − 4l

Step 3: Calculate the stationary point

To find the stationary point, we set A′ (l) = 0 and solve for the value(s) of l that maximises the area:

A′(l) = 160 − 4l

0 = 160 − 4l

4l = 160

∴ l = 40

Therefore, the length of the garden is 40 m.

Substitute to solve for the width:

w = 160 − 2l

= 160 − 2 (40)

= 160 − 80

= 80

Therefore, the width of the garden is 80 m.

Step 4: Determine the second derivative A′′(l)

We can check that this gives a maximum area by showing that A′′ (l) < 0:

A′′ (l) = −4

Step 5: Write the final answer

A width of 80 m and a length of 40 m will give the maximum area for the garden.

#### Questions

1\. The sum of two positive numbers is 20. One of the numbers is multiplied by the square of the other. Find the numbers that make this product a maximum.

2\. DIAGRAM: Triangular prism, with right-angle triangles at each end. Hypotenuse is 5x, the sides that are perpendicular to each other are 3x and 4x in length. The length between the triangular ends is labelled y.

A wooden block is made as shown in the diagram. The ends are right-angled triangles having sides 3x, 4x and 5x. The length of the block is y. The total surface area of the block is 3600 cm^2

a) Show that y = (300-x^2)/x.

b) Find the value of x for which the block will have a maximum volume. (Volume = area of base × height).

3\. DIAGRAM: Curves of the functions f(x) = -x^2 + 2x + 3 and g(x) = 8/x, x>0 are drawn on the same cartesian set of axes.

 Determine the shortest vertical distance between the curves of f and g if it is given that:

f(x) = −x^2 + 2x + 3

and g(x) = 8/x, x > 0

4\. . A rectangular juice container, made from cardboard, has a square base and holds 750 cm3 of juice. The container has a specially designed top that folds to close the container. The cardboard needed to fold the top of the container is twice the cardboard needed for the base, which only needs a single layer of cardboard.

a) If the length of the sides of the base is x cm, show that the total area of the

cardboard needed for one container is given by:

A(in square centimetres) = 3000/x + 3x^2

b) Determine the dimensions of the container so that the area of the cardboard used is minimised.

### Applications of differential calculus to rates of change problems

* It is very useful to determine how fast (the rate at which) things are changing. Mathematically we can represent change in different ways. For example we can use algebraic formulae or graphs.
* Graphs give a visual representation of the rate at which the function values change as the independent (input) variable changes. This rate of change is described by the gradient of the graph and can therefore be determined by calculating the derivative.
* We have learnt how to determine the average gradient of a curve and how to determine the gradient of a curve at a given point. These concepts are also referred to as the average rate of change and the instantaneous rate of change.

Average rate of change  = \[*f*(x+h) - *f*(x)]/\[(x+h)-x]

Instantaneous rate of change = lim{h→0}\[*f*(x+h) - *f*(x)]/h

When we mention rate of change, the instantaneous rate of change (the derivative) is implied. When average rate of change is required, it will be specifically referred to as average rate of change.

Velocity is one of the most common forms of rate of change:

Average velocity = Average rate of change

Instantaneous velocity = Instantaneous rate of change = Derivative

Velocity refers to the change in distance (s) for a corresponding change in time (t).

ν (t) = ds/dt = s′(t)

Acceleration is the change in velocity for a corresponding change in time. Therefore, acceleration is the derivative of velocity

a(t) = ν′(t)

This implies that acceleration is the second derivative of the distance.

a (t) = s′′(t)

##### Examples

1. Problem: The height (in metres) of a golf ball t seconds after it has been hit into the air, is given by H (t) = 20t − 5t^2

Determine the following:

a. The average vertical velocity of the ball during the first two seconds.

b. The vertical velocity of the ball after 1,5 s.

c. The time at which the vertical velocity is zero.

d. The vertical velocity with which the ball hits the ground.

e. The acceleration of the ball.

SOLUTION

Step 1: Determine the average vertical velocity during the first two seconds

ν\_ave = \[H(2) - H(0)]/(2-0)

= (\[20(2) - 5(2)^2] - \[20(0) - 5(0)^2])/2

= (40 - 20)/2

= 10 m.s^-1

Step 2: Calculate the instantaneous vertical velocity

ν(t) = H′(t)

= dH/dt

= 20 − 10t

Velocity after 1,5 s:

ν(1,5) = 20 − 10 (1,5)

= 5 m.s^-1

Step 3: Determine the time at which the vertical velocity is zero

ν(t) = 0

20 − 10t = 0

10t = 20

t = 2

Therefore, the velocity is zero after 2 s

Step 4: Find the vertical velocity with which the ball hits the ground

The ball hits the ground when H (t) = 0

20t − 5t^2 = 0

5t(4 − t) = 0

t = 0 or t = 4

The ball hits the ground after 4 s. The velocity after 4 s will be:

v (4) = H0

(4)

= 20 − 10 (4)

= −20 m.s^−1

The ball hits the ground at a speed of 20 m.s^-1. Notice that the sign of the velocity is negative which means that the ball is moving downward (a positive velocity is used for upwards motion).

Step 5: Acceleration

a = v′(t) = H′′(t)

= −10

∴ a = -10 m.s^-2

Just because gravity is constant does not mean we should necessarily think of acceleration as a constant. We should still consider it a function.

#### Questions

1\. A pump is connected to a water reservoir. The volume of the water is controlled by the pump and is given by the formula:

V (d) = 64 + 44d − 3d^2

where V = volume in kilolitres

d = days

a) Determine the rate of change of the volume of the reservoir with respect to time after 8 days.

b) Is the volume of the water increasing or decreasing at the end of 8 days.

Explain your answer.

c) After how many days will the reservoir be empty?

d) When will the amount of water be at a maximum?

e) Calculate the maximum volume.

f) Draw a graph of V (d).

2\. A soccer ball is kicked vertically into the air and its motion is represented by the equation:

D(t) = 1 + 18t − 3t^2

where D = distance above the ground (in metres)

t = time elapsed (in seconds

a) Determine the initial height of the ball at the moment it is being kicked.

b) Find the initial velocity of the ball.

c) Determine the velocity of the ball after 1,5 s.

d) Calculate the maximum height of the ball.

e) Determine the acceleration of the ball after 1 second and explain the meaning of the answer.

f) Calculate the average velocity of the ball during the third second.

g) Determine the velocity of the ball after 3 seconds and interpret the answer.

h) How long will it take for the ball to hit the ground?

i) Determine the velocity of the ball when it hits the ground.

3\. If the displacement s (in metres) of a particle at time t (in seconds) is governed by the equation s = 1/2t^3 − 2t, find its acceleration after 2 seconds.

4\. During an experiment the temperature T (in degrees Celsius) varies with time t (in hours) according to the formula:

T (t) = 30 + 4t −1/2 t^2, t ∈ \[1; 10].

a) Determine an expression for the rate of change of temperature with time.

b) During which time interval was the temperature dropping?

### Revision

1\. Determine f(x) from first principles if f (x) = 2x − x^2.

2\. Given f (x) = 1/x + 3, find f′(x) using the definition of the derivative.

3\. Calculate: lim{x→1} \[(1-x^3)/(1-x)]

4\. Determine dy/dx if:

a) y = (x + 2)(7 − 5x)

b) y = (8x^3+1)/(2x+1)

c) y = (2x)^2 −1/ 3x

d) y = (2√x - 5) / √x

5\. Given: f (x) = 2x^2 − x

a) Use the definition of the derivative to calculate f′(x).

b) Hence, calculate the coordinates of the point at which the gradient of the tangent to the graph of f is 7.

6\. If g(x) = (x^-2 + x^2)^2 , calculate g′(2)

7\. Given: f (x) = 2x − 3

a) Find f^-1(x).

b) Solve f^-1(x) = 3f′(x).

8\. Find the derivative for each of the following:

a) p(t) = ({5}√\[t^3])/3 + 10

b) k(n) = \[(2n^2 - 5)(3n + 2)]/n^2

9\. If xy - 5 = √(x^3), determine dy/dx .

10\. Given: y = x^3

a) Determine dy/dx .

b) Find dx/dy .

c) Show that dy/dx × dx/dy = 1.

11\. Given: f (x) = x^3 − 3x^2 + 4

a) Calculate f (−1).

b) Hence, solve f (x) = 0.

c) Determine f′(x).

d) Sketch the graph of f, showing the coordinates of the turning points and the intercepts on both axes.

e) Determine the coordinates of the points on the graph of f where the gradient is 9.

f) Draw the graph of f′(x) on the same system of axes.

g) Determine f′′(x) and use this to make conclusions about the concavity of f.

12\. Given f (x) = 2x^3 − 5x^2 − 4x + 3.

a) If f(−1) = 0, determine the x-intercepts of f.

b) Determine the coordinates of the turning points of f.

c) Draw a sketch graph of f. Clearly indicate the coordinates of the turning points and the intercepts with the axes.

d) For which value(s) of k will the equation f (x) = k have three real roots of which two are equal?

e) Determine the equation of the tangent to the graph of 

f (x) = 2x^3 − 5x^2 − 4x + 3 at the point where x = 1.

13\. Given the function f(x) = x^3 + bx2 + cx + d with y-intercept (0; 26), x-intercept (−2; 0) and a point of inflection at x = −3.

a) Show by calculation that b = 9, c = 27 and d = 26.

b) Find the y-coordinate of the point of inflection.

c) Draw the graph of f.

d) Discuss the gradient of f.

e) Discuss the concavity of f.

14\. DIAGRAM: Cartesian axes. Curve with 1 minimum turning point in the 4th quadrant (quadratic facing upwards). Intercepts the x-axis at -1 and 3. Intercepts the y-axis at -2. Curve labelled g′.

The sketch shows the graph of g′(x).

a) Identify the stationary points of the cubic function, g(x).

b) What is the gradient of function g where x = 0.

c) If it is further given that g(x) has only two real roots, draw a rough sketch of g(x) . Intercept values do not need to be shown.

15\. Given that h(x) is a linear function with h(2) = 11 and h'(2) = −1, find the equation of h(x).

16\. DIAGRAM: \[Cartesian axes with 2 curves. A blue curve annotated as g has 1 turning point, a maximum (quadratic facing down), and inteceptes the x-axis at A (on the negative x-axis) and B on the positive x-axis. A second curve annotated as f is a cubic curve drawn in black, has 2 turning points, 1 local minimum at point labelled C and 1 local maximum at point labelled B where the blue curve intercepts the x-axis; intecepts the y axis at A, where the quadratic also intercepts the x-axis. Point E is labelled on the cubic curve.]

The graphs of f and g and the following points are given below:

A(−3; 0) B(3; 0) C(−1; −32) D(0; −27) E(2; y)

a) Use the graphs and determine the values of x for which:

i. f(x) is a decreasing function.

ii. f(x) . g(x) ≥ 0.

iii. f'(x) and g(x) are both negative.

b) Given f(x) = −x^3 + 3x^2 + 9x − 27, determine the equation of the tangent to f at the point E(2; y).

c) Find the coordinates of the point(s) where the tangent in the question above meets the graph of f again.

d) Without any calculations, give the x-intercepts of the graph of f'(x). Explain reasoning.

17\. a) Sketch the graph of f (x) = x^3 − 9x^2 + 24x − 20, show all intercepts with the axes and turning points.

b) Find the equation of the tangent to f (x) at x = 4.

c) Determine the point of inflection and discuss the concavity of f.

18\. Determine the minimum value of the sum of a positive number and its reciprocal.

19\. t minutes after a kettle starts to boil, the height of the water in the kettle is given

by d = 86 −1/8 t −1/4 t^3, where d is measured in millimetres.

a) Calculate the height of the water level in the kettle just before it starts to boil.

b) As the water boils, the water level in the kettle decreases. Determine the rate at which the water level is decreasing when t = 2 minutes.

c) How many minutes after the kettle starts to boil will the water level be decreasing at a rate of 12 1/8 mm per minute?

20\. The displacement of a moving object is represented by the equation:

D(t) = 4/3 t^3 − 3t

where D = distance travelled in metres

t = time in seconds

Calculate the acceleration of the object after 3 seconds.

21\. DIAGRAM \[Semi-circle with diameter PQ labelled P and Q on each end. A point R on the circumference such that a triangle PRQ is inscribed within the semi-circle.]

In the figure PQ is the diameter of the semi-circle PRQ. The sum of the lengths of PR and QR is 10 units. Calculate the perimeter of 4P QR when 4P QR covers the maximum area in the semi-circle. Leave the answer in simplified surd form.

22\.  The capacity of a cylindrical water tank is 1000 litres. Let the height be H and the radius be r. The material used for the bottom of the tank is twice as thick and also twice as expensive as the material used for the curved part of the tank and the top of the tank.

Remember: 1000 ` = 1 m^3

a) Express H in terms of r.

b) Show that the cost of the material for the tank can be expressed as:

C = 3πr^2 + 2/r

c) Determine the diameter of the tank that gives the minimum cost of the materials.

\[IEB, 2006]

23\. DIAGRAM \[Cone with diameter , d  and height h, labelled]

The diameter of an icecream cone is d and the vertical height is h. The sum of the diameter and the height of the cone is 10 cm.

a) Determine the volume of the cone in terms of h and d.

(Volume of a cone: V = 1/3 πr^3h)

b) Determine the radius and height of the cone for the volume to be a maximum.

c) Calculate the maximum volume of the cone.

24\. A water reservoir has both an inlet and an outlet pipe to regulate the depth of the water in the reservoir. The depth is given by the function:

D(h) = 3 + 1/2 h −1/4 h^3

where D = depth in metres

h = hours after 06h00

a) Determine the rate at which the depth of the water is changing at 10h00.

b) Is the depth of the water increasing or decreasing?

c) At what time will the inflow of water be the same as the outflow?

\[IEB, 2006]

