import blueprint
import random

al_ahly = blueprint.Team("Al Ahly FC", "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Al_Ahly_SC_logo.svg/640px-Al_Ahly_SC_logo.svg.png", "Egypt")
wydad = blueprint.Team("Wydad AC", "https://upload.wikimedia.org/wikipedia/en/thumb/1/18/Wydad_AC_crest_%282022%29.svg/1200px-Wydad_AC_crest_%282022%29.svg.png", "Marocco")
esperance = blueprint.Team ("Espérance Sportive de Tunis", "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Espérance_Sportive_de_Tunis_logo.png/250px-Espérance_Sportive_de_Tunis_logo.png", "Tunis")
mamelodi = blueprint.Team ("Mamelodi Sundowns FC", "https://upload.wikimedia.org/wikipedia/en/thumb/c/c6/Mamelodi_Sundowns_F.C.svg/1200px-Mamelodi_Sundowns_F.C.svg.png", "South Africa")
al_hilal = blueprint.Team("Al Hilal SFC", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Al-Hilal_SFC_logo.svg/1200px-Al-Hilal_SFC_logo.svg.png", "Saudi Arabia")
urawa = blueprint.Team ("Urawa Red Diamonds", "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Urawa_Red_Diamonds_logo.svg/640px-Urawa_Red_Diamonds_logo.svg.png", "Japan")
al_ain = blueprint.Team ("Al Ain FC", "https://upload.wikimedia.org/wikipedia/en/6/62/Al_Ain_FC_logo_2024.png", "United Arab Emirates")
ulsan = blueprint.Team("Ulsan HD", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b5/Ulsan_Hyundai_FC.svg/1200px-Ulsan_Hyundai_FC.svg.png", "Korea")
chelsea = blueprint.Team ("Chelsea FC", "https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/1200px-Chelsea_FC.svg.png", "England")
real_madrid = blueprint.Team ("Real Madrid", "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/1200px-Real_Madrid_CF.svg.png", "Spain")
man_city = blueprint.Team ("Manchester City", "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/1200px-Manchester_City_FC_badge.svg.png", "England")
b_munich = blueprint.Team("Bayern Munich", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/FC_Bayern_München_logo_%282024%29.svg/250px-FC_Bayern_München_logo_%282024%29.svg.png", "Germany")
paris = blueprint.Team ("Paris", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Paris_Saint-Germain_F.C..svg/1200px-Paris_Saint-Germain_F.C..svg.png", "France")
inter = blueprint.Team ("Inter", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/1200px-FC_Internazionale_Milano_2021.svg.png", "Italy")
porto = blueprint.Team("FC Porto", "https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/FC_Porto.svg/1200px-FC_Porto.svg.png", "Portugal")
benfica = blueprint.Team("Benfica", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/SL_Benfica_logo.svg/1200px-SL_Benfica_logo.svg.png", "Portugal")
b_dortmund = blueprint.Team("Borussia Dortmund", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/1200px-Borussia_Dortmund_logo.svg.png", "Germany")
juventus = blueprint.Team("Juventus", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkPh1ChmR7xKX0jAJSGYmtyvqfRRGdo8sKWQ&shttps://image.similarpng.com/file/similarpng/very-thumbnail/2020/06/Logo-Juventus-transparent-PNG.png","Italy")
atl_matrid = blueprint.Team ("Atletico Madrid", "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Atletico_Madrid_Logo_2024.svg/1200px-Atletico_Madrid_Logo_2024.svg.png", "Spain")
rb_salzburg = blueprint.Team ("RB Salzburg", "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/FC_Red_Bull_Salzburg_logo.svg/1200px-FC_Red_Bull_Salzburg_logo.svg.png", "Austria")
monterrey = blueprint.Team ("CF Monterrey", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Club_de_Fútbol_Monterrey_2019_Logo.svg/1200px-Club_de_Fútbol_Monterrey_2019_Logo.svg.png", "Mexico")
seattle = blueprint.Team ("Seattle Sounders", "https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Seattle_Sounders_logo.svg/1200px-Seattle_Sounders_logo.svg.png", "USA")
leon = blueprint.Team ("Club Leon", "https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Club_León_FC.svg/1200px-Club_León_FC.svg.png", "Mexico")
pachuca = blueprint.Team ("CF Pachuca", "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Pachuca_Tuzos_logo.svg/800px-Pachuca_Tuzos_logo.svg.png", "Mexico")
auckland = blueprint.Team ("Auckland City", "https://upload.wikimedia.org/wikipedia/en/5/53/New_Auckland_City_FC_logo_%28updated_2022%29.png", "New Zeland")
palmeiras = blueprint.Team ("SE Palmeiras", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Palmeiras_logo.svg/250px-Palmeiras_logo.svg.png", "Brazil")
flamengo = blueprint.Team ("CR Flamengo", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Flamengo_braz_logo.svg/1200px-Flamengo_braz_logo.svg.png", "Brazil")
fluminense = blueprint.Team ("Fluminense FC", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/FFC_crest.svg/1200px-FFC_crest.svg.png", "Brazil")
botafogo = blueprint.Team ("Botafogo", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Botafogo_de_Futebol_e_Regatas_logo.svg/1200px-Botafogo_de_Futebol_e_Regatas_logo.svg.png", "Brazil")
river = blueprint.Team ("River Plate", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Escudo_del_C_A_River_Plate.svg/1200px-Escudo_del_C_A_River_Plate.svg.png", "Argentina")
boca = blueprint.Team ("Boca Juniors", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Boca_Juniors_logo18.svg/1200px-Boca_Juniors_logo18.svg.png", "Argentina")
miami = blueprint.Team ("Inter Miami", "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Inter_Miami_CF_logo.svg/1200px-Inter_Miami_CF_logo.svg.png", "USA")

teams = {1:al_ahly, 2:wydad, 3:esperance, 4:mamelodi, 5:al_hilal, 6:urawa, 7:al_ain, 8:ulsan, 9:chelsea, 10:real_madrid, 11:man_city, 12:b_munich, 
         13:paris, 14:inter, 15:porto, 16:benfica, 17:b_dortmund, 18:juventus, 19:atl_matrid, 20:rb_salzburg, 21:monterrey, 22:seattle, 23:leon,
         24:pachuca, 25:auckland, 26:palmeiras, 27:flamengo, 28:fluminense, 29:botafogo, 30:river, 31:boca, 32:miami}

groups = { 'A':[26, 15, 1, 32], 'B':[13, 19, 29, 22], 'C':[12, 25, 16, 31], 'D':[27, 3, 9, 23], 'E':[30, 6, 21, 14], 'F':[28, 17, 8, 4],
          'G':[11, 2, 7, 18], 'H':[10, 5, 24, 20]}