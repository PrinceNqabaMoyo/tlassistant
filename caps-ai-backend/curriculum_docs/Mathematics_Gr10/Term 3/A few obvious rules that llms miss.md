# A few obvious rules that llms somehow miss



## 1

When ever I use '^' as to mean exponent/power, that's a limitation of the word processor I am using, ensure that all exponents/powers throught the app are subscripts



### 2

Any constant should be italised



## 3

The use of / to mean  division is a limitation of the weord processor which cant render fractions properly. Render them appropriately in app



## 4

Do the libraries that have been installed have a way of rendering the long division sign? lower grade math has long division component.



## 5

The use of '\_' to mean subscript is a limitation of the word processor, ensure all subscripts are rendered properly



## 6

The use of csv or ';' as separators in a table is a limitation of the word processor, ensure rendering of tables appropriately.



## 7

Throughtout the curriculum docs the statement DIAGRAM\[..] should immediately elicit consideration for the construction of a diagram ...



## 8

{n}√x : means the nth root of x



## 9

\-llm should think deeply about how we code for users to be able to construct tables and even shape and render in the most instructionally potent and beneficial way. Do we use pick and drop or make them select a scale, plot points and then have auto-smooth line connection?



## 10

\-llm should also think about the best and most instructionally potent and beneficial way to implement Interactives for graphs and geometric shapes



## 11

Brackets (smooth) are usually used for clarity due to the limitations of the editor used. Do not render brackets where its not necessary since you will be able to render fractions, exponents, subscripts and others properly.



## 12

\-I need you to come up with a marking scheme. It should be editable for users on teacher mode. The editability should be human readable and doable at the same time effective changes that the code can ingest.

\-Maybe for accounting tables, if a teacher has asked you to generated questions for a test or exam you show them the answer with clickable and editables that update the marking scheme for that user.

\-There should be 1 mark tick, half a mark tick in box, and the ability to place a mark on single value in a working. Or for semantic answers the ability to bracket/highlight marking points. When a user does this the system can then ask them if they want to save this as worth a mark.

\-I am open to discuss better suggestions if you have them



## 13

\-In accounting and perhaps in EMS aswell curriculum documents questions come in  a mix of ways in which names are used. Some time a name may appear as Initial then full stop then surname, or Initial without the dot then surname, or full name and surname or any other variation.

\-Perhaps we need a single way to represent them or a way for the sytem to be agile enough to recognise the variations





## 14

The architypes are taken from past exam papers. Unfortunately the English especially in accounting is ambiguous at best and of little sense at worst especially in the information sections. Try your best to make sense of it and interpret correctly so generated questions are sensible.



## 15

In a multi-step calculation, user may do some operations implicitly (especially basic additions) while some may include all elementary values and operations. Ensure your marking scheme reasonably takes this into account.



## 16

In comments of ratios like acid test and current ratio changes is it reasonable to say for instance if the ratio changed from 2:1 to 1,2 : 1 that it changed by 0,8 : 1. Is this mathematically sound way of stating this?



## 17

I think for some stages in the adaptive progression for accounting ems or even maths you may want to include questions that test the procedural understanding of the user. Before they get questions that require them to fill in the table they maybe should get the same kind of questions but asking things like how do you get the value for cell x, or arrange these steps in the right order for how to answer this questions .



## 18

As a corollary for point 17. for calculation requiring questions, before the user progresses to having to do full questions they maybe should get questions that have the worked out solution but missing values along the steps, and user are required to pick and drop or type in. This would be a good diagnostic step.



## 19

Some questions require comments and semantic answers. They are not the curriculum docs sometimes gives these as point form. However users may be writing semantic answers sometimes as a paragraph and sometimes in point form. The answer marking tool should be able to take care of that without glitches.



## 20

I want to know if the code can handle hundreds or thousand of people generating questions at the same time, different subjects, different topics, different grades or it will crash?





## 21

Look at the following question:

\[Calculate the Bad debts to be written off during April 20.2 (4 marks)



\-Answer

Credit sales: February 140 400

Bad debts in April: 5% × 140 400 = 7 020]

\-A user can provide the answer just like above or can simply just do a calculation or even arrange the answer differently and still be correct. e.g



\[Bad debts = 5% × February Credit sales

= 5/100 × 140 400

= 7 020]



\-Thats why i think for calculations we need a special way of being able to handle the variation in procedures because in mathematical processes there are many ways of skinning a cat.

\-Variations in order of operations.

\-This makes deterministic marking difficult.

\-Perhaps all marking should therefore be routed via an llm.

\-The llm receives the deterministically produced memo alongside the user input and allocates marks.

\-The above would apply to tests, quizzes, exams and class work instatiated by a teacher

\-For the personal study adaptive progression, maybe we dont have to apply an llm step because that will be costly. We just evaluate the answer, unless there is truly a way to design a system that evaluates the different ways calculation steps can be arranged.

\-Maybe we should have a user self marking package such that the standard package only generates the question and then deterministically provides a memo, but does not get into the weeds of trying to mark procedure, just says whether the final answer is correct or not and shows the deterministic derivation and the user decides if they have procedure marks. I dont know!!



## 22

\-For questions that require users to fill in table types in which part of the table may come already pre filled, ensure that the prefilled cells make sense and the unfilled cells can rightly be deduced for the totality of the information provided.

\-In cases where the row label is unfilled, ensure that if there is no specific rule for ordering the rows then there is allowance for various configurations,

\-e.g the cash budget in grade 11 has a receipts section and a payments section, its standard to have the receipt section above the payment section but is it standard that within the receipt section interest on fixed deposit should be above rent income? or that within the payments section Loan repayment be above Interest on loan?

