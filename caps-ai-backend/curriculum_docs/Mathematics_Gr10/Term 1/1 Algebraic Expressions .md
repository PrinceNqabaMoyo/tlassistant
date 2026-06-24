# Algebraic expressions



## Comments

* Due to the limitations of the text editor, fractions cannot be written as a number over another. The use of '/' is implemented.
* Fractions which could be easily misinterpreted have () around numerator or denominator
* Brackets around whole fractions/numerator/denominator are often necessitated by the limitations of the word editor. If the llm renders numerator directly above denominator, brackets may be unnecessary
* The llm should code for proper rendering of fractions vertically, and does not have to use () where clarity is not needed
* Also due to limitations of the word editor the dots or bar directly over the decimal digits to denote recurrence is not possible so dots and bars are misaligned.
* The llm should code for proper rendering of dots and bar over decimal digits to denote recurrence.
* For the decimal point I want the app to use '.' as standard.
* To give render demonstration of procedures; use of animated arrows is required.
* The use of '^' to denote powers is due to a limitation of note pad. Powers must be rendered as superscripts





## The real number system

DIAGRAM\[Concentric ellipses or ovals Withe the overall title, Real ℝ. Inside the largest outermost oval, There is a vertical line that divides the oval into 2 parts, one is the labelled , Rational ℚ, and the other Irrational ℚ'. The rational part has further concentric ovals, the next largest being labelled Integer ℤ. The next inner oval has the label Whole ℕ₀. The last inner oval is labelled Natural ℕ.]



We use the following definitions:

• ℕ: natural numbers are {1; 2; 3; . . .}

• ℕ₀: whole numbers are {0; 1; 2; 3; . . .}

• ℤ: integers are {. . . ; − 3; − 2; − 1; 0; 1; 2; 3; . . .}



### Working with Rational, irrational and decimal numbers

* A rational number (ℚ) is any number which can be written as: a/b, where a and b are integers and b≠0.
* The following numbers are all rational numbers: 10/1 ;21/7 ; -1/−3; 10/20; -3/6. We see that all numerators and all denominators are integers. This means that all integers are rational numbers, because they can be written with a denominator of 1.
* Irrational numbers (ℚ') are numbers that cannot be written as a fraction with the numerator and denominator as integers.
* Examples of irrational numbers: √2; √3; ∛4, π; (1+ √5)/2. These are not rational numbers, because either the numerator or the denominator is not an integer.
* You can write any rational number as a decimal number but not all decimal numbers are rational numbers. These types of decimal numbers are rational numbers:
1. Decimal numbers that end (or terminate). For example, the fraction 4/10 can be written as 0,4.
2. Decimal numbers that have a repeating single digit. For example, the fraction 1/3 can be written as 0,3˙ or as 0,¯3. The dot and bar notations are equivalent and both represent recurring 3’s, i.e. 0,3̇ = 0,3̄  = 0,333 \[Markdown doesnt allow to put a dot or bar above a number, llm should include code for rendering correct format]. . ..
3. Decimal numbers that have a recurring pattern of multiple digits. For example, the fraction 2/11 can also be written as 0,18 ̅. The bar represents a recurring pattern of 1 and 8’s i.e. 0,18 ̅ = 0,181818 . . .



Notation: You can use a dot or a bar over the repeated numbers to indicate that the decimal is a recurring decimal. If the bar covers more than one number, then all numbers beneath the bar are recurring.

If you are asked to identify whether a number is rational or irrational, first write the number in decimal form. If the number terminates then it is rational. If it goes on forever, then look for a repeated pattern of digits. If there is no repeated pattern, then the number is irrational.

When you write irrational numbers in decimal form, you may continue writing them for many, many decimal places. However, this is not convenient and it is often necessary to

round off.



* A decimal number has an integer part and a fractional part. For example, 10,589 has an integer part of 10 and a fractional part of 0,589 because 10 + 0,589 = 10,589. The fractional part can be written as a rational number, i.e. with a numerator and denominator that are integers.
* Each digit after the decimal point is a fraction with a denominator in increasing powers of 10. For example: 0,1 is 1/10; 0,01 is 1/100; 0,001 is 1/1 000
* This means that 10,589 = 10 + 5/10 + 8/100 + 9/1 000 = 10 000/1 000 + 500/1 000 + 80/1 000 + 9/1 000 = 10 589/1 000
* When the decimal is a recurring decimal, a bit more work is needed to write the fractional part of the decimal number as a fraction.
* In general, to convert decimals to fractions, if you have one digit recurring, then multiply by 10. If you have two digits recurring, then multiply by 100. If you have three digits recurring, then multiply by 1 000 and so on.
* Not all decimal numbers can be written as rational numbers. Why? Irrational decimal numbers like √2 = 1,4142135 . . . cannot be written with an integer numerator and denominator, because they do not have a pattern of recurring digits and they do not terminate. However, when possible, you should try to use rational numbers or fractions instead of decimals.





### Examples

#### 1\.

Which of the following are not rational numbers?

##### a.

π = 3,141 592 653 589 793 238 462 643 383 279 502 884 197 169 399 375 10 . . .



###### Answer

Irrational, decimal does not terminate and has no repeated pattern.



##### b.

1,4



###### Answer

&#x20;Rational, decimal terminates.



##### c.

1,618033989 . . .



###### Answer

&#x20;Irrational, decimal does not terminate and has no repeated pattern.



##### d.

100



###### Answer

Rational, all integers are rational.



##### e.

1,7373737373 . . .



Answer

Rational, decimal has repeated pattern.



##### f.

0,02 \[bar over the 2 decimal places]



###### Answer

Rational, decimal has repeated pattern.

#### 

#### 2\.

Problem: Write 0,3˙\[dot over 3] in the form a/b (where a and b are integers).



##### SOLUTION

###### Step 1 : Define an equation

Let x = 0,33333 . . .



###### Step 2 : Multiply by 10 on both sides

10x = 3,33333 . . .     (1 recurring digit, so multiply by 10)



###### Step 3 : Subtract the first equation from the second equation

9x = 3



###### Step 4 : Simplify

x = 3/9 = 1/3





#### 3\.

Problem: Write 5,4˙3˙2˙ as a rational fraction \[dot over each of 4, 3 and 2]



##### SOLUTION

###### Step 1 : Define an equation

x = 5,432432432 . . .



###### Step 2 : Multiply by 1000 on both sides

1 000x = 5 432,432432432 . . . (3 recurring digits, so we multiply by 1000)



###### Step 3 : Subtract the first equation from the second equation

999x = 5 427



###### Step 4 : Simplify

x = 5 427/999 = 201/37 = 5 16/37





### Questions 1

#### 1\.

State whether the following numbers are rational or irrational. If the number is rational, state whether it is a natural number, whole number or an integer:

(a) −1/3

(b) 0,651268962154862 . . .

(c)√9 /3

(d) π^2



#### 2\.

If a is an integer, b is an integer and c is irrational, which of the following are rational numbers?

(a) 5/6

(b) a/3

(c) −2/b

(d) 1/c



#### 3\.

For which of the following values of a is a

14 rational or irrational?

(a) 1

(b) -10

(c) √2

(d) 2,1



#### 4\.

Write the following as fractions:

(a) 0,1

(b) 0,12

(c) 0,58

(d) 0,2589



#### 5\.

Write the following using the recurring decimal notation:

(a) 0,11111111 . . .

(b) 0,1212121212 . . .

(c) 0,123123123123 . . .

(d) 0,11414541454145 . . .



#### 6\.

Write the following in decimal form, using the recurring decimal notation:

(a) 2/3

(b) 1 3/11

(c) 4 5/6

(d) 2 1/9



#### 7\.

Write the following decimals in fractional form:

(a) 0,5˙

(b) 0,63˙

(c) 5,31  ̅  \[bar over 31]



### Questions 2

#### 1

* DIAGRAM\[Concentric ellipses or ovals Withe the overall title, Real ℝ. Inside the largest outermost oval, There is a vertical line that divides the oval into 2 parts, one is the labelled , Rational ℚ, and the other Irrational ℚ'. The rational part has further concentric ovals, the next largest being labelled Interger ℤ. The next inner oval has the label Whole ℕ₀. The last inner oval is labelled Natural ℕ.]



The figure here shows the Venn diagram for the special sets ℕ, ℕ₀ and ℤ.



##### a)

Where does the number -12/3 belong in the diagram?



##### b)

&#x20;In the following list, there are two false statements and one true statement. Which of the statements is true?

###### i.

Every integer is a natural number.



###### ii.

Every natural number is a whole number.



###### iii.

There are no decimals in the whole numbers.





#### 2

* DIAGRAM\[Concentric ellipses or ovals Withe the overall title, Real ℝ. Inside the largest outermost oval, There is a vertical line that divides the oval into 2 parts, one is the labelled , Rational ℚ, and the other Irrational ℚ'. The rational part has further concentric ovals, the next largest being labelled Interger ℤ. The next inner oval has the label Whole ℕ₀. The last inner oval is labelled Natural ℕ.]



The figure here shows the Venn diagram for the special sets  ℕ, ℕ₀ and ℤ.



##### a)

Where does the number -1/2 belong in the diagram?



##### b)

In the following list, there are two false statements and one true statement. Which of the statements is true?

###### i.

Every integer is a natural number.



###### ii.

Every whole number is an integer.



###### iii.

There are no decimals in the whole numbers.





#### 3\.

State whether the following numbers are real, non-real or undefined.



##### a)

\-√3



##### b)

0/√2



##### c)

√-9



##### d)

\-√7/0



##### e)

\-√-16



##### f)

√2



#### 4\.

State whether the following numbers are rational or irrational. If the number is rational, state whether it is a natural number, whole number or an integer.



##### a)

\-1/3



##### b)

0,651268962154862...



##### c)

(√9)/3



##### d)

Π^2



##### e)

Π^4



##### f)

∛19



##### g)

(∛1)^7



##### h)

Π + 3



##### i)

Π + 0,858408346



#### 5\.

If a is an integer, b is an integer and c is irrational,which of the following are rational numbers?

##### a)

5/6



##### b)

a/3



##### c)

(-2)/b



##### d)

1/c



#### 6\.

##### a)

1



##### b)

\-10



##### c)

√2



##### d)

2.1





#### 7\.

Consider the following list of numbers:

\-3; 0; √-1; -8 4/5; -√8; 22/7; 14/0; 7; 1.34 (bar over 34); 3,3231089...; 3 + √2; 9 7/10; Π; 11



Which of the numbers are:

##### a)

natural numbers



##### b)

irrational numbers



##### c)

non-real numbers

&#x20;

##### d)

rational numbers



##### e)

integers



##### f)

undefined



#### 8\.

For each of the following numbers:

* write the next three digits and
* state whether the number is rational or irrational.

##### a)

1,15˙



##### b)

2,121314...



##### c)

1,242244246...



##### d)

3,324354...



##### e)

3,32435˙4˙



#### 9\.

Write the following as fractions:

##### a)

0,1



##### b)

0,12



##### c)

0,58



##### d)

0,2589



#### 10\.

Write the following using the recurring decimal notation:

##### a)

0,1111111...



##### b)

0,1212121212...



##### c)

0,123123123123...



##### d)

0,11414541454145...



#### 11\.

Write the following in decimal form, using the recurring decimal notation:

##### a)

25/45



##### b)

10/18



##### c)

7/33



##### d)

2/3



##### e)

1 3/11



##### f)

4 5/6



##### g)

2 1/9



#### 12\.

Write the following decimals in fractional form:

##### a)

0,5˙

&#x20;

##### b)

0,63˙

&#x20;

##### c)

0,4˙

&#x20;

##### d)

5,31 (bar over '31')



##### e)

4,93 (bar over '93')



##### f)

3,93 (bar over '93')





## Rounding off

Rounding off a decimal number to a given number of decimal places is the quickest way to approximate a number. For example, if you wanted to round off 2,6525272 to three decimal places, you would:

* count three places after the decimal and place a | between the third and fourth numbers
* round up the third digit if the fourth digit is greater than or equal to 5
* leave the third digit unchanged if the fourth digit is less than 5
* if the third digit is 9 and needs to be round up, then the 9 becomes a 0 and the second digit rounded up
* So, since the first digit after the | is a 5, we must round up the digit in the third decimal place to a 3 and the final answer of 2,6525272 rounded to three decimal places is 2,653.



### Example

#### 1

Problem: Round off the following numbers to the indicated number of decimal places:

##### a.

120/99 = 1,1˙2˙ \[dots over the 1 and 2 after decimal point] to 3 decimal places.



##### b.

π = 3,141592653 . . . to 4 decimal places.



##### c.

√3 = 1,7320508 . . . to 4 decimal places.



##### d.

2,78974526 to 3 decimal places.





#### SOLUTION

##### Step 1 : Mark off the required number of decimal places

a. 120/99 = 1,212|121212 . . .

b. π = 3,1415|92653 . . .

c. √3 = 1,7320|508 . . .

d. 2,789|74526



##### Step 2 : Check the next digit to see if you must round up or round down

a. The last digit of 120/99 = 1,212|1212121˙2˙ must be rounded

down.

b. The last digit of π = 3,1415|92653 . . . must be rounded up.

c. The last digit of √3 = 1,7320|508 . . . must be rounded up.

d. The last digit of 2,789|74526 must be rounded up.

Since this is a 9, we replace it with a 0 and round up

the second last digit.



##### Step 3 : Write the final answer

###### a.

120/99 = 1,212 rounded to 3 decimal places.



###### b.

π = 3,1416 rounded to 4 decimal places.



###### c.

√3 = 1,7321 rounded to 4 decimal places.



###### d.

2,790





### Questions

#### 1\.

Round off the following to 3 decimal places:

##### a.

12,56637061 . . .



##### b.

3,31662479 . . .



##### c.

0,26666666 . . .



##### d.

1,912931183 . . .



##### e.

6,32455532 . . .



##### f.

0,05555555 . . .



#### 2\.

Round off each of the following to the indicated number of decimal places:

##### a)

345,04399906 to 4 decimal places.



##### b)

1361,72980445 to 2 decimal places.



##### c)

728,00905239 to 6 decimal places.



##### d)

1/27 to 4 decimal places.



##### e)

45/99 to 5 decimal places



##### f)

1/12 to 2 decimal places.





#### 3\.

DIAGRAM\[Quadrilateral ABDE attached to triangle BDC. AB, AE and DC are all labelled π. ]



##### Comment for the llm agent:

By sight, the diagram looks like a square and a right-angled triangle, but the data given cannot conclusively assure us that



##### a)

Calculate the area of ABDE to 2 decimal places.



##### b)

Calculate the area of BCD to 2 decimal places.



##### c)

Using you answers in (a) and (b) calculate the area of ABCDE



##### d)

Without rounding off, what is the area of ABCDE?





#### 4\.

Given I = r/600; r = 7.4; n = 96; P = 200 000.



a)

Calculate correct to 2 decimal places.



b)

Using you answer from (a), calculate A in A = P(1+i)^n.



c)

Calculate without rounding off your answer in (a), compare this answer with your answer in (b).



#### 5\.

If it takes 1 person to carry 3 boxes, how many people are needed to carry 31 boxes?



#### 6\.

If 7 tickets cost R 35,20, how much does one ticket cost?



## Estimating surds

* If the nth root of a number cannot be simplified to a rational number, we call it a surd.
* For example, √2 and ∛6 are surds, but √4 is not a surd because it can be simplified to the rational number 2.
* In this section we will look at surds of the form {n}√\[a] where a is any positive number, for example, √7 or ∛5. It is very common for n to be 2, so we usually do not write {2}√\[a]. Instead we write the surd as just √a.
* It is sometimes useful to know the approximate value of a surd without having to use a calculator. For example, we want to be able to estimate where a surd like √3 is on the number line. From a calculator we know that √3 is equal to 1,73205 . . .. It is easy to see that √3 is above 1 and below 2. But to see this for other surds like √18 without using a calculator, you must first understand the following: If a and b are positive whole numbers, and a < b, then {n}√\[a] < {n}√\[b].
* A perfect square is the number obtained when an integer is squared. For example, 9 is a perfect square since 3^2 = 9.
* Similarly, a perfect cube is a number which is the cube of an integer. For example, 27 is a perfect cube, because 3^3 = 27.
* The value of a surd lies between the consecutive roots of perfect exponents
* Consider the surd ∛52. It lies somewhere between 3 and 4, because ∛27 = 3 and ∛64 = 4 and 52 is between 27 and 64.





### Examples

#### 1\.

Problem: Find the two consecutive integers such that √26 lies between them. (Remember that consecutive integers are two integers that follow one another on the number line, for example, 5 and 6 or 8 and 9).



##### SOLUTION

###### Step 1 : Use perfect squares to estimate the lower integer

52 = 25. Therefore 5 < √26.



###### Step 2 : Use perfect squares to estimate the upper integer

62 = 36. Therefore √26 < 6.



###### Step 3 : Write the final answer

5 < √26 < 6.







#### 2\.

Problem: Find the two consecutive integers such that √3 49 lies between them.



##### SOLUTION

###### Step 1 : Use perfect cubes to estimate the lower integer

3^3 = 27, therefore 3 < ∛49.



###### Step 2 : Use perfect cubes to estimate the upper integer

4^3 = 64, therefore ∛49 < 4.



###### Step 3 : Write the answer

3 < ∛49 < 4



###### Step 4 : Check the answer by cubing all terms in the inequality and then simplify

27 < 49 < 64. This is true, so ∛49 lies between 3 and 4.





### Questions

#### 1\.

Determine between which two consecutive integers the following numbers lie, without using a calculator:

##### a)

√18



##### b)

√29



##### c)

∛5



##### d)

∛79



##### e)

√155



##### f)

√57



##### g)

√71



##### h)

∛123



##### i)

∛90



##### j)

∛81



#### 2\.

Estimate the following surds to the nearest 1 decimal place, without using a calculator.

##### a)

√10



##### b)

√82



##### c)

√15



##### d)

√90





#### 3\.

Consider the following list of numbers:

27/7 ; √19 ; 2π ; 0.45 (bar over '45' denoting recurrence) ; -√(9/4) ; 6; -√8 ; √51

Without using a calculator, rank all the numbers in ascending order.



## Products (monomial.binomial, binomial.binomial, binomial.trinomial multiplication)

Mathematical expressions are just like sentences and their parts have special names. You should be familiar with the following words used to describe the parts of mathematical expressions.

Consider : 3x^2 + 7xy − 5^3 = 0,



term: 3x^2; 7xy; − 5^3 are each terms

expression: 3x^2 + 7xy − 5^3

coefficient: 3; 7

exponent: 2; 1; 3

base: x; y; 5

constant: 3; 7; 5

variable: x; y

equation: 3x^2 + 7xy − 5^3 = 0



* A monomial is an expression with one term, for example, 3x or y^2. A binomial is an expression with two terms, for example, ax + b or cx + d. A trinomial is an expression with three terms, for example, ax^2 + bx + c.
* When multiplying these kinds of expressions we expand brackets, by multiplying into them , and opening them.
* To multiply a monomial and binomial, simply multiply each of the terms in the binomial by the term of the monomial.\[Visual aid required]
* When multiplying 2 binomials. Take the 1st term of one binomial and multiply each of the terms of the second binomial in turn. Then take the second term of the first binomial and multiply each of the terms of the second binomial in turn. Add or subtract like terms.\[Visual aid required]. The product of two identical binomials is known as the square of the binomial and is written as: (ax + b)^2 = a^2x^2 + 2abx + b^2. If the two terms are of the form ax + b, and ax − b then their product is: (ax + b)(ax − b) = a^2x^2 − b^2. This product yields the difference of two squares.
* When multiplying a binomial and trinomial take the 1st term of the binomial and multiply each of the terms of the trinomial. Take the second term of the binomial and multiply each of the terms of the trinomial, combine like terms.\[VISUAL AID REQUIRED]



### Examples

#### 1

Problem: Simplify: 2a(a − 1) − 3(a^2 − 1).



##### SOLUTION

2a(a − 1) − 3(a^2 − 1) = 2a(a) + 2a(−1) + (−3)(a^2) + (−3)(−1)

= 2a^2 − 2a − 3a^2 + 3

= −a^2 − 2a + 3





#### 2

Problem: Find the product: (3x − 2)(5x + 8).



##### SOLUTION

(3x − 2)(5x + 8) = (3x)(5x) + (3x)(8) + (−2)(5x) + (−2)(8)

= 15x^2 + 24x − 10x − 16

= 15x^2 + 14x − 16





#### 3

Problem: Find the product: (x − 1)(x^2 − 2x + 1).



##### SOLUTION

###### Step 1 : Expand the bracket

(x − 1)(x^2 − 2x + 1) = x(x^2 − 2x + 1) − 1(x^2 − 2x + 1)

= x^3 − 2x^2 + x − x^2 + 2x − 1



###### Step 2 : Simplify

= x^3 − 3x^2 + 3x − 1





### Questions

1. #### Expand the following products:

##### a.

2y(y + 4)



##### b.

(y + 5)(y + 2)



##### c.

(2 − t)(1 − 2t)



##### d.

(x − 4)(x + 4)



##### e.

(2p + 9)(3p + 1)



##### f.

(3k − 2)(k + 6)



##### g.

(s + 6)^2



##### h.

−(7 − x)(7 + x)



##### i.

(3x − 1)(3x + 1)



##### j.

(7k + 2)(3 − 2k)



##### k.

(1 − 4x)^2



##### l.

(−3 − y)(5 − y)



##### m.

(8 − x)(8 + x)



##### n.

(9 + x)^2



##### o.

(−2y^2 − 4y + 11)(5y − 12)



##### p.

(7y^2 − 6y − 8)(−2y + 2)



##### q.

(10y + 3)(−2y^2 − 11y + 2)



##### r.

(−12y − 3)(12y^2 − 11y + 3)



##### s.

(−10)(2y^2 + 8y + 3)



##### t.

(2y^6 + 3y^5)(−5y − 12)



##### u.

(−7y + 11)(−12y + 3)



##### v.

(7y + 3)(7y2 + 3y + 10)



##### w.

9(8y^2 − 2y + 3)



##### x.

(−6y^4 + 11y^2 + 3y)(y + 4)(y − 4)



##### y.

\- (a + b)(b - a )



##### z.

(g - 5)^2



##### aa.

(d + 9)^2



##### ab.

(6d + 7)(6d - 7)



##### ac.

(5z + 1)(5z - 1)



##### ad.

(1 - 3h)(1 + 3h)



##### af.

(2p + 3)(2p + 2)



##### ag.

(8a + 4)(a + 7)



##### ah.

(5r + 4)(2r + 4)



##### ai.

(w + 1)(w - 1)



#### 2\.  Expand the following products:



##### a.

(g + 11)(g - 11)



##### b.

(4b - 2)(2b - 4)



##### c.

(4b - 3)(2b - 1)



##### d.

(6x - 4)(3x + 6)



##### e.

(3w - 2)(2w + 7)



##### f.

(2t - 3)^2



##### g.

(5p - 8)^2



##### h.

(4y + 5)^2



##### i.

(2y^6 + 3y^5)(-5y - 12)



##### j.

9(8y^2 - 2y + 3)



##### k.

(-2y^2 - 4y + 11)(5y - 12)



##### l.

(7y^2 - 6y - 8)(-2y + 2)



##### m.

(10y + 3)(-2y^2 - 11y + 2)



##### n.

(-12y - 3)(2y^2 - 11y + 3)



##### o.

(-10)(2y^2 + 8y + 3)



##### p.

(7y + 3)(7y^2 + 3y + 10)



##### q.

(a + 2b)(a^2 + b^2 + 2ab)



##### r.

(x + y)(x^2 - xy + y^2)



##### s.

3m(9m^2 + 2) + 5m^2(5m + 6)



##### t.

4x^2(10x^3 + 4) + 4x^3(2x^2 + 6)



##### u.

3k^3(k^2 + 3) + 2k^2(6k^3 + 7)



##### v.

(3x + 2)(3x - 2)(9x^2 - 4)



##### w.

(-6y^4 + 11y^2 + 3y)(y + 4)(y - 4)



##### x.

(x + 2)(x - 3)(x^2 + 2x - 3)



##### y.

(a + 2)^2 - (2a - 4)^2





#### 3\. Expand the following products:

##### a.

(2x + 3)^2 - (x - 2)^2



##### b.

(2a^2 - a - 1)(a^2 + 3a + 2)



##### c.

(y^2 + 4y - 1)(1 - 4y - y^2)



##### d.

2(x - 2y)(x^2 + xy + y^2)



##### e.

3(a - 3b)(a^2 + 3ab - b^2)



##### f.

(2a - b)(2a + b)(2a^2 - 3ab + b^2)



##### g.

2(3x + y)(3x - y) - (3x - y)^2



##### h.

(x + y)(x - 3y) + (2x - y)^2



##### i.

(x/3 - 3/x)(x/4 + 4/x)



##### j.

(x - 2/x)(x/3 + 4/x)



##### k.

1/2(10x - 12y) + 1/3(15x - 18y)



##### l.

1/2 a(4a + 6b) + 1/4 (8a + 12b)



#### 4\.

What is the value of b, in (x + b)(x - 1) = x^2 + 3x - 4



#### 5\.

What is the value of g, in (x - 2)(x + g) = x^2 - 6x + 8



#### 6\.

In (x - 4)(x + k) = x^2 + bx + c:



##### a)

For which of these values of k will b be positive?

3; 1;0;3;5



##### b)

For which of these values of k will c be positive?

3; 1;0;3;5



##### c)

For what real values of k  will c be positive?



##### d)

For what real values of k  will b be positive?





#### 7\.

Answer the following:



##### a)

Expand (x + 4/x)^2



##### b)

Given that (x + 4/x)^2 = 14, determine the value of x^2 + 16/(x^2) without solving for x.



#### 8\.

Answer the following:

##### a)

Expand: (a + 1/a)^2



##### b)

Given that (a + 1/a) = 3, determine the value of (a + 1/a)^2 without solving for a.



##### c)

Given that (a - 1/a) = 3, determine the value of (a + 1/a)^2 without solving for a.



#### 9

##### a)

Expand (3y + 1/2y)^2



##### b)

Given that 3y + 1/2y = 4, determine the value of (3y + 1/2y)^2 without solving for y.



#### 10

##### a)

Expand (a + 1/3a)^2



##### b)

Expand (a + 1/3a)(a^2 - 1/3 + 1/(9a^2))



##### c)

Given that a + 1/3a = 2, determine the value of a^3 + 1/27a^3 without solving for a.



## Factorisation using common factors and recognising a difference of 2 squares

* Factorisation is the opposite process of expanding brackets. For example, expanding brackets would require 2(x + 1) to be written as 2x + 2. Factorisation would be to start with 2x + 2 and to end up with 2(x + 1).
* The two expressions 2(x + 1) and 2x + 2 are equivalent; they have the same value for all values of x. In previous grades, we factorised by taking out a common factor and using difference of squares.
* Factorising based on common factors relies on there being factors common to all the terms. For example, 2x − 6x2 can be factorised as follows: 2x − 6x^2 = 2x(1 − 3x)
* We have seen that (ax + b)(ax − b) can be expanded to a^2x^2 − b^2, Therefore, a2^x^2 − b^2 can be factorised as (ax + b)(ax − b). x^2 − 16 can be written as x^2 − 4^2 which is a difference of two squares. Therefore, the factors of x2 − 16 are (x − 4) and (x + 4).
* To spot a difference of two squares, look for expressions:
1.  consisting of two terms;
2. with terms that have different signs (one positive, one negative); with each term a perfect square.
3. For example: a^2 − 1; 4x^2 − y^2; −49 + p^4.





### Examples

#### 1

Problem: Factorise: 5(a − 2) − b(2 − a).



##### SOLUTION

Use a “switch around” strategy to find the common factor.

Notice that 2 − a = −(a − 2)

5(a − 2) − b(2 − a) = 5(a − 2) − \[−b(a − 2)]

= 5(a − 2) + b(a − 2)

= (a − 2)(5 + b)





#### 2

Problem: Factorise: 3a(a^2 − 4) − 7(a^2 − 4).



##### SOLUTION

###### Step 1 : Take out the common factor (a^2 − 4)

3a(a^2 − 4) − 7(a^2 − 4) = (a^2 − 4)(3a − 7)



###### Step 2 : Factorise the difference of two squares (a^2 − 4)

(a^2 − 4)(3a − 7) = (a − 2)(a + 2)(3a − 7)





### Questions



#### Factorise:

##### 1\.

2l + 2w



##### 2\.

12x + 32y



##### 3\.

6x^2 + 2x + 10x^3



##### 4\.

2xy^2 + xy^2z + 3xy



##### 5\.

−2ab^2 − 4a^2b



##### 6\.

7a + 4



##### 7\.

20a − 10



##### 8\.

18ab − 3bc



##### 9\.

12kj + 18kq



##### 10\.

16k^2 − 4



##### 11\.

3a^2 + 6a − 18



##### 12\.

−12a + 24a^3



##### 13\.

−2ab − 8a



##### 14\.

24kj − 16k^2j



##### 15\.

−a^2b − b^2a



##### 16\.

12k^2j + 24k^2j^2



##### 17\.

72b^2q − 18b^3q^2



##### 18\.

4(y − 3) + k(3 − y)



##### 19\.

a^2(a − 1) − 25(a − 1)



##### 20\.

bm(b + 4) − 6m(b + 4)



##### 21\.

a^2(a + 7) + 9(a + 7)



##### 22\.

3b(b − 4) − 7(4 − b)



##### 23\.

a^2b^2c^2 − 1



##### 24\.

125x^6 - 5y^2



##### 25\.

3g(z + 6) + 2(6 + z)



##### 26\.

4b(y + 2) + 5(2 + y)



##### 27\.

3d(r + 5) + 14(5 + r)



##### 28\.

(6x + y)^2 - 9



##### 29\.

4x^2 - (4x - 3y)^2



##### 30\.

16a^2 - (3b + 4c)^2



##### 31\.

(b - 4)^2 - 9(b - 5)^2



##### 32\.

4(a - 3)^2 - 49(4a - 5)



##### 33\.

a^2b^2 - 1



##### 34\.

(1/9)a^2 - 4b^2



##### 35\.

(1/2)x^2 - 2



##### 36\.

y^2 - 8



##### 37\.

y^2 - 13



##### 38\.

a^2(a - 2ab - 15b^2) - 9b^2(a^2 - 2ab - 15b^2)







## Factorising by grouping in pairs

* The taking out of common factors is the starting point in all factorisation problems. We know that the factors of 3x + 3 are 3 and (x + 1). Similarly, the factors of 2x^2 + 2x are 2x and (x + 1). Therefore, if we have an expression 2x^2 + 2x + 3x + 3 there is no common factor to all four terms, but we can factorise as follows: (2x^2 + 2x) + (3x + 3) = 2x(x + 1) + 3(x + 1)
* We can see that there is another common factor (x + 1). Therefore, we can now write: (x + 1)(2x + 3)
* We get this by taking out the (x + 1) and seeing what is left over. We have 2x from the first group and +3 from the second group. This is called factorising by grouping.



### Example

#### 1

Problem: Find the factors of 7x + 14y + bx + 2b



##### SOLUTION

###### Step 1 : There are no factors common to all terms



###### Step 2 : Group terms with common factors together

7 is a common factor of the first two terms and b is a common factor of the second two terms.

We see that the ratio of the coefficients 7 : 14 is the same as b : 2b.



7x + 14y + bx + 2by = (7x + 14y) + (bx + 2by)

= 7(x + 2y) + b(x + 2y)



Step 3 : Take out the common factor (x + 2y)

7(x + 2y) + b(x + 2y) = (x + 2y)(7 + b)



###### OR



###### Step 1 : Group terms with common factors together

x is a common factor of the first and third terms and 2y is a

common factor of the second and fourth terms (7 : b = 14 : 2b).



###### Step 2 : Rearrange the equation with grouped terms together

7x + 14y + bx + 2by = (7x + bx) + (14y + 2by)

= x(7 + b) + 2y(7 + b)



###### Step 3 : Take out the common factor (7 + b)

x(7 + b) + 2y(7 + b) = (7 + b)(x + 2y)



###### Step 4 : Write the final answer

The factors of 7x + 14y + bx + 2by are (7 + b) and (x + 2y).





### Questions

#### Factorise the following:

##### 1\.

6x + a + 2ax + 3



##### 2\.

x^2 − 6x + 5x − 30



##### 3\.

5x + 10y − ax − 2ay



##### 4\.

6d - 9r + 2(t^5)d - 3(t^5)r



##### 5\.

9z - 18m + (b^3)z - 2(b^3)m



##### 6\.

35z - 10y + 7(c^5)z - 2(c^5)y



##### 7\.

a^2 - 2a - ax + 2x



##### 8\.

5xy - 3y + 10x - 6



##### 9\.

ab - a^2 - a + b



##### 10\.

14m - 4n + 7jm - 2jn



##### 11\.

28r - 20z + 7gr - 5gx



##### 12\.

25d - 15m + 5yd - 3ym



##### 13\.

45q - 18z + 5cq - 2cz



##### 14\.

6j - 15v + 2yj - 5yv



##### 15\.

16a - 40k + 2za - 5zk



##### 16\.

ax - bx + ay - by + 2a - 2b



##### 17\.

3ax + bx - 3ay - by - 9a - 3b





## Factorising a quadratic trinomial

* Factorising is the reverse of calculating the product of factors. In order to factorise a quadratic, we need to find the factors which, when multiplied together, equal the original quadratic.
* Consider a quadratic expression of the form ax^2 + bx. We see here that x is a common factor in both terms. Therefore, ax^2 + bx factorises as x(ax + b). For example, 8y^2 + 4y factorises as 4y(2y+1).
* Another type of quadratic is made up of the difference of squares. We know that: (a + b)(a − b) = a^2 − b^2. So a^2 − b^2 can be written in factorised form as (a + b)(a − b). This means that if we ever come across a quadratic that is made up of a difference of squares, we can immediately write down the factors.
* These types of quadratics are very simple to factorise. However, many quadratics do not fall into these categories and we need a more general method to factorise quadratics.
* We can learn about factorising quadratics by looking at the opposite process, where two binomials are multiplied to get a quadratic. For example, x + 2)(x + 3) = x^2 + 3x + 2x + 6 = x^2 + 5x + 6. We see that the x^2 term in the quadratic is the product of the x-terms in each bracket. Similarly, the 6 in the quadratic is the product of the 2 and 3 in the brackets. Finally, the middle term is the sum of two terms.
* Let us start with factorising x2+ 5x+ 6 and see if we can decide upon some general rules. Firstly, write down two brackets with an x in each bracket and space for the remaining terms.
1. (x )(x )
2. Next, decide upon the factors of 6. Since the 6 is positive, possible combinations are: 1 and 6; 2 and 3; -1 and -6; -2 and -3. We therefore have 4 possibilities: (x + 1)(x + 6); (x − 1)(x − 6); (x + 2)(x + 3) and (x − 2)(x − 3)
3. Next, we expand each set of brackets to see which option gives us the correct middle term. (x + 1)(x + 6) = x^2 + 7x + 6; (x − 1)(x − 6)= x^2 − 7x + 6; (x + 2)(x + 3) = x^2 + 5x + 6; (x − 2)(x − 3) = x^2 − 5x + 6
* We see that the 3rd option, (x + 2)(x + 3), is the correct solution.
* The process of factorising a quadratic is mostly trial and error but there are some strategies that can be used to ease the process.



### General procedure for factorising a trinomial:

1. Divide the entire equation by any common factor of the coefficients so as to obtain an equation of the form ax^2 +bx+c where a, b and c have no common factors and a is positive.
2. Write down two brackets with an x in each bracket and space for the remaining terms: (x )(x )
3.  Write down a set of factors for a and c.
4. Write down a set of options for the possible factors for the quadratic using the factors of a and c.
5. Expand all options to see which one gives you the correct middle term bx.



#### Note:

If c is positive, then the factors of c must be either both positive or both negative. If c is negative, it means only one of the factors of c is negative, the other one being positive. Once you get an answer, always multiply out your brackets again just to make sure it really works.



### Example

1. Problem: Factorise: 3x2 + 2x − 1.



#### SOLUTION

##### Step 1 :

Check that the quadratic is in required form ax^2 + bx + c



##### Step 2 :

Write down a set of factors for a and c

( x )( x )

The possible factors for a are: (1; 3).

The possible factors for c are: (−1; 1) or (1; − 1).

Write down a set of options for the possible factors of the quadratic

using the factors of a and c. Therefore, there are two possible options as shown in the table \[csv]:



Option 1, Option 2,

(x-1)(3x+1), (x+1)(3x-1),

3x^2 − 2x − 1, 3x^2 + 2x − 1



##### Step 3 :

Check that the solution is correct by multiplying the factors

(x + 1)(3x − 1) = 3x^2 − x + 3x − 1

= 3x^2 + 2x − 1



##### Step 4 :

Write the final answer

The factors of 3x^2 + 2x − 1 are (x + 1) and (3x − 1).





### Questions

#### 1\. Factorise the following:

(a)

x^2 + 8x + 15



(b)

x^2 + 10x + 24



(c)

x^2 + 9x + 8



(d)

x^2 + 9x + 14



(e)

x^2 + 15x + 36



(f)

x^2 + 12x + 36



(g)

2



#### 2\. Write the following expressions in factorised form:

(a) x^2 − 2x − 15

(b) x^2 + 2x − 3

(c) x^2 + 2x − 8

(d) x^2 + x − 20

(e) x^2 − x − 20

(f) 2x^2 + 22x + 20



#### 3\. Find the factors of the following trinomial expressions:

(a) 3x^2 + 19x + 6

(b) 6x^2 + 7x + 1

(c) 12x^2 + 8x + 1

(d) 8x^2 + 6x + 1



#### 4\. Factorise:

##### (a)

3x^2 + 17x − 6



##### (b)

7x^2 − 6x − 1



##### (c)

8x^2 − 6x + 1



##### (d)

6x^2 − 15x − 9



##### (e)

2h^2 + 5h -3



##### (f)

3x^2 + 4x + 1



##### (g)

3s^2 + s - 10



##### (h)

6v^2 - 27v + 27



##### (i)

6g^2 - 15g - 9



##### j)

a^2 - 7ab + 12b



##### k)

3a^2 + 5ab - 12b^2



##### l)

98x^4 + 14x^2 - 4



##### m)

(x - 2)^2 - 7(x - 2) + 12



##### n)

(a - 2)^2 - 4(a - 2) - 5



##### o)

(y + 3)^2 - 3(y + 3) - 18



##### p)

3(b^2 + 5b) + 12



##### q)

6(a^2 + 3a) - 168





## Sum and difference of two cubes

We now look at two special results obtained from multiplying a binomial and a trinomial:



### Sum of two cubes:

(x + y)(x^2 − xy + y^2) = x(x^2 − xy + y^2) + y(x^2 − xy + y^2)

= \[x(x^2) + x(−xy) + x(y^2)] + \[y(x2) + y(−xy) + y(y2)]

= x^3 − x^2y + xy^2 + x^2y − xy^2 + y^3

= x^3 + y^3



### Difference of two cubes:

(x − y)(x^2 + xy + y^2) = x(x^2 + xy + y^2) − y(x^2 + xy + y^2)

= \[x(x^2) + x(xy) + x(y^2)] − \[y(x^2) + y(xy) + y(y^2)]

= x^3 + x^2y + xy^2 − x^2y − xy^2 − y^3

= x^3 − y^3



### So we have seen that:

x^3 + y^3 = (x + y)(x^2 − xy + y^2)

x^3 − y^3 = (x − y)(x^2 + xy + y^2)



We use these two basic equations to factorise more complex examples.



### Examples

#### 1

Problem: Factorise: x^3 − 1.



##### SOLUTION

###### Step 1 : Take the cube root of terms that are perfect cubes

Notice that ∛x^3 = x and ∛1 = 1. These give the terms in the first

bracket.



###### Step 2 : Use inspection to find the three terms in the second bracket

(x^3 − 1) = (x − 1)(x^2 + x + 1)



###### Step 3 : Expand the brackets to check that the expression has been correctly factorised

(x − 1)(x^2 + x + 1) = x(x^2 + x + 1) − 1(x^2 + x + 1)

= x^3 + x^2 + x − x^2 − x − 1

= x^3 − 1





#### 2\.

Problem: Factorise: x^3 + 8.



##### SOLUTION

###### Step 1 : Take the cube root of terms that are perfect cubes

Notice that ∛x^3 = x and ∛8 = 2. These give the terms in the first

bracket.



###### Step 2 : Use inspection to find the three terms in the second bracket

(x^3 + 8) = (x + 2)(x^2 − 2x + 4)



###### Step 3 : Expand the brackets to check that the expression has been correctly factorised

(x + 2)(x^2 − 2x + 4) = x(x^2 − 2x + 4) + 2(x^2 − 2x + 4)

= x^3 − 2x^2 + 4x + 2x^2 − 4x + 8

= x^3 + 8



#### 3\.

Problem: Factorise: 16y^3 − 432.



##### SOLUTION

###### Step 1 : Take out the common factor 16

16y^3 − 432 = 16(y^3 − 27)



###### Step 2 : Take the cube root of terms that are perfect cubes

Notice that ∛y^3 = y and ∛27 = 3. These give the terms in the first

bracket.



###### Step 3 : Use inspection to find the three terms in the second bracket

16(y^3 − 27) = 16(y − 3)(y^2 + 3y + 9)



Step 4 : Expand the brackets to check that the expression has been correctly factorised

16(y − 3)(y^2 + 3y + 9) = 16\[(y(y^2 + 3y + 9) − 3(y^2 + 3y + 9)]

= 16\[y^3 + 3y^2 + 9y − 3y^2 − 9y − 27]

= 16y^3 − 432





#### 4\.

Problem: Factorise: 8t^3 + 125p^3.



##### SOLUTION

###### Step 1 : There is no common factor



###### Step 2 : Take the cube roots

Notice that ∛8t^3 = 2t and ∛(125p^3) = 5p. These give the terms in

the first bracket.



###### Step 3 : Use inspection to find the three terms in second bracket

(8t^3 + 125p^3) = (2t + 5p)\[(2t)^2 − (2t)(5p) + (5p)^2]

= (2t + 5p)(4t^2 − 10tp + 25p^2)



###### Step 4 : Expand the brackets to check that expression has been correctly factorised

(2t + 5p)(4t^2 − 10tp + 25p^2)

= 2t(4t^2 − 10tp + 25p^2) + 5p(4t^2 − 10tp + 25p^2)

= 8t^3 − 20pt^2 + 50p^2t + 20pt^2 − 50p^2t + 125p^3

= 8t^3 + 125p^3



### Questions

#### Factorise:

##### 1\.

x^3 + 8



##### 2\.

27 − m^3



##### 3\.

2x^3 − 2y^3



##### 4\.

3k^3 + 81q^3



##### 5\.

64t^3 − 1



##### 6\.

64x^2 − 1



##### 7\.

125x^3 + 1



##### 8\.

25x^2 + 1



##### 9\.

z − 125z^4



##### 10\.

8m^6 + n^9



##### 11\.

p^15 − 1/8 y^12



##### 12\.

1 − (x − y)^3



##### 13\.

216n^3 - k^3



##### 14\.

125s^3 + d^3



##### 15\.

8k^3 + r^3



##### 16\.

8j^3 k^3 t^3 - b^3



##### 17\.

27x^3 y^3 + w^3



##### 18\.

128m^3 + 2f^3



##### 19\.

27/t^3 - s^3



##### 20\.

1/(64q^3) - h^3



##### 21\.

72g^3 + (1/3)v^3



##### 22\.

1 - (x - y)^3



##### 23\.

h^4(8g^6 + h^3) - (8g^6 + h^3)



##### 24\.

x(125w^3 - h^3) + y(125w^3 - h^3)



##### 25\.

x^2(27p^3 + w^3) - 5x(27p^3 + w^3) - 6(27p^3 + w^3)



##### 26

w^3 - 8



##### 27\.

g^3 + 64



##### 28\.

h^3 + 1





## Simplification of fractions

We have studied procedures for working with fractions in earlier grades:

1\. a/b ×c/d = ac/bd  (b ≠ 0; d ≠ 0)

2\. a/b + c/b = (a + c)/b (b ≠ 0)

3\. a/b ÷ c/d = a/b × d/c = ad/bc (b ≠ 0; c ≠ 0; d ≠ 0)

Note: dividing by a fraction is the same as multiplying by the reciprocal of the fraction.



* In some cases of simplifying an algebraic expression, the expression will be a fraction. For example, (x^2 + 3x)/(x+3) has a quadratic binomial in the numerator and a linear binomial in the denominator. We have to apply the different factorisation methods in order to factorise the numerator and the denominator before we can simplify the expression.



(x^2 + 3x)/(x+3) = x(x + 3)/(x+3) = x    (x ≠ −3)



If x = −3 then the denominator, x + 3 = 0, and the fraction is undefined.





### Examples

#### 1

Problem: Simplify: (ax − b + x − ab)/(ax^2 − abx), (x ≠ 0; x ≠ b).



##### SOLUTION

###### Step 1 :

Use grouping to factorise the numerator and take out the common factor ax in the denominator

(ax − b + x − ab)/(ax^2 − abx) = \[a(x-b)+(x-b)]/ax(x-b)



###### Step 2 :

Take out common factor (x − b) in the numerator

= (x − b)(a + 1)/ax(x-b)



###### Step 3 :

Cancel the common factor in the numerator and the denominator to give the final answer

= (a+1)/ax





#### 2\.

Problem: Simplify: (x^2 − x − 2)/(x^2 − 4) ÷ (x^2+x)/x(x+2), (x ≠ 0; ≠ ±2).



##### SOLUTION

###### Step 1 : Factorise the numerator and denominator

= (x + 1)(x − 2)/(x + 2)(x − 2) ÷ x(x+1)/x(x+2)



###### Step 2 : Change the division sign and multiply by the reciprocal

= (x + 1)(x − 2)/(x + 2)(x − 2) × x(x+2)/x(x+1)

 

###### Step 3 : Write the final answer

= 1





### 3\.

Problem: Simplify:

(x−2)/(x^2−4) + x^2/(x-2) - (x^3+x-4)/(x^-4), (x ≠ ±2).



#### SOLUTION

###### Step 1 : Factorise the denominators

(x-2)/(x+2)(x-2) + x^2/(x-2) - (x^3+x-4)/(x+2)(x-2)



###### Step 2 : Make all denominators the same so that we can add or subtract the fractions

The lowest common denominator is (x − 2)(x + 2).



(x-2)/(x+2)(x-2) + (x^2)(x+2)/(x+2)(x-2) - (x^3+x-4)/(x+2)(x-2)





###### Step 3 : Write as one fraction

\[(x-2) + (x^2)(x+2)) - (x^3+x-4)]/(x+2)(x-2)



###### Step 4 : Simplify

\[x-2 + x^3 + 2x^2 - x^3 - x + 4]/(x+2)(x-2) = (2x^2 + 2)/(x+2)(x-2)



###### Step 5 : Take out the common factor and write the final answer

2(x^2 + 1)/(x + 2)(x − 2)





#### 4\.

Problem: Simplify:

2/(x^2-x) + (x^2+x+1)/(x^3-1)-x/(x^2-1), (x ≠ 0; x ≠ ±1).



##### SOLUTION

###### Step 1 : Factorise the numerator and denominator

2/x(x-1) + (x^2+x+1)/(x-1)(x^2 + x + 1) - x/(x-1)(x+1)



###### Step 2 : Simplify and find the common denominator

\[2(x + 1) + x(x + 1) − x^2]/x(x − 1)(x + 1)



###### Step 3 : Write the final answer

\[2x + 2 + x2 + x − x2]/x(x − 1)(x + 1) = (3x + 2)/x(x − 1)(x + 1)





### Questions

#### Simplify (assume all denominators are non-zero):

##### 1\.

3a/15



##### 2\.

(2a + 10)/4



##### 3\.

(5a + 20)/(a + 4)



##### 4\.

(a^2 - 4a)/(a-4)



##### 5\.

(3a^2 - 9a)/(2a - 6)



##### 6\.

(9a + 27)/(9a + 18)



##### 7\.

(6ab + 2a)/2b



##### 8\.

(16x^2y − 8xy)/(12x - 6)



##### 9\.

(4xyp − 8xp)/12xy



##### 10\.

(3a + 9)/14 ÷ (7a + 21)/(a + 3)



##### 11\.

(a^2 − 5a)/(2a +10) × 4a/(3a +15)



##### 12\.

(3xp + 4p)/8p ÷ 12p^2/(3x+4)



##### 13\.

(24a -8)/12 ÷ (9a -3)/6



##### 14\.

(a^2 + 2a)/5 ÷ (2a +4)/20



##### 15\.

(p^2 + pq)/7p × 21q/(8p + 8q)



##### 16\.

(5ab − 15b)/(4a-12) ÷ 6b^2/(a+b)



##### 17\.

(f^2 a- f a^2)/(f-a)



##### 18\.

2/xy + 4/xz + 3/yz



##### 19\.

5/t-2 - 1/t-3



##### 20\.

(k+2)/(k^2+2) - 1/(k+2)



##### 21\.

(t+2/3q) + (t+1)/2q



##### 22\.

3/(p^2 - 4) + 2/(p - 2)^2



##### 23\.

x/(x+y) + x^2/(y^2 - x^2)



##### 24\.

1/(m+n) + 3mn/(m^3 + n^3)



##### 25\.

h/(h^3 - f^3) - 1/(h^2 + hf + f^2)



##### 26\.

(x^2 -1)/3 × 1/(x-1) -1/2



##### 27\.

(x^2 − 2x + 1)/(x-1)^3 - (x^2 + x + 1)/(x^3 -1)



##### 28\.

1/(x-1)^2 - 2x/(x^3 - 1)



##### 29\.

(p^3 + q^3)/p^2 × (3p - 3q)/(p^2 - q^2)



##### 30\.

1/(a^2 - 4ab +4b^2) + (a^2 + 2ab + b^2)/(a^3 -8b^3) - 1/(a^2 - 4b^2)



##### 31\.

(9x^2 - 16)/(6x - 8)



##### 32\.

(b^2 - 81a^2)/(18a - 2b)



##### 33\.

(t^2 - s^2)/(s^2 - 2st + t^2)



##### 34\.

(x^2 - 2x - 15)/(5x - 25)



##### 35\.

(x^2 + 2x - 15)/(x^2 + 8x + 15)



##### 36\.

(x^2 - x - 6)/(x^3 - 27)



##### 37\.

(a^2 + 6a - 16)/(a^3 - 8)



##### 38\.

(a^2 - 4ab - 12b^2)/(a^2 - 4ab + 4b^2)



##### 39\.

(6a^2 - 7a -3)/(3ab + b)



##### 40\.

(2x^2 - x -1)/(x^3 - x)



##### 41\.

(qz + qr + 16z + 16r)/(z + r)



##### 42\.

(pz - pq + 5z - 5q)/(z - q)



##### 43\.

(hx - hg + 13x - 13g)/(x - g)



##### 44\.

(b^2 + 10b + 21)/\[3(b^2 - 9)] ÷ (2b^2 + 14b)/(30b^2 - 90b)



##### 45\.

(x^2 + 17x + 70)/5(x^2 - 100) ÷ (3x^2 + 21x)/(45x^2 - 450x)



##### 46\.

(z^2 + 17z + 66)/3(z^2 - 121) ÷ (2z^2 + 12z)/(24z^2 - 264z)



##### 47\.

(16 - x^2)/(x^2 - x - 12) × (x + 3)/(x + 4)



##### 48\.

(a^3 + b^3)/a^3 ×(5a + 5b)/(a^2 + 2ab + b^2)



##### 49\.

(a -4)/(a + 5a + 4) × (a^2 + 2a + 1)/(a^2 - 3a - 4)



##### 50\.

(3x + 2)/(x^2 - 6x + 8) × (x - 2)/(3x^2 + 8x + 4)



##### 51\.

(a^2 - 2a + 8)/(a^2 + 6a + 8) × (a^2 + a -12)/3 - 3/2



##### 52\.

(4x^2 - 1)/(3x^2 + 10x + 3) ÷ (6x^2 + 5x + 1)/(4x^2 + 7x - 3) × (9x^2 + 6x + 1)/(8x^2 - 6x + 1)



##### 53\.

(x + 4)/3 - (x - 2)/2



##### 54\.

(x - 3)/3 - (x + 5)/4



##### 55\.

(2x - 4)/9 - (x - 3)/4 + 1



##### 56\.

1 + (3x - 4)/4 - (x + 2)/3



##### 57\.

11/(a + 11) + 8/(a - 8)



##### 58\.

12/(x - 12) - 6/(x - 6)



##### 59\.

12/(r + 12) + 8/(r - 8)



##### 60\.

(t^2 + 2t - 8)/(t^2 + t - 6) + 1/(t^2 - 9) + (t + 1)/(t - 3)





#### 2

What are the restrictions in the following:

##### a)

1/(x - 2)



##### b)

(3x - 9)/(4x + 4)



##### c)

3/x - 1/(x^2 - 1)



## Revision

### 1

If a is an integer, b is an integer and c is irrational, which of the following are rational numbers?
(a) −b/a
(b) c ÷ c
(c) a/c
(d) 1/c



### 2\.

Write each decimal as a simple fraction.

(a) 0,12

(b) 0,006

(c) 1,59

(d) 12,277̇ \[dot over the last 7]



### 3\.

Show that the decimal 3,211˙8˙ \[dots over the 2nd 1 and 8] is a rational number.



### 4\.

Express 0,78˙\[dot over 8] as a fraction a/b where a,b ∈ ℤ (show all working).



### 5\.

Write the following rational numbers to 2 decimal places.

#### (a)

1/2



#### (b)

1



#### (c)

0,111111 ̅ \[bar over the last 1]



#### (d)

0,999991 ̅ \[bar over 1]



### 6\.

Round off the following irrational numbers to 3 decimal places.

#### (a)

3,141592654 . . .



#### (b)

1,618033989 . . .



#### (c)

1,41421356 . . .



#### (d)

2,71828182845904523536 . . .



### 7\.

Use your calculator and write the following irrational numbers to 3 decimal places.

#### (a)

√2



#### (b)

√3



#### (c)

√5



#### (d)

√6



### 8\.

Use your calculator (where necessary) and write the following numbers to 5 decimal places. State whether the numbers are irrational or rational.

#### (a)

√8



#### (b)

√768



#### (c)

√0,49



#### (d)

√0,0016



#### (e)

√0,25



#### (f)

√36



#### (g)

√1960



#### (h)

√0,0036



#### (i)

−8√0,04



#### (j)

5√80



### 9\.

Write the following irrational numbers to 3 decimal places and then write each one as a rational number to get an approximation to the irrational number.

#### (a)

3,141592654 . . .



#### (b)

1,618033989 . . .



#### (c)

1,41421356 . . .



#### (d)

2,71828182845904523536 . . .



### 10\.

Determine between which two consecutive integers the following irrational numbers lie, without using a calculator.

#### (a)

√5



#### (b)

√10



#### (c)

√20



#### (d)

√30



#### (e)

∛5



#### (f)

∛10



#### (g)

∛20



#### (h)

∛30



### 11\.

Find two consecutive integers such that √7 lies between them.



### 12\.

Find two consecutive integers such that √15 lies between them.



### 13\. Factorise:

#### (a)

a^2 − 9



#### (b)

m^2 − 36



#### (c)

9b^2 − 81



#### (d)

16b^6 − 25a^2



#### (e)

m^2 − 1/9



#### (f)

5 − 5(a^2)(b^6)



#### (g)

16ba^4 − 81b



#### (h)

a^2 − 10a + 25



#### (i)

16b^2 + 56b + 49



#### (j)

2a^2 − 12ab + 18b^2



#### (k)

−4b^2 − 144b^8 + 48b^5



#### (l)

(16 − x^4)



#### (m)

7x^2 − 14x + 7xy − 14y



#### (n)

y^2 − 7y − 30



#### (o)

1 − x − x^2 + x^3



#### (p)

&#x20;−3(1 − p^2) + p + 1



#### (q)

x − x^3 + y − y^3



#### (r)

x^2 − 2x + 1 − y^4



#### (s)

4b(x^3 − 1) + x(1 − x^3)



#### (t)

3p^3 − 1/9



#### (u)

8x^6 − 125y^9



#### (v)

(2 + p)^3 − 8(p + 1)^3





### 14\. Simplify the following:

#### (a)

(a − 2)^2 − a(a + 4)



#### (b)

(5a − 4b)(25a^2 + 20ab + 16b^2)



#### (c)

(2m − 3)(4m^2 + 9)(2m + 3)



#### (d)

(a + 2b − c)(a + 2b + c)



#### (e)

(p^2 − q^2)/p ÷ (p + q)/(p^2 − pq)



#### (f)

2/x + x/2 − 2x/3



#### (g)

1/(a + 7) − (a + 7)/(a^2 − 49)



#### (h)

(x + 2)/(2x^3) + 16



#### (i)

(1 − 2a)/(4a^2 − 1) - (a-1)/(2a^2 -3a +1) - 1/(1-a)



#### (j)

(x^2 + 2x)/(x^2 + x + 6) × (x^2 + 2x + 1)/(x^2 + 3x + 2)



### 15\.

Show that (2x − 1)^2 − (x − 3)^2 can be simplified to (x + 2)(3x − 4).



### 16\.

What must be added to x^2 − x + 4 to make it equal to (x + 2)^2

?



### 17\.

Evaluate (x^3 +1)/(x^2 - x + 1) if x = 7,85 without using a calculator. Show your work.



### 18\.

With what expression must (a − 2b) be multiplied to get a product of a^3 − 8b^3?



### 19\.

With what expression must 27x^3 + 1 be divided to get a quotient of 3x + 1?







# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

