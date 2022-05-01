# m1_traduction_auto
TP 1 - Analyse linguistique avec la plateforme Stanford CoreNLP

Les étapes du TP1:

2. Evaluation:

a.Lancement du POS tagger sur le fichier « wsj_0010_sample.txt » : 
./stanford-postagger.sh models/english-left3words-distsim.tagger
wsj_0010_sample.txt > wsj_0010_sample.txt.pos.stanford

b.Script Python qui permet de convertir le fichier de référence
wsj_0010_sample.pos.ref au format de la sortie du Stanford POS tagger.

script: I2b_script.py
Je lance le script sur le terminal:  python3 2d_script.py ./wsj_0010_sample.txt.pos.stanford ./wsj_0010_sample.pos.stanford.ref
Résultat de sortie : 
wsj_0010_sample.pos.stanford.ref

c. Calcul de la précision de ce POS tagger en utilisant les étiquettes PTB:
Résultat:
I2c_result_evaluate.txt


d. Remplacement à l’aide d’un programme Python les étiquettes Penn TreeBank des fichiers
wsj_0010_sample.txt.pos.stanford et
wsj_0010_sample.pos.stanford.ref

Script : 12d_script
Je lance le script sue le terminal: python3 2d_script.py 
python3 2d_script.py ./wsj_0010_sample.txt.pos.stanford ./wsj_0010_sample.txt.pos.univ.stanford
Résultat: 
wsj_0010_sample.txt.pos.univ.stanford


e. Calcul de  la précision de ce POS tagger : 
I2e_result_evaluate.txt

f.Conclusion:

II.2. Extraction d’entités nommées:
Script : 
II2_script.py
Résultat:
wsj_0010_sample.txt.ner.stanford.output