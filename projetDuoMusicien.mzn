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

array[MUSICIEN] of var MUSICIEN : duo;

array[MUSICIEN] of var NB_HEURE : nb_heure = 			[3,	3,	2,	3,	5,	3,	3,	3,	2,	2,	3,	3];
array[MUSICIEN] of var NIVEAU : niveau = 				[2,	1,	5,	2,	2,	3,	5,	5,	5,	2,	2,	4];
array[MUSICIEN] of var NB_HEURE_MIN : nb_heure_min = 	[2,	1,	1,	1,	3,	1,	1,	3,	2,	1,	3,	3];
array[MUSICIEN] of var NB_HEURE_MAX : nb_heure_max = 	[4,	5,	2,	4,	6,	5,	5,	3,	3,	5,	5,	6];
array[MUSICIEN] of var NIVEAU_MIN : niveau_min = 		[1,	1,	3,	1,	1,	1,	1,	5,	4,	1,	1,	2];
array[MUSICIEN] of var NIVEAU_MAX : niveau_max = 		[4,	2,	5,	5,	3,	3,	5,	5,	5,	3,	3,	5];
array[MUSICIEN] of var NB_STYLE_MIN : nb_style_min = 	[2,	3,	1,	1,	2,	2,	1,	1,	1,	1,	2,	1];
array[MUSICIEN] of set of STYLE : style = [
														{Rock, Metal, Jazz},
														{Jazz, Pop, Classique, Rock, Funk},
														{RnB, Rap,Classique},
														{Pop, Punk, Electro},
														{Classique, Metal, Jazz},
														{Punk, Rock, Classique, Jazz},
														{Pop, Rock, Jazz, Classique},
														{Classique},
														{Classique, Jazz},
														{Jazz, Electro},
														{Jazz, Rap, Funk, Rock},
														{Metal, Pop, Electro, Jazz}
];

array[MUSICIEN] of INSTRUMENT : instrument = [
														Guitare,
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

constraint all_different(duo);

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


/*le niveau de chaque musicien du duo doit être dans l’intervalle de niveau accepté par
l’autre musicien*/
constraint forall(m in MUSICIEN)(niveau[m] in niveau_min[duo[m]]..niveau_max[duo[m]]);
constraint forall(m in MUSICIEN)(niveau[duo[m]] in niveau_min[m]..niveau_max[m]);

/*le duo est consistant : il s’agit donc d’un matching parfait, c’est à dire que si m est associé à m’ alors m’ est associé aussi à m*/
constraint forall(m, n in MUSICIEN where n == duo[m]) (m == duo[n]);

solve satisfy;

output[
          "\(p) <-> \(duo[p]) \n" | p in MUSICIEN
];