include "globals.mzn";

enum MUSICIEN = 	{Alex,			Billie,			Chris,		Dora,		Emile,			Franck,		Gisele,		Horst, 		Iris, 		Jean,		Karl,		Lisa};
enum STYLE = 		{Rock,			Metal,			Jazz, 		Pop, 		Classique,		Funk,		RnB,		Rap, 		Punk, 		Electro};
enum INSTRUMENT = 	{Guitare,		Batterie,		Violon,		Piano, 		Basse};
enum VILLE = 		{Angers,		Nantes};

set of int : NB_HEURE = 		2..5;
set of int : NIVEAU = 			1..5;
set of int : NB_HEURE_MIN = 	1..3;
set of int : NB_HEURE_MAX = 	2..6;
set of int : NIVEAU_MIN = 		1..5;
set of int : NIVEAU_MAX = 		2..5;
set of int : NB_STYLE_MIN = 	1..3;

array[MUSICIEN] of var MUSICIEN : trio1;
array[MUSICIEN] of var MUSICIEN : trio2;
array[MUSICIEN] of var NB_HEURE : nb_heure = 			[3,	3,	2,	3,	5,	3,	3,	3,	2,	2,	3,	3];
array[MUSICIEN] of var NIVEAU : niveau = 				[2,	3,	5,	2,	2,	3,	3,	3,	5,	2,	2,	4];
array[MUSICIEN] of var NB_HEURE_MIN : nb_heure_min = 	[2,	1,	1,	1,	2,	1,	1,	2,	2,	1,	2,	2];
array[MUSICIEN] of var NB_HEURE_MAX : nb_heure_max = 	[5,	5,	5,	4,	6,	5,	5,	3,	3,	5,	5,	6];
array[MUSICIEN] of var NIVEAU_MIN : niveau_min = 		[1,	1,	3,	1,	1,	1,	1,	2,	2,	1,	1,	2];
array[MUSICIEN] of var NIVEAU_MAX : niveau_max = 		[5,	4,	5,	5,	3,	3,	5,	5,	5,	3,	3,	5];
array[MUSICIEN] of var NB_STYLE_MIN : nb_style_min = 	[2,	3,	1,	1,	2,	2,	1,	1,	1,	1,	2,	1];
array[MUSICIEN] of set of STYLE : style = [
														{Rock,		Metal,		Jazz},
														{Jazz,		Pop,		Classique,	Rock,	Funk},
														{RnB,		Rap,		Classique},
														{Pop,		Punk,		Electro},
														{Classique,	Metal,		Jazz},
														{Punk,		Rock,		Classique,	Jazz},
														{Pop,		Rock,		Jazz,		Classique},
														{Classique},
														{Classique,	Jazz},
														{Jazz, 		Electro},
														{Jazz,		Rap,		Funk,		Rock,	Electro},
														{Metal,		Pop,		Electro,	Jazz,	Classique}
];

array[MUSICIEN] of INSTRUMENT : instrument = [
														Basse,
														Batterie,
														Guitare,
														Batterie,
														Violon,
														Guitare,
														Piano,
														Violon,
														Piano,
														Piano,
														Basse,
														Basse
];

array[MUSICIEN] of VILLE : ville = [
														Angers,
														Nantes,
														Angers,
														Nantes,
														Angers,
														Angers,
														Nantes,
														Nantes,
														Angers,
														Nantes,
														Nantes,
														Angers
];

/*=============================Les contraintes==========================*/
%constraint forall(m in MUSICIEN)(card(trio[m]) == 2);

constraint all_different(trio1);
constraint all_different(trio2);

% les trios doivent être differents 
constraint forall(m in MUSICIEN) (m != trio1[m] /\ m != trio2[m] /\ trio1[m] != trio2[m]);

/*Les trios habitent la même ville*/
constraint forall(m in MUSICIEN) (ville[m] == ville[trio1[m]] /\ ville[m] == ville[trio2[m]]);

/*le nombre d’heures voulues doit être dans le créneau Min - Max souhaité par l’autre*/
constraint forall(m in MUSICIEN)(nb_heure[m] in nb_heure_min[trio1[m]]..nb_heure_max[trio1[m]] /\ nb_heure[m] in nb_heure_min[trio2[m]]..nb_heure_max[trio2[m]]);
constraint forall(m in MUSICIEN)(nb_heure[trio1[m]] in nb_heure_min[m]..nb_heure_max[m] /\ nb_heure[trio1[m]] in nb_heure_min[trio2[m]]..nb_heure_max[trio2[m]]);
constraint forall(m in MUSICIEN)(nb_heure[trio2[m]] in nb_heure_min[m]..nb_heure_max[m] /\ nb_heure[trio2[m]] in nb_heure_min[trio1[m]]..nb_heure_max[trio1[m]]);

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

solve satisfy;

output[
          "{ \(p) | \(trio1[p])  | \(trio2[p]) }\n" | p in MUSICIEN
];