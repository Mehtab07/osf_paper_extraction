## Introduction

Electoral manifestos are a common subject of political studies. They provide 
researchers with valuable information about the priorities, goals and intentions 
of political parties. Many political science projects deal exclusively with them, 
such as the Manifesto Project, which offers a widely shared coding scheme al­
lowing diverse kinds of analysis. Academic research related to electoral mani­
Politics in Central Europe (ISSN: 1801-3422)
Vol. 16, No. 1
DOI: 10.2478/pce-2020-0012
260
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
festos has come a long way. The content analysis of manifestos started in the 
1970s (Volkens – Bara – Budge 2009) and developed into specialised projects 
that used a common framework for textual analysis (for example, Electoral Stud­
ies). Today, comparing and estimating policy positions based on electoral mani­
festos is quite common in the field of political science. The prevailing method 
of manifesto research is based on coding procedures, which depend on human 
judgement. This creates methodological problems, mainly objectivity, reliability 
and replicability (Rourke – Anderson – Garrison – Archer 2001). All these issues 
stem from the interpretative nature of coding. In fact, the coding procedures 
had to improve due to the criticism of their reliability and subjectivity. And the 
advent of greater computational power has brought new approaches to content 
analysis. Computer­‑driven methods have been developed to overcome the likely 
human bias. The arguments in favour of computer­‑driven analysis are that it 
processes large quantities of text faster and more cheaply than humans (Bara 
2006) and the outcomes of such analysis are more reliable.
But computer content analysis has flaws as well. The main objection is that 
it lacks semantic validity. In order to understand the meaning of a text, a re­
searcher must consider its cultural context and socio­‑economic environment 
(Volkens – Bara – Budge 2009). Human language is complex for computers to 
understand (its syntax, semantics and meaning). Computers do not get the 
right meaning all the time, because words have different meanings in different 
contexts and are used in idiomatic expressions and irony.1
This paper proposes using the computer­‑driven text analysis of party mani­
festos to add another layer of understanding to existing research. It is an 
opportunity to apply new methods to old content and come up with more reli­
able interpretations. It does not mean that previous academic interpretations 
and conclusions are obsolete. Natural language processing (hereinafter NLP) 
has become a useful technique in political science as it might provide new 
perspectives on the data or to test previous conclusions from other content 
based methods. This is connected with the availability of digital data (electoral 
manifestos, official statements, social media posts, etc.) provided by political 
parties and with the development of software capable of categorising text. NLP 
relies on increased computing performance to analyse such data. Computers can 
represent text numerically and analyse it in a way that is difficult for humans. 
Additionally, the results from NLP methods are quick and reproducible due to 
computer scripts (or algorithms) available on the Internet. Researchers with 
similar interests might continue where others have left off.
Computer­‑driven content analysis is more widespread in Anglo­‑Saxon coun­
tries, due to the quicker computer advances in understanding English as a lan­
guage. Merz, Regel and Lewandowski (2016) show what is possible with the 
1	 Idioms and irony are, however, less likely to occur in formal electoral manifestos.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
261
fully digitalised corpus of manifestos collected by the Manifesto Project. Such 
data can be used for computing frequencies of texts, tracking policy ideas in 
manifestos, and even training machine algorithms to automatically code sen­
tences. Slapin and Proksch (2008) propose an algorithm that estimates par­
ties’ policy positions based on word frequencies in texts. Having tested it on 
German political parties’ manifestos from 1990 to 2005, they conclude that the 
algorithm estimated policy positions better than existing time­‑series estimates. 
Another aspect of natural language processing is opinion mining and sentiment 
analysis. Pang and Lee (2008) outline ways of extracting opinion­‑oriented 
positions from texts, while Young and Soroka (2012) apply computer­‑driven 
sentiment analysis to selected political texts and evaluate the validity of such 
an approach. Rudkowsky et al. (2018) test a different approach to evaluating 
sentiment with word embedding. Sentiment analysis has become one of the 
major areas of research in political communication.
Natural language processing has been little practised on electoral manifestos in 
Central Eastern Europe. The academic research related to social democratic parties 
in the region is mostly based on human­‑based content analysis and expert reviews. 
Typically, ideology and programmes are analysed only as part of a broader con­
text and often by using case studies or qualitative comparisons (Kopeček 2005; 
Kopeček 2007; Curry – Urban 2003; White – Lewis – Batt 2013; Bozóki – Ishiyama 
2002; Hloušek – Kopeček 2016; Koubek ‑ Polášek 2017; Krašovec – Cabada 2018). 
The relative lack of a robust methodology influences the theory behind this paper 
that needs to rely on a general set of assumptions from a wider literature.
This paper aims to analyse the available manifestos of a single social demo­
cratic party family. Social democracy is considered one of the general party 
families in academic literature (Beyme 1985, Mair – Mudde 1998). There is 
an assumption of a unity in values, positions, and programmatic convergence 
in each party family (ibid.), something that makes social democratic parties 
closer to each other than to other political opponents. This party family is 
also considered one of the most coherent party families in Europe (Hloušek – 
Kopeček 2016). Some empirical observations contradict such close proximity 
within social democratic party family, at least in Western Europe (Delwit 2005; 
Keman 2017). Both in domestic politics and at the EU level, social democratic 
parties have been constrained by diverse economic, social and political reality 
(Lightfoot 2005). This theoretical contradiction whether social democratic par­
ties are really similar or diverse in their priorities provides a first assumption 
to check with the analysis of electoral manifestos.
The second theoretical argument for the analysis of social democratic party 
family is its slow decline in politics. Social democratic parties are still being 
considered establishment parties2. They are connected with the support of lib­
2	 At least in European democratic countries.
262
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
eral democracy, the support for equal rights for everyone, the implementation 
of a welfare state, and moderate policies that avoid extreme, populist solutions 
(Meyer 2000; Sasoon 2014; Keman 2008). However, they are not as dominant 
a political force as they were in the past century. Researchers argue that the 
globalisation of economy and the limitation of powers of a nation state are one 
of the main reasons for the decline of social democratic parties (Pierson 2001; 
Thomson 2000; Gallaghan – Tuney 2000, Gallaghan 2000). Thomson (2000) 
summed up the problem as a social democratic dilemma – it is increasingly 
hard to achieve the political goals of social democratic parties in a globalised 
capitalism and international politics. From this point of view, it might be useful 
to knowhow these global developments are reflected in electoral manifestos and 
how often parties talk about it. This forms a second assumption of the paper.
The paper focuses its attention to the region of Central Eastern Europe (the 
Czech Republic, Hungary, Poland and Slovakia). The selected social democratic 
parties are ČSSD (Czechia), MSZP (Hungary), SLD (Poland) and Smer­‑SD 
(Slovakia). These parties have been crucial in the democratic transition and 
consolidation of democracy in all the selected countries (a slight exception 
is Smer­‑SD in Slovakia). They have become well established actors in their 
domestic political systems but most have been losing political support and 
impact (except for Smer­‑SD in Slovakia). The parties share a similar political 
environment, they are all accepted as members of the Party of European Social­
ists (PES). Hloušek and Kopeček (2016) have confirmed that their manifesto 
claims are similar to the ones made in manifestos of PES.
Moreover, these parties have not been widely covered in academic litera­
ture when it comes to the computer analysis of their manifestos. The above 
mentioned analysis by Hloušek and Kopeček (ibid.) used the content analysis 
of manifestos. This is an opportunity to explore and test the computer­‑driven 
method on new cases, and evaluate whether such approaches yield similar re­
sults as previous content­‑based methods. A well­‑established social democratic 
agenda in most post­‑communist countries is generally missing.3 Some parties 
might use a more nationalistic rhetoric or advocate for more protest issues. This 
makes the situation in the Visegrad countries even more complex for the analysis.
The selection of salient issues depends mostly on important cleavages in soci­
ety (Lipset – Rokkan 1967; Bartolini – Mair 1990; Bartolinin 2000). Kriesi et al. 
(2008) argued that with the continuing influence of globalisation the parties 
have to take a position on socio­‑economic and cultural issues in the society. 
This theory is the basis for the examination of how the selected parties, in the 
framework of social democratic policies, have adapted their electoral strate­
gies in their own political environment, and to study their goals, priorities 
3	 The exception is the ČSSD party in the Czech Republic, which is considered by many in the academic 
literature a party with deep historical roots in socialism.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
263
and intentions, and where they stand between socio­‑economic and cultural 
cleavages. The assumption of the paper is that parties in the post­‑communist 
democracies would still position themselves mostly on socio­‑economic issues, 
not the cultural ones.
Data and methods
The data for the analysis were obtained from the Manifesto Project. Only mani­
festos after 2000 could be considered because only they were available as digital 
texts readable by computers. The table below shows the years for which mani­
festos were transformed into textual data for each country.
Table 1: List of electoral years for which manifestos were available in 
computer­‑readable text
Party (Country)
Publication year of party manifesto
ČSSD (Czech Republic)
2002, 2006, 2010, 2013, 2017
MSZP (Hungary)
2002, 2006, 2010, 2014
SLD (Poland)
2001, 2007, 2011, 2016
Smer-SD (Slovakia)
2006, 2010, 2012, 2016
Unfortunately, many Natural Language Processing tools are available only in 
widely spoken languages (English, French, Chinese, Spanish and German), so 
once the manifesto texts were ready for analysis, they were translated into Eng­
lish. This brings additional problems in interpreting the results, but no other 
option was viable. Thus, the text files were translated by Google Translate API 
into English. The decision was practical due to easy access to the API (applica­
tion program interface) and the reasonably robust English translation facility 
that Google has built. The translated texts are not a perfect end product, but 
they are of sufficient quality to apply selected NLP tools to them.
The NLP analysis focuses on two dimensions of manifestos: sentiment analy­
sis and keywords. Sentiment is used to analyse how parties express their priori­
ties (their way of communication – positive, neutral or negative) and keywords 
are used to determine what parties talk about the most (the content of their 
communication). The analysis uses two sentiment analysers,4 Textblob and 
4	 The reason to choose two tools for sentiment analysis is to cover the weaknesses of these tools. It is 
likely that both tools produce slightly different results because they use various criteria to evaluate 
264
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
Vader, applied at the sentence level of the document. Both packages work with 
a scale from –1.0 to +1.0, where –1.0 is the most negative and +1.0 is the most 
positive. The package then evaluates whether a sentence is negative or positive 
by averaging values of polarity and intensity for each word in the sentence. Senti­
ment analysers refer to a well­‑defined lexicon of English words and take values 
of polarity and intensity from them.5 The final interval of a sentence between 
[–1.0; –0.25] means the sentence is negative and the interval [0.25; 1.0] means 
that it is positive. Every sentence outside these intervals is considered neutral. 
The script then automatically counts the number of sentences in the text, and 
calculates the ratio positive and negative sentences in a given text.
The paper uses a combination of tools for the keyword analysis too. The 
selected tools complement each other and can point to different aspects of the 
manifestos. These tools are listed here:
RAKE6 (Rapid Automatic Keyword Extraction) is an algorithm that deter­
mines key phrases in a body of text by analysing the frequency of word appear­
ance and its co‑occurrence with other words in the text. Ten keywords with the 
most impact on a selected manifesto are taken into account.
Noun phrase analysis is a part of the Textblob library used for sentiment 
analysis. It extracts noun phrases from the text and ranks them according to 
their impact on the text. Nouns usually carry important pieces of information 
about places, organisations, actions, etc. The extraction of such information 
from the text is beneficial for the comparison between various manifestos and 
also among various political parties. Phrases with at least seven occurrences 
are taken into account.
Frequency distribution counts occurrences of specific words in a text. It is 
necessary to conduct some text cleaning before running this method on a text. 
It consists of three steps – make all words lowercase, delete stop words7 in a text 
and lemmatise each word to its lemma according to a dictionary. Words with at 
least seven occurrences in a manifesto are taken into account.
The Python development environment powered the NLP analysis. All of 
the code used for the analysis is stored in a public repository on OSF.8 Any 
researcher can download the files and replicate the analysis.9
the sentiment of the sentence. Thus by combining the results and making an average from them, the 
analysis gets a more accurate picture of the sentiment from selected manifestos.
5	 More information about this technique is written in this article – https://planspace.org/20150607-
textblob_sentiment/.
6	 The Python package used in the analysis is available at this link– https://pypi.org/project/rake­‑nltk/.
7	 The list of stop words in NLTK package is available at this link – https://gist.github.com/sebleier/554280.
8	 Web link: https://osf.io/ndtqg/.
9	 This, however, depends on the development environment on the researcher’s computer. MacOS/Linux 
systems share similarities, while Windows has some other commands for dealing with the Python 
development environment. The analysis for this article was conducted on a Linux machine.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
265
Research questions
The questions reflect broad theoretical assumptions from the Introduction sec­
tion. These assumptions are, in short, as follows:
There is a unity in values, positions, and programmatic convergence in each 
party family, and social democratic parties are closely related.
Global challenges to social democratic parties are reflected in their mani­
festos and these parties need to take a position in the face of globalisation in 
economics and politics.
Parties in opposition use a more critical language in its manifestos, while 
incumbent parties prefer to mention more positive messages to the electorate.
The electorate of social democratic parties in European post­‑communist 
countries still prefers materialistic values (social security, employment, state 
support) to more post­‑materialistic values (gender, minorities, environment) 
as is the case in West­‑European democracies.
Sentiment and keyword analysis provide a method to answer these assump­
tions. The analysis of keywords aims at words in a manifesto that either occur 
very often or have an impact on the composition of the text. This is directly 
linked to the three assumptions above. A comparison within party manifestos 
gives an idea of main topics the party advocates. The analysis also evaluates if 
there are similarities or differences within a group of social democratic parties 
in the Visegrad countries.
The sentiment analysis provides more data for the third assumption about 
the difference in sentiment between an incumbent and opposition party. For 
the effect of incumbency, the analysis adds a categorical variable is_incumbent 
into the data table with two possible values.
Values
Description
0
the party competed in elections as an opposition party
1
the party held government office at the time of the election
The values were coded based on the historical records of governing coalitions 
in each state. The variable made it possible to check whether position in the 
government affects how the party speaks about its electoral priorities. To evalu­
ate this effect, the analysis used a difference of means test (known as a t­‑test), 
a standard tool to discover whether differences between groups (measured in 
averages) could have happened by chance. The null hypothesis against which 
the test is conducted is that there is no significant difference between the groups. 
This determines whether there is a significant statistical difference in manifesto 
sentiment between an incumbent and an opposition party.
266
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
Problems with and limitations of the research
The first automatic objection to this type of research is the small number of 
cases in the analysis. Elections happen at four or five­‑year intervals and the 
selected countries in the analysis have been enjoying democratic regimes only 
since 1989. Additionally, not all manifestos have been available as digital texts. 
Thus, the analysis only included 17 manifestos from four countries. Naturally, 
results from such an analysis cannot be robust and need to be checked in the 
future with a larger sample. Translating the text into English further limits the 
value of the analysis as it is prone to changing its structure and meaning. Thus, 
this paper sets only modest research goals to adapt to this limitation and aims 
merely to test the new approach to analysis.
Some sources, also, question the usefulness of electoral manifestos as 
a source of data. It is reasonable to assume that these documents are mostly 
Public Relations texts aimed at voters, most of whom do not read them. Also, 
any post­‑election coalition negotiation alters the electoral priorities of a party, 
so what is written in the manifesto might not be set in stone. However, this 
criticism is not directed at the language of the manifestos that is the subject of 
this paper. Electoral manifestos might not decide election results, but they do 
reflect how a party expresses its priorities. They aim to convey what parties are 
trying to achieve and what kind of language they use in public to justify their 
goals. With that in mind, the paper aims to conduct a comparative analysis of 
language usage, rather than trying to make a logical link between manifestos 
and electoral outcomes.
Findings
The summary of the main findings is discussed below according to the type of 
analysis. Full tables are included in Appendices and also in the OSF repository10.
Keywords analysis
In the ČSSD manifestos, the expected social democratic themes appeared. ČSSD 
consistently covered topics such as social policy and social spending (parental 
allowance, affordable housing and care­‑giving services) in its manifestos. To­
gether with an emphasis on avoiding social exclusion (measures like indem­
nity obligation) and preventing negative behaviour (regulation of gambling 
websites), the party advocated the idea that a state has a legitimate power to 
regulate social relationships. Additionally, ČSSD consistently emphasised eco­
nomic development in its manifestos. Ideas such as investment in transportation 
10	 Web link: https://osf.io/ndtqg/.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
267
(highways, railways, airports, etc.) and in underdeveloped regions appeared 
many times. Keywords covering corruption were not covered frequently in the 
party’s official documents during the analysed period. In terms of frequency, 
the manifestos paid attention to words connected with the Czech state, being 
in Europe and the management of public services (such as taxation, state sup­
port and development). Other topics of the European Left (minority rights, 
environmental protection and migration) did not appear in the analysis.
The MSZP results were in many areas similar to ČSSD’s. What distinguishes 
this party from ČSSD was its emphasis in its manifestos on agricultural topics. 
Keywords such as domestic cultivation, programme NATURA 2000, GMO food 
production, food control and landscape varieties appeared during the analysed 
period. Social programmes (health care, social security, pensions, subsidised 
housing), economic incentives (such as investments in roads) and agriculture 
played the dominant role in MSZP’s manifesto keywords. Frequent words re­
lated to Hungary and Europe; the use of public powers to support people were 
also present. MSZP also frequently mentioned the Roma question in its mani­
festos. Moreover, mentions of FIDESZ and Viktor Orbán increased in the later 
manifestos. This is most likely connected with the changing status of MSZP in 
Hungarian politics, which saw the downfall of its electoral preferences and not 
holding government power.
The SLD manifestos did not confirm the trends set by ČSSD and MSZP. 
SLD manifesto keywords over time did not form a unified set of ideas. There 
was no strong theme that ran through all selected manifestos. It seems as if 
the party was trying to find topics that would attract voters from other par­
ties. Economic regulations were represented by keywords such as bank credit 
guarantees, carbon emissions, protection against excessive imports, balanc­
ing trade and quantitative easing. Pension schemes were mentioned in social 
policy as well as keywords related to religion, tourism, culture and justice. But 
these keywords did not appear regularly in its manifestos as opposed to ČSSD 
or MSZP. Additionally, SLD manifestos stressed international matters such as 
the Frontex Agency and NATO. In terms of frequency, SLD used similar words 
to other parties. Words related to Poland and Europe, frequent terms such as 
state, development, people, health care and non­‑governmental organisations 
point to a more standard social democratic agenda.
Smer­‑SD showed the highest consistency of keywords in its manifestos. 
Smer­‑SD used similar wording, topics and some typical social democratic ideas. 
Keywords connected with economic development and social security have been 
a standard of the social democratic agenda. Where Smer­‑SD differed from the 
other selected parties was in its emphasis on the law and criminal issues. The 
party tended to emphasise keywords such as sanction regime, criminal code 
and punishment, restitution claims and constitutional provisions. Moreover, 
fiscal responsibility also appeared frequently in the manifestos. This was not 
268
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
that common among the other selected social democratic parties. Smer­‑SD, as 
a Slovak political party, was constrained by Slovakia’s membership of the Eu­
rozone and its fiscal rules. Regarding word selection and frequency, Smer­‑SD 
consistently used language related to economic development and labour market 
policies. Words such as social, government, development, state and public often 
appeared in the results.
Sentiment
The positive sentiment in ČSSD’s manifestos had a greater variation than the 
negative one. The party was trying to convey more positive messages, in general 
(approximately one­‑third of sentences were evaluated as positive). A signifi­
cant change happened in 2010 when the percentage of positive sentences had 
dropped and the percentage of negative sentences had increased in compari­
son with previous elections. This was influenced by the global economic and 
Eurozone crises, and by the fact that ČSSD was competing in the election as an 
opposition party. The opposite trend is visible in the 2017 elections when ČSSD 
was running as an incumbent party and the economy was prospering.
The results for MSZP offer a different picture. The MSZP election manifesto in 
2002 had the highest percentage of positive sentences and the lowest percentage 
of negative ones. The manifesto in 2002 was also relatively short in comparison 
with later manifestos. From 2002 on, positive sentences decreased, and nega­
tive sentences increased. Even though MSZP was part of the government from 
2002 to 2010, its manifestos did not contain more positive sentences. Over 
that time, the change in the sentiment can be linked to MSZP’s problems in 
domestic politics (corruption cases, the rise of other parties and a reputation 
for incompetence).
SLD is the only party in the selected cases that did not hold government office 
during the analysed period. Even though SLD tried to form broad left alliances 
with other leftist parties, such efforts were in vain. SLD contested all elections 
from 2001 as an opposition party. The election manifesto in 2001, the one before 
Poland joined the EU, showed the greatest proportion of positivity and small­
est amount of negativity compared with the later manifestos.11 Additionally, 
proportion of negative sentences was among the highest in the selected cases.
Slovak party Smer­‑SD had the most stable results in the group of parties 
over the analysed period. It was a successful national party that won the largest 
share of votes in every election from which the data were taken. A low variation 
among all the manifestos’ sentiments means that the content of the election 
programme did not change much (it is in line with the findings from keyword 
11	 The only exception in this case was the proportion of negative sentences in the 2016 manifesto that 
was slightly, but not significantly, lower.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
269
analysis). Smer­‑SD stuck with what was apparently working, even when it was 
in opposition.12 Positive sentences make up around 40% of the manifestos. This 
is in contrast to the cases of ČSSD and MSZP, which moved from incumbency 
to opposition with more dramatic changes in their manifestos.

## Discussion

In this part of the paper, the empirical results from the analysis are discussed 
in the light of the theoretical assumptions stated at the beginning of the paper.
There is a unity in values, positions and programmatic convergence in each 
party family, and social democratic parties are closely related.
In general, traditional social democratic values are summed up in the values 
of PES on the European level. These are democracy, freedom, equality, peace, 
justice13. No selected party based its manifesto on protest or criticism of democ­
racy. This is in line with the standard theory of social democratic parties, which 
assumes that social democratic parties accept the rules of the democratic game 
and are fully supportive of representative democracy. The pro‑European direc­
tion of the selected parties was also evident from the analysis. Ideas of Europe 
and the European Union were present in every manifesto. The references to 
the EU in observed manifestos reached their peak around the time of acces­
sion to the EU in 2004. However, the idea of being in the EU and supporting 
integration and its values were constant even after accession. This supports the 
convergence of the selected parties into a unified set of values and positions 
in their manifestos.
In terms of general electoral priorities, the parties advocated ideas of eco­
nomic development, social policy and belonging to international institutions 
such as the EU and NATO. These ideas fit into the typical social democratic 
agenda throughout Europe. This was confirmed by the keyword and frequency 
analysis. Topics such as the development of transport, the regulation of hous­
ing, unemployment, health care support and education were present, although 
not evenly, in the analysed manifestos. These topics fall under a general term of 
socio­‑economic policy, which is not the political domain of only social demo­
cratic parties.
But the variation in the socio­‑economic issues matters. This was the reason 
for the keyword and frequency analysis in the paper. The results of the selected 
parties mostly followed traditional social democratic ideas based on an em­
phasis on development and growth, state support, the public management of 
resources and support for the middle class. This is all in line with the theoretical 
12	 The total number of sentences in Smer­‑SD manifestos was also consistent. One might assume that they 
did not change the content of their manifestos significantly. But this is not clear based on the sheer 
number of sentences in manifestos.
13	 The official webpage of PES – https://www.pes.eu/en/about­‑us/our­‑values/.
270
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
argument of Hloušek and Kopeček (2016) from the Introduction. But there were 
also signs of contradiction to a general similarity of social democratic parties. As 
stated above, Delwit (2005) argued that when one observes priorities of social 
democratic parties more empirically, there is not a close proximity of these ideas. 
Lightfoot (2005) also pointed out that these parties are constrained by their 
own national political realities. These views reflected some observations from 
the analysis. Mainly, MSZP’s emphasis on agriculture and the environment in 
its keywords or ČSSD’s focus on industrial and employment policies rather than 
on protecting the environment14, or the importance of law and order in Smer­
‑SD manifestos. These aspects show the diversity of ideas that the parties work 
with. Empirically speaking, there is no blueprint for what a social democratic 
party should put its emphasis on.
Global challenges to social democratic parties are reflected in their mani­
festos and these parties need to take a position in the face of globalisation in 
economics and in politics.
The analysis did not provide much evidence in terms of tackling global is­
sues in the selected manifestos or a novelty of ideas. These documents were 
still mainly oriented towards a national electorate, which is expected. Most 
frequent words did not mention anything global or international, but state, 
government, tax and public support. Even capitalism was not a frequent word 
in manifestos. This leads to the impression that the selected social democratic 
parties did not aspire beyond their national borders. They just used what had 
apparently worked in the past. They seemed to hold onto the approach of an 
independent nation state even though the reality of economic globalisation and 
internationalisation of politics leaves less and less space for the nation state 
to act independently. This evolution is not really reflected in the words of the 
manifestos. At least, the references to the European Union were constant, as 
mentioned above. This might qualify as a sign that selected social democratic 
parties looked beyond their national borders.
Additionally, the topic of migration was absent from the results of the analy­
sis. This is a strange observation bearing in mind that migration has been 
a highly politicised topic in the Visegrad region in recent years. At least three 
manifestos were expected to be influenced by this topic – ČSSD in 2017, SLD in 
2016 and Smer­‑SD in 2016. But migration was not present as a keyword in any 
observed manifesto, and words related to migration were not even represented 
among the most frequent words. Two explanations might be possible. First, the 
manifestos really did not have significant mentions of the topic of migration. 
Parties might have used other communication channels to state their position 
on the topic (TV debates, interviews or social media posts) that they deemed to 
14	 This might be in line with its electoral strongholds in the north­‑east industrial regions of the Czech 
Republic, but not with the general direction of social democracy in Europe.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
271
be more effective. Second, the most frequent words in mentioned manifestos 
were not related to security issues at all. But given the saliency of the issue in 
political agenda­‑setting, the result of the analysis seems counter­‑intuitive.
This observation is in line with the general theory behind the relative decline 
of electoral support for the social democratic parties. As Thomson (2000) coined 
the term ‘social democratic dilemma’, the selected parties in the analysis found 
it hard to react promptly to a changing global environment. Their manifestos 
looked like relics of the past. Nowadays, many areas of economic and social 
policy are constrained by global forces beyond the nation state. But it seems that 
according to the manifestos of the parties in four post­‑communist countries in 
Central­‑Eastern Europe, they have not started to reflect upon it. If the theory 
about the decline of social democratic parties has some predictive power, the 
selected parties will find it hard to gain a dominant position in national politics 
unless they change and react to the issues arising from the globalisation.
Parties in opposition use a more critical language in its manifestos, while 
incumbent parties prefer to mention more positive messages to the electorate.
Most of the sentences in the manifestos tended to be positive or neutral. 
Only once did the proportion of negative sentences in a manifesto exceed 10%. 
The small proportion of negative sentences in manifestos also points to the 
pro­‑system character of the social democratic parties, or at least to a lack of 
opposition to a democratic regime. On average, positive sentiment tended to be 
higher when the selected party was taking part in an election as an incumbent 
(39.11% as incumbent vs 35.21% as opposition). These numbers, however, do 
not constitute a causal mechanism. The t­‑test on positive sentiment between 
incumbent parties and opposition ones produced a statistically significant result 
(p = 0.04, two­‑tailed test). The difference in means was therefore not very likely 
to have been due to chance only. One can assume that this difference probably 
exists in the populations from which it was drawn. It is reasonable to assume 
that a party running in an election as an incumbent will present itself with 
a more positive sentiment in its manifesto.
On the other hand, negative sentiment followed the trend outlined by the 
positive one, with its values in a different order. Incumbent parties had on aver­
age 5.26% of negative sentiment, and opposition parties scored 7.13%. From 
the available theory, it is likely that when a social democratic party was in op­
position, the ratio of negative words in its manifesto might be expected to be 
higher than when the same party was incumbent. The difference of means in 
the case of negative sentiment does not result in a rejection of the t­‑test’s null 
hypothesis (p = 0.1, two­‑tailed test). The difference between the mean nega­
tive sentiment for incumbent (0.05) and opposition parties (0.07) was narrow. 
The paper cannot provide statistical evidence that this result was not due to 
chance only. More data need to be gathered in order to test this hypothesis 
further. A one­‑tailed (or directional) test, however, showed a significant level 
272
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
(p = 0.05). A directional test only points to a directional relationship between 
two groups. The null hypothesis is: ‘incumbent parties do not score a signifi­
cantly lower negative sentiment in their manifestos than opposition parties.’ 
Since the p­‑value was below the expected threshold of 0.05, one can assume 
that there might be statistically significant lower scores of negative sentiment 
in incumbent manifestos.
As results of the above­‑mentioned test, the assumption of the change in 
a sentiment of an electoral manifesto when being incumbent holds only partially. 
When taken into an account a positive sentiment, one can observe a statistical 
significance of change between incumbent and opposition parties, at least on 
the selected cases in the analysis. Other way around, however, does not fully 
work. A change in negative sentences in manifestos failed to pass difference of 
means test. It means that a ration of negative sentences in electoral manifesto 
is most likely not dependent on the position of the party in government or in 
opposition. Thus, the stated assumption in the beginning has to be rewritten 
into a statement similar to this: „Social democratic parties running for an elec­
tion as an opposition party tend to articulate less amount of positive sentences 
to their voters as compared to the situation when they run in elections as an 
incumbent party.“
The electorate of social democratic parties in European post­‑communist 
countries still prefers materialistic values (social security, employment, state 
support) to more post­‑materialistic values (gender, minorities, environment) 
as is the case in West­‑European democracies.
The emphasis of the selected parties on the socio‑economic policies has 
already been established above. It is no surprise that social democratic parties 
deal with the issues of state subsidies, taxation, social benefits, health care, or 
education. On the other hand, the analysis proved that the post­‑materialistic 
dimension of progressive leftist politics was under‑represented (issues such 
as gender equality, environment protection and minority rights) or missing in 
all observed cases. The keyword analysis of MSZP’s manifestos included some 
mentions of a preservation of land and the Roma minority, but it was an excep­
tion from the general rule.
Based on the theory of Kriesi et al. (2008), the economic dimension takes 
precedence over the cultural one in the selected manifestos. This means that 
the selected social democratic parties try to focus on the preservation of social 
achievements and to protect social rights of citizens from the disruptive global 
market. It also shows where the priorities of a national electorate might lie. Vot­
ers still demand an improvement of their economic well­‑being and the standard 
social guarantees. This is understandable from the point of view of developing 
economies. Czech Republic, Hungary, Poland, and Slovakia are catching up with 
the rest of Western European countries in economic development. This is in 
contrast with the social democratic electoral priorities in the developed Western 
POLITICS IN CENTRAL EUROPE 16 (2020) 1
273
European democracies. Material well­‑being and a system of social welfare in 
these states is already established, so the post­‑materialistic values can be fully 
articulated by voters. Therefore, the difference in electoral priorities of parties 
from the same party family is influenced by the structural conditions in which 
parties compete for electoral support.

## Conclusion

The aim of the paper was to test the theoretical assumptions related to the 
social democratic parties in Europe. The paper applied the method of Natural 
language processing to electoral manifestos. And since the computer­‑driven 
content analysis has only been applied minimally to electoral manifestos in 
Central Eastern Europe, the paper applied a new method on an old content. The 
results of the analysis, then, served as a check against the already established 
theory about the social democratic parties. Based on the analysis, the paper 
concluded the following:
It is not clear if social democratic parties converge in electoral priori­
ties. Here, the theory about the social democratic parties is not unified. Some 
claim that these parties share a unified set of values and goals, some claim that 
there are still differences among these parties based on the empirical study of 
their priorities. The analysis has confirmed both views as valid. It is true that 
the selected parties, generally, accepted same values, like support for the liberal 
democracy, the European Union, emphasis on economic development and so­
cial policy. However, in terms of electoral solutions to voters, the parties were 
constrained by their nation­‑states.
The selected social democratic parties do not aspire for ideas outside of 
nation­‑state in their electoral manifestos. On the one hand, this is under­
standable, because the manifestos are primarily directed to a national electorate. 
On the other hand, the theory about the decline of social democratic parties ar­
gues that these parties need to find ways how to apply their ideas to a new global 
environment where economic and political forces are oftentimes outside the 
national borders. Based on the keyword analysis, these parties still rely mostly 
on the idea of an independent state power to change citizens lives for better.
A significant change in positive sentiment of manifestos happened when 
social democratic parties run in elections as incumbents. They stressed more 
positive sentences than when they were in opposition. The change was evalu­
ated by a difference of mean test. However, more observations will be needed 
in the future to further confirm this conclusion.
Social democratic parties primarily competed on economic issues during 
election campaigns. The cultural dimension of the social democratic agenda 
was missing, or it merely appeared. No selected party strongly featured topics 
like gender equality, environmentalism or minority rights. Also, the topic of 
274
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
immigration was excluded from manifestos from 2014 onwards, which seems 
strange considering the strong opposition to migration in the region during 
the recent migration crisis in Europe. Based on the theory of political cleavages, 
these parties and the societies where they compete for votes still hold mostly 
regards the socio­‑economic topics as more relevant than the cultural ones.
The NLP method of computer analysis proved to be an useful analytical tool, 
despite of all its discussed limitations. The method, nevertheless, does bring new 
perspectives and increases analytical rigour. Sentiment analysis and keyword 
extractions have found their place in the pursuit of better understanding how 
political parties shape their electoral manifestos. But while NLP can tell us what 
was said and how, it cannot tell us why. For this reason, the interpretation of 
manifestos will still be an important part of political science and should remain 
an integral part of any computer­‑powered method of analysing textual data.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
275
Appendix
Table: Results of keyword and frequency analysis
ČSSD
Year
Keywords
Noun phrases
Frequency distribution
2002
„receiving parental 
allowance“, „indemnity 
obligation“, „belt 
tightening“, „black sheep 
anymore“, „50 thousand 
apartments“
eu (14), czech (13)
„want“ (42), „support“ (27), 
„year“ (26), „people“ (25), 
„family“ (20), „state“ (17), 
„education“ (17), „would“ 
(16), „work“ (16), „citizen“ 
(16)
2006
„R6 karlovy vary“, 
„behavioral disorders“, 
„minimal added value“, 
„combating extremist 
movements“, „10 
million passengers“, 
„environmentally friendly 
substitutes“, „prefabricated 
housing estates“
cssd (157), czech (153), eu 
(40), european union 
(29), europe (17), public 
administration (15), health 
care (15), economic growth 
(13), labor market (12), 
roma (12), non-profit 
sector (11), non-profit 
organizations (11), prague 
(10)
„social“ (169), „support“ 
(166), „cssd“ (165), „czech“ 
(164), „public“ (136), 
„development“ (134), „state“ 
(115), „education“ (110), 
„european“ (105), „system“ 
(102)
2010
„wastewater treatment 
plants“, „valuable raw 
materials“, „upgrade river 
vessels“, „traditional urban 
agglomeration“, „licensed 
gambling sites“, „heavy 
transit traffic“, „dangerous 
traffic violations“
czech (57), eu (17), cssd 
(16), europe (12), european 
union (9)
„social“ (87), „support“ 
(77), „public“ (67), „state“ 
(61), „czech“ (58), „tax“ 
(44), „service“ (42), „system“ 
(42), „increase“ (41), 
„development“ (41)
2013
„resisting corrupt pressures“, 
„4th railway corridors“, 
„regional differences“, 
„liberalized railway market“, 
„individual constitutional 
actors“, „socially excluded 
localities“
czech (34), european union 
(7)
„support“ (50), „public“ 
(48), „state“ (46), „czech“ 
(34), „social“ (32), „tax“ (28), 
„service“ (28), „development“ 
(27), „european“ (24), 
„citizen“ (23)
2017
„traditional agricultural 
crops“, „railway stations“, 
„gray zones“, „mental 
health centers“, „including 
rewarding caregivers“, 
„television broadcasting act“
czech (65), europe (15), 
cssd (10), public services 
(10), large companies (8), 
european union (8)
„czech“ (69), „support“ 
(61), „people“ (54), „state“ 
(44), „care“ (43), „public“ 
(42), „social“ (39), „tax“ (39), 
„service“ (37)
276
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
MSZP
Year
Keywords
Noun phrases
Frequency distribution
2002
„successful domestic 
cultivation“, „obsolete 
hospital buildings“, 
„incentives“, „flexible 
retirement scheme“, „flat 
rate optional“, „180 
thousand homes“, 
„predictable agricultural 
policy“
hungarian (8)
„new“ (14), „program“ (12), 
„create“ (12), „system“ (11), 
„education“ (11), „allowance“ 
(9), „hungarian“ (9), „public“ 
(8), „social“ (7)
2006
„someone else losing“, 
„senior citizenship council“, 
„scale hospital renovations“, 
„per capita aid“, „internet 
accessible everywhere“, 
„blood supply“, „gross 
national product“, „natura 
2000 program“
hungary (52), hungarian 
(39), roma (9), eu (8), young 
people (7), mszp (7), europe 
(7), european union (7)
„hungary“ (55), „social“ 
(53), „development“ (50), 
„hungarian“ (49), „program“ 
(45), „security“ (42), 
„people“ (40), „country“ (40), 
„state“ (39), „national“ (39)
2010
„recorded crimes fell“, 
„preventing occasional 
infections“, „placing 
dangerous foods“, 
„genetically modified maize“
hungarian (74), hungary 
(62), eu (46), roma (30), 
young people (18), national 
modernization (16), public 
education (16), recent years 
(13)
„development“ (126), 
„program“ (121), „public“ 
(113), „new“ (112), „support“ 
(109), „system“ (103), „year“ 
(101), „hungarian“ (97), 
„people“ (94), „education“ 
(86)
2014
„lease contract“, „traditional 
landscape varieties“, 
„secret sound recording“, 
„scale horticultural farming“, 
„repair inferior roads“, 
„locally produced goods“, 
„frequent extremist 
thoughts“, „declare zero 
tolerance“
hungary (73), hungarian 
(58), mszp (35), fidesz 
(30), hungarians (25), eu 
(25), europe (18), offer for 
hungary (13), economic 
growth (10), young people 
(10), orbán (10), labor 
market (7)
„people“ (106), „hungary“ 
(93), „hungarian“ (86), 
„support“ (71), „state“ (71), 
„public“ (69), „country“ (69), 
„economic“ (69), „social“ 
(65), „government“ (65)
POLITICS IN CENTRAL EUROPE 16 (2020) 1
277
SDL
Year
Keywords
Noun phrases
Frequency distribution
2001
„sensitivity regarding trade“, 
„credit guarantee banks“, 
„counteracts excessive 
import“, „occupational 
pension schemes“, „meets 
allied standards“
polish (23), poland (19), eu 
(12), european union (7)
„development“ (59), „state“ 
(54), „program“ (49), 
„system“ (46), „social“ (45), 
„education“ (34), „fund“ (33), 
„government“ (32), „polish“ 
(27), „public“ (27)
2007
„warsaw frontex agency“, 
„violent behavioral 
patterns“, „insulting 
religious feelings“, 
„beautiful literature 
published“
poland (134), polish (87), 
european union (25), 
europe (24), left (21), eu (21), 
poles (17), pis (13), medical 
services (13), diagnosis 
(11), health care system 
(10), non-governmental 
organizations (10)
„poland“ (143), „state“ 
(96), „polish“ (90), 
„social“ (84), „system“ 
(82), „development“ (76), 
„european“ (74), „people“ 
(70), „country“ (70), „policy“ 
(69)
2011
„iustitia“, „magnet 
attracting tourists“, 
„urban communication“, 
„solid defensive“, „night 
watchman“
poland (200), polish (187), 
eu (67), diagnosis (54), 
left (47), suggestions (46), 
local governments (44), 
europe (38), young people 
(37), poles (35), forces 
(33), non-governmental 
organizations (33), 
european union (32), labor 
market (30), state budget 
(26), foreign policy (24), 
ministry (22), rural areas 
(19), internet (19), public 
finances (17), education 
system (15)
„state“ (245), „system“ 
(215), „development“ (209), 
„poland“ (209), „education“ 
(206), „social“ (197), „polish“ 
(195), „public“ (189), 
„government“ (188), „service“ 
(147)
2016
„square postal items“, 
„north atlantic alliance“, 
„carbon dioxide emissions“, 
„called quantitative easing“
poland (69), polish (36), 
poles (27), european union 
(18), eu (16), support (11), 
europe (10)
„state“ (101), „people“ (77), 
„poland“ (70), „right“ (65), 
„social“ (64), „public“ (63), 
„development“ (54), „care“ 
(51), „school“ (51), „citizen“ 
(48)
278
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
Smer-SD
Year
Keywords
Noun phrases
Frequency distribution
2006
„stricter sanction regime“, 
„negotiating probationary 
periods“, „motor vehicle 
tolls“, „macroeconomic 
figures“, „jaslovské 
bohunice site“, „genetically 
modified organisms“, 
„electricity imports“, 
„supplementary pension 
saving“, „draft criminal 
codes“
smer (118), democracy 
(67), social democracy 
(61), slovak (59), slovakia 
(37), economic growth (11), 
european union (11), roma 
(10)
„social“ (245), „democracy“ 
(143), „state“ (74), „slovak“ 
(60), „government“ 
(52), „tax“ (51), „health“ 
(50), „condition“ (49), 
„development“ (49)
2010
„satisfying restitution 
claims“, „facilitate 
transitional insolvency“, 
„danube river basin“, 
„winning parliamentary 
elections“, „eliminate 
money laundering“
slovak (86), slovakia (64), 
eu (61), european union 
(17), labor market (13), 
government (12), economic 
policy (12), sustainable 
development (11), economic 
growth (10), europe (10)
„government“ (212), „social“ 
(149), „development“ (132), 
„economic“ (104), „policy“ 
(98), „state“ (97), „support“ 
(90), „slovak“ (90), „quality“ 
(81), „public“ (74)
2012
„remove unconstitutional 
provisions“, „jaslovské 
bohunice site“, 
„railway“, „danube river 
basin“, „conduct expert 
discussions“, „‘stricter 
punishment mechanisms“, 
„reduce carbon footprint“, 
„reduce budget chapters“, 
„supplementary pension 
saving“
slovak (98), slovakia 
(63), eu (55), european 
union (24), labor market 
(14), economic policy 
(12), government (11), 
sustainable development 
(11), economic growth 
(11), europe (10), public 
administration (10)
„government“ (207), 
„development“ (153), „social“ 
(133), „economic“ (109), 
„policy“ (107), „slovak“ (102), 
„state“ (96), „support“ (93), 
„public“ (92), „quality“ (87)
2016
„remove unconstitutional 
provisions“, „jaslovské 
bohunice site“, 
„railway“, „danube river 
basin“, „conduct expert 
discussions“, „stricter 
punishment mechanisms“, 
„supplementary pension 
saving“, „varied family 
models“
slovak (98), slovakia 
(61), eu (56), european 
union (24), labor market 
(15), economic policy (13), 
sustainable development 
(11), government considers 
(11), economic growth 
(11), europe (10), public 
administration (10)
„government“ (207), 
„development“ (150), „social“ 
(130), „economic“ (107), 
„policy“ (107), „slovak“ (101), 
„support“ (95), „state“ (94), 
„public“ (92), „quality“ (85)
POLITICS IN CENTRAL EUROPE 16 (2020) 1
279
Table: Results of sentiment analysis
 ČSSD
Year
is_
incumbent
Share of 
votes %
No of 
sentences
% pos
Pos 
election 
change
% neg
Neg 
election 
change
2002
1
30.2
359
34.96
0.00
5.99
0.00
2006
1
32.3
1332
39.83
4.87
5.59
-0.40
2010
0
22.1
657
33.56
-6.27
8.45
2.85
2013
0
20.5
338
36.24
2.68
6.8
-1.64
2017
1
7.3
518
42.57
6.32
5.89
-0.92
 MSZP
Year
is_
incumbent
Share of 
votes %
No of 
sentences
% pos
Pos 
election 
change
% neg
Neg 
election 
change
2002
0
42.1
100
42.50
0
2.50
0
2006
1
43.2
588
36.73
-5.77
4.17
1.67
2010
1
19.3
1306
38.90
2.16
5.82
1.65
2014
0
25.6
1400
28.54
-10.36
8.07
2.25
 SDL
Year
is_
incumbent
Share of 
votes %
No of 
sentences
% pos
Pos 
election 
change
% neg
Neg 
election 
change
2001
0
41
214
39.72
0
6.78
0
2007
0
13.2
797
30.80
-8.92
10.41
3.64
2011
0
8.2
1953
29.70
-1.11
9.96
-0.46
2016
0
7.6
856
31.66
1.96
6.60
-3.36
280
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
 Smer-SD
Year
is_
incumbent
Share of 
votes %
No of 
sentences
% pos
Pos 
election 
change
% neg
Neg 
election 
change
2006
0
29.1
254
38.78
0
6.69
0
2010
1
34.8
579
40.93
2.15
4.75
-1.94
2012
0
44.4
578
40.57
-0.36
5.02
0.27
2016
1
28.3
596
39.85
-0.72
4.61
-0.40
Definitions of column names:
 ·	
is_incumbent – whether or not a party competed in a given elections as an incumbent.
 ·	
Share of votes % – how many per cent the party won nationally in a given election.
 ·	
No of sentences – number of sentences in a manifesto.
 ·	
% pos – percentage of positive sentences in a manifesto.
 ·	
Pos election change – computed metric showing the increase or decrease of positive sentences in 
a manifesto compared to the previous one. A positive number means an increase in positive sentences, 
a negative one means a decrease in positive sentences.
 ·	
% neg – percentage of negative sentences in a manifesto.
 ·	
Neg election change – the same principle as with Pos election change; however, a positive number means 
an increase in negativity and a negative number means a decrease in negativity.

## References

Bara, J. (2006): Do Parties Reflect Public Concerns? In: Bara, J. and Weale, A. (eds.): Democratic 
Politics and Party Competition. Essays in Honour of Ian Budge. London and New York: Rout­
ledge. 105–124.
Bartolini, S. (2000). National Cleavage Structures and the Integration Issue Dimension. Paper 
presented at the Colloque – Science Po. Paris, 26–27 May 2000.
Bartolini, S. – Mair, P. (1990). Identity, Competition, and Electoral Availability: The Stability of 
European Electorates, 1885–1985. Cambridge: Cambridge University Press.
Bernstein, E. (1899): Die Voraussetzungen des Sozialismus und die Aufgaben der Sozialdemokratie. 
Stuttgart: J.H.W. Dietz Nachfolg.
Beyme, K. von (1985): Political Parties in Western Democracies. Aldershot: Gower.
Bozóki, A. – Ishiyama, J. T. (2002): The Communist Successor Parties of Central and Eastern 
Europe. New York: ME Sharpe.
Callaghan, J. T. (2000). The retreat of social democracy. Manchester University Press.
Callaghan, J., & Tunney, S. (2000). Prospects for Social Democracy: a critical review of the argu­
ments and evidence. Contemporary Politics 6(1): 55–75.
Crosland, C. A. R. (1956): The Future of Socialism. London: Jonathan Cape.
POLITICS IN CENTRAL EUROPE 16 (2020) 1
281
Curry, J. L. – Urban, J. B. (2003): The Left Transformed in Post­‑Communist Societies: the Cases of 
East­‑Central Europe, Russia, and Ukraine. Lanham: Rowman & Littlefield.
Däubler, T. – Benoit, K. – Mikhaylov, S. – Laver, M. (2012): Natural Sentences as Valid Units 
for Coded Political Texts. British Journal of Political Science 42(4): 937–951. doi:10.1017/
S0007123412000105
Delwit, P. (c2005): Social Democracy in Europe. Bruxelles: Editions de l’Université de Bruxelles.
Hloušek, V. – Kopeček, L. (2016): Origin, Ideology and Transformation of Political Parties: East­
‑Central and Western Europe Compared. London and New York: Routledge.
Keman, H. (2008). Contemporary approaches to social democracy: Old wines in new bottles. 
European Political Science 7(4): 494–506. doi: http://dx.doi.org/10.1057/eps.2008. 42.
Keman, H. (2017). Social Democracy: A Comparative Account of the Left­‑Wing Party Family. 
Routledge.
Kopeček, L. (2005): Trajectories of the Left: Social Democracy and (Ex-)Communist Parties in 
Contemporary Europe: Between Past and Future. Brno: CDK.
Kopeček, L. (2007): Politické strany na Slovensku 1989 až 2006. Brno: CDK.
Koubek, J. – Polášek, M. (2017): Strengthening Social Democracy in the Visegrad Countries: The 
Czech Social Democratic Party. Prague: Friedrich­‑Ebert­‑Stiftung e.V. Available at: http://library.
fes.de/pdf­‑files/bueros/prag/13254.pdf (15 September 2019).
Krašovec, A. – Cabada, L. (2018): Adaptability of political parties to the economic and financial 
crisis? Some evidence from Slovenia and the Czech Republic. Annales, Series Historia et So­
ciologia 28(4): 865–880, doi: 0.19233/ASHS.2018. 53.
Lightfoot, S. (2005). Europeanizing social democracy?: the rise of the Party of European Social­
ists. Routledge.
Lightfoot, S. (2005): Europeanizing Social Democracy? The Rise of the Party of European Social­
ists. London and New York: Routledge.
Lipset, S. M., & Rokkan, S. (Eds.). (1967). Party systems and voter alignments: Cross­‑national 
perspectives (Vol. 7). Free press.
Mair, P. – Mudde, C. (1998): The Party Family and its Study. Annual Review of Political Science, 
1(1), 211–229.
Merz, N. – Regel, S. – Lewandowski, J. (2016): The Manifesto Corpus: A New Resource for Research 
on Political Parties and Quantitative Text Analysis. Research & Politics 3(2). 2053168016643346.
Meyer, T. – Hinchman, L. (2007): The Theory of Social Democracy. Cambridge: Polity Press.
Meyer, T. (2000). Transformace sociální demokracie: Strana na cestě do 21. století. Brno: Doplněk.
Pang, B. – Lee, L. (2008): Opinion Mining and Sentiment Analysis. Foundations and Trends in 
Information Retrieval 2(1–2): 1–135.
Pierson, C. (2001). Hard Choices: Social Democracy in the 21st Century. Cambridge: Polity.
Rourke, L. – Anderson, T. – Garrison, D. – Archer, W. (2001): ‘Methodological Issues in the Content 
Analysis of Computer Conference Transcripts.’ International Journal of Artificial Intelligence 
in Education (IJAIED), 12.
282
Application of natural language processing to the electoral manifestos of social democratic …  Ivan Bielik
Rudkowsky, E. – Haselmayer, M. – Wastian, M. – Jenny, M. – Emrich, Š. – Sedlmair, M. (2018): More 
than Bags of Words: Sentiment Analysis with Word Embeddings. Communication Methods 
and Measures 12(2–3): 140–157.
Sassoon, D. (2014). One hundred years of socialism: the west european left in the twentieth 
century (New ed.). London: I.B. Tauris.
Slapin, J. B. – Proksch, S. O. (2008): A Scaling Model for Estimating Time­‑Series Party Positions 
from Texts. American Journal of Political Science 52(3): 705–722.
Thomson, S. (2000). The Social Democratic Dilemma: Ideology, Governance and Globalization. 
Springer.
Volkens, A. – Bara, J. – Budge, I. (2009): Data Quality in Content Analysis. The Case of the 
Comparative Manifestos Project. Historical Social Research / Historische Sozialforschung, 
34(1): 234–251.
White, S. – Lewis, P. G. – Batt, J. (eds.). (2013): Developments in Central and East European Politics 
5. Basingstoke, Hampshire: Palgrave Macmillan.
Young, L. – Soroka, S. (2012): Affective News: The Automated Coding of Sentiment in Political 
Texts.’ Political Communication 29(2): 205–231.
Zirn, C. – Glavaš, G. – Nanni, F. – Eichorts, J. – Stuckenschmidt, H. (2016): Classifying Topics and 
Detecting Topic Shifts in Political Manifestos. Proceedings of the International Conference 
on the Advances in Computational Analysis of Political Text (PolText 2016). 88–93, Dubrovnik, 
Croatia, 14–16 July 2016.
Ivan Bielik is a PhD student at Masaryk University in Brno. His research topics 
cover party politics and policy analysis. Email: ivanb@mail.muni.cz

