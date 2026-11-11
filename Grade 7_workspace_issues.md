# General

\-All of the point may refer to a single archetype, but the issues may apply across the board, so dont just fixe for one archetype fixe across the board.

\-is there a simulearn for each archetype?

\-MCQ memo states the whole answer without the letter option and sometimes the explanation which is good, but order of priority is weird. I think it should start with the correct letter option alongside  the answer associated with the letter, then the explanation.

\-Diagrams should be quality, medical textbook grade illustrations unless simple lines and shapes are the optimal. You are connected via blender and so should do good diagrams

\-i think multi part questions should be arranged like the following

a. blah blah blah

b. blah

c. blah

letters as priority, then roman numerals. This will make it easy when in the teacher mode test and exams with multiple questions in one document are being made, where questions have to be numbered Question 1, 2, 3 etc. As it is parts are numbered and that will cause confusion.

\-Also the answer card for a multi part question should be further divided into those parts so that part a or i has its on space for typing. Then in teacher mode for printable purposes, the answer section dimensions should be changeable by dragging on the corner, because the teacher will know better how much space a student needs to write in. does that make sense? 

\-Pay attention to data/information booklets that students are given as part of the exam, this will inform which visual aids and support information need to be available alongside topics.



# Grade 7

## Ems

1. Too few architypes for Accounting principles and other topics: do counts, some in the single digits.
2. Seems to use Imran, Chloe  and Mitchel Plains a lot, does it iterate through the names.py like accounting?
3. Need to look at each topic in turn, and review whether the number of archetypes covers the breadth of the curriculum requirements and whether tweaks in the entropy are required
4. There is a topic called business: epidemics impact? Topic names need to be clear to the user.
5. There are no diagram questions like e.g an economic cycle diagram related somehow in a question.
6. Questions requiring calculations seem to appear as mcq. Does the architype entropy render it as a non mcq where working inputs are marked for procedure?
7. We need to explore how semantic/essay answers are marked, i need playwright test that will show how various levels of semantic answers to a question are marked against the sample/expected answers/memo. If this system is weak we may need to introduce an llm to brigde the gap reviewing the user's answer against the expected answers and awarding marks. The prompt to the llm and its response should be guardrailed for token efficiency. The user doesn't communicate directly with the llm. The system recognises a question requiring semantic answer, relays questions, user answer and memo/scheme to llm.
8. I think we need to realise that ems branches out to accounting and business studies at fet level. We may have limited ems curriculum source of truth docs, but surveying BS textbook and diluting it using the ems syllabus docs so that its not beyond scope for grade 7-9 may improve our non-accounting ems offering. Does this make sense?
9. There are questions like, 'Studying economic challenges in Mitchells Plain, which of the following is a major cause of poverty in South Africa?/ Comparing mitchels plains to outlying rural communities, rural South Africa often face more challenges becuase:' No case study context is given, are users supposed to go to the browser and google mitchells plain? We may need to have hard coded economic case study for 2 places in each of the 10 provinces, 1 rural , 1 urban. Maybe you can the use this in  context to some questions in ems and business studies for such questions and others. Maybe you can access the internet to get news articles, opinion pieces and aggregate them to form such case studies. What do you think?
10. When a semantic/ calc questions have parts, maybe there should be input space under each part, to make it easier for the system to sort answers when they are used in the llm prompt.
11. Evaluate what prompts the showing of the keypad
12. Start from whats in the syllabus of gr7 EMS, then see if all that's required in it is covered across the topics implemented.
13. I didn't encounter any questions with journals, any type of source document, ledger etc. We need to review that. Are they totally missing in gr7 ems?
14. Are all topics covered: 1-The history of money; 2-Needs and wants; 3-Goods and services; 4-Businesses; 5-Accounting concepts; 6-Income and expenses; 7-Budgets; 8-The entrepreneur; 9-Starting a business; 10-Entrepreneur's Day; 11-Inequality and poverty and the term 4 topics?



## Maths

1. Is explaining the balance of an algebraic expression a kind of question that appears in curriculum docs auto e.g for a question : 'an algebraic equation represents a balance scale where the left hand side (LHS) must exactly balance the right hand side (RHS: 1. Explain what value of x makes this  true mathematical sentence; 2. Verify your solution by showing that LHS = RHS). I personally like the question, because it goes deeper than 'calculate the value of x'. But i am worried about the use of the word 'mass' in the memorandum. Is that a syllabus or textbook obtained word found in curriculum docs? I also worried because to me it seems a different explanation can be proffered or users just are not deft enough in English to explain it and so they will just work it out and also answer the second part by working it out, which makes the question seem rendundant, like it could have been just 1 question. Does this make sense?
2. A question like 'Solve the linear equation by inspection (trial and improvement or mental arithmetic).. should have in the memorandum, the kind of procedural thought processes users need to engage in to come up with the answer for each of the methods/approaches. Also what does \*\*m=14\*\* in the memo mean is that a latex leak?
3. w/6 = 3 . Can we have simulearn visualization showing the actual steps taken to solve problems, even adding arrows to show movement of numbers where necessary. The simulearn should be pausible and reversible so that a user can take aslong as they need to understand. We may need to actually show how those steps in the memo are actually done in an actual calculation.
4. Lets review the difference between algebraic equation 1 and 2 and ensure we are sticking to the guardrails
5. 7K -9 =26.. If the memo says add 9 on both sides, your steps then need to involve 7K-9 + 9 = 2 + 9, dont just jump to 7K = 26 + 9, But the marker should be able to mark the steps by approving that the LHS na RHS are balancing since users are going to approach this differently there is no one set of steps that have to be followed exactly. Also if the memo says multiply or divide both sides, then that step of multiplying or dividing both side needs to be shown.  Do you understand what i mean
6. The answer area should not have  just one input section, but an add new line option so that users can input each step in their working in a new line. Just having a single input space for the answer does quite cut it, if our principle is marking the working aswell. Do you understand?
7. Are questions like state the coefficient of x^2 the kind of questions asked of grade 7s in mathematics or they are only limited to the diagnostic test. whilethese  kind of questions may be important for diagnosis, If such questions dont appear in curriculum docs, i dont want them in scaffold/practice and exams because they would not be the type that students get in real life.
8. Questions like 'Describe the following algebraic expression in clear English words: 4y - 8. Are they limited to diagnosis or they are given in exams. Please check that curriculum docs has such architypes, if not, they should not be in practice and exam.
9. Questions like 'How many terms are in this expression/ classify this expression as a monomial, binomial or trinomial and justify your answer, should be reviwed to see if the architype is present in curriculum docs, if not.. limit them to diagnostic test. Furthermore, how do you mark such semantic answers deterministically
10. A question like 'Write down an algebraic expression for the following word description:  the difference between a number y and 7, divided by 6; is ambiguous, is it y-7 or 7-y. Additionally there is latex leak or unnecessary double asterik (\*\*) symbols.
11. I think we need simulearn or visualization tools that bridge the gap between textbook paragraphs and questions, i.e explaining things like how a stem and leaf is plotted, not with paragraphs but with visuals.
12. Some tables given in the collecting and organising data dont align the name of the column and the entries in the column, everything in the column should be centred.
13. In question where there is a table with tally marks, you cant be saying '13' you need to be able to do the 4 vertical strokes and 1 diagonal thing/symbol, you cant have tally mark 13, then frequency 13, it doesn't make sense and doesn't teach students much.
14. In construction of geometric figures, there is an architype like 'Two parallel lines are cut by a transversal line. The alternate interior angles are given as 4z + 16 and 100 . Calculate the value of z and state the geometric reason'. Such questions are missing geometric diagrams. The memorandum step by step procedures has abbreviations like SS\[M], SS\[A], (alt. ||) where students cant even get explanations for. Review needed.
15. There is a question like 'Angles on a straight-line add up to 180. If one angle is 104, calculate the size of the adjacent angle x.' This question is italicized and there are no spaces between words.. Fix needed.
16. You need to review all the questions in construction of geometric figures, most need to have a diagram, but is missing
17. I need to understand how you differentiate between adding from left to right and using bomdas.
18. Questions like calculating the cube root of 216 need memo where what should happen in the mind/ mental processes need to be verbalised, to be of benefit to students. do you understand what im trying to say?
19. In the fractions topic answers like 13/10 should have allowance for mixed number format like 1 3/10
20. Does the keypad allow users to insert/type in  fractions? i think it should also allow for mixed number
21. Tables in Functions and relationships 1 are such that the column entries are right shifted wrt the column headers. This is bad aesthetics given that the tables do not have lines. There has to be centred. I like the lack of vertical table lines but it means the column entries need to be aligned.
22. We need to ensure that the textbook/syllabus docs difference between Functions and relationships 1 , 2 and 3 is reflected in the app
23. There is a question: 'In a direct proportion table, 1 notebook costs R40.; 1. What is the constant rate of cost per notebook; 2. Complete the table to determine the cost of 5 notebooks in Rands.' The problem is that no table is given for users to fill in.
24. A question like 'A straight line graph contains the points (1, 5); (2, 7), and (3, 9). Which of the following equations correctly matches this graph? A. y = 2x + 3; B. y = 2x - 3; C. y = 3x + 3. The problem is that the question doesn't act like an MCQ, non of the options are selectable, the architype answer requires the rewriting of the correct option.
25. Does the keypad have a 'delta' symbol and other Greek symbols that are standards in high school maths and science input?
26. We need visualization tools for geometry e.g for the visualization of chords/arc/radius/diameter/tangent/ types of triangles/ types of quadrilaterals etc. of course the tool needs to be related to the grade and topic or even the particular question.. no need for trapezium when you are dealing with a question of circles in grade 7.
27. A question in geometry of 2D shapes: 'Refer to the diagram of quadrilateral PQRS, where three interior angles are given as: P = 90, Q = 102, and R = 81. The fourth interior angle is S = w.' The problem is that the diagram is located in the answer section. The diagram necessary for the context of the question should be in the question card. And this problem seems to apply to all questions with 'Refer to the diagram..'
28. In geometry of 3d objects, the geometric nets visualizations seem to be there opening alongside the question. a)we need to decide when visual aids/tools should become available. The point of a question is to determine what a student knows, so providing a visual aid from the get go, might not fulfil our purposes,
29. I do not particularly like the color schemes and aesthetics of the geometric nets visualization aids, i am using screenshots from before atlas of physics based changes to the code base. Have they been improved or left alone by that implementation. do students need the Euler's check based on the syllabus for grade 7.
30. The diagrams in geometry of 3d objects are also in the answer card section
31. The visualization aid when activated should be about what's in the question, not general aspects of the topic
32. In geometry of straight lines and graph paper types there are questions like: 'consider the opposite long edges of an Olympic swimming pool, where two straight lane  ropes remain exactly 10 cm apart at every point along their length/ In architectural construction, the vertical goalpost and the horizontal crossbar on a soccer field meet at a single intersection point/ A geometric shape drawn on a 1 cm \* 1 cm square grid completely encloses a rectangle measuring 7 squares in length by 3 squares in width.' These questions have real world context or objects on a graph paper but no diagrammatic depiction of the objects. I dont know what the limitations for trying to implement diagrams to them is. Does it limit entropy??
33. I think graph paper types questions need diagrams
34. In the graphs topic for questions like : 'A 24 hour temperature graph for a winter day in Johannesburg shows:- the lowest point on the curve at 5am, the highest peak on the curve at 2pm'. Is there a version/variety of this question that actually shows the graphs with the points in question?
35. In the graphs topic, i think its fine to have questions where graphs are described instead of drawn, but that shouldn't be the backbone. There should be questions where the context is derived from a graph diagram , after all the topic is graphs.
36. i think some topics such as graphs, integers may need more architypes, check the appropriate textbooks, exam and syllabus in curriculum docs auto.
37. is there a usefule number line or some such visualization tool design that you can think of that can aid users when it comes to adding/subtracting integers?
38. The topic numeric and geometric patterns has a question like : ' A decorative tile patten grows symmetrically in four directions from \\a central tile..' dont such questions require diagrams?
39. We need to review the patterns section of numeric and geometric patterns to determine if it cant be improved by designing archetypes with diagram while keeping within the scope of the syllabus.
40. Are there visual aids for geometric patterns that can be designed?
41. The Perimeter and area of 2D shapes topic has descriptions of diagrams, but no diagrams
42. The following architype in probability: 'An 8-sector circular spinner is divided into eight equal sections numbered 1 to 8' . Cant a diagram be set up?
43. in the topic relationships between variables might have an incomplete architype: 'Consider the following situation: Situation: A learner bakes biscuits using a fixed recipe in varying batch quantities. Between the two quantities involved (the amount of baking powder required per 12 biscuits (1 teaspoon) and the total number of biscuits baked): 1. Identify the constant quantity, 2. Identify the variable quantity and explain why it is classified as variable.
44. Represent data topic has a question about bar graph, but no graph diagram. we need to review the need of diagrams
45. review the need of diagram such as frequency polygons, bar graph, double bar graph, pie charts
46. It may be difficult to ask questions where users are required to draw graphs, maybe the use of mcq, where the choices are graphs can come in handy. However we may need questions that aks about drawing graphs and other diagrams reserved for the printable tests and exams that teachers print for students in class.. do you get my drift??
47. Questions involving prisms don't seem to have diagrams
48. Wouldn't it be wise to have vertical addition/subtraction questions for the decimal notation for fractions topic
49. Please check the curriculum docs auto for questions or exam papers that expressly prohibit use of calculators, we need to know whether users ata grade 7 are using calculators for each archetype or not.
50. We need to review transformation geometry for the need of diagrams which are lacking
51. I am worried about how students can do long division in the working with whole numbers topic we need to mimic how they would do it on actual paper because thats what the app should be helping learners do. Just because we are on screen shouldn't allow us to offer something that will handicap them during exams. Can the long division symbol on the keypad be typed on in a way that mimics how they solve on physical paper??
52. There are questions that might not have working procedure but the mental processes to find a solution are obviously there. in such case the memo should absolutely record what should be happening in the learners brain in order to solve the problem.



## NATURAL SCIENCE

1. is it possible to design a litmus paper, universal indicator visual tool for questions that may need it
2. A question like 'Acid + Base -> \[?] + \[?]' raises questions about how we handle imput of answers. Some of these questions are good but where is the user supposed to input their answer in a way that a deterministic system will process it. You need to think about all of this.
3. In the acids and bases 3 part question, a apart questions 'Suggest a suitable household or agricultural remedy to treat this condition' In bold it leaks the answer (dilute vinegar or lemon juice (mild household acid))
4. Based on the text book lets review if we can increase the architypes in acids and bases
5. Review whether some of the architypes in biodiversity/energy transfer to surroundings make sense without diagrams
6. Under Energy transfer to surrounding thee is a question about Sankey diagrams but the diagram is not shown.
7. The mcq question in heat energy transfer doesnt seem to show the which answer is correct in its memo: 'A coper stirring rod submerged in a beaker of boiling water in a science lab quickly conducts heat from the submerged tip to the handle. How does heat transfer through the metal by conduction.  Check that all architypes have the correct answer in the memo.
8. Probably need a SOTA visualisation tool for a vaccum flask, conduction, convection, radiation
9. need quality diagrams for the telescopes named in the syllabus/textbooks
10. At this point the Square kilometre array has been developed and running, please check you data and update questions that seem to be stuck on before development.
11. Need diagrams for questions relating to energy transformations
12. Visualisation related to states of matter changes/ Relationships of the moon to the earth/tides/ relationship of the sun to the earth
13. Diagrams for questions and visualisations for separating mixtures topic
14. review the simple distillation apparatus master diagram.. it seems that it is reused without modifying for each question.... the letter labels sometimes are not needed but are present. I think this is the configuration of all if not most of the diagram so far implemented.. we need to be professional. Letters should point to actual parts of a diagram and be present only if the question requires it. This means the diagram should be created without any labels, then svg layers should be question dependent if i understand correctly how the diagram system works. Some questions have actual annotations not letters. so we need to apply what each question requires. . Eg this question is confused: "C:\\Users\\princ\\fundile-tlassistant-vite\\reports\\full\_archetype\_audit\\shots\\gr7\_natural\_sciences\_separating\_mixtures\_thermal\_separation\_principle\_memo\_full.png"
15. Diagrams for pollinations and other aspects of reproduction other than the human organs/ flowers/ visualisation and diagrams for seed dispersal
16. Diagrams for sources of energy e.g hydroelectric/ coal-fired thermal generation. Parts should be based on what the syllabus and textbook expects learners to know
17. Diagrams and visualisations for biosphere topic
18. Periodic table visualization
19. Review the variatio topic and see if it can be expanded form the textbook extractions in curriculum docs auto

