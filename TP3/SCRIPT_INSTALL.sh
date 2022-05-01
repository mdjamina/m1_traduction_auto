#I. INSTALLATION
#===============



export HOME_TOOLS=/home/amina/tools



#0) Prepare the installation of software
#--------------------------------------

sudo rm /var/lib/dpkg/lock
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo apt-get update


#1) Installation de packages logiciels de compilation et d'installation
#----------------------------------------------------------------------
		
sudo apt-get install g++

sudo apt-get install git

sudo apt-get install subversion automake libtool zlib1g-dev libboost-all-dev libbz2-dev liblzma-dev python-dev

#(for tcmalloc)
sudo apt-get install libgoogle-perftools-dev 

#2) Installation de Boost (Dans le cas où les commandes précédentes n'ont pas donné les résultats souhaités)
#-----------------------------------------------------------------------------------------------------------

#a. Installer libboost-all-dev

sudo apt-get install libboost-all-dev

#b. Installer les fichiers d'entête (e.g.: bzlib.h)

sudo apt-get install libbz2-dev

#c. Récupérer la librairie boost (Par exemple: boost_1_57_0.tar.gz => https://sourceforge.net/projects/boost/files/boost/1.57.0/boost_1_57_0.tar.gz/download) et l'installer

tar zxvf boost_1_57_0.tar.gz

cd boost_1_57_0/

./bootstrap.sh

./b2 -j8 --prefix=$HOME_TOOLS/boost_1_57_0 --libdir=$HOME_TOOLS/boost_1_57_0/lib64 --layout=system link=static install || echo FAILURE


#Remarque:
#Le répertoire d'installation de la librairie Boost est $HOME_TP3/boost_1_57_0 ($PWD)


$HOME_TOOLS/boost_1_57_0

#3) Installation de Moses
#------------------------

#a. Récupérer Moses

git clone https://github.com/moses-smt/mosesdecoder.git


#b. Installer Moses

cd mosesdecoder/

./bjam --with-boost=$HOME_TOOLS/boost_1_57_0 -j8

mkdir tools



#4) Installation de GIZA++
#-------------------------

#a. Récupérer GIZA++ (à partir de https://code.google.com/archive/p/moses-suite/downloads)

git clone https://github.com/moses-smt/giza-pp.git

#b. Installer GIZA++

cd giza-pp/

make


#c. Utilisation des binaires de GIZA++ par Moses lors de la construction du modèle de traduction 

#Sur le répoertoire /home/semmar/Projects/Moses/mosesdecoder

cd $HOME_TOOLS/mosesdecoder/tools


cp $HOME_TOOLS/giza-pp/GIZA++-v2/GIZA++ $HOME_TOOLS/giza-pp/GIZA++-v2/snt2cooc.out $HOME_TOOLS/giza-pp/mkcls-v2/mkcls .







#Exemple de lancement de Giza++:

#1. Sur le répertoire $HOME_TP3

source Moses.env

#2. Sur le répertoire $HOME_TP3/Experiments/WordAlignment

plain2snt.out Europarl_dev_1k.en Europarl_dev_1k.fr

#Résultat:
#Europarl_dev_1k.en_Europarl_dev_1k.fr.snt
#Europarl_dev_1k.en.vcb
#Europarl_dev_1k.fr_Europarl_dev_1k.en.snt
#Europarl_dev_1k.fr.vcb

#3. Sur le répertoire $HOME_TP3/Experiments/WordAlignment

mkcls -pEuroparl_dev_1k.en -VEuroparl_dev_1k.en.vcb.classes

#(ou mkcls -c2 -n2 -pEuroparl_dev_1k.en -VEuroparl_dev_1k.en.vcb.classes => Generates 2 classes in 2 optimization runs for the corpus 'pEuroparl_dev_1k.en' and writes the classes in 'Europarl_dev_1k.en')

mkcls -pEuroparl_dev_1k.fr -VEuroparl_dev_1k.fr.vcb.classes

#Résultat:

#Europarl_dev_1k.en.vcb.classes
#Europarl_dev_1k.en.vcb.classes.cats
#Europarl_dev_1k.fr.vcb.classes
#Europarl_dev_1k.fr.vcb.classes.cats

#Remarque:
mkcls - a program for making word classes
#Usage: 
# mkcls [-nnum] [-ptrain] [-Vfile] opt

# -V output classes (Default: no file)
#-n number of optimization runs (Default: 1); larger number => better results
#-p filename of training corpus (Default: 'train')

#Example:
mkcls -c80 -n10 -pin -Vout opt => Generates 80 classes for the corpus 'in' and writes the classes in 'out'

#4. Sur le répertoire $HOME_TP3/Experiments/WordAlignment

snt2cooc.out Europarl_dev_1k.en.vcb Europarl_dev_1k.fr.vcb Europarl_dev_1k.en_Europarl_dev_1k.fr.snt > Europarl_dev_1k.en_Europarl_dev_1k.fr.snt.cooc

#Résultat:
#Europarl_dev_1k.en_Europarl_dev_1k.fr.snt.cooc

#5. Sur le répertoire /home/semmar/Projects/Moses/Experimentation/GIZA/WordAlignment/Small

#./GIZA++ -S [target_language_corpus].vcb -T [source_language_corpus].vcb -C [target_language_corpus]_[source_language_corpus].snt -o [prefix] -outputpath [output_folder]


GIZA++ -S Europarl_dev_1k.en.vcb –T Europarl_dev_1k.fr.vcb –C Europarl_dev_1k.en_Europarl_dev_1k.fr.snt -CoocurrenceFile Europarl_dev_1k.en_Europarl_dev_1k.fr.snt.cooc -o AlignmentResult

#Résultat:
#AlignmentResult.*

#Remarque:
#- La table de traduction se trouve dans le fichier "AlignmentResult.t3.final"




 ./bjam --with-irstlm=/home/amina/tools/irstlm-5.80.08/trunk