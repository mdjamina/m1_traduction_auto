# m1_traduction_auto

TP 2 - - Analyse linguistique avec le framework NLTK
Les étapes du TP_2:

1.Evaluation de l’analyse morpho-syntaxique de la plateforme NLTK:

1.Programme Python utilisant le package pos_tag pour désambiguïser morpho-
syntaxiquement le texte du fichier wsj_0010_sample.txt.

 Script: script_1.py
 Résultat:
 wsj_0010_sample.txt.pos.nltk

1.2. Evaluation à l’aide des étiquettes Penn TreeBank (PTB):


1.3.Evaluation à l’aide des étiquettes universelles :
a.programme Python les étiquettes Penn TreeBank des fichiers « wsj_0010_sample.txt.pos.nltk » et « wsj_0010_sample.txt.pos.ref » par les
étiquettes universelles en utilisant la table de correspondance « POSTags_PTB_Universal.txt ».
Script:


2.Utilisation de la plateforme NLTK pour l’analyse syntaxique
2.1. Ecrire un programme Python utilisant le package parse pour extraire les mots composés
(chunks) ayant la structure syntaxique Déterminant-Adjectif-Nom (grammar =
"Compound: {<DT>?<JJ>*<NN>}")

script:
script2_1_analyse_syntaxique.py

Résultat:

wsj_0010_sample.txt.chk.nltk

2. Généraliser le programme Python  pour extraire les mots composés:
Adjectif-Nom
Nom-Nom
Adjectif-Nom-Nom
Adjectif-Adjectif-Nom

script: 
script2_1_analyse_syntax.py



3.Utilisation de la plateforme NLTK pour l’extraction d’entités nommées
3.1: programme Python utilisant le package ne_chunk pour extraire les entités
nommées: 
script: script3_a.py
Résultat:
wsj_0010_sample.txt.ne.nltk

3.2. Ecrire un programme Python permettant de convertir les étiquettes des entités nommées:
script3_2.a.py
Résultat: 
wsj_0010_sample.txt.ne.standard

script3_2.b.py
Résultat: 
wsj_0010_sample.txt.ne.bio


3. Utiliser les deux programmes Python des questions 1 et 2 pour l’analyse du fichier
formal-tst.NE.key.04oct95_sample.txt.

scripts:
script3_2.a.py
script3_2.b.py 
Je lance sur le terminal : 
python3 script3_2.a.py formal-tst.NE.key.04oct95_sample.txt.ne.nltk 
python3 script3_2.b.py formal-tst.NE.key.04oct95_sample.txt.ne.standard






