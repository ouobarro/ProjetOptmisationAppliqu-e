%___________________________________________________________________
%    Nom :				BARRO, SYLLA, TOURE
%	 Prénom :       	Juliette, Mohamed, Boubacar
%    Date :             16/11/2022
%    Master 2 Informatique à la faculté de sciences d'Angers    
%___________________________________________________________________
%    Objectif : Réalisation du Modèle 1 permettant d'assurer la
%    formation d'un duo de musiciens
%___________________________________________________________________

include "globals.mzn";

enum MUSICIEN;
enum STYLE;
enum INSTRUMENT;
enum VILLE;

set of int : NB_HEURE;
set of int : NIVEAU;
set of int : NB_HEURE_MIN;
set of int : NB_HEURE_MAX;
set of int : NIVEAU_MIN;
set of int : NIVEAU_MAX;
set of int : NB_STYLE_MIN;

array[MUSICIEN] of var MUSICIEN : duo;
array[MUSICIEN] of var NB_HEURE : nb_heure;
array[MUSICIEN] of var NIVEAU : niveau;
array[MUSICIEN] of var NB_HEURE_MIN : nb_heure_min;
array[MUSICIEN] of var NB_HEURE_MAX : nb_heure_max;
array[MUSICIEN] of var NIVEAU_MIN : niveau_min;
array[MUSICIEN] of var NIVEAU_MAX : niveau_max;
array[MUSICIEN] of var NB_STYLE_MIN : nb_style_min;
array[MUSICIEN] of var INSTRUMENT : instrument;
array[MUSICIEN] of var VILLE : ville;
array[MUSICIEN] of set of STYLE : style;

/*=============================Les contraintes==========================*/
/*Les musiciens doivent être différents de leur duos*/
constraint forall(m in MUSICIEN)(m != duo[m]);
  
/*Les duos habitent la même ville*/
constraint forall(m in MUSICIEN)(ville[m] == ville[duo[m]]);

/*le nombre d’heures voulues doit être dans le créneau Min - Max souhaité par l’autre*/
constraint forall(m in MUSICIEN)(nb_heure[m] in nb_heure_min[duo[m]]..nb_heure_max[duo[m]]);
constraint forall(m in MUSICIEN)(nb_heure[duo[m]] in nb_heure_min[m]..nb_heure_max[m]);

/*le nombre de style commun doit respecter les exigences de chacun*/
constraint forall(m in MUSICIEN)(card(style[m] intersect style[duo[m]]) >= nb_style_min[m]);
constraint forall(m in MUSICIEN)(card(style[m] intersect style[duo[m]]) >= nb_style_min[duo[m]]);

/*deux musiciens jouant du même instrument ne peuvent former un duo*/
constraint forall(m in MUSICIEN)(instrument[m] != instrument[duo[m]]);


/*le niveau de chaque musicien du duo doit être dans l’intervalle de niveau accepté par l’autre musicien*/
constraint forall(m in MUSICIEN)(niveau[m] in niveau_min[duo[m]]..niveau_max[duo[m]]);
constraint forall(m in MUSICIEN)(niveau[duo[m]] in niveau_min[m]..niveau_max[m]);

/*le duo est consistant : il s’agit donc d’un matching parfait, c’est à dire que si m est associé à m’ alors m’ est associé aussi à m*/
constraint forall(m, n in MUSICIEN where n == duo[m]) (m == duo[n]);

constraint all_different(duo);

solve satisfy;

output[
          "\(p) <-> \(duo[p]) \n" | p in MUSICIEN
];