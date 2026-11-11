before looking at table, few general rules

1. Go through each question 1 step at a time and fix latex issues, see whether the level of question matches the curriculum docs auto and grade level and ensufre diagram quality is ideal
2. Latex symbols should not leak into user ui
3. Annotation line should never cross
4. Watch out for superimposed annotation text
5. Font color of annotations should be such that it pops out and doe not blend into the drawing
6. The expected answer should align with the marking points, not have something in marking points thats not in the expected answer
7. The questions with 3D shapes, do they need both net and 3D at once, this needs to be done thoroughly
8. check that the distractors in annotated diagrams are annotating actual parts not between parts
9. just because a question has a digram, does not automatically mean its asking to name annotated part A, B, C or D. You have technical maths and maths literacy questions that are not mathematical because you seem to have concluded that wherever a diagram exist, the question is about annotation. You need to ground your questions on curriculum docs auto, if the question used a diagram, learn how that question used a diagram, some diagrms are just information to be used in a calculation or answr
10. What is the difference between questions that use the same diagram across grades, surely while the diagrams are the same there should be deifferences in focus or even depth
11. I am looking at a lot of math sample answers without actual working procedures, how will the procedure tracker work if there are no sample procedures?
12. Error found: 

Download the React DevTools for a better development experience: https://react.dev/link/react-devtools

dashboard:1 <meta name="apple-mobile-web-app-capable" content="yes"> is deprecated. Please include <meta name="mobile-web-app-capable" content="yes">

2AdminView.jsx:17 \[AdminView] Current view state: dashboard

AdminView.jsx:26 \[AdminView] Selecting new view: archetypeVetting

AdminView.jsx:17 \[AdminView] Current view state: archetypeVetting

firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel?gsessionid=yS1zR-HZTWW4PO686ZRn70j1EBPrKvAzYmlT2zz-GtSuj1vTjqyrOg\&VER=8\&database=projects%2Fcaps-ai-math-assistant-app%2Fdatabases%2F(default)\&RID=rpc\&SID=GV1CNgoH8MQkaefUlX4iZA\&AID=0\&CI=0\&TYPE=xmlhttp\&zx=zhpbvsoisxc1\&t=1:1  Failed to load resource: net::ERR\_QUIC\_PROTOCOL\_ERROR.QUIC\_TOO\_MANY\_RTOS

react-dom\_client.js?v=aacecd33:4503 Uncaught Error: Rendered fewer hooks than expected. This may be caused by an accidental early return statement.

&#x20;   at finishRenderingHooks (react-dom\_client.js?v=aacecd33:4503:17)

&#x20;   at renderWithHooks (react-dom\_client.js?v=aacecd33:4481:9)

&#x20;   at updateFunctionComponent (react-dom\_client.js?v=aacecd33:6873:21)

&#x20;   at beginWork (react-dom\_client.js?v=aacecd33:7908:20)

&#x20;   at runWithFiberInDEV (react-dom\_client.js?v=aacecd33:1739:72)

&#x20;   at performUnitOfWork (react-dom\_client.js?v=aacecd33:11122:98)

&#x20;   at workLoopSync (react-dom\_client.js?v=aacecd33:10982:43)

&#x20;   at renderRootSync (react-dom\_client.js?v=aacecd33:10965:13)

&#x20;   at performWorkOnRoot (react-dom\_client.js?v=aacecd33:10613:46)

&#x20;   at performWorkOnRootViaSchedulerTask (react-dom\_client.js?v=aacecd33:11877:9)

react-dom\_client.js?v=aacecd33:6483 An error occurred in the <FunctionGraph> component.



Consider adding an error boundary to your tree to customize error handling behavior.

Visit https://react.dev/link/error-boundaries to learn more about error boundaries.



defaultOnUncaughtError @ react-dom\_client.js?v=aacecd33:6483



11\. 

|grade|subject|diagram|issues found||
|-|-|-|-|-|
|7|NS|Liebig simple distillation|i dont like the double start on either side of D:  'callout \*\*D\*\*'||
|7|NS|Solar system orbits|\*Diagram quality could be improved, <br />\*planets look incomplete, planets do not look like the actual planets, accuracy may be better, <br />\*I dont like annotation lines crossing each other<br />-I dont like  'callout \*\*C\*\*'||
|7|math|cylinder\_net|a) The first part questions ask for geometric shapes that make up the cylinder 2D net and  at the same time give the actual surface net drawing, <br />b) The text editing leaks things like '(use $\\pi \\approx 3,14$).' and '($A$)'||
|7|math|cube\_net|1) Leak of things like '\*\*6 congruent squares\*\*', 2) The question seems like it should read 'A learner cuts out a 2D geometric net composed of 6 congruent squares as shown in the diagram below', then only the net diagram should appear, not the cube itself as it gives away the answer<br />3)The mark for 'Eliminate inconsistent 3D geometric polyhedra'' is given but there is no statement in the expected answer showing the eleimination of said inconsistent polyhedra. 4) Leaking latex '$$\\therefore \\text{Correct Answer is } \\mathbf{C}:\~Cube$$'||
|7|math|triangular\_prism\_net|1) For all questions involving the nets, you need to decide whether the shape itself, its net diagram or both are actually needed as part of the question. In many cases they are both available and giving away answers.<br />2) Again, lots of latex leaking||
|7|math|triangle\_interior\_angles|1) Leaking latex 2) Diagram not visually plausible, looks equilateral but angles say otherwise, 3) why is it tagged 'geogebra', i just wanted you to look at the edutech web site 'geogebra' so we can bring our diagrams to the same quality.||
|7|math|quadrilateral\_interior\_angles|1) Latex leaking||
|8|natural science|planetary heliocentric orbits and asteroid belts|1) quality of diagram not satisfactory 2) Latex leaking||
|8|natural science|particle model|1) the diagram seems to be track 2 drawing instead of the textbook quality, cant we enhance this? 2) the question is poor, ambiguosity isn't professional'<br />1. Identify the apparatus component or structural region labeled with callout \*\*C\*\*.<br />2. Explain the scientific function or physical principle of this component in the investigation.'||
|8|math|geometric dot array pattern \& Nth-term derivation|1) question refers to tiles when its rendering dots 2) The sample answer and marking points dont show working, the whole point is to show actual working/procedure wherever needed cant just give the final answer!!!||
|8|math|cartesian\_point|1) latex leak 2)the coordinates are actually shown on point P in the diagram, are users supposed to deduce it or spot it? 3) Procedure i marking points or expected answers should be actual things that a user has to do.||
|8|math|solid\_3D; Ployhedra \&Euler|1) Latex leak 2)||
|9|natural science|heart chamber, gross heart chamber anatomy|1)No consistency in the veins and arteries into and out of the textbook, blood flow and exam versions 2) only 1 of these should be used in a pariticulary question, not availing all 3.||
|9|natural science|heart vessels|||
|9|natural science|alveolus diffusion|1) There should be a color gradient between red cells yet to reach the alvelus and take up oxygen and those that haven't, eg. make those with oxygen red and those without blue 2) Arent arrows for oxygen\\ amd carbon dioxide needed<br />3) Annotation lines overlap, not goo||
|9|natural science|digestive tract|||
|9|natural science|male reproductive|1) the C annotation positioning is off, its not on the urethra 2) need to ensure annotations are on the exact place they are pointing to.||
|9|natural science|female reproductive|||
|9|natural science|plant cell|1) position A is ambiguous 2) annotation lines crossing||
|9|natural science|animal cell|1) annotation line for A and D are overlayed||
|9|natural science|Earth strata, concentric planetary strata|2) Diagram quality is shit, needs to be enhance to the anatomy quality||
|9|natural scinece|supply\_demand: market equilibrium prce|1) Review quality of question||
|10|life sciences|heart anatomy|1) the annotation on tendinous cords and semilunar valaves arr not exactly on the actual structures||
|10|life sciences|heart cardiac cycle: 3-phase cardiac cycle|1) what are the dashed lines for 2)the sinoatrial node  label lies on top of he  semi luna valve label 3) annotation lines are unclear and annotations are squashed together 4) Atrioventricular valves annotation lines are not on point ||
|10|life sciences|heart pacemaker- electrical conduction system|the diagram labelling needs work||
|10|life sciences|mitosis stages|annotations A nad D are on top of each other||
|10|life sciences|plant cell ultrastructure - plant cell eukaryote|annotation line are crossing each other 2) The annotations are not accurately on the intended organelles||
|10|life sciences|animal cell ultra structure|||
|10|life sciences|leaf tissue: dicotyledonous leaf transverse|annotation  for D is pointing between parts not at a a single clear part?!!||
|10|physical science|bohr electron energy shell|2 annotations are pointing at electrons, the answer says its pointing at an enegy shell, id rather it point to the concentric circle and not electron if it wants to say energy shell. 2) The annotation of the nuclus are all pointing to the red parts when i assume it wanted to point to neutrons and protons different colors. Besides there are no standard color differences for protons and neutron, so the diagram/question would need tweaking if it entropies to ask about protons and neutrons||
|10|technical mathematics|Pascal Hydraulic Press, Meshed Gear Trains \& Belt Pulley Drives|1) the quality of the diagram needs to be upgraded to anatomic textbook quality<br />2) not all diagram questions are about asking what par A, B, C or D represent. this question is technical mathematics...you need to ground your questions on curriculum docs auto, then create a diagram if necessary. you seem||
|10|Mathematical literacy|Floor\_packaging\_plan: architectural floor plan|are you sure ML asks questions where users just name parts of a diagram in grade 10???||
|10|Technical mathematics|RADIAN SECTOR: radian angle, circular sector arc length|1) the question leaks latex<br />2)the diagram has an angle labelled 120 (2{,}09 rad): what the fuck is that?<br />3) the commas seem to be curly bracketed||
|10|Mathematical literacy|box and whisker, five number summary|latex leak||
|11|Life sciences|alveolus histology: alveolar epithelial ultrastructure|1) annotation lines cross 2) no oxygen /carbon dioxide transfer arrows 3) latex leak||
|11|Life sciences|digestive glands: gastrointestinal sphincters..|the question asked about a liver, is that withing the scope of the topic or just taken from other grades||
|11|Life sciences|Villus absorption: villus histological ultrastructure|seems to not change from grade to grade||
|11|Life science|Nephron tubule: Nephron microstructure|is there a difference from grade to grade on this diagram||
|11|Life science|leaf photosynthesis adaptations: leaf structural adaptations..|1) D is pointing between parts 2) does depth increase from grade to grade||
|11|Physical science|Chemical bonding lewis dot structures|1)in chemistry especially at grade 11 quetions like 'identify component indicated by callout D' are not likely. 2) im not sure that is a standard way to represent delocalised electrons as D ||
|11|Physical science|pulley incline: connected two-body system on fiction|1) at this grade questions are not about labelling parts of a pulley, instead there a forces or masses or something, please anchor questions on curriculum docs auto 2) Does the diagram descriptors have the detail of forces and masess,becuase i dont understand why the question generated are so lame.||
|11|Maths|Ogive: Cumulative S-curve|Latex leaks||
|11|Maths|Finance timeline|1) Latex leaks <br />2) Its difficult to tell which 'T' the information box is refering to because there are so many. It would be helpful if The 'TX' is also put into the information box||
|12|Life sciences|Eye Accomodatio: Eye sagittal anatomy, refraction..|1) D and A  annotation lines are crossing. 2) The annotation lines need to be a color that doesn't get swallowed up in the diagram color scheme. 3) is there depth increase from grade to grade||
|12|Life sciences|Ear hearing balance: Ear cross section|1) The question about the physiological pathway of sound transmission the diagram has letter annotations when its not a labelling question.||
|12|Life sciences|Endocrine glands location|1) Question about homeostatic response, does not neeed abcd annotations. 2)cant the diagrams in some cases just have the actual labels when its not about which part is which.||
|12|Life sciences|Male spermatogenesis|Does question depth ever increase from grade to grade or just shift to asking about other parts.||
|12|Life science|Female ovarian cycle: ovarian follicle|1) Does the question depth increase form grade to grade||
|12|Life sciences|Meiosis crossing over|1) Can the digram be improved? 2) Does the question depth increase from grade to grade||
|12|Physical science|Titration endpoint|Is there a possibility for a titration simulation as a visual aid for enhancement not as part of a question, But it needs to be good quality and using the type of reagents appropriate for the grade||
|12|Physical science|Galvanic cell|is the best use of this diagram to ask about parts?||
|12|Physical science|electrolytic cell|is the best use of the diagram to ask about naming parts?||
|12|Physical science|Gas evolution kinetics|is the best use of the diagram to ask about naming parts?||
|12|Physical science|AC alternator vs DC Motor electrodynamics|1) The diagram needs to be improved to anaotomy textbook level <br />2) Can the question be better than just naming parts||
|12|Technical mathematics|Argand complex|1) Just ensure the questions is good enough||
|12|Technical mathematics|Trapezoidal rule|Latex leak is really bad||
|12|Math|Circle geometry|latex leak||
|12|Math|Cubic calculus|1) Latex leak 2) pointd of interest already are given in the graph, which is poor design.||
|12|Math|Scatter regression|1) Lots of latex leak, tables are not rendered as tables 2) Sample answers need to include actual steps of solutions||
|12|Math|Venn 3 sets: 3-event compound venn diagram|1) Latex leak 2) no proceure steps in expected answers||
|12|Physical science|Motion graph|The graph is not actually referenced within the question||
|12|Physical science|Reaction profile: Exothermic and endothermic potential energy...|we need actual procedure steps in expected answers||



