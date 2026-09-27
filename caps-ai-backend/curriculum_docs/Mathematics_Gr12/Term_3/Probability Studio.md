# Counting and probability

## Revision

### Terminology

\-Outcome: a single observation of an uncertain or random process (called an experiment). For example, when you accidentally drop a book, it might fall on its cover, on its back or on its side. Each of these options is a possible outcome.



\-Sample space of an experiment: the set of all possible outcomes of the experiment. For example, the sample space when you roll a single 6-sided die is the set {1; 2; 3; 4; 5; 6}. For a given experiment, there is exactly one sample space. The sample space is denoted by the letter S.



\-Event: a set of outcomes of an experiment. For example, if you have a standard deck of 52 cards, an event may be picking a spade card or a king card.



\-Probability of an event: a real number between and inclusive of 0 and 1 that describes how likely it is that the event will occur. A probability of 0 means the outcome of the experiment will never be in the event set. A probability of 1 means the outcome of the experiment will always be in the event set. When all possible outcomesof an experiment have equal chance of occurring, the probability of an event is the number of outcomes in the event set as a fraction of the number of outcomes in the sample space. To calculate a probability, you divide the number of favourable outcomes by the total number of possible outcomes.



\-Relative frequency of an event: the number of times that the event  occurs during experimental trials, divided by the total number of trials conducted. For example, if we flip a coin 10 times and it landed on heads 3 times, then the relative frequency of the heads event is 3/10 = 0,3.



\-Union of events: these to fall out comes that occur in at least one of the events. For 2 events called A and B, we write the union as “A or B ”. Another way of writing the union is using set notation: A ∪ B. For example, if A is all the countries in Africa and B is all the countries in Europe, A or B is all the countries in Africa and Europe.



\-Intersection of events: the set of all outcomes that occur in all of the events. For 2 events called A and B, we write the intersection as “A and B”. Another way of writing the intersection is using set notation: A ∩ B. For example, if A is soccer players and B is cricket players, A and B refers to those who play both soccer and cricket.



\-Mutually exclusive events: events with no outcomes in common, that is (A and B) is an empty set. Mutually exclusive event scan never occur simultaneously. For example the event that a number is even and the event that the same number is odd are mutually exclusive, since a number can never be both even and odd.



\-Complementary events: two mutually exclusive events that together contain all the outcomes in the sample space. For an event called A, we write the complementas “notA”. Another way of writing the complement is as A.



\-Dependent and independent events: two events, A and B, are independent if the outcome of the first event does not influence the outcome of the second event. For example, if you flip a coin and it lands on tails and flip it again and it lands on heads, neither outcome influences the other. Two events, C and D, are dependent if the out come of one event influences the outcome of the other. For example, if your lunchbox contains 3 sandwiches and 2 apples, when you eat one of the items, this reduces the number of choices you have when deciding to eat a second item.



## Identities

\-The addition rule (also called the sum rule) for any 2 events, A and B is

* P(A or B) = P(A) + P(B) − P(A and B)



\-This rule relates the probabilities of 2 events with the probabilities of their union and intersection.

\-The addition rule for 2 mutually exclusive events is

* P(A or B) = P(A) + P(B)

\-This rule is a special case of the previous rule. Because the events are mutually exclusive, P(A and B) = 0.

\-The complementary rule is P(not A) = 1 − P(A)

\-This rule is a special case of the previous rule. Since A and (not A) are complementary,

* P(A or (not A)) = 1.

\-The product rule for independent events A and B is:

* P(A and B) =P(A)×P(B)

\-If two events A and B are dependent then:

* P(A and B) ≠ P(A)×P(B)



>WARNING!

\-Just because two events are mutually exclusive does not necessarily mean that they are independent. To test whether events are mutually exclusive, always check that P(A and B) =0. To test whether events are independent, always check that P(A and B) =

P(A) × P(B). See the exercises below for examples of events that are mutually exclusive and independent in different combinations.



### EXAMPLES

#### 1

Write down which of the following events are dependent and which are independent:



##### a. 

The student council chooses a head student and then a deputy head student.



##### b.

A bag contains blue marbles and red marbles. You take a red marble out of the bag and then throw it back in again before you take another marble out of the bag.



##### SOLUTION

###### Step 1: Ask the question: Did the available choices change for the second event because of the first event?



\####### a. 

Yes, because after selecting the head student there are fewer council members available to choose for the deputy headstudent position. Therefore the two events are dependent.



\####### b.

No, because when you throw the first marble back into the bag, there are the same number and colour composition of choices for the second marble.Therefore the two events are independent.





#### 2

A bag contains 3 yellow and 4 black beads. We remove a random bead from the bag, record its colour and put it back into the bag. We then remove another random bead from the bag and record its colour.



##### a.

What is the probability that the first bead is yellow?



##### b.

What is the probability that the second bead is black?



##### c.

What is the probability that the first bead is yellow and the second bead is black?



##### d. 

Are the first bead being yellow and the second bead being black independent events?



##### SOLUTION

###### Step 1: Probability of a yellow bead first

Since there is a total of 7 beads, of which 3 are yellow, the probability of getting a yellow bead is P(first bead yellow) = 3/7



###### Step 2: Probability of a black bead second

\-The problem states that the first be a displaced back into the bag before we take the second bead. This means that when we draw the second bead, there are again a total of 7 beads in the bag, of which 4 are black. Therefore the probability of drawing a black bead is P(second bead black) = 4/7



###### Step 3: Probability of yellow first and black second

\-When drawing two beads from the bag, there are 4 possibilities.We can get

* a yellow bead and then another yellow bead;
* a yellow bead and then a black bead;
* a black bead and then a yellow bead;
* a black bead and then another black bead.



\-We want to know the probability of the second outcome, where we have to get a yellow bead first. Since there are 3 yellow beads and 7 beads in total, there are 3/7 ways to get a yellow bead first. 

\-Now we put the first bead back, so there are again 3 yellow beads and 4 black beads in the bag. Therefore there are 4/7 ways to get a black bead second if the first bead was yellow. This means that there are 3/7 × 4/7 = 12/49



ways to get a yellow bead first and a black bead second. So, the probability of getting a yellow bead first and a black bead second is 12/49.



###### Step 4: Dependent or independent?

According to the definition, events are independent if and only if

P(A and B) = P(A) × P(B)



In this problem:

* P(first bead yellow) = 3/7
* P(second bead black) = 4/7
* P(first bead yellow and second bead black) = 12/49

Since 12/49 = 3/7 × 4/7, the events are independent.





#### 3

\-In the previous example, we picked a random bead and put it back into the bag before continuing. This is called sampling with replacement. In this worked example, we will follow the same process, except that we will not put the first bead back into the

bag. This is called sampling without replacement.

\-So, from a bag with 3 red and 5 green beads, were move a random bead and record its colour. Then, without putting back the first bead, we remove another random bead from the bag and record its colour.



##### a.

What is the probability that the first bead is red?



##### b.

What is the probability that the second bead is green?



##### c.

What is the probability that the first bead is red and the second bead is green?



##### d. 

Are the first bead being red and the second bead being green independent events?





##### SOLUTION

###### Step 1: Count the number of outcomes

\-We will examine the number ways in which we can get the different possible outcomes when removing 2 beads. The possible outcomes are

* a red bead and then another red bead (RR);
* a red bead and then a green bead (RG);
* a green bead and then  a red bead (GR);
* a green bead and then another green bead (GG).



\-For the first outcome, we have to get a red bead first. Since there are 3 red beads and 8 beads in total, there are 3/8 ways to get a red bead first. After we have taken out a red bead, there are now 2 red beads and 5 green beads left. 

\-Therefore there are 2/7 ways to get a red bead second if the first bead was also red. This means that there are 3/8 × 2/7 = 6/56 = 3/28 ways to get a red bead first and a red bead second. The probability of the first outcome is 3/28.



\-For the second outcome, we have to get a red bead first. As in the first outcome, there are 3/8 ways to get a red bead first; and there are now 2 red beads and 5 green beads left. 

\-Therefore there are 5/7 ways to get a green bead second if the first bead was red.

\-This means that there are 3/8 × 5/7 = 15/56 ways to get a red bead first and a green bead second. The probability of the second outcome is 15/56.

\-In the third out come, the first bead is green and the second bead is  red. There are 5/8 ways to get a green bead first; and there are now 4 green beads and 3 red beads left.

\-Therefore there are 3/7 ways to get a red bead second if the first bead was green. This means that there are 5/8 × 3/7 = 15/56 ways to get a red bead first and a green bead second. The probability of the third outcome is 15/56.

\-In the fourth outcome, the first and second beads are both green. Since there are 5 green beads and 8 beads in total, there are 5/8 ways to get a green bead first. After we have removed a green bead, 3 red beads and 4 green beads remain in the bag.

\-Therefore there are 4/7 ways to get a green bead second if the first bead was also green. This means that there are 5/8 × 4/7 = 20/56 =  5/14 ways to get a green bead first and a green bead second. 

\-Therefore the probability of the fourth outcome is 5/14.

\-To summarise, these are the possible out comes and their probabilities:

* first bead red and second bead red (RR): 3/28;
* first bead red and second bead green (RG): 15/56;
* first bead green and second bead red (GR): 15/56;
* first bead green and second bead green (GG): 5/14.



###### Step 2: Probability of a red bead first

\-To determine the probability of getting a red bead on the first draw, we look at all of the outcomes that contain a red bead first. These are:

* a red bead and then another red bead (RR);
* a red bead and then a green bead (RG).



\-The probability of the first outcome is 3/28 and the probability of the second outcome is 15/56. 

\-By adding these two probabilities, we see that the probability of getting a red bead first is

P(first bead red) = 3/28 + 15/56 = 6/56 + 15/56 = 21/56 = 3/8



\-This is the same as in the previous worked example, which should not be too surprising since the probability of the first bead being red is not affected by whether or not we put it back into the bag before drawing the second bead.



###### Step 3: Probability of a green bead second

\-To determine the probability of getting a green bead on the second draw, we look at all of the outcomes that contain a green bead second. These are:

* a red bead and then a green bead (RG);
* a green bead and then another green bead (GG).



\-The probability of the first outcome is 15/56 and the probability of the second outcome is 5/14. By adding these two probabilities, we see that the probability of getting a green bead second is

P(second bead green) = 15/56 + 5/14 = 15/56 + 20/56 = 35/56 = 5/8



###### Step 4: Probability of red first and green second

\-We have already calculated the probability that the first bead is red and the second bead is green (RG). It is 15/56.



###### Step 5: Dependent or independent?

\-According to the definition, events are independent if and only if

P(A and B) =P(A) × P(B)



\-In this problem:

* P(first bead red) = 3/8
* P(second bead green) = 5/8
* P(first bead red and second bead green) = 15/56

\-Since 3/8 × 5/8 = 15/64 ≠ 15/56, the events are dependent.





#### 4

\-A sample space, S, consists of all natural numbers less than 16. A is the event of drawing an even number at random. B is the event of randomly drawing a prime number. Are A and B mutually exclusive events? Prove this using the addition rule.



##### SOLUTION

###### Step 1: Write down the sample space

\-The sample space contains all the natural numbers less than 16.

S ={1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15}



###### Step 2: Write down the events

\-The even natural numbers less than 16 are

A = {2; 4; 6; 8; 10; 12; 14}



\-The prime numbers less than 16 are

B ={2;3;5;7;11;13}

\-We can already see from writing down our event sets that A and B share the event 2 and are thus not mutually exclusive. However, the question asked us to prove this using the addition rule so let’s go ahead and do that.



###### Step 3: Compute the probabilities

\-The probability of an event is the number of outcomes in the event set divided by the number of outcomes in the sample space. There are 15 outcomes in the sample space.



a. 

Since there are 7 outcomes in the A event set, P(A) = n(A)/n(S) = 7/15 .



b. 

Since there are 6 outcomes in the B event set, P(B) = n(B)/n(S) = 6/15 = 2/5 .



c. 

\-The event that is a prime number or an even number is the union of the above two event sets. There are 12 elements in the union of the event sets, so P(A or B) = n(A or B)/n(S) = 12/15 .



###### Step 4: Are the two events mutually exclusive?

\-To test whether two events are mutually exclusive, we can use the addition rule. For two mutually exclusive events,

\-P(A and B) is an empty set, therefore P(A or B) = P(A) + P(B)

\-Since P(A or B) = 12/15 and P(A) + P(B) = 6/15 + 7/15 = 13/15

P(A or B) ≠ P(A)+P(B)

\-Therefore the intersection of A and B is nonzero. This means that the events A and B are not mutually exclusive.



#### 5

\-The probability that a person drinks tea is 0,5. The probability that a person drinks coffee is 0,4. The probability that a person drinks tea, coffee or both is 0,8. Determine the probability that a person drinks tea and coffee.



##### SOLUTION

###### Step1: Determine if the events are mutually exclusive

\-Let the probability that a person drinks tea = P(T) and the probability that a person drinks coffee = P(C).

\-From the information provided in the question, we know that:

* P(T) = 0,5
* P(C) = 0,4
* P(T or C) = 0,8
* P(T) + P(C) = 0,5+0,4=0,9

\-Therefore P(T or C)=P(T)+P(C)

\-Therefore the events are not mutually exclusive.



###### Step 2: Compute the probability that a person drinks tea and coffee

\-Using the addition rule, we know that:

P(A or B) = P(A) + P(B) − P(A and B)

∴P(T or C) = P(T) + P(C) − P(T and C)

0,8 = 0,4 + 0,5 − P(T and C)

∴P(T and C) = 0,4 + 0,5 − 0,8 = 0,1

\-Therefore the probability that a person drinks tea and coffee is 0,1.



#### 6

\-Joe wants to open a tuck shop at his school but is not sure which cool drinks to stock.

\-Before opening, he interviewed a sample of learners to determine what types of cool drinks they like. From his research, he determined that the probability that a learner drinks cola is 0,3, the probability that a learner drinks lemonade is 0,6 and the probability that a learner drinks neither is 0,2. Determine:

* the probability that a learner drinks cola and lemonade.
* the probability that a learner drinks only cola or only lemonade.



##### SOLUTION

###### Step 1: Dermine the probability that a learner drinks cola or lemonade

\-Let the probability that a learner drinks cola = P(C) and the probability that a learner drinks lemonade = P(L).

\-From the information provided in the question, we know that:

* P(C) = 0,3
* P(L) = 0,6
* P(not(C or L)) = 0,2



\-Using the complementary rule:

P(not(C or L)) = 1 − P(C or L)

∴ P(C or L) = 1 − P(not(C or L))

= 1 − 0,2

= 0,8



###### Step 2: Calculate the probability that a learner drinks cola and lemonade

\-Using the addition rule:

P(C or L) = P(C) + P(L) − P(C and L)

∴P(C and L) = P(C) + P(L) − P(C or L)

= 0,3 + 0,6 − 0,8

= 0,1

\-The probability that a learner drinks both cola and lemonade is 0,1.



###### Step 3: Determine the probability that a learner drinks only cola or only lemonade

\-This question requires us to calculate the probability that a learner likes lemonade or cola but not both of them. We can write this as:

P(only C or only L) = P(C or L) − P(C and L) since a learner can like either cola or lemonade but not both.

\-We already know P(C or L) = 0,8 and P(C and L) = 0,1, therefore the probability of a learner drinking only cola or only lemonade is 0,7.





### QUESTIONS

#### 1\.

Determine whether the following events are dependent or independent and give areas on for your answer:

##### a) 

Joan has a box of yellow, green and orange sweets. She takes out a yellow sweet and eat sit. Then, she chooses another sweet and eat sit.



##### b) 

Vuzi throws a die twice.



##### c) 

Celia chooses a card at random from a deck of 52 cards. She is unhappy with her choice, so she places the card back in the deck, shuffles it and chooses a second card.



##### d) 

Thandi has a bag of beads. She randomly chooses a yellow bead, looks at it and then puts it back in the bag. Then she randomly chooses another bead and sees that it is red and puts it back in the bag.



##### e) 

Mark has a container with calculators. Some of them work and some are broken. He randomly chooses a calculator and sees that it does not work and throws it away. He then chooses another calculator, sees that it works and keeps it.



#### 2\. 

Given that P(A) = 0,7; P(B) = 0,4 and P(A and B) = 0,28,

##### a) 

are events A and B mutually exclusive? Give a reason for your answer.



##### b) 

are the events A and B independent? Give a reason for your answer.



#### 3\. 

In the following examples, are A and B dependent or independent?

##### a) 

P(A) = 0,2;P(B) = 0,7 and P(A and B) = 0,21



##### b) 

P(A) = 0,2;P(B) = 0,7 and P(B and A) = 0,14.



#### 4\. 

n(A) = 5;n(B) = 4;n(S) = 20 and n(A or B) = 8.



##### a) 

Are A and B mutually exclusive?



##### b) 

Are A and B independent?



#### 5\. 

Simon rolls a die twice. What is the probability of getting:

##### a) 

two threes.



##### b) 

a prime number then an even number.



##### c) 

no threes.



##### d) 

only one three.



##### e) 

at least one three.



#### 6\. 

\-The Mandalay Secondary soccer team has to win both of their next two matches in order to qualify for the finals. The probability that Mandalay Secondary will win their first soccer match against Ihlumelo High is 2/5 and the probability of winning their second soccer match against Masiphumelele Secondary is 3/7. Assume

each match is an independent event.



##### a) 

What is the probability they will progress to the finals?



##### b) 

What is the probability they will not win either match?



##### c) 

What is the probability they will win only one of their matches?



##### d) 

You were asked to assume that the matches are independent events but this is unlikely in reality. What are some factors you think may result in the outcome of the matches being dependent?



### 7\. 

Apencil bag contains 2 red pens and 4 green pens. A pen is drawn from the bag and then replaced before a second pen is drawn. Calculate:



##### a) 

The probability of drawing a red pen first if a green pen is drawn second.



##### b) 

The probability of drawing a green pen second if the first pen drawn was red.



##### c) 

The probability of drawing a red pen first and a green pen second.



#### 8\. 

A lunch box contains 4 sandwiches and 2 apples. Vuyele chooses a food item randomly and eats it. He then chooses another food item randomly and eats that.

Determine the following:



##### a) 

The probability that the first item is a sandwich.



##### b) 

The probability that the first item is a sandwich and the second item is an apple.



##### c) 

The probability that the second item is an apple.



##### d) 

Are the events in a) and c) dependent? Confirm your answer with a calculation.



#### 9\. 

Given that P(A) = 0,5; P(B) = 0,4 and P(A or B) = 0,7, determine by calculation whether events A and B are:



##### a) 

mutually exclusive



##### b) 

independent



#### 10\. 

\-A and B are two events in a sample space where P(A) = 0,3; P(A or B) = 0,8 and P(B) = k. Determine the value of k if:



##### a) 

A and B are mutually exclusive



##### b) 

A and B are independent



#### 11\. 

A and B are two events in sample space S where n(S) = 36; n(A) = 9; n(B) = 4 and n(not (A or B)) = 24. Determine:



##### a) 

P(A or B)



##### b) 

P(A and B)



##### c)

whether events A and B independent. Justify your answer with a calculation.



#### 12\. 

\-The probability that a Mathematics teacher is absent from school on a certain day is 0,2. The probability that the Science teacher will be absent that same day is 0,3.



##### a) 

Do you think these two events are independent? Give a reason for your answer.



##### b) 

Assuming the events are independent, what is the probability that the Mathematics teacher or the Science teacher is absent?



##### c) 

What is the probability that neither the Mathematics teacher nor the Science teacher is absent?



#### 13\. 

Langa Cricket Club plays two cricket matches against different clubs. The probability of winning the first match is 3/5 and the probability of winning the second match is 4/9. Assuming the results of the matches are independent, calculate the probability that Langa Cricket Club will:



##### a) 

win both matches.



##### b) 

not win the first match.



##### c) 

win one or both of the two matches.



##### d) 

win neither match.



##### e) 

not win the first match and win the second match.



#### 14\. 

Two teams are working on the final problem at a Mathematics Olympiad. They have 10 minutes remaining to finish the problem. The probability that team A will finish the problem in time is 40% and the probability that team B will finish the problem in time is 25%. Calculate the probability that both teams will finish before they run out of time.



##### 15\. 

\-Thabo and Julia were arguing about whether people prefer tea or coffee. Thabo suggested that they do a survey to settle the dispute. In total, they surveyed 24 people and found that 8 of them preferred to drink coffee and 12 of them preferred to drink tea. The number of people who drink tea, coffee or both is 16.



\-Determine:

##### a) 

the probability that a person drinks tea, coffee or both.



##### b) 

the probability that a person drinks neither tea nor coffee.



##### c) 

the probability that a person drinks coffee and tea.



##### d) 

the probability that a person does not drink coffee.



##### e)

whether the event that a person drinks coffee and the event that a person drinks tea are independent.



## Tools and Techniques

### Venn diagrams 

\-used to show how events are related to one another. A Venn

diagram can be very helpful when doing calculations with probabilities. In a Venn diagram each event is represented by a shape, often a circle or a rectangle. The region inside the shape represents the outcomes included in the event and the region outside the shape represents the outcomes that are not in the event.



### Tree diagrams

\-are useful for organising and visualising the different possible outcomes of a sequence of events. Each branch in the tree shows an outcome of an event, along with the probability of that outcome. For each possible outcome of the first event, we draw a line where we write down the probability of that outcome and the state of the

world if  that outcome happened. Then, for each possible outcome of the second event we do the same thing. The probability of a sequence of outcomes is calculated as the product of the probabilities along the branches of the sequence.



### Two-way contingency tables

\-are a tool for keeping a record of the counts or percent ages in a probability problem. Two-way contingency tables are especially helpful for figuring out whether events are dependent or independent.



### EXAMPLES

#### 1

\-There are 200 boys in Grade 12 at Marist Brothers High School. 

\-Their participation in sport can be broken down as follows:

* 107 play rugby
* 90 play soccer
* 63 play cricket
* 35 play rugby and soccer
* 23 play rugby and cricket
* 15 play rugby, soccer and cricket
* 190 boys play rugby, soccer or cricket



##### i.

How many boys do not play any of these sports?



##### ii.

Draw a Venn diagram to illustrate the given information and use it to answer the following questions:



###### a)

How many boys play soccer and cricket, but not rugby?



###### b)

What is the probability that a randomly chosen Grade 12 boy at Marist Brothers High School will take part in at least two of the sports: rugby, soccer or cricket?Give your answer correct to 3 decimal places.



###### SOLUTION

\####### Step 1: Calculate the number of boys playing none of the given sports

\-In order to calculate the number of boys playing none of the sports, we subtract the number of boys playing any of the three sports from the total number of boys in the sample space.

\-Not rugby, cricket or soccer = 200 − 190 = 10

\-Therefore 10 boys do not play rugby, cricket or soccer.



\####### Step 2: Draw the outline of the Venn diagram

\-Let X = the sample space; R = rugby; S = soccer and C = cricket. Put this information on a Venn diagram:



>DIAGRAM\[

\-Venn diagram

\-3 intersecting circles labelled R; C and S inside a box labelled X

]



\####### Step 3: Calculate the counts for the different groupings

\-The following groupings exist:



>DIAGRAM\[

\-Venn diagram

\-The circle R has RR; Circle C has CC, Circle S has SS

\-The intersection of all 3 circles has RCS

\-Intersection of R and C has RC

\-Intersection of R and S has RS

\-Intersection of C and S has CS

\-Inside the box but outside th circles there is not(R, C, S)

]



* Rugby, cricket and soccer: RCS

RCS = 15



* Rugby and soccer but not cricket: RS

RS=(RandS)−RCS

=35−15=20



* Rugby and cricket but not soccer: RC

RC=(RandC)−RCS

=23−15=8



* Cricket and soccer but not rugby: CS

CS = (S and C) − RCS

Let (S and C) = x

Therefore CS = x − 15



* Only rugby: RR

RR=R−RS−RC−RCS

=107−20−8−15

=64



* Only soccer: SS

SS=S−RS−CS−RCS

=90−20−(x−15)−15

=70−x



* Only cricket: CC

CC=C−RC−CS−RCS

=63−8−(x−15)−15

=55−x



* Not rugby, cricket or soccer:

not(R,C,S)

not(R,C,S)=10



\####### Step 4: Fill in the counts on the Venn diagram



>DIAGRAM\[

\-Venn diagram

\-Circles R, C and S

\-Box labelled X

\-The circle R has 64; Circle C has 55 - x, Circle S has 70 - x

\-The intersection of all 3 circles has 15

\-Intersection of R and C has 8

\-Intersection of R and S has 20

\-Intersection of C and S has x - 15

\-Inside the box but outside the circles there is 10

]



\####### Step 5: Calculate the unknown values

\-Since 190 of the boys play at least one of the sports, using the values on our Venn diagram, we can setup the following equation to solve for x.

64 + 8 + 15 + 20 + (x−15) + (70−x) + (55−x) = 190

217 − x = 190

\-Therefore x = 27



\-We know that:

Cricket and soccer but not rugby (CS) = x−15

Therefore CS = 27−15

= 12



\-Therefore there are 12 boys who play cricket and soccer but not rugby.



\####### Step 6: Calculate the probability that a randomly chosen Grade 12 boy plays at least two of the given sports

\-We know the number of boys who play two or more of rugby, cricket or soccer and we know the total number of boys. Therefore, we can calculate the probability using the following equation:



P(at least two sports) = \[n(RC) + n(RS) + n(CS) + n(RCS)]/n(X)

= (8 + 15 + 20 + 12)/200

= 55/200 = 0,275



\-Therefore the probability that a randomly chosen Grade 12 boy plays at least 2 of either rugby, cricket or soccer = 0,275 or 27,5%







#### 2

\-The probability that the floor of a supermarket will be wet when it opens in the morning is 30% and there is a 10% probability of the floor being very wet. The probability that a person will slip and fall if the floor is dry is 12% and a person is three times as likely

to fall if the floor is wet. 

\-If the floor is very wet, the probability that a person will fall is

0,6. Draw a tree diagram to represent the given information, showing the probabilities of each outcome, and use it to answer the following questions:



##### a.

What is the probability that a person will fall on any given day?



##### b. 

What is the probability that a person will not fall on any given day?



##### c. 

Are the events of the floor being dry and a person falling independent? Justify your answer with a calculation.



##### SOLUTION

###### Step 1: Identify the events

\-There are three outcomes for the floor, namely, dry, wet and very wet, and two out comes for a person, namely fall or not fall.



###### Step 2: Draw the first level of the tree diagram

>DIAGRAM\[

\-Root Node: Surface Condition

\--Branch 1 (Top): "very wet" | Probability = 0,1

\--Branch 2 (Middle): "wet" | Probability = 0,3

\--Branch 3 (Bottom): "dry" | Probability = 0,6

]



\-This tree diagram shows the possible outcomes and probabilities of the status of the floor.



###### Step 3: Draw the second level of the tree diagram



>DIAGRAM\[

\-Root Node: Surface Condition

\--Level 1 Node: "very wet" \[Prob: 0,1]

\---Level 2 Branch (Top): "fall" | Conditional Probability = 0,6

\---Level 2 Branch (Bottom): "not fall" | Conditional Probability = 0,4

\--Level 1 Node: "wet" \[Prob: 0,3]

\---Level 2 Branch (Top): "fall" | Conditional Probability = 0,36

\---Level 2 Branch (Bottom): "not fall" | Conditional Probability = 0,64

\--Level 1 Node: "dry" \[Prob: 0,6]

\---Level 2 Branch (Top): "fall" | Conditional Probability = 0,12

\---Level 2 Branch (Bottom): "not fall" | Conditional Probability = 0,88

]



\-This tree diagram shows the possible outcomes and probabilities based on whether the floor is very wet, wet or dry. 

\-Remember that the sum of the probabilities for any set of branches is 1. 

\-Use this as a logical check whenever you are constructing a tree diagram.



###### Step 4: Compute the probabilities of the various outcomes

\-We can calculate the probability of each outcome by multiplying the probabilities along the path from the start of the tree to the end of the branch containing the desired outcome.

* P(very wet and fall) = 0,1 ×0,6 = 0,06
* P(very wet and not fall) = 0,1 ×0,4 = 0,04
* P(wet and fall) = 0,3×0,36 = 0,108
* P(wet and not fall) = 0,3 ×0,64 = 0,192
* P(dry and fall) = 0,6 ×0,12 = 0,072
* P(dry and not fall) = 0,6 ×0,88 = 0,528



###### Step 5: Compute the probability of falling or not falling

\-We can calculate the probability of falling or not falling by adding the probabilities of all the desired outcomes.



* P(fall) = 0,06 + 0,108 + 0,072 = 0,24
* P(not fall) = 0,04 + 0,192 + 0,528 = 0,76



\-Therefore the probability of falling on a given day is 24% and the probability of not falling is 76%.



###### Step 6: Determine whether  the floor being dry and a person falling are independent events

\-Logically, it appears that these events are dependent but the question asked us to prove this using a calculation. We can do this using the rule for independent events:

P(A and B) = P(A) × P(B)

P(dry and fall) = 0,072

P(dry) × P(fall) = 0,6 × 0,24

= 0,144

Therefore P(dry and fall) ≠ P(dry) × P(fall)



\-Therefore we can conclude that the floor being dry and a person falling are dependent events.





### QUESTIONS

#### 1\. 

A survey was done on a group of learners to determine which type of TV shows they enjoy: action, comedy or drama. Let A = action, C = comedy and D = drama. The results of the survey are shown in the Venn diagram below.



>DIAGRAM\[

\-3 intersecting circles labelled A, C and D

\-The box is labelled S

\-A has 21; C has 31; D has 23

\-The intersection of A and C has 6

\-Intersection of A and D has 10

\-Intersection of C and D has 3

\-Intersection of all 3 circles has 5

\-Inside the box but outside the circles there is 16

]



Study the Venn diagram and determine the following:



##### a) 

the total number of learners surveyed



##### b) 

the number of learners who do not enjoy any of the mentioned types of TV shows



##### c) 

P(not A)



##### d) 

P(A or D)



##### e) 

P(A and C and D)



##### f) 

P(not (A and D))



##### g) 

P(A or not C)



##### h) 

P(not (A or C))



##### i) 

the probability of a learner enjoying at least two types of TV shows



##### j) 

Describe, in words, the meaning of each of the questions c) to h) in the context of this problem.



#### 2\. 

\-At Thandokulu Secondary School, there are are 320 learners in Grade 12, 270 of whom take one or more of Mathematics, History and Economics. The subject choice is such that everybody who takes Physical Sciences must also take Mathematics and nobody who takes Physical Sciences can take History or Economics.

\-The following is known about the number of learners who take these subjects:



* 70 take History
* 50 take Economics
* 120 take Physical Sciences
* 200 take Mathematics
* 20 take Mathematics and History
* 10 take History and Economics
* 25 take Mathematics and Economics
* x learners take Mathematics and History and Economics



##### a) 

Represent the information above in a Venn diagram. Let Mathematics be M, History be H, Physical Sciences be P and Economics be E.



##### b) 

Determine the number of learners, x, who take Mathematics, History and Economics.



##### c) 

Determine P(not (M or H or E)) and state in words what your answer means.



##### d) 

Determine the probability that a learner takes at least two of these subjects.





#### 3\. 

A group of 200 people were asked about the kind of sports they watch on television. The information collected is given below:



* 180 watch rugby, cricket or soccer
* 5watch rugby, cricket and soccer
* 25 watch rugby and cricket
* 30 watch rugby and soccer
* 100 watch rugby
* 65 watch cricket
* 80 watch soccer
* x watch cricket and soccer but not rugby



##### a) 

Represent all the information in a Venn diagram. Let rugby watchers = R, cricket watchers = C and soccer watchers = F.



##### b) 

Find the value of x.



##### c) 

Determine P(not (R or F or C))



##### d) 

Determine P(R or F or not C)



##### e) 

Are watching cricket and watching rugby independent events? Confirm your answer using a calculation.





#### 4\. 

There are 25 boys and 15 girls in the English class. Each lesson, two learners are randomly chosen to do an oral.



##### a) 

Represent the composition of the English class in a tree diagram. Include all possible outcomes and probabilities.



##### b) 

Calculate the probability that a boy and a girl are chosen to do an oral in any particular lesson.



##### c) 

Calculate the probability that at least one of the learners chosen to do an oral in any particular lesson is male.



##### d) 

Are the events picking a boy first and picking a girl second independent or dependent? Justify your answer with a calculation.



#### 5\. 

During July in Cape Town, the probability that it will rain on a randomly chosen day is 4/5. 

Gladys either walks to school or gets a ride with her parents in their car. If it rains, the probability that Gladys’ parents will take her to school by car is 5/6.

If it does not rain, the probability that Gladys’ parents will take her to school by car is 1/12.



##### a) 

Represent the above information in a tree diagram. On your diagram show all the possible outcomes and respective probabilities.



##### b) 

What is the probability that it is a rainy day and Gladys walks to school?



##### c) 

What is the probability that Gladys’ parents take her to school by car?





#### 6\. 

There are two types of property burglaries: burglary of private residences and burglary of business premises. In Metropolis, burglary of a private residence is four times as likely as that of a business premises. The following statistics for each type of burglary were obtained from the Metropolis Police Department:



Burglary of private residences

Following a burglary:

* 25%of criminals are arrested within 48 hours.
* 15%of criminals are arrested after 48 hours.
* 60%of criminals are never arrested for that particular burglary.



Burglary of business premises

Following a burglary:

* 36%of criminals are arrested within 48 hours.
* 54%of criminals are arrested after 48 hours.
* 10%of criminals are never arrested for that particular burglary.



##### a) 

Represent the information above in a tree diagram, showing all outcomes and respective probabilities.



##### b) 

Calculate the probability that a private home is burgled and nobody is arrested.



##### c) 

Calculate the probability that burglars of private homes and business premises are arrested.



##### d)

Use your answer in the previous question to construct a tree diagram to calculate the probability that a burglar is arrested after atmost three burglaries.



##### e)

Determine after how many burglaries a burglar has at least a



###### i. 

90% chance of being arrested.



###### ii. 

99% chance of being arrested.







## Contingency tables

### Example

\-The table below shows the results of testing two different treatments on 240 fruit trees which have a disease causing the trees to die.Treatment A involves the careful removal of infected branches and treatment B involves removing infected branches as well as spraying the tree with antibiotic.



||Tree dies within 4 years|Tree lives > 4 years|Total|
|-|-|-|-|
|Treatment A|70|50||
|Treatment B||||
|Total|90|150||



#### 1\. 

Fill in the missing values on the table.



#### 2\.

What is the probability the a tree received treatment B?



#### 3\.

What is the probability that a tree will live beyond 4 years?



#### 4\.

What is the probability that a t ree is given treatment B and lives beyond 4 years?



#### 5\.

Of the trees who were given treatment B, what is the probability that a tree lives beyond 4 years?



#### 6\. 

Area tree given treatment B and living beyond 4 years independent events?

Justify your answer with a calculation.



#### SOLUTION

##### Step 1: Complete the contingency table

Since each column has to sum to its total, we can work out the number of trees which fall into each category for treatments A and B. Then, we can add each row to get the totals on the right hand side of the table.



||Tree dies within 4 years|Tree lives > 4 years|Total|
|-|-|-|-|
|Treatment A|70|50|120|
|Treatment B|20|100|120|
|Total|90|150|240|



##### Step 2: Compute the required probabilities

\-For the second question, we need to determine the probability that a tree receives treatment B. This means that we do not include treatment A in this calculation. So, the probability that treatment B is given to a tree is the ratio between the number of trees that received treatment B and the total number of trees.



* P(treatment B) = n(treatment B)/n(total trees)

= 120/240 = 1/2



\-Similarly for the third question, the probability that a tree will live beyond 4 years:



* P(lives beyond 4 years) = \[n(lives > 4 years)]/n(total trees)

= 150/240 = 5/8



\-In the fourth question, we need to determine the probability that a tree receives treatment B and lives beyond 4 years.



* P(treatment B and lives > 4 years) = \[n(treatment B and lives > 4 years)]/n(total trees)

= 100/240 = 5/12



\-In the fifth question, there is a subtle change from the fourth question. Here, we need to determine the probability that of the trees which received treatment B, a tree lives beyond 4 years. This means we are only concerned with those trees which received

treatment B. We no longer need to care about the trees given treatment A, so our denominator needs to be adjusted accordingly.



* P(lives > 4 years having received treatment B) = \[n(treatment B and lives > 4 years)]/n(total treatment B)

= 100/120 = 5/6



##### Step 3: Independence

\-We need to determine whether a tree given treatment B and living beyond 4 years are dependent or independent events. According to the definition, two events are independent if and only if



\-P(A and B) =P(A) × P(B)

\-P(treatment B) × P(lives > 4 years) = 1/2× 5/8 = 5/16

\-P(treatment B and lives > 4 years) = 5/12



\-From these probabilities we can see that



* P(treatment B and lives > 4 years) ≠ P(treatment B) × P(lives > 4 years)



and therefore the treatment of a tree with treatment B and living beyond 4 years are dependent events.





### QUESTIONS

#### 1\. 

A number of drivers were asked about the number of motor vehicle accidents they were involved in over the last 10 years. Part of the data collected is shown in the table below.



||≤ 2 accidents|≥ 2 accidents|Total|
|-|-|-|-|
|Female|210|90||
|Male||||
|Total|350|150|500|



##### a)

What are the variables investigated here and what is the purpose of the research?



##### b) 

Complete the table.



##### c)

Determine whether gender and number of accidents are independent using a calculation.



#### 2\. 

Researchers conducted a study to test how effective a certain inoculation is at preventing malaria. Part of their data is shown below:



||Malaria|No Malaria|Total|
|-|-|-|-|
|Male|a|b|216|
|Female|c|d|648|
|Total|108|756|864|



#### a) 

Calculate the probability that a randomly selected study participant will be female.



#### b) 

Calculate the probability that a randomly selected study participant will have malaria.



#### c) 

If being female and having malaria are independent events, calculate the value c.



#### d)

Using the value of c, fill in the missing values on the table.





#### 3\. 

The reaction time of 400 drivers during an emergency stop was tested. Within the study cohort (the group of people being studied), the probability that a driver chosen at random was 40 years old or younger is 0,3 and the probability of a reaction timeless than 1,5 seconds is 0,7.



##### a) 

Calculate the number of drivers who are 40 years old or younger.



##### b) 

Calculate the number of drivers who have a reaction time of less than 1,5 seconds.



##### c) 

If age and reaction time are independent events, calculate the number of drivers 40 years old and younger with a reaction time of less than 1,5 seconds.



##### d) 

Complete the table below.



||Reaction time < 1,5 s|Reaction time > 1,5 s|Total|
|-|-|-|-|
|≤ 40 years||||
|> 40 years||||
|Total|||400|



#### 4\. 

A new treatment for influenza (the flu) was tested on a number of patients to determine if it was better than a placebo (a pill with no therapeutic value). The table below shows the results three days after treatment:



||Flu|No Flu|Total|
|-|-|-|-|
|Placebo|228|60||
|Treatment||||
|Total|240|312||



##### a) 

Complete the table.



##### b) 

Calculate the probability of a patient receiving the treatment.



##### c) 

Calculate the probability of a patient having no flu after three days.



##### d) 

Calculate the probability of a patient receiving the treatment and having no flu after three days.



##### e) 

Using a calculation, determine whether a patient receiving the treatment and having no flu after three days are dependent or independent events.



##### f) 

Calculate the probability that a patient receiving treatment will have no flu after three days.



##### g) 

Calculate the probability that a patient receiving a placebo will have no flu after three days.



##### h) 

Comparing you answers in f) and g), would you recommend the use of the new treatment for patients suffering from influenza?



##### i) 

A hospital is trying to decide whether to purchase the new treatment. The new treatment is much more expensive than the old treatment. According to the hospital records, of the 72 024 flu patients that have been treated with the old treatment, only 3200 still had the flu three days after treatment.



* Construct a two-way contingency table comparing the old treatment data with the new treatment data.
* Usingthe data from your table, advise the hospital whether to purchase the new treatment or not.





#### 5\. 

Human immunodeficiency virus (HIV) affects 10% of the South African population.



##### a) 

If a test for HIV has a 99,9% accuracy rate (i.e. 99,9% of the time the test is correct, 0,1% of the time, the test returns a false result), draw a two-way contingency table showing the expected results if 10 000 of the general population are tested.



##### b) 

Calculate the probability that a person who tests positive for HIV does not have the disease, correct to two decimal places.



##### c) 

In practice, a person who tests positive for HIV is always tested a second time. Calculate the probability that an HIV-negative person will test positive after two tests, correct to four decimal places.



## The fundamental counting principle

>DEFINITION: -The fundamental counting principle states that if there are n(A)outcomes in event A and n(B)outcomes in event B, then there are n(A) × n(B) outcomes in event A and event B combined.

\-Mathematics began with counting. Initially ,fingers, beans and buttons were used  to help with counting, but these are only practical for small numbers. What happens when a large number of items must be counted?

\-This section focuses on how to use mathematical techniques to count different assortments of items.



\-An important aspect of probability theory is the ability to determine the total number of possible outcomes when multiple events are considered.

\-For example, what is the total number of possible outcomes when a die is rolled and then a coin is tossed? The roll of a die has six possible outcomes (1; 2; 3; 4; 5 or 6) and the toss of a coin, 2 outcomes (heads or tails). The sample space (total possible outcomes) can be represented as follows:

* S= {(1;H); (2;H); (3;H); (4;H); (5;H); (6;H); (1;T); (2;T); (3;T); (4;T); (5;T); (6;T)}

\-Therefore there are 12 possible outcomes.

\-The use of lists, tables and tree diagrams is only feasible for events with a few outcomes. When the number of outcomes grows, it is not practical to list the different possibilities and the fundamental counting principle is used instead.



\-If we apply the fundamental counting principle to our previous example, we can easily calculate the number of possible outcomes by multiplying the number of possible die rolls with the number of outcomes of tossing a coin: 6 × 2 = 12 outcomes. This allows us to formulate the following:



\-If there n\_1 possible outcomes for event A and n\_2 outcomes for event B, then the total possible number of outcomes for both events is n\_1 × n\_2

\-This can be generalised to k events, where k is the number of events. The total number of outcomes for k events is:

* n\_1 × n\_2 × n\_3 ×···× n\_k



NOTE:

The order in which the experiments are done doesnot affect the total numberof possible outcomes.



\-We can apply this to choices without repitition as we shall see in one of the examples.



>If the number of choices is unchanged each time you choose?

For example, if a coin is flipped three times,what is the total number of different results? Each time a coin is flipped, there are two possible outcomes, namely heads or tails. The coin is flipped 3 times. We can use a tree diagram to determine the total number of possible outcomes:



>DIAGRAM\[

\-Root Node: Start (Flip 1)

\--Level 1 Node (Top): H 

\---Level 2 Branch (Top): H

\----Level 3 Branch (Top): H → Path Outcome: HHH

\----Level 3 Branch (Bottom): T → Path Outcome: HHT

\---Level 2 Branch (Bottom): T

\----Level 3 Branch (Top): H → Path Outcome: HTH

\----Level 3 Branch (Bottom): T → Path Outcome: HTT

\--Level 1 Node (Bottom): T

\---Level 2 Branch (Top): H

\----Level 3 Branch (Top): H → Path Outcome: THH

\----Level 3 Branch (Bottom): T → Path Outcome: THT

\---Level 2 Branch (Bottom): T

\----Level 3 Branch (Top): H → Path Outcome: TTH

\----Level 3 Branch (Bottom): T → Path Outcome: TTT

]



\-From the tree diagram, we can see that there is a total of 8 different possible outcomes.

\-Drawing a tree diagram is possible for three different coin flips, but as soon as the number of events increases, the total number of possible outcomes increases to the point where drawing a tree diagram is impractical.

\-For example, think about what a tree diagram would look like if we were to flip a coin six times. In this case, using the fundamental counting principle is a far easier option. We know that each time a coin is flipped that there are two possible out comes.

\-So if we flip a coin six times, the total number of possible outcomes is equivalent to multiplying 2 by itself six times:

2 × 2 × 2 × 2 × 2 × 2 = 26 = 64



\-Another example is if you have the letters A, B, C, and D and you wish to discover the number of ways of arranging them in  three-letter patterns if repetition is allowed, such as ABA, DCA, BBB etc. Youwillfindthat thereare64ways. This isbecausefor the

first letter of the pattern, you can choose any of the four available letters, for the second letter of the pattern, you can choose any of the four letters,and for the final letter of

the pattern you can choose any of the four letters. Multiplying the number of available

choices for each letter in the pattern gives the total available arrangements of letters:

* 4 × 4 × 4 = 4^3 = 64

\-This allows us to formulate the following:



\-When you have n objects to choose from and you choose from them r times, then the total number of possibilities is:

* n × n × n...× n (r times) = n^r



### EXAMPLES

#### 1  Choices without repetition

A take-away has a 4-piece lunch special which consists of a sandwich, soup, dessert and drink for R25,00. They offer the following choices for:

Sandwich: chicken mayonnaise, cheese and tomato, tuna mayonnaise, ham and lettuce

Soup: tomato,chicken noodle, vegetable

Dessert: ice-cream, piece of cake

Drink: tea, coffee, Coke, Fanta, Sprite

How many possible meals are there?



##### SOLUTION

###### Step 1: Determine how many parts to the meal there are

There are 4 parts: sandwich, soup, dessert and drink.



###### Step 2: Identify how many choices there are for each part

|Meal component|Sandwich|Soup|Dessert|Drink|
|-|-|-|-|-|
|Number of choices|4|3|2|5|



###### Step3: Use the fundamental counting principle to determine how many different meals are possible

4 × 3 × 2 × 5 = 120

\-So there are 120 possible meals.





#### 2 Choices with repetition

A school plays a series of 6 soccer matches. For each match there are 3 possibilities: a win, a draw or a loss. How many possible results are there for the series?



##### SOLUTION

###### Step 1: Determine how many outcomes you have to choose from for each event

There are 3 outcomes for each match: win, draw or lose.



###### Step 2: Determine the number of events

There are 6 matches, therefore the number of events is 6.



###### Step 3: Determine the total number of possible outcomes

There are 3 possible outcomes for each of the 6 events. Therefore, the total number of possible outcomes for the series of matches is

* 3×3×3×3×3×3 = 3^6 = 729



### QUESTIONS

#### 1\.

Tarryn has five different skirts, four different tops and three pairs of shoes. Assuming that all the colours complement each other, how many different outfits can she put together?



#### 2\. 

In a multiple-choice question paper of 20 questions the answers can be A, B, C or D. How many different ways are there of answering the question paper?



#### 3\. 

A debit card requires a five digit personal identification number (PIN) consisting of digits from 0 to 9. The digits may be repeated. How many possible PINs are there?



#### 4\. 

The province of Gauteng ran out of unique number plates in 2010. Prior to 2010, the number plates were formulated using the style LLLDDDGP, where L is any letter of the alphabet excluding vowels and Q, and D is a digit between 0 and9. The new style the Gauteng government introduced is LLDDLLGP. How many

more possible number plates are there using the new style when compared to the old style?



#### 5\. 

A gift basket consists of one CD, one book, one box of sweets, one packet of nuts and one bottle of fruit juice. The person who makes the gift basket can choose from five different CDs, eight different books, three different boxes of sweets, four kinds of nuts and six flavours of fruit juice. How many different gift baskets

can be produced?



#### 6\. 

The code for a safe is of the form XXXXYYY where X is any number from 0 to 9 and Y represents the letters of the alphabet. How many codes are possible for each of the following cases:

##### a) 

the digits and letters of the alphabet can be repeated.



##### b) 

the digits and letters of the alphabet can be repeated, but the code may not contain a zero or any of the vowels in the alphabet.



##### c) 

the digits and letters of the alphabet can be repeated, but the digits may only be prime numbers and the letters X, Y and Z are excluded from the code.



#### 7\. 

Arestaurant offers four choices of starter, eight choices for the main meal and six choices for dessert. A customer can choose to eat just one course, two different courses or all three courses. Assuming that all courses are available, how many different meal options does the restaurant offer?



## Factorial notation

\-It is a common occurrence in counting problems that the

outcome of the first event reduces the number of possible outcomes for the second event by exactly 1, and the outcome of the second event reduces the possible outcomes for the third event by 1 more, etc.

\-As this sort of problem occurs so frequently, we have a special notation to represent the answer. For an integer, n, the notation n! (read n factorial) represents: n × (n−1) × (n−2) ×···× 3 × 2 × 1

\-This allows us to formulate the following:



* The total number of possible arrangements of n different objects is

>n × (n−1) × (n−2) ×...× 3 × 2 × 1 = n!

>with the following definition: 0! = 1.



### EXAMPLES

#### 1

Eight athletes take part in a 400m race. In how many different ways can all 8 places in the race be arranged?



##### SOLUTION

\-Any of the 8 athletes can come first in the race. Now there are only 7 athletes left to be second, because an athlete cannot be both second and first in the race. 

\-After second place, there are only 6 athletes left for the third place, 5 athletes for the fourth place, 4 athletes for the fifth place, 3 athletes for the sixth place, 2 athletes for the seventh place and 1 athlete for the eighth place. Therefore the number of ways that the athletes can be ordered is as follows:

* 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 40320



#### 2

##### a.

Determine 12!



##### b. 

Show that 8!/4! = 8 × 7 × 6 ×5



##### c. 

Show that n!/(n−1)! = n



##### SOLUTION

###### a.

\-We know from the definition of a factorial that 12! = 12 × 11 × 10×...× 3 × 2 × 1. However, it can be quite tedious to work this out by calculating each multiplication step on paper or typing each step into your calculator. 

\-Fortunately, there is a button on your calculator which makes this much easier. To use your calculator to work out the factorial of a number:

* Input the number.
* Press SHIFT on your CASIO or 2ndF on your SHARP calculator.
* Then press x! on your CASIO or n! on your SHARP calculator.
* Finally, press equals to calculate the answer.

\-If we follow these steps for 12!, we get the answer 479 001 600.



###### b. 

\-Expand the factorial notation:

8!/4! = (8×7×6×5×~~4~~×~~3~~×~~2~~×~~1~~)/(~~4~~×~~3~~×~~2~~×~~1~~) =8×7×6×5=RHS



###### c. 

\-Expand the factorial notation:

n!/(n−1)! = (n×~~(n−1)~~×~~(n−2)~~×~~(n−3)~~×...×~~3~~×~~2~~×~~1~~)/~~(n−1)~~×~~(n−2)~~×~~(n−3~~)×...×~~3~~×~~2~~×~~1~~ = n



\-If n= 1,we get 1!/0! .This is a special case. Both 1! and 0! =1, therefore 1!/0! = 1 so our identity still holds.





### QUESTIONS

#### 1\.

Work out the following without using a calculator:

##### a) 

3!



##### b) 

6!



##### c) 

2!3!



##### d) 

8!



##### e) 

6!/3!



##### f) 

6!+4!−3!



##### g) 

(6!−2!)/2!



##### h) 

(2!+3!)/5!



##### i) 

(2!+3!−5!)/(3!−2!)



##### j) 

(3!)^3



##### k) 

(3!×4!)/2!



#### 2\. 

Calculate the following using a calculator:

##### a) 

12!/2!



##### b) 

10!/20!



##### c) 

(10!+12!)/(5!+6!)



##### d) 

5!(2!+3!)



##### e) 

(4!)^2 (3!)^2





#### 3\. 

Show that the following is true:

##### a) 

n!/(n−2)! = n^2−n



##### b)

(n−1)!/n! = 1/n



##### c)

(n−2)!/(n−1)! = 1/(n−1) for n > 1





## Application to counting problems



### EXAMPLES

#### 1 Further arrangement of outcomes without repetition



\-Eight athletes take part in a 400m race. In how many different ways can the first three places be arranged?



##### SOLUTION

\-Eight different athletes can occupy the first 3 places. For the first place, there are 8 different choices. For the second place there are 7 different choices and for the third place there are 6 different choices. Therefore 8 different athletes can occupy the first

three places in:

* 8 × 7 × 6 = 336 ways



#### 2 Arrangement of objects with constraints

\-In how many ways can seven boys of different ages be seated on a bench if:



##### a. 

the youngest boys its next to the oldest boy?



##### b. 

the youngest and the oldest boys must not sit next to each other?





##### SOLUTION

###### a. 

\-This question is a little different to the previous problems of arrangements without repetition. 

\-In this question, we have the constraint that the youngest

boy and the oldest boy must sit together. The easiest way to think about this, is to see each set of objects which have to be together as a single object to arrange.

\-If we let boy = B and let the number subscript indicate order of age,we can view the objects to arrange as follows:



(B1;B7)- 1; (B2)-  2; (B3)- 3; (B4)- 4; (B5)- 5; (B6)- 6



\-If the youngest and oldest boys are treated as a single object, there are six different objects to arrange so there are 6! different arrangements. However, the youngest and oldest boys can be arranged in 2! different ways and still be together:



(B1;B7) or (B7;B1)



\-Therefore there are:

6! × 2! = 1440 ways for the boys to be seated



###### b. 

\-The arrangements where the youngest and oldest must not sit together is the total number of arrangements minus the number of arrangements where the oldest and youngest sit together. 

\-Therefore, there are:

7!−1440 = 3600 ways for the boys to be seated.



### QUESTIONS Number of choices in a row

#### 1\.

How many different possible outcomes are therefor a swimming event with six competitors?



#### 2\.

How many different possible outcomes are therefore the gold (1st), silver (2nd) and bronze (3rd) medals in a swimming event with six competitors?



#### 3\. 

Susan wants to visit her friend sin Pretoria, Johannesburg, Phalaborwa, East London and Port Elizabeth. In how many different ways can the visits be arranged?



#### 4\. 

A headboy, a deputy head boy, a head girl and a deputy head girl must be chosen out of a student council consisting of 18 girls and 18 boys. In how many ways can they be chosen?



#### 5\. 

Twenty different people enter a golf competition. Only the first six of them can win prizes. In how many different ways can the prizes be won?



#### 6\. 

Three letters of the word ’EMPTY’ are arranged in a row. How many different arrangements are possible?



#### 7\. 

Pool balls are numbered from 1 to 15. You have only one set of pool balls. In how many different ways can you arrange:



##### a) 

all 15 balls. Write your answer in scientific notation, rounding off to two decimal places.



##### b) 

four of the 15 balls.



#### 8\. 

The captains of all the sports teams in a school have to stand next to each other for a photograph. The school sports programme offers rugby, cricket, hockey, soccer, netball and tennis.



##### a) 

In how many different orders can they stand in the photograph?



##### b) 

In how many different orders can they stand in the photograph if the rugby captain stands on the extreme left and the cricket captain stands on the extreme right?



##### c) 

In how many different orders can they stand if the rugby captain, netball captain and cricket captain must stand next to each other?



#### 9\.

How many three-digit numbers can be made from the digits 1 to 6 if:



##### a) 

repetition is not allowed?



##### b) 

repetition is allowed?



#### 10\. 

There are two different red books and three different blue books on a shelf.



##### a) 

In how many different ways can these books bearranged?



##### b) 

If you want the red books to be together, in how many different ways can the books bearranged?



##### c) 

If you want all the red books to be together and all the blue books to be together, in how many different ways can the books be arranged?



#### 11\. 

There are two different Mathematics books, three different Natural Sciences books, two different Life Sciences books and four different Accounting books on a shelf. In how many different ways can they be arranged if:



##### a) 

the order does not matter?



##### b) 

all the books of the same subject stand together?



##### c) 

the two Mathematics books stand first?



##### d) 

the Accounting books stand next to each other?





### Examples

#### 1 Arrangement of letters

If you take the word,’OMO’, how many letter arrangements can we make if:

##### a.

we consider the two O’s as different letters?



##### b.

we consider the two O’s as identical letters?



##### SOLUTION

###### a

\-Since we consider the two O’s as different letters, write the first O as O\_1 and the second O\_2.

The different letter arrangements are as follows:

O\_1MO\_2; MO\_1O\_2; O\_1O\_2M;

O\_2MO\_1; MO\_2O\_1; O\_2O\_1M



\-We can see from writing out all the arrangements that there are 6 different ways for the letters to be arranged. This is not practical if there are a large number of letters. Instead, we can work this out more easily using the fundamental counting principle.

\-Using the fundamental counting principle, as there are 3 letters in the word OMO if we treat each O as a separate letter, there are 3! = 6 different arrangements.



###### b 

If we consider the two O’s as identical letters, only 3 arrangements are possible:

OMO MOO OOM



\-We can also work this out using a modified version of the previous identity.

\-We know that if we treat each letter as different, the number of arrangements is 3!. However, when we have duplicate letters, we have to remove the identical arrangements of these letter from our final answer.So we divide by the factorial of the number of times a letter is repeated.

\-In this example, O appears twice so we divide 3! by 2!:

number of arrangements = 3!/2! = 3



#### 2

If you take the word ’BASSOON’, how many letter arrangements can you make if:

##### a. 

repeated letters are treated as different?



##### b. 

repeated letters are treated as identical?



##### c. 

the word starts with an O and repeated letters are treated as identical?



##### d. 

the word starts and ends with the same letter and repeated letters are treated as identical?



##### SOLUTION

###### 1\. 

There are 7 letters in the word ’BASSOON’. If we treat each letter as a different letter, there are 7! = 5040 arrangements.



###### 2\. 

\-If repeated letters are treated as identical characters, there are two S’s and two O’s. This is similar to the previous worked example except now we have more than one letter repeated. When more than one letter is repeated, we have to divide the total number of possible arrangements by the product of the factorials of the number of times each letter is repeated.



\-Number of arrangements = 7!/(2!×2!) = 1260 arrangements



###### 3\. 

If the word starts with an ’O’, there are still 6 letters left of which two are S’s.

Number of arrangements = 6!/2! = 360 arrangements



###### 4\. 

If the word starts and ends with the same letter, there are two possibilities:

* S-----S with the letters in between consisting of ’B’, ’A’, ’O’, ’O’ and ’N’.

Therefore:

Number of arrangements = 5!/2! = 60 arrangements



* O-----Owiththeletters inbetweenconsistingof ’B’,’A’,’S’,’S’and’N’.

Therefore:

Number of arrangements = 5!/2! = 60 arrangements



>This allows us to formulate the following:

* Therefore, the total number of arrangements = 60 + 60 = 120.
* For  a set of n objects, of which n\_1 are the same, n\_2 are the same...,n\_k are the same, the number of arrangements =  n!/(n1!× n2!...nk!)



### QUESTIONS

#### 1

&#x20;You have the word ’EXCELLENT’.

##### a) 

If the repeated letters are regarded as different letters, how many letter arrangements are possible?



##### b) 

If the repeated letters are regarded as identical, how many letter arrangements are possible?



##### c) 

If the first and last letters are identical, how many letter arrangements are there?



##### d)

How many letter arrangements can be made if the arrangement starts with an L?



##### e)

How many letter arrangements are possible if the word ends in a T?



#### 2\. 

You have the word ’ASSESSMENT’.

##### a) 

If the repeated letters are regarded as different letters, how many letter arrangements are possible?



##### b) 

If the repeated letters are regarded as identical, how many letter arrangements are possible?



##### c) 

If the first and last letters are identical, how many letter arrangements are there?



##### d)

How many letter arrangements can be made if the arrangement starts with a vowel?



##### e)

How many letter arrangements are possible if all the S’s are at the beginning of the word?



#### 3\.

On a piano the white keys represent the following notes: C, D, E, F, G, A, B.

How many tunes, seven notes in length, can be composed with these notes if:

##### a) 

a note can be played only once?



##### b) 

the notes can be repeated?



##### c) 

the notes can be repeated and the tune begins and ends with a D?



##### d) 

the tune consists of 3D’s, 2B’s and 2A’s.



#### 4\. 

There are three black beads and four white beads in a row. In how many ways can the beads be arranged if:



##### a) 

same-coloured beads are treated as different beads?



##### b) 

same-coloured beads are treated as identical beads?



#### 5\. 

There are eight balls on a table. Some are white and some are red. The white balls are all identical and the red balls are all identical. The balls are removed one at a time. In how many different orders can the balls be removed if:

##### a) 

seven of the balls are red?



##### b) 

three of the balls are red?



##### c) 

there are four of each colour?



#### 6\.

How many four-digit numbers can be formed with the digits 3, 4, 6 and 7 if:

##### a) 

there can be repetition?



##### b) 

each digit can only be used once?



##### c) 

if the number is odd and repetition is allowed





## Application to probability problems

\-When needing to determine the probability that an even to ccurs, and the total number of arrangements of the sample space, S, and the total number arrangements for the event, E, are very large, the techniques used earlier in this chapter may no longer be practical. 

\-In this case, the probability may be determined using the fundamental counting principle. The probability of the event, E, is the total number of arrangements of the event divided by the total number of arrangements of the sample space or n(E)/n(S) 



### Examples

#### 1

Every client of a certain bank has a personal identification number (PIN) which consists of four randomly chosen digits from 0 to 9.



##### a. 

How many PINs can be made if digits can be repeated?



##### b. 

How many PINs can be made if digits cannot be repeated?



##### c. 

If a PIN is made by selecting four digits at random, and digits can be repeated,

what is the probability that the PIN contains at least one eight?



##### d. 

If a PIN is made by selecting four digits at random, and digits cannot be repeated, what is the probability that the PIN contains at least one eight?



##### SOLUTION

###### a. 

If digits can be repeated: you have 10 digits to choose from and you have to choose four times, therefore the number of possible PINs = 104 = 10 000.



###### b. 

If digits cannot be repeated: you have 10 digits for your first choice, nine for your second, eight for your third and seven for your fourth. Therefore, the number of possible PINs = 10 ×9×8×7 = 5040



###### c. 

\-Let B be the event that at least one eight is chosen. Therefore the complement of B is the event that no eights are chosen.

If no eights are chosen, there are only nine digits to choose from. Therefore, n(not B) = 94 = 6561.

\-The total number of arrangements in the set, as calculated in Question 1, is 10 000. Therefore:

P(B) = 1−P(not B)

= 1− n(not B)/n(S)

= 1− 6561/10 000

= 0,3439



###### d. 

Let B be the event that at least one eight is chosen. Therefore the complement of B, is the event that no eights are chosen.

If no eights are chosen, there are only 9 then 8 then 7 then 6 digits to choose from as we cannot repeat a digit once it is chosen. Therefore,

n(not B) = 9×8×7×6 = 3024

\-The total number of arrangements in the set, as calculated in Question 1, is 10 000. Therefore:

P(B) = 1−P(not B)

1 − n(not B)/n(S)

=1− 3024/10 000

= 0,6976



#### 2

The number plate on a car consists of any 3 letters of the alphabet (excluding the vowels and ’Q’), followed by any 3 digits (0 to 9). For a car chosen at random, what is the probability that the number plate starts with a ’Y’ and ends with an odd digit?



##### SOLUTION

###### Step 1: Identify what events are counted

The number plate starts with a ’Y’, so there is only 1 option for the first letter, and ends with an odd digit, so there are 5 options for the last digit (1; 3; 5; 7; 9).



###### Step 2: Find the number of events

\-Use the counting principle. For the second and third letters, there are 20 possibilities (26 letters in the alphabet, minus 5 vowels and ’Q’). There are 10 possibilities for the first and second digits.

\-Number of events = 1 × 20 × 20 × 10 × 10 × 5 = 200000



###### Step 3: Find the total number of possible number plates

\-Use the counting principle. This time, the first letter and last digit can be anything.

\-Total number of choices = 20 × 20 × 20 × 10 × 10 × 10 = 8000000



###### Step 4: Calculate the probability

\-The probability is the number of out comes in the event, divided by the total number of outcomes in the sample space.

Probability = 200 000/8 000 000 = 1/40 = 0,025

### 

#### 3

Refer to  worked example for the arrangment of letters OMO ofr context. If you take the word, ’BASSOON’ and you randomly rearrange the letters, what is the probability that the word starts and ends with the same letter if repeated letters are treated as identical?



##### SOLUTION

\-If the word starts and ends with the same letter, there are a total number of 120 possible arrangements (from worked example 16) . Let this event = A.

\-The total number of possible arrangements if repeated letters are treated as identical = 1260 (from worked example 16).

\-Therefore, the probability of an arrangement beginning and ending with the same letter

= n(A)/n(S) = 120/1260 = 0,1





### QUESTIONS

#### 1\. 

\-A music group plans a concert tour in SouthAfrica. They will perform in Cape Town, Port Elizabeth, Pretoria, Johannesburg, Bloemfontein, Durban and East London.



##### a) 

\-In how many different orders can they plan their tour if there are no restrictions?



##### b) 

\-In how many different orders can they plan their tour if their tour begins in Cape Town and ends in Durban?



##### c) 

\-If the tour cities are chosen at random, what is the probability that their performances in Cape Town, Port Elizabeth, Durban and East London happen consecutively? Give your answer correct to 3 decimal places.



#### 2\. 

\-A certain restaurant has the following course options available for a three-course set menu:



|STARTERS|MAINS|DESSERTS|
|-|-|-|
|Calamari salad|Fried chicken|Ice cream and chocolate sauce|
|Oysters|Crumbed lamb chops|strawberries and cream|
|Fish in garlic sauce|Mutton Bobotie|Malva pudding with custard |
||Chicken schnitzel|Pears in brandy sauce|
||Chicken nuggets||



##### a)

How many different set menus are possible?



##### b)

What is the probability that a set menu includes a chicken course?



#### 3\. 

Eight different pairs of jeans and 5 different shirts hang on a rail.



##### a) 

In how many different ways can the clothes be arranged on the rail?



##### b) 

In how many ways can the clothing be arranged if all the jeans hang together and all the shirts hang together?



##### c)

What is the probability, correct to three decimal places, of the clothing being arranged on the rail with a shirt a tone end and a pair of jeans at the other?



#### 4\. 

&#x20;A photographer places eight chairs in a row in his studio in order to take a photograph of the debating team. The team consists of three boys and five girls.



##### a) 

In how many ways can the debating team beseated?



##### b) 

What is the probability that a particular boy and a particular girl sit next to each other?



#### 5\. 

If the letters of the word ’COMMITTEE’ are randomly arranged, what is the probability that the letter arrangements start and end with the same letter?



#### 6\. 

Four different Mathematics books, three different Economics books and two different Geography books are arranged on a shelf. What is the probability that all the books of the same subject are arranged next to each other?



#### 7\. 

A number plate is made up of three letters of the alphabet (excluding F and S) followed by three digits from 0 to 9. The numbers and letters can be repeated.



Calculate the probability that a randomly chosen number plate:



##### a) 

starts with the letter D and ends with the digit 3.



##### b) 

has precisely one D.



##### c) 

contains at least one 5.



#### 8\. 

In the 13-digit identification (ID) numbers of South African citizens:

* The first six numbers are the birth date of the person p in YYMMDD format.
* The next four digits indicate gender, with 5000 and above being male and 0001 to 4999 being female.
* The next number is the country ID; 0 is South Africa and 1 is not.
* The second last number used to be a racial identifier but it is now 8 for everybody.
* The last number is a control digit, which verifies the rest of the number.

\-Assume that the control digitis a randomly generated digit from 0 to 9 and ignore the fact that leap years have an extra day.



##### a) 

Calculate the total number of possible ID numbers.



##### b) 

Calculate the probability that a randomly generated ID number is of a South African male born during the 1980s. Write your answer correct to two decimal places.





## QUESTION

### 1\. 

An ATM card has a four-digit PIN. The four digits can be repeated and each of them can be chosen from the digits 0 to 9.



#### a)

What is the total number of possible PINs?



#### b)

What is the probability of guessing the first digit correctly?



#### c)

What is the probability of guessing the second digit correctly?



#### d)  

If your ATM card is stolen, what is the probability, correct to four decimal places, of a thief guessing all four digits correctly on his first guess?



#### e) 

After three in correct PIN attempts, an ATM card is blocked from being used.

If your ATM card is stolen, what is the probability, correct to four decimal places, of a thief blocking the card? Assume the thief enters a different PIN each time.



### 2\. 

The LOTTO rules state the following:

* Six numbers are drawn from the numbers 1 to 49- this is called a ’draw’.
* Numbers are not replaced once drawn, so you cannot have the same number more than once.
* The order of the drawn numbers does not matter.



You decide to buy one LOTTO ticket consisting of 6 numbers.



#### a) 

How many different possible LOTTO draws are there? Write your answer in scientific notation, rounding to two digits after the decimal point.



#### b) 

\-Complete the tree diagram below after the first two LOTTO numbers have been drawn showing the possible outcomes and probabilities of the numbers on your ticket.



>DIAGRAM\[

\-Node

\--Branch 1 top| Correct

\--Branch 2 top| Wrong



#### c) 

What is the probability of getting the first number drawn correctly?



#### d) 

What is the probability of getting the second number drawn correctly if you get the first number correct?



#### e) 

What is the probability of getting the second number drawn correct if you do not get the first number correctly?



#### f) 

What is the probability of getting the second number drawn correct?



#### g) 

What is the probability of getting all 6 LOTTO numbers correct? Write your answer in scientific notation, rounding to two digits after the decimal point.



### 3\. 

The population statistics of South Africa show that 55% of all babies born are female. Calculate the probability that a couple planning to have children will have a boy followed by a girl and then a boy. Assume that each birth is an independent event. Write your answer as a percentage, correct to two decimal places.



### 4\. 

Fezile and Vuzi write a Mathematics test. The probability that Fezile will pass the test is 0,8. The probability that Vuzi will pass the test is 0,75. What is the probability that only one of them will pass the test?



### 5\. 

Landline telephone numbers are 10 digits long. Numbers begin with a zero followed by 9 digits chosen from the digits 0 to 9. Repetitions are allowed.



#### a) 

How many different phone numbers are possible?



#### b) 

The first three digits of a number form an area code. The area code for Cape Town is 021. How many different phone numbers are available in the Cape Town area?



#### c) 

What is the probability of the second digit being an even number?



#### d) 

Ignoring the first digit, what is the probability of a phone number consisting of only odd digits? Write your answer correct to three decimal places.



### 6\. 

Take the word ’POSSIBILITY’.

#### a)

&#x20;In how many way can the letters be arranged if repeated letters are considered identical?



#### b) 

Whatis the probability that a randomly generated arrangement of the letters will begin with three I’s? Write your answer as a fraction.



### 7\. 

\-The code to a safe consists of 10 digits chosen from the digits 0 to 9. None of the digits are repeated. Determine the probability of a code where the first digit is odd and none of the first three digits may be a zero. Write your answer as a percentage, correct to two decimal places.



### 8\. 

Four different red books and three different blue books are to be arranged on a shelf. What is the probability that all the red books and all the blue books stand together on the shelf?



### 9\. 

The probability that Thandiswa will go dancing on a Saturday night (event D) is 0,6 and the probability that she will go watch a movie is 0,3 (event M). Determine the probability that she will:



#### a) 

go dancing and watch a movie if D and M are independent.



#### b) 

go dancing or watch a movie if D and M are mutually exclusive.



#### c) 

go dancing and watch a movie if P(D or M) = 0,7.



#### d)

not go dancing or go to a movie if P(D and M) = 0,8.



### 10\. 

Three boys and four girls sit in a row.

#### a) 

In how many ways can they sit in the row?



#### b) 

What is the probability that they sit in alternating gender positions?



### 11\. 

The number plate on a car consists of any 3 letters of the alphabet (excluding the vowels, J and Q), followed by any 3 digits from 0 to 9. For a car chosen at random, what is the probability that the number plate starts with a Y and ends with an odd digit? Write your answer as a fraction.



### 12\. 

There are four black balls and y yellow balls in a bag. Thandi takes out a ball, notes its colour and then puts it back in the bag. She then takes out another ball and also notes its colour. If the probability that both balls have the same colouris 5/8 , determine the value of y.



### 13\. 

A rare kidney disease affects only 1 in 1000 people and the test for this disease has a 99% accuracy rate.



#### a) 

Draw a two-way contingency table showing the results if 100 000 of the general population are tested.



#### b) 

Calculate the probability that a person who tests positive for this rare kidney disease is sick with the disease, correct to two decimal places.

