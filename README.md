# uib-django-eksperiment

The TEG I am going to be constructing is based on the TEG conducted in the academic article "Why do people pay taxes?" by James Alm et al. \cite{whytaxes}, but with some simple adjustments. These adjustments will be discussed in great detail later. 

The experiment was programmed and designed in Otree, an open-source platform for behavioral research and licensed under the MIT open source license. 

We have 8 participants that play the game simultaneously. The game starts by giving the participants instructions on how to play the game. The instructions are followed up by four control questions that highlight the most crucial aspects of the game.  Every participant needs to get all the control questions right in order to progress to the actual game. If they don't get them right, they are transferred back to the instruction page and forced to read the instructions again and retake the control questions until they get them all right. The participants that get the questions right are forced to wait for the other players. And that is generally how every step of the game is going to play out. The participants need to wait for the last person to contribute before the game continues. When all participants understand the instructions, the real game begins.

In every round each player pulls a random value from the following set: <img src="https://latex.codecogs.com/gif.latex? {1, 2, 3, 4, 5, 6, 7, 8\} " /> 
Once a value is assigned to an individual, only this individual gets that value that round. So if individual 1 gets the value 7, no other participant gets that value in that round. These values are payments in Norwegian kroner (NOK). When the individuals receive their payment, they are asked to declare their payment to an auctioneer who will take 40 percent of what they declare. The auctioneer sums up what every participant declared, and multiplies it by 2. This multiplicator is referred to as the "group surplus multiplicator", and reflects the consumer surplus the individual gets from the public good. This sum is then distributed evenly between the eight players each round. 

The participants decide themself how much they wish to declare of the received payment, but they know that there is a punishment associated with not declaring their full payment. There is a chance of getting audited. If a participant gets audited and did not declare the full payment that round, the participant is forced to pay a fine equivalent of ($15\times \textit{undeclared income}$). The sum of what the auctioneer collects in fines from the people that got audited, and did not declare their full income is removed from the game. Even tho a participant gets couth evading and is forced to pay a fine, the evader will still receive the same public good payment that everyone else in the game receives. 

When every participant has declared their income, all audits have been completed, and the public good sum has been divided between all the participants, a new round starts. A round is a part of a section. In this TEG we have three sections; each section has a total of 8 rounds. What separates these sections are the possibility of getting audited. In the first section $(1)$ is the possibility of getting audited $0\%$, in section two $(2)$ the audit ratio is $2\%$ and in section three $(3)$ the audit ratio is $10\%$. The participants are not informed of how many rounds there are. The only information the participants know before entering the game is that they will participate in a multiplayer game where they are handed some amount of money each round and that they need to declare this money to a third party, and that the game will take between 15-30 minutes to complete. This TEG will be running three different times, and the total number of participants will be 24. The thing that will change from every iteration of the game is the order of the sections. So, the second time the sections will be: $(2)$, $(3)$ and $(1)$. And the third time we will have this setup: $(3)$, $(1)$ and $(2)$.

In the original experiment conducted by James Alm, Gary H.McClelland and William D. Schulze there where a brief discussion about what language best suited for a experiment like this. The discussion was about using neutral terminology, or a more cumbersome terminology. By using neutral terminology, you terminate every "complex" word or word directly associated with what the experiment is realy about. \textbf{[Skriv mer utfyllende her..]}

It is possible to find the optimal strategy for each individual for each period by maximizing each individual's expected utility function. 

<img src="https://latex.codecogs.com/gif.latex? EU=I-tD+ms(G-tD)-pf[t(I-D)] " />


 
Here is $I$ the individual's income, so this is essentially the amount the individual gets paid each round. $D$ is how much of the income the individual decides to declare. $G$ is the tax paid by all members of the experiment. $t$ is the tax variable. $f$ is the size of the fine as a part of what the individual does not declare. p is the probability to be audited, and $m$ is the group surplus multiplicator. $s$ is how big part of the TEG the individual is since there are always eight players in the game, therefor the variable will always be 0.125. To find the optimal strategy for the individuals, we derivate the expected utility function $(1)$ with respect to the declared income $(D)$, and we get:

<img src="https://latex.codecogs.com/gif.latex? \frac{dEV}{dD}(I-tD+ms(G-tD)-pf[t(I-D)]) " />
<img src="https://latex.codecogs.com/gif.latex? pf+ms>1 " />



If <img src="https://latex.codecogs.com/gif.latex? pf+ms>1 " /> the individual wants to declare his whole income, so the optimal choise is to set $D = I$. But if the  $pf+ms<1$, the optimal choice for the individual is to report zero income, $D = 0$. We can demonstrate this with an example. We have a risk-averse player, the group surplus multiplicator is default set to 2. The public good is shared equally among the players and is therefore by default $s=0.125$ since we have eight players. The punishment for evading if the individual gets caught is $f=15$. We are now able to calculate the cutoff where $pf+ms=1$. 

\begin{equation} \label{eq:2}
\frac{1-2\times0.125}{15}=0.05 
\end{equation}
$$\frac{1-2*0.125}{15}=0.05$$. \\

We see that the cutoff is at $5\%$. Therefore the dominant strategy will be to report zero income $(D=0)$ when the audit probability is equal to $0\%$ and $2\%$. And report the full income $(D = I)$ when the audit probability is equal to $10\%$

