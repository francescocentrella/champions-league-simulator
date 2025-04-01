class Team:
    def __init__(self, name, logo):
        self.name = name
        self.logo = logo
        self.game_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0
        self.scored = 0
        self.conceded = 0
        self.difference = 0
        self.eliminated = False
        
ac_milan = Team("Milan", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Logo_of_AC_Milan.svg/1200px-Logo_of_AC_Milan.svg.png")
as_monaco = Team("Monaco", "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/LogoASMonacoFC2021.svg/1200px-LogoASMonacoFC2021.svg.png")
arsenal = Team ("Arsenal", "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/1200px-Arsenal_FC.svg.png")
aston_villa = Team ("Aston Villa", "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Aston_Villa_FC_new_crest.svg/250px-Aston_Villa_FC_new_crest.svg.png")
atalanta = Team("Atalanta", "https://upload.wikimedia.org/wikipedia/en/thumb/6/66/AtalantaBC.svg/250px-AtalantaBC.svg.png")
atl_matrid = Team ("Atletico Madrid", "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Atletico_Madrid_Logo_2024.svg/1200px-Atletico_Madrid_Logo_2024.svg.png")
barcelona = Team ("Barcelona", "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/640px-FC_Barcelona_%28crest%29.svg.png")
b_leverkusen = Team ("Bayer Leverkusen", "https://upload.wikimedia.org/wikipedia/en/thumb/5/59/Bayer_04_Leverkusen_logo.svg/1200px-Bayer_04_Leverkusen_logo.svg.png")
b_munich = Team("Bayern Munich", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/FC_Bayern_München_logo_%282024%29.svg/250px-FC_Bayern_München_logo_%282024%29.svg.png")
benfica = Team("Benfica", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/SL_Benfica_logo.svg/1200px-SL_Benfica_logo.svg.png")
bologna = Team("Bologna", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Bologna_F.C._1909_logo.svg/1200px-Bologna_F.C._1909_logo.svg.png")
b_dortmund = Team("Borussia Dortmund", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/1200px-Borussia_Dortmund_logo.svg.png")
brest = Team ("Brest", "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Stade_Brestois_29_logo.svg/1200px-Stade_Brestois_29_logo.svg.png")
c_brugge = Team ("Club Brugge", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Club_Brugge_KV_logo.svg/1200px-Club_Brugge_KV_logo.svg.png")
celtic = Team ("Celtic", "https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Celtic_FC_crest.svg/1200px-Celtic_FC_crest.svg.png")
d_zagreb = Team ("Dinamo Zagreb", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Club_Brugge_KV_logo.svg/1200px-Club_Brugge_KV_logo.svg.png")
feyenoord = Team ("Feyenoord", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Club_Brugge_KV_logo.svg/1200px-Club_Brugge_KV_logo.svg.png")
girona = Team ("Girona", "https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/Girona_FC_Logo.svg/1200px-Girona_FC_Logo.svg.png")
inter = Team ("Inter", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/1200px-FC_Internazionale_Milano_2021.svg.png")
juventus = Team("Juventus", "https://upload.wikimedia.org/wikinews/en/d/d2/Juventus_Turin.svg")
lille = Team("Lille", "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Lille_OSC_2018_logo.svg/800px-Lille_OSC_2018_logo.svg.png")
liverpool = Team("Liverpool", "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/1200px-Liverpool_FC.svg.png")
man_city = Team ("Manchester City", "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/1200px-Manchester_City_FC_badge.svg.png")
psv = Team("PSV", "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/PSV_Eindhoven.svg/1200px-PSV_Eindhoven.svg.png")
paris = Team ("Paris", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Paris_Saint-Germain_F.C..svg/1200px-Paris_Saint-Germain_F.C..svg.png")
rb_leipzig = Team ("RB Leipzig", "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/RB_Leipzig_2014_logo.svg/1200px-RB_Leipzig_2014_logo.svg.png")
rb_salzburg = Team ("RB Salzburg", "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/FC_Red_Bull_Salzburg_logo.svg/1200px-FC_Red_Bull_Salzburg_logo.svg.png")
real_madrid = Team ("Real Madrid", "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/1200px-Real_Madrid_CF.svg.png")
red_star = Team ("Red Star", "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Red_Star_Belgrade_crest.svg/1200px-Red_Star_Belgrade_crest.svg.png")
sk_sturm = Team ("Sturm Graz", "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/SK_Sturm_Graz_logo.svg/1200px-SK_Sturm_Graz_logo.svg.png")
shaktar = Team ("Shakhtar", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/FC_Shakhtar_Donetsk.svg/1200px-FC_Shakhtar_Donetsk.svg.png")
slovan = Team ("Slovan Bratislava", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/SK_Slovan_Bratislava_logo.svg/1200px-SK_Slovan_Bratislava_logo.svg.png")
sparta_praga = Team ("Sparta Prague", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/AC-Sparta-LOGO2021.svg/1200px-AC-Sparta-LOGO2021.svg.png")
sporting = Team  ("Sporting Lisbon", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Sporting_Clube_de_Portugal_%28Logo%29.svg/1200px-Sporting_Clube_de_Portugal_%28Logo%29.svg.png")
stuttgart = Team ("Stuttgart", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Sporting_Clube_de_Portugal_%28Logo%29.svg/1200px-Sporting_Clube_de_Portugal_%28Logo%29.svg.png") 
young_boys = Team ("Young Boys", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/BSC_Young_Boys.svg/800px-BSC_Young_Boys.svg.png")

teams = {1: ac_milan, 2: as_monaco, 3: arsenal, 4: aston_villa, 5: atalanta, 6: atl_matrid, 7: barcelona, 8: b_leverkusen, 9: b_munich,
         10: benfica, 11: bologna, 12: b_dortmund, 13: brest, 14: celtic, 15: c_brugge, 16: d_zagreb, 17: feyenoord, 18: girona, 19: inter,
         20: juventus, 21: lille, 22: liverpool, 23: man_city, 24: psv, 25: paris, 26: rb_leipzig, 27: rb_salzburg, 28:real_madrid,
         29: red_star, 30: sk_sturm, 31: shaktar, 32: slovan, 33: sparta_praga, 34: sporting, 35: stuttgart, 36: young_boys}