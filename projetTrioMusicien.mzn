%___________________________________________________________________
%    Nom :				BARRO,		SYLLA,		TOURE
%	 Prénom :       	Juliette,	Mohamed,	Boubacar
%    Date :             16/11/2022
%    Master 2 Informatique à la faculté de sciences d'Angers    
%___________________________________________________________________
%    Objectif : Réalisation du Modèle 2 permettant d'assurer la
%    formation d'un trio de musiciens
%___________________________________________________________________

include "globals.mzn";

enum MUSICIEN ;
enum STYLE ;
enum INSTRUMENT ;
enum VILLE ;

set of int : NB_HEURE;
set of int : NIVEAU;
set of int : NB_HEURE_MIN;
set of int : NB_HEURE_MAX;
set of int : NIVEAU_MIN;
set of int : NIVEAU_MAX;
set of int : NB_STYLE_MIN;

array[MUSICIEN] of var MUSICIEN : trio1;
array[MUSICIEN] of var MUSICIEN : trio2;
array[MUSICIEN] of var NB_HEURE : nb_heure;
array[MUSICIEN] of var NIVEAU : niveau;
array[MUSICIEN] of var NB_HEURE_MIN : nb_heure_min ;
array[MUSICIEN] of var NB_HEURE_MAX : nb_heure_max;
array[MUSICIEN] of var NIVEAU_MIN : niveau_min;
array[MUSICIEN] of var NIVEAU_MAX : niveau_max;
array[MUSICIEN] of var NB_STYLE_MIN : nb_style_min;
array[MUSICIEN] of var INSTRUMENT : instrument ;
array[MUSICIEN] of var VILLE : ville ;
array[MUSICIEN] of set of STYLE : style ;

/*=============================Les contraintes==========================*/
/*les trios doivent être differents*/
constraint forall(m in MUSICIEN) (m != trio1[m] /\ m != trio2[m] /\ trio1[m] != trio2[m]);

/*Les trios habitent la même ville*/
constraint forall(m in MUSICIEN) (ville[m] == ville[trio1[m]] /\ ville[m] == ville[trio2[m]]);

/*le nombre d’heures voulues doit être dans le créneau Min - Max souhaité par l’autre*/
/*
constraint forall(m in MUSICIEN)(nb_heure[m] in nb_heure_min[trio1[m]]..nb_heure_max[trio1[m]] /\ nb_heure[m] in nb_heure_min[trio2[m]]..nb_heure_max[trio2[m]]);
constraint forall(m in MUSICIEN)(nb_heure[trio1[m]] in nb_heure_min[m]..nb_heure_max[m] /\ nb_heure[trio1[m]] in nb_heure_min[trio2[m]]..nb_heure_max[trio2[m]]);
constraint forall(m in MUSICIEN)(nb_heure[trio2[m]] in nb_heure_min[m]..nb_heure_max[m] /\ nb_heure[trio2[m]] in nb_heure_min[trio1[m]]..nb_heure_max[trio1[m]]);
*/
/*le nombre de style commun doit respecter les exigences de chacun*/
constraint forall(m in MUSICIEN)(card(style[m] intersect style[trio1[m]]) >= 1);
constraint forall(m in MUSICIEN)(card(style[m] intersect style[trio2[m]]) >= 1);
constraint forall(m in MUSICIEN)(card(style[trio1[m]] intersect style[trio2[m]]) >= 1);

/*deux musiciens jouant du même instrument ne peuvent former un trio*/
constraint forall(m in MUSICIEN)(instrument[m] != instrument[trio1[m]] /\ instrument[m] != instrument[trio2[m]] /\ instrument[trio1[m]] != instrument[trio2[m]]);

/*le niveau de chaque musicien du trio doit être dans l’intervalle de niveau accepté par l’autre musicien*/
constraint forall(m in MUSICIEN)(niveau[m] in niveau_min[trio1[m]]..niveau_max[trio1[m]] /\ niveau[trio1[m]] in niveau_min[m]..niveau_max[m]);
constraint forall(m in MUSICIEN)(niveau[m] in niveau_min[trio2[m]]..niveau_max[trio2[m]] /\ niveau[trio2[m]] in niveau_min[m]..niveau_max[m]);
constraint forall(m in MUSICIEN)(niveau[trio1[m]] in niveau_min[trio2[m]]..niveau_max[trio2[m]] /\ niveau[trio2[m]] in niveau_min[trio1[m]]..niveau_max[trio1[m]]);

/*le trio est consistant : il s’agit donc d’un matching parfait, c’est à dire que si m est associé à m’ alors m’ est associé aussi à m*/
constraint forall(m, n, o in MUSICIEN where (n == trio1[m] /\ o == trio2[m]) \/ (n == trio2[m] /\ o == trio1[m])) ((m == trio1[n] \/ m == trio2[n]) /\ (m == trio2[o] \/ m == trio1[o]));

/*Les musiciens doivent être différents de leur duos*/
constraint all_different(trio1);
constraint all_different(trio2);

solve satisfy;

output[
          "{ \(p) | \(trio1[p])  | \(trio2[p]) }\n" | p in MUSICIEN
];