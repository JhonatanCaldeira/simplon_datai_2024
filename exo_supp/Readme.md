Exercice 6 - Traitement des valeurs manquantes :
- Téléchargez le fichier CSV "sales_data.csv" à partir du lien suivant : https://github.com/ine-rmotr-curriculum/FreeCodeCamp-Pandas-Real-Life-Example/blob/master/data/sales_data.csv
- Chargez le fichier dans un DataFrame nommé "sales_df".
- Affichez le nombre de valeurs manquantes dans chaque colonne du DataFrame.

Exercice 7 - Suppression des doublons :
- Téléchargez le fichier CSV "GlobalLandTemperaturesByMajorCity.csv" à partir du lien suivant : https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByMajorCity.csv
- Chargez le fichier dans un DataFrame nommé "duplicate_df".
- Supprimez les lignes en double du DataFrame.
- Afficher la taille des Dataframes avant et après

Exercice 8 - Remplacement des valeurs incorrectes :
- Chargez le fichier dans un DataFrame nommé "temperature_df".
- Remplacez les valeurs négatives dans la colonne "AverageTemperature" par la valeur absolue de ces valeurs.
- Afficher le minimum avant et après

Exercice 9 - Extraction de données :
- Téléchargez le fichier CSV "email_jetable.csv" à partir du lien suivant : https://sql.sh/ressources/sql-email-jetable/email_jetable.csv
- Chargez le fichier dans un DataFrame nommé "emails_df".
- Donnez un nom aux colonnes: [index, emails]
- Créez une nouvelle colonne "extension" contenant uniquement l’extension du domaines des adresses e-mail (com, fr etc…).
- Affichez les valeurs unique de la colonne “extension”

Exercice 10 - Transformation de données :
- Téléchargez le fichier CSV "student_grades.csv" à partir du lien suivant : https://raw.githubusercontent.com/datasciencedojo/datasets/master/student_grades.csv
- Chargez le fichier dans un DataFrame nommé "grades_df".
- Donnez un nom aux colonnes: ['ID','salle','note']
- Ajoutez une colonne note_dec qui contient les notes de 0 à 17 (E- à A+)
- Convertissez les notes pour qu’elles soient entre 0 et 20 en appliquant une fonctino
- Ajoutez une colonne "result" qui contiendra "Réussite" pour les étudiants ayant une note supérieure ou égale à 10, sinon "Échec".

Exercice 1 - Visualisation des notes des étudiants :

a) Chargez le fichier "student_grades.csv" dans un DataFrame nommé "grades_df".

b) Utilisez Seaborn pour créer un histogramme représentant la distribution des notes des étudiants.

Exercice 2 - Comparaison des notes en fonction des salles :

a) Utilisez le DataFrame "grades_df" pour créer un graphique à barres montrant la moyenne des notes des étudiants pour chaque salle.

Exercice 3 - Comparaison des notes en fonction du statut de réussite :

a) Utilisez le DataFrame "grades_df" pour créer un graphique à barres montrant le nombre d'étudiants ayant réussi et échoué.

Exercice 4 - Visualisation de la corrélation entre les variables :

a) Chargez le fichier "titanic.csv" dans un DataFrame nommé "titanic_df".

b) Utilisez Seaborn pour créer une matrice de corrélation pour les variables numériques du DataFrame "titanic_df".

Exercice 5 - Comparaison des tarifs en fonction du statut de survie :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte (boxplot) montrant la distribution des tarifs payés par les passagers en fonction de leur statut de survie (survécu ou non).

Exercice 6 - Visualisation des âges des passagers :

a) Utilisez le DataFrame "titanic_df" pour créer un histogramme représentant la distribution des âges des passagers.

Exercice 7 - Comparaison des âges en fonction du statut de survie :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des âges des passagers en fonction de leur statut de survie.

Exercice 8 - Visualisation de la répartition des tarifs :

a) Utilisez le DataFrame "titanic_df" pour créer un histogramme représentant la répartition des tarifs payés par les passagers.

Exercice 9 - Comparaison des tarifs en fonction de la classe :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction de leur classe (1ère, 2ème ou 3ème classe).

Exercice 10 - Visualisation de la répartition du genre des passagers

a) Utilisation du DataFrame "titanic_df" pour créer un histogramme représentant la répartition des genres.

Exercice 11 - Comparaison des âges des étudiants en fonction du statut de réussite :
D'accord, merci de me fournir les noms corrects des colonnes du fichier CSV "sales_data.csv". Voici l'exercice mis à jour en utilisant les bonnes colonnes :

Exercice sur le jeu de données "sales_data" :

Le jeu de données "sales_data.csv" contient des informations sur les ventes de produits dans un magasin. Chaque ligne représente une transaction avec les colonnes suivantes :

- `Date`: La date de la transaction.
- `Product`: Le nom du produit vendu.
- `Unit_Price`: Le prix unitaire du produit.
- `Order_Quantity`: Le nombre d'unités vendues.

Votre tâche est de réaliser les étapes suivantes :

a) Chargez le fichier "sales_data.csv" dans un DataFrame nommé "sales_df".
b) Affichez les 10 premières lignes du DataFrame pour visualiser les données.
c) Calculez le chiffre d'affaires total réalisé sur l'ensemble des transactions.
d) Tracez un graphique à barres montrant les 5 produits les plus vendus (en termes de quantité) avec le nom du produit sur l'axe des x et la quantité vendue sur l'axe des y.

Exercice 12 - Visualisation de la répartition des notes des étudiants :

a) Utilisez le DataFrame "grades_df" pour créer un histogramme représentant la répartition des notes des étudiants.

Exercice 13 - Comparaison des notes des étudiants en fonction de la salle :

a) Utilisez le DataFrame "grades_df" pour créer un graphique en boîte montrant la distribution des notes des étudiants en fonction de la salle.

Exercice 14 - Visualisation des tarifs des passagers en fonction de la classe :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction de leur classe.

Exercice 15 - Comparaison des tarifs des passagers en fonction du port d'embarquement :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction du port d'embarquement (C = Cherbourg, Q = Queenstown, S = Southampton).

Exercice 16 - Visualisation de la répartition des tarifs des passagers :

a) Utilisez le DataFrame "titanic_df" pour créer un histogramme représentant la répartition des tarifs payés par les passagers.

Exercice 17 - Comparaison des tarifs des passagers en fonction du sexe :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction du sexe (homme ou femme).

Exercice 18 - Visualisation des tarifs des passagers en fonction du statut de survie :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction de leur statut de survie (survécu ou non).

Exercice 19 - Comparaison des âges des passagers en fonction du port d'embarquement :

a) Utilisez le DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des âges des passagers en fonction du port d'embarquement.

Exercice 20 - Visualisation de la répartition des âges des passagers :

a) Utilisez le DataFrame "titanic_df" pour créer un histogramme représentant la répartition des âges des passagers.