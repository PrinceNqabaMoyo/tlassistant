# Term 1

## Differential calculus

1. An intuitive understanding of the limit concept, in the context of approximating the rate of change or gradient of a function at a point.



2\. Determine the average gradient of a curve between two points. Determine the average gradient of a curve between two points.

                 m = (f(x+h)-f(x))/h



3\. Determine the gradient of a tangent to a graph, which is also the gradient of the graph at that point. Introduce the limit-principle by shifting the secant until it becomes a tangent



4\. By using first principals for:



f'(*x*) = lim(*h*>0) (f(*x*+*h*)-f(*x*))/*h*, for f(x) = k, f(x) = ax and f(x) = ax + b



5\. Use the rule:

 	d/dx (ax^n) = axn^(n-1), for nϵℝ



6\. Find equations of tangents for graphs of functions



7\. Sketch the graph of cubic polynomial functions, using differentiation to determine the co-ordinates of the stationary points. Also determine the x-intercept of the graph using the factor theorem and other techniques.



8\. Solve practical problems concerning optimisation and rates of change, including calculus of motion.





Comment: Differentiation form 1st principles will be examinined on any of the types described in 4.

Understand that the following notations mean the same thing: D\_x, d/dx, f'(x)



Examples:

1. In each of the following cases, find the derivative of f(x) at the point where x=-1, using the definition of the derivative:

 	1.1 f(x) = x^2

 	1.2 f(x) = x^2+2



2\. Sketch the graph defined by y = -x^3+4x^2-x by:

 	2.1 finding the intercepts with the axes;

 	2.2 finding maxima, minima



On word problems the diagram with all the measurements must be given. Guide the learners through the question with subsections.



Refer to displacement formulae like s = u + (1/2)at^2



Very simple problems.

Refer to practical application in the technical field.



### The concept of a limit

Examples:

1. lim\_n→∞ 1/2^n means what is the value of 1/2^n as n approaches infinity.

 	Table: n=1; 1/2^n = 0.5, n=2; 1/2^n = 0.25, n=3; 1/2^n = 0.125, n=4; 1/2^n= 0.0625, n=5; 1/2^n =0.03125, n=6; 1/2^n = 0.015625, n=7; 1/2^n = 0.0078125



2\. f(x)= x+1. What is lim\_x→1 f(x).

we simply replace x by 1 and compute. Therefore, lim\_x→1 f(x) = f(1) = 2



3\. Show that lim\_x→4 (x^2-4) = 12 by substituting x with the values close to 4.

Table 1: x= 3.8; x^2-4 = 10.44, x= 3.9; x^2-4 = 11.21, x=3.99; x^2-4= 11.9201, x=3.999; x^2-4= 11.992001



Table 2: x=4.1; x^2-4=12.81, x=4.01; x^2-4=12.0801, x=4.001; x^2-4=12.008001, x=4.0001; x^2-4=12.00080001.



In the first table, the values of x approaches 4 from the left, and in the second table the

values of x approaches 4 from the right. Thus, the limit of x^2 – 4 as x approaches 4 is 12.

If f(x) = x^2-4, then lim\_x→4 (x^2-4) = f(4) = 16-4 = 12.



#### Questions

1. Calculate the following limits (if they exist).

 a. lim\_x→2 (x^3)

 b. lim\_x→3 (x^2-2x+5)

 c. lim\_t→1 \[(t^2-3t+2)/(t-2)]

 d. lim\_h→0 \[(h^2-h)/h]

 e. lim\_z→1 \[(z-1)/(z+1)]

 f. lim\_z→1 \[(z+1)/(z-1)]

 g. lim\_x→4 \[(x^2-16)/(x^2+7x+12)]

 h. lim\_x→1 \[(x^2-1)/(x-1)]

 i. lim\_x→3 \[(x+3)/(x^2-9)]

 j. lim\_x→-1 \[(x^2-1)/(x+1)]

 k. lim\_x→-3 \[(x+3)/(x^2-9)]

 l. lim\_x→3 (x+4)





### The average gradient of a curve between two points

A straight line passing through 2 points of a curve is called a secant. The gradient of a secant is equal to the average gradient between points A and B on the curve.

Average gradient of the curve between points A and B, m\_AB = (y\_B - y\_A)/(x\_B - x\_A) OR

\[f(x\_B)-f(x\_A)]/(x\_B - x\_A)



#### Questions

1. Consider the function given by f(x) = 2x^2+3 . Calculate the average gradient of f(x) between:

 a.  A(− 1;5)  and B(− 2;11)

 b.  A (1;f(1)) and B(2;f(2))



2\. Given  f(x) = x^2+3x − 1  calculate the average gradient between  x=3 and x=5.



3\. Given  f(x)= −x^2 +3  calculate the average gradient between  x=−1 and x=1.



4\. Given  f(x)= x^2−2x+1 . Determine the average gradient between the points where  x=−1 and x=2.



5\. Calculate the average gradient of each of the following functions between the points where x=1 and x=3

 a. f(x) = x^2 + 5

 b. f(x) = 3x-1

 c. f(x) = x^3 - 6x^2 + 11x - 6



6\. Given  f(x)= -x^2 + 9 . The points  A(−2;5), B(−1;8) and C(2;5) are on the graph of f(x). Calculate the average gradient,

 a. From A to B

 b. From B to C

 c. From A to C





### Finding the gradient of a curve (derivative) at a point using the first principles

Derivative f'(x)-  The gradient of the curve at any point



 f'(*x*) = lim(*h*>0) (f(*x*+*h*)-f(*x*))/*h*



Examples:

1. Find the derivative of f(x) = 2 using the first principles.

f(x) = 2 is the same as f(x) = 2x^0 (remember x^0 = 1)

f'(*x*) = lim(*h*>0) (f(*x*+*h*)-f(*x*))/*h*

      = lim(*h*>0) (2(x+h)^0 - 2x^0)/h

      = lim(*h*>0) (2-2)/h

      =0



2\. Find the derivative of f(x) = 3x using the first principles.

  f'(x)= lim(*h*>0) (f(*x*+*h*)-f(*x*))/*h*

       = lim(*h*>0) (3(x+h)-3x)/h

       = lim(*h*>0) 3h/h

       = lim(h>0) 3

       =3



3\. Find the derivative of f(x) = 4x + 2 using the first principles.

  f'(x)= lim(*h*>0) (f(*x*+*h*)-f(*x*))/*h*

       = lim(*h*>0) (4x+4h+2 - (4x+2))/h

       = lim(*h*>0) 4h/h

       = lim(*h*>0) 4

       = 4



#### Questions

1\. Calculate the derivative of the following functions using the first principles.

 a.  f(x)  = 6

 b.  f(x)  = x

 c.  f(x) = −2x

 d.  f(x) = 3x − 1

 e.  f(x) = −4x + 3

 f.  f(x) = x^2 + 2

 g.  f(x) = −2x^2 + 5

 h.  f(x) = 3x^2 − 2

 i.  f(x) = −5x^2 + 3

 j.  f(x) = 2−x^2

 k.  f(x) = x^2 + 2x + 1

 l.  f(x) = 4x^2 + 3





### Differentiating using the power rule

If   f(x) = *a*x^n and n is a real number and *a* is a constant, then    f′(x) = anx^(n−1)



Note:

 • The derivative of a constant is always 0

 • We use the following notations for the derivatives of functions:

 •   D~x~ or d/dx or dy/dx or f′(x)



#### Questions

1. Calculate:

 a. d/dx(3x^2)

 b. d/dx(-4x^2+1)

 c. D~x~(x^3 - 4x^2)

 d. f′(x) if f(x) = 1/2(x^4) - 6

 e. d/dx(-8x^(1/2) - 7x^3)

 f. dy/dx if y = 5/6(x^6) - 7

 g. d/dx(3x^(1/9) - 4x^2 - 9)

 h. D~x~(-2x^5 + x^6 - 9)

 i. D~x~(4-2x^2)

 j. f'(x) if f(x) = 3x^2 + 2x - 1

 k. dy/dx if y = -3x^2 + 5x

 l. dy/dx if y = 7x^3 + 3x^2 + x - 10



### The equation of a tangent at a given point

Example: Find the equation of the tangent to the curve  f(x)  = 2x^3 - x^2 + x + 1  at  x = -1

The gradient of the tangent is calculated as follows:

  f′(x) = 3\*2*x*^(3−1)-2x^(2−1) + 1x^(1−1) + 0

        = 6x^2 - 2x + 1x^0

        = 6x^2 - 2x + 1

gradient at x=-1: 6(-1)^2 - 2(-1) + 1 = 9



x coordinate = -1; y coordinate = 2\*-1^3 - (-1^2) - 1 + 1

Tangent passes through (-1;-3)

Equation of a straight line: y = mx+c

therefore,  y = 9x + c

           -3 = 9(-1) + c

            c = 6



This implies that, equation of gradient is y = 9x + 6



Simpler formular: y - y~1~ = m(x - x~1~)



#### Questions

1.  Determine the equation of the tangent at the given point for the following curves.

 a. f(x) =  x^2 - 4 at x = 2

 b. f(x) = -3x^2 - x at x = - 1

 c. f(x) =  x^3 - x^2 at x = - 2

 d. f(x) =  x^2 + 3x + 2 at x = 3

 e. f(x) = -1/2x^2 + 3x at x = 4

 f. f(x) =  x^2 at x = -1.

 g. f(x) = -x^2 + 1 at x = -1

 h. f(x) =  x^2 + 10x + 25 at x = 1

 i. f(x) =  x^3 + 3x^2 + 1 at x = 1

 h. f(x) = -x^3 + 2 at x = -1



### Cubic functions

Diagram: HTML of cubic graph that shows turning points, increasing and decreasing gradients properly annotated

 f′(x) < 0, f(x)  is increasing

 f′(x) > 0, f(x)  is decreasing

 f′(x) = 0, At the turning point (critical point/stationary point)



 Suppose   f′(x) = a

 • If   f′(x)  changes from positive to negative as x increases through a, then f has a local

maximum at a.

 • If   f′(x)  changes from negative to positive as x increases through a, then f has a local

minimum at a.



Example: Find and classify the stationary points of  f(x) = x^3 - 3x^2 - 9x.

  f′(x) = 3x^2 - 6x - 9 = 3(x + 1)(x − 3)

Table:

x|-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6|

f′(x) = 3x^2 - 6x - 9|+, +, +, 0, -, -, -, 0, +, +, +|



Before x = –1, derivative is positive, after x=-1 derivative is  negative. Therefore, stationary pointg at  x = –1 is a maximum.



Before x = 3, derivative is negative, after x=3, derivative is positive, therefore stationary point at x=3 is a minimum.



#### Questions

1.  Determine and classify all stationary points of:

 a.  f(x) = 2x^2 - 8x + 1

 b.  f(x) = -x^2 + 6x - 3

 c.  f(x) = x^3 + 3x^2

 d.  f(x) = x^3 - 2x^2 - 15

 e.  f(x) = x^3 - 3x

 f.  f(x) = x^3 - 12x + 3

 g.  f(x) = x^3

 h.  f(x) = 3x^3 - 2x^2 + 1

 i.  f(x) = x^3 + 1

 j.  f(x) = 2x^2 + 5x - 3



### Cubic Curve sketching

Visual Aid needs to include cubic curve sketching based on the following principles



Users should

Step 1- Determine the y- intercept, where x=0

Step 2- Determine the x- intecepts (solutions), where y/ f(x) = 0

Step 3- Determine the stationary points, where f'(x) = 0

Step 4- Determine the ranges of positive and negative gradient

Step 5- Determine the which stationary point is a maximum and which is a minimum



The visual aid will then plot the points as the user goes through the steps. Then it will prompt user to connect points 2 at a time by clicking them consecutively. The Aid will first render straight (zig/zag) lines connecting the points, then show a (smooth curve) button, which when the user clicks makes the curve smooth like a proper cubic curve.



#### Questions

Questions involving curve sketching should render an html container that allows user to input y-intercept, x-intercepts, stationary points, ranges of positive and negative gradient, and maxima/minima.



1.  Sketch each graph below. Clearly indicate the:

 a. f(x) = –x^3 – 3x^2 + 4

 b. f(x) = x^3 – 2x^2 – 4x + 8

 c. f(x) = (x – 2)^2 (x + 3)

 d. f(x) = x^3 – 4x^2 – 3x + 18

 e. f(x) = x^3 – 4x

 f. f(x) = x^3

 g. f(x) = x^3 – 11x^2 + 24x

 h. f(x) = –2x^3

 i. f(x) = (x + 1)(x^2 - 9)

 j. f(x) = (x + 1)(x + 2)(x − 1)



### Applications of differentiation

Applied to  rate of change and optimisation problems



Examples:

1. A football is punted into the air. Its displacement is given by the equation s(t)= -16t^2 + 37t + 3   where s(t) is its displacement in metres and t is time in seconds.

 a) Find equations for its velocity.

 b) Find velocity at t = 1 and at t = 2.

 c) Find its acceleration.



a. Velocity =  s′(t) = -32t + 37

b.  t= 1: s′(1) = -32(1 ) + 37 = 5 m/s

    t =2: s′(2) = -32(2 ) + 37 = -27 m/s

c. The instantaneous rate of change of velocity is called acceleration. It is the derivative of

the velocity. Using v for velocity,  v = -32t + 37 , thus acceleration  = dv/dt = -32.



2\. The edges of a rectangular box are height= x, Breadth= 2x and Length= 180 - 3x.

Determine:

 a) the volume of box in terms of x

 b) the value of x which will make the volume of the box a maximum

 c) the dimensions of the box.



a. The volume V of the box in terms of x is given by:

     V(x)= (x)(2x )(180 − 3x)

         = 360x^2 - 6x^3

b.  V = 360x^2 - 6x^3

    V′(x) = 720x − 18x^2

    V′(x) = 0 at max or min

    x^2 - 40x = 0

   x(x − 40) = 0

 x = 0  or  x = 40

             ∴ x = 40



c.  The dimensions of the box are:

 Height   = 40 units

 Breadth  = 2(40) = 80 units

 Length   = 180 - 3(40)

          = 180 - 120

          = 60 units



#### Questions

1. The object moves in the x-direction with displacement from the y-axis given by

x = 3t^3 - 30t^2 + 64t + 57, for t ≥ 0, where x is in metres and t is in hours.

 1.1 Find the equation for its velocity.

 1.2 Find the equation of its acceleration.

 1.3 Find the velocity at t = 3.

 1.4 Find the acceleration at t = 3



2\. When a ball is thrown straight up into the air, it travels along a straight line. Its motion

can be described in the same manner as the motion of a car, thus regard up as the positive direction and let s(t) be the height of the ball in metres after t seconds.

Suppose that  s(t) = -16t^2 + 128t + 5 .

 2.1 What will the velocity be after 2 seconds?

 2.2 What will the acceleration be after 2 seconds?

 2.3 After how many seconds will the ball attain its greatest height?



3\. A helicopter is ascending straight up into the air. Its distance from the ground t seconds

after take-off is s(t) m, where  s(t) =  t^2 + t.

 3.1 How long will it take for the helicopter to ascend 20 m?

 3.2 Find the velocity and the acceleration of the helicopter when it is 20 m above the

     ground?



4\. Diagram: A rectangle with Length = x, Width = y. 1 length side is walled off by the building, so no need for a fence.

 Mr Smith wants to enclose his field with a rectangular fence. He has 500 m of fencing

material, and a building on one side of the field. This region will not need any fencing. Determine the dimensions of the field that will enclose the largest area.



5\. Diagram: A rectangle with 4 squares cut of from the corner. The side of the square cutoffs = x.Lines are drawn along the fold lines of the cardboard depiction. A box without a lid is made by removing squares from each corner of a rectangular piece of cardboard and then folding up the sides. The original cardboard is 75 cm long and  45 cm wide.

 a. Show that the volume of the box is given by  V(x) = 4x^3 - 240x^2 + 3375x

 b. Calculate the value of x that will result in the maximum possible volume.

 c. Calculate the maximum volume.



6.A steel producing company determines that in order to sell  x  units of a particular type of

steel pipes, the price per unit, in rands, must be p(x) = 1500 − x. The company also determines that the total cost of producing  x  units of steel pipes is given by C(x) = 4500 + 60x

 6.1 Show that the total revenue is given by the formula:

          R(x)= 1500x - x^2 Hint:Revenue = quantity × price

 6.2 Write down the formula for calculating the total profit  (P(x)) in terms of x.

 6.3 How many units must the company produce and sell in order to make maximum profit?

 6.4 Calculate the maximum profit.

 6.5 What price must the company charge for the steel pipes in order to make this maximum profit



### Revision

 1. Find the following limits (if they exist).

  a. lim\_x→3(2x + 5)

  b. lim\_x→2(x^2 - 1)

  c. lim\_x→3(1/(x-1))

  d. lim\_x→a(1/(x-a))

  e. lim\_x→2(x^2 - 4x + 4/(x-2))

  f. lim\_x→3((x^3-1)/(x-1))



2\. Determine the average gradient of the following function between the given points.

 f(x) = -2x + 6

 2.1 between x = 2 and x = 5

 2.2 between x = –1 and x = 0

 2.3 between x = –2 and x = 3



3\. Determine the gradients and the equations of the tangents of the following curves for the given values of x.

 3.1  f(x)  = -x^2 + 2x at x= 4

 3.2  f(x)  = 2x^2 - 5x + 7 at x = 2

 3.3  f(x)  = (x + 4)(x + 1)^2  at x = –1

 3.4  f(x)  = 2x^3 at x = –2

 3.5  f(x)  = 2/x at x = 4



4\. Use the first principles method to determine the derivatives of the following:

 4.1  f(x)  = -2x + 6

 4.2  f(x)  = -3x

 4.3  h(x)  = 6x + 6

 4.4  f(x)  = 4x^2 + 9

 4.5  f(x)  = -7x^2 - 4



5\. Determine the following using the rules of differentiation.

 5.1  dy/dx  if  y =  x^3  + 4

 5.2  d/dt(3t - 4t^2 )

 5.3  D~x~(2x^2 - x - 6)

 5.4  f'(x) if  f(x) = -3x^2 + 2x

 5.5  dy/dx if  y = 5x(x + 8)



6\. Sketch the following graphs. Show the:

 (i) intercepts

(ii) coordinates of the stationary points.

 6.1  f(x) = x^3 + 3x^2 - 4

 6.2  f(x) = x^3 - 4x

 6.3  f(x) = 2x^3 - 2x^2 - 5x - 1

 6.4  f(x) = x^3 - 3x^2 - x + 3



7\. A rocket is fired vertically upwards and its height in metres is measured by  h(t) = 40t – 5t^2.

 7.1 Calculate the rocket’s initial velocity.

 7.2 Determine the rocket’s maximum height.

 7.3 Calculate the rocket’s acceleration.



8\.  Diagram: Rectangular prism/box with Length = 4x, Breadth = x and Height = h. A storage container takes the form of a right    prism. It has a volume of 5 000 cm2.  Its length is four times its breadth.

  8.1. Determine the total surface area of the container in terms of x.

  8.2.  Determine the dimensions of the container for which the total surface will be a minimum.

  8.3  Calculate the minimum surface area.







 

## Integration

Introduce integration

1. Understand the concept of integration  as a summation function (definite  integral) and as converse of  differentiation (indefinite integral).

2\. Apply standard forms of integrals as a  converse of differentiation.

3\. Integrate the following functions:

 	3.1 kx^n, nϵℝ with n ≠ -1

 	3.2 k/x and ka^(nx) with a≥0, k, a ϵ ℝ

4\. Integrate polynomials consisting of terms of the above forms (3.1 and 3.2)

5\. Apply integration to determine the magnitude of an area included by a curve and the x-axis or by a curve, the x-axis and the ordinates x=a and x=b where a, b ϵ ℤ



Examples

1. Calculate the values of

 	1.1 ∫\_{0}^{1} xdx

 	1.2 ∫\_{1}^{2} (x^3 + 2x^2 -3)dx



Determine the area included by the curve of y = x^2 +x and the x-axis.



The curve is drawn below and the area between the curve and x-axis is shaded.



### The Indefinite integrals

1\. ∫x^n dx =  x^(n+1)/(n + 1) + C, n ≠ -1



2\. A constant factor in an integral can be moved outside the integral sign ∫kx^n dx = k∫x^n dx



Including in our answer an unknown constant, C, called the constant of integration.   The function being integrated is called the integrand.

The answer is called an indefinite integral and represents many possible anti-derivatives.



#### Questions

1.  Find the following indefinite integrals

 a. ∫5dx

 b. ∫3x^3dx

 c. ∫x^3dx

 d. ∫6x^5dx

 e. ∫8x^7dx

 f. ∫(-x)dx

 g. ∫x^4dx

 h. -∫3xdx

 i. ∫1/2(x)dx

 j. 5∫x^4dx

 k. ∫x^6dx

 l. ∫(-9x^8)dx



### The integral of f(x)+g(x) or of f(x)-g(x)

We can integrate the sum or difference of two or more functions by integrating each term separately.

  ∫(4x^3 - 2x^2 + x - 2)dx  =  ∫4x^3dx - ∫2x^2dx + ∫xdx - ∫2dx



1. Find each integral.

 a. ∫(x + 1)dx

 b. ∫(-x + 1)dx

 c. ∫(3x + 2)dx

 d. ∫(1 - x^2)dx

 e. ∫(1 - x^3)dx

 f. ∫(x^2 - 2x + 1)dx

 g. ∫(x^3 - 2x^2 + x - 5)dx

 h. ∫(3x^4 - x^5)dx

 i. ∫(5 + 3x + x^2)dx

 j. ∫(-3x^2 + 1/2x + 1)dx



### The integral of the form ∫1/x dx, x ≠ 0

we use the general logarithm rule  ∫1/xdx = ln|x| + C, x ≠ 0



#### Questions

1.  Find the following integrals

 a. ∫7/x dx

 b. ∫100/x dx

 c. ∫23/x dx

 d. ∫(√3)/x dx

 e. ∫(√5)/x dx

 f. ∫(√11)/x dx

 g. ∫(2)/3x dx

 h. ∫(2)/5x dx

 i. ∫(-1)/3x dx

 j. ∫2/x dx

 k. ∫(3)/2x dx

 l. ∫(√7)/x dx

 m. ∫(100/x + x^2) dx

 n. ∫(-x + 5/(6x) + 1) dx

 n. ∫(-1/x + 6) dx



### Definite integrals

The quantity    ∫~a~^b f(x) dx   is called the definite integral of  f(x)  from  a to b .

The numbers  a and b are called the limits of integration. They tell us the interval we are working in. The number a is called the lower limit and  b  is called the upper limit.

If  f(x)  is the integral of  f'(x) , then ∫~a~^b f'(x) dx  = f(b )  − f(a) . To evaluate the definite integral we:

 • integrate the given function but we do not include the constant of integration

 • then substitute the value of the upper limit into the integral  f (b)

 • substitute the value of the lower limit into the integral  f (a)

 • subtract the value of the lower from that of the upper limit.

 • i.e we calculate  f (b) - f(a)

 • The answer is a number

 • The constant C is omitted when using the integration formulas to find a definite integral.



Examples



1.  ∫~1~^2 (2x)dx =  2∫~1~^2 xdx = 2\[x^2/2]~1~^2 = 2\[(2^2/2)-(1^2/2)] = 3
2.  ∫~1~^3 (3x-x^3)dx = \[(3x^2)/2 - (x^4)/4]~1~^3=\[(3\*9/2)-81/4]-(3/2 - 1/4) = -27/4 - 5/4 = -32/4 =8



#### Questions

&nbsp;1. ∫~0~^2 (x^2 + x)dx

&nbsp;2. ∫~1~^3 (3u^3 - 1)du 

&nbsp;3. ∫~-2~^-1 (x^3 - 2x)dx

&nbsp;4. ∫~-2~^1 (6x^2 - 5x + 2)dx

&nbsp;5. ∫~0~^4 √t(t + 2)dt

&nbsp;6. ∫~0~^1 (4x − 6x^2/3)dx 

&nbsp;7. ∫~-2~^0 ((1/3)x^2 - 2)dx

&nbsp;8. ∫~2~^3 (1/2)x^4 + x)dx

&nbsp;9. ∫~0~^2 (1 - x^2 )dx 

&nbsp;10.∫~-1~^1 (x + 1)dx 



### Using integration to find the area included by a curve and the x-axis or by a curve the x-axis and the ordinates x – *a* and x – *b*, where *a*, *b* ∈ ℤ.



Required visual aid: A graph drawing HTML that shows shading between the x-axis and curve within a specific range.



When a function f(x) is both positive and negative in the given interval like the example above, and the area is to be found, the limits of integration must be split at the zeros of the function. Areas A1 and A2 were calculated separately. The total area is the sum of two areas. 



Example:

Find the total area between f(x) = x^3 – x and the x-axis from x = –1 to x = 1.



Diagram- Graph of x^3 – x on  a grid with the area between the graph and x-axis shaded form x=-1 to x=1. 



Answer:  

A1 = ∫~-1~^0 (x^3 - x)dx = \[(x^4 - 2x^2)/4]~-1~^0 = 0 - (-1/4) = 1/4

A2 = ∫~0~^1 (x^3 - x)dx = \[(x^4 - 2x^2)/4]~0~^1 = -1/4 We take the modulus (absolute value) 1/4

Total area = A1 + A2 = 1/4 + 1/4 = 1/2 square units.



#### Questions

1. &nbsp;Use integration to find the shaded areas of the following.

&nbsp; a. Diagram: Graph of  y = -4 + x^2 with shaded area in range -2<x<2

&nbsp; b. Diagram: Graph of  y = –x^2 + 4 with shaded area in range 0<x<2

&nbsp; c. Diagram: Graph of  f(x) = 2x + 1 with shaded area in range -3<x<2

&nbsp; d. Diagram: Graph of  f(x) = x^2 – 6x + 5 with shaded area in range 1<x<5

&nbsp; e. Diagram: Graph of   y = x^3 – 6x^2 + 11x – 6 with shaded area in range 1<x<3

&nbsp; f. Diagram: Graph of   y = x^2 + 2 with shaded area in range 1<x<3

&nbsp; g. Diagram: Graph of   y = 3x - x^2 with shaded area in range 0<x<3

&nbsp; h. Diagram: Graph of   y = x^3 – 6x^2 + 11x – 6 with shaded area in range 1<x<3

&nbsp; I. Diagram: Graph of   y = -x^2 + 3x + 4 with shaded area in range -1<x<4

&nbsp; j. Diagram: Graph of   y = x^2 – x – 6 with shaded area in range -2<x<3

&nbsp; h. Diagram: Graph of   y = x^2 + 5x + 4 with shaded area in range -4<x<-1

&nbsp; I. Diagram: Graph of   y = x^3 – 4x with shaded area in range -2<x<2





### The indefinite integral of an exponential function of the form f(x) = e^x

To integrate exponential functions of the form  f(x) = e^x   we use the rule:   ∫e^xdx =  e^x+C



#### Question

1. Find the following integrals:

&nbsp;a. ∫9e^xdx

&nbsp;b. ∫15e^tdt

&nbsp;c. ∫(x - ex )dx

&nbsp;d. ∫(-3)e^xdx

&nbsp;e. ∫(e^x)/2 dx

&nbsp;f. ∫(3e^x + 2/x  ) dx

&nbsp;g. ∫(3x^4 + 2e^x - 6)dx

&nbsp;h. ∫(e^x + 1)dx

&nbsp;i. ∫(7/x - 3e^x)dx

&nbsp;j. ∫(e^x + 1/x)dx

&nbsp;k. ∫(1 + 2x + 1/x + e^x)dx

&nbsp;l. ∫(2 - e^x )dx



### The indefinite integral of an exponential function of the form f(x) = e^(ax)

To integrate exponential functions of the form f(x) = e^(ax) we use the rule:∫e^(ax)dx =(e^(ax))/a + C 



Example:

&nbsp;Find ∫e^(2x)dx

&nbsp;∫e^(2x)dx = (e^(2x))/2 + C 



#### Questions

1. Find the following integrals:

&nbsp;a. ∫e^(3x)dx

&nbsp;b. ∫3e^(3x)dx

&nbsp;c. ∫4e^(4x)dx

&nbsp;d. ∫(1/2)e^(2x)dx

&nbsp;e. ∫(1/3)e^(5x)dx

&nbsp;f. ∫(-3e^(-3x))dx

&nbsp;g. ∫(1 +  e^−x )dx 

&nbsp;h. ∫(1 + x + e^2x)dx

&nbsp;i. ∫(e^x + 4e^4x + 1/x)dx

&nbsp;j. ∫(-e^-x)dx

&nbsp;k. ∫(100 - 3/x + 3e^3x)dx

&nbsp;l. ∫(1/2)x^3 + (3/2)e^(5x) - 1)dx 



### The indefinite integral of an exponential function of the form  f(x) =  *a*^x, *a* > 0

To integrate exponential functions of the form  f (x)  =  ax where a > 0  we use the rule:

&nbsp;∫a^x dx = (1/(lna))a^x + C



#### Questions

1. Find the following integrals:

&nbsp;a. ∫5^x dx

&nbsp;b. ∫6^x dx

&nbsp;c. ∫4^x dx

&nbsp;d. ∫9^x dx

&nbsp;e. ∫2^x dx

&nbsp;f. ∫10^x dx

&nbsp;g. ∫(7^x + e^(7x) + e^x) dx

&nbsp;h. ∫(8^x - 20) dx

&nbsp;i. ∫(2x + 2e^2x + 1) dx

&nbsp;j. ∫(a^x + 1/x) dx

&nbsp;k. ∫(e^x + (3/4)e^3x - 7a^x) dx

&nbsp;l. ∫(5^x + 5/x) dx



### The indefinite integral of an exponential function of the form f(x) = a^(nx)

To integrate a function of the form a^(nx) where a>0 we use the rule ∫a^(nx)dx = 1/(nlnx)(a^nx + C)



Examples:

Find ∫2^(3x) dx 



∫2^(3x) dx = (1/(3ln2))2^(3x) + C

&nbsp;          = (2^(3x))/(3ln2) + C



#### Questions

1. &nbsp;Find the following integrals:

&nbsp;a. ∫3^2x dx

&nbsp;b. ∫6^3x dx

&nbsp;c. ∫5^4x dx

&nbsp;d. ∫2^5x dx

&nbsp;e. ∫4^5x dx

&nbsp;f. ∫10^2x dx

&nbsp;g. ∫7^2x dx

&nbsp;h. ∫3^3x dx

&nbsp;i. ∫8^3x dx

&nbsp;j. ∫(ax + a^2x + 1/x)dx

&nbsp;k. ∫(1 + 3^2x) dx

&nbsp;l. ∫(e^x - 5a^(5x) - 6/x) dx

&nbsp;

### Revision

1. &nbsp;Find each integral.

&nbsp; a. ∫(1/2)x dx 

&nbsp; b. ∫(-2x + 3) dx

&nbsp; c. ∫(4x^2 + 3x - 1) dx

&nbsp; d. ∫(8x^7 + 3x) dx

&nbsp;

2\.  Evaluate each definite integral.

&nbsp;a. ∫~0~^1 (3x^2 + 7x + 1) dx

&nbsp;b. ∫~-1~^0(1 - x^2) dx

&nbsp;c. ∫~4~^5 (-7 + 6x + x^2) dx

&nbsp;d. ∫~-2~^3(x + 2)(x − 3) dx  



3\. Use integration to find the area of the shaded region.

&nbsp; a. Diagram: Graph of f(x) = x^2 - 6, Shaded range = -2<x<2

&nbsp; b. Diagram: Graph pf y = -3x^2 - 2x



4\. Graph each of the following functions. Then, find the area between the function and the 

x-axis for the given interval using integration.

&nbsp;a.  f(x) = -2x + 3  for  x = 1  to  x = 4

&nbsp;b.  f(x) = -x^2  for  x = 0  to  x = 5

&nbsp;c.  f(x) = 9 - 3x^2 for x = 0 to x = 3

&nbsp;d.  f(x) = x^3 + 4x for x = –2 to x = 2

&nbsp;e.  f(x) = -x^3 for x = -4 to x = 0





















