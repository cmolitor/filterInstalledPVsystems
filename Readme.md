This script "filter.py" filters all registered PV systems in Germany by a specific zip codes (Postleitzahlen).

So you can put all zip codes of a certain area you are interested in, in a file and the scripts returns the number of the PV system in this area.

The zip codes are provided in the file "PLZ_tmpl.txt". Rename and change accordingly in the script.

The list of PV systems with zip codes is provided by Bundesnetzagentur at the following web site:
https://www.bundesnetzagentur.de/DE/Sachgebiete/ElektrizitaetundGas/Unternehmen_Institutionen/ErneuerbareEnergien/Photovoltaik/DatenMeldgn_EEG-VergSaetze/DatenMeldgn_EEG-VergSaetze_node.html#doc405794bodyText2

I copied all the data provided in different files into the file "200901-201612.csv". The file contains PV systems registered installed between January 2009 and December 2016.