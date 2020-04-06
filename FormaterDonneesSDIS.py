import string
#Développement par Charles-Henry de Guillebon - Esri France
#Mars 2020 (fichier CSV à transformer pour @KMA)
#Objectif : passer des données en colonne pour chaque caserne dans une ligne par date avec le nom de la caserne
#En entrée, fournir le nom du fichier sans son extension CSV
#En sortie, fichier CSV avec le même nom ajouté de "_ok"
version = "1.0.1" #correction 26/3/20 : ne pas écrire quand il n'y a pas d'intervention, 0 ou nul
#version = "1.0.0" #1ère version du 26/03/2020

#Lire un fichier en entrée et création du fichier de sortie en écriture
def traiterFichierCSV( ficcsv ):
	cheminE = ficcsv + ".csv"
	cheminS = ficcsv + "_OK.csv"
	try:
		fichierE = open(cheminE, "r")
	except:
		print "Version", version, ": fichier", cheminE, "inexistant !","\n","Version", version, ": essayer de nouveau...","\n"
		return None #sortir
	fichierS = open(cheminS, "w")
	
	#Lire la liste des casernes sur la 1ère ligne du fichier CSV
	ligne = fichierE.readline() #lecture de la 1ère ligne pour l'entête avec la liste des casernes
	txt = ligne.strip() #.strip = supprimer les caracteres speciaux a la fin comme le CRLF
	casernes = txt.split(",")
	casernes = casernes[1:] #Enlever le libellé Date pour garder que les libellés de chaque caserne

	#Ecrire l'entête du fichier CSV de sortie
	fichierS.write("date,caserne,interventions" + "\n")

	#Boucle de lecture ligne a ligne après lecture de l'entête
	for ligne in fichierE:
		txt = ligne.strip() #.strip = supprimer les caracteres speciaux a la fin comme le CRLF
		msg = traiterLigne(txt, casernes, fichierS) #texte corrigé

	fichierE.close()
	fichierS.close()
	return cheminS

#Traiter une ligne
def traiterLigne( ligne, casernes, fichierS ):

	#Aucun texte ou ligne vide
	if ligne is None : return ""
	if len(ligne) == 0 : return ""

	#Récupérer les valeurs d'une ligne
	valeurs = ligne.split(",")
	txtdate = valeurs[0] #Date
	valeurs = valeurs[1:]

	#Boucle sur les casernes
	i = 0
	for caserne in casernes:
		interventions = valeurs[i]
		if len(interventions) > 0 :
			if interventions > 0 : #écrire que si il y a des interventions !
				txt = txtdate + "," + caserne + "," + valeurs[i]
				fichierS.write(txt + "\n")
		i += 1

	return "Ligne OK"


#==================
#DEBUT DU PROGRAMME
#==================

#Boucle pour demander le nom du fichier CSV à tratier
while True:
  #Demander le nom du fichier CSV en entrée
  ficcsv = raw_input("Version " + version + ", entrer le nom du fichier CSV (SANS SON EXTENSION) : ")
  if (len(ficcsv) < 1 or string.upper(ficcsv) == "FIN") : break
  #Lancer le traitement du fichier en entrée
  retour = traiterFichierCSV(ficcsv)
  if not (retour is None) : print "Version", version, ": fichier CSV", retour, "ok !", "\n"
#FIN DU PROGRAMME
#quit()
print "Version", version, ": fin du programme."

