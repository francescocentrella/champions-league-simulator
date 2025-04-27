import blueprint
import random

ac_milan = blueprint.Team("Milan", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Logo_of_AC_Milan.svg/1200px-Logo_of_AC_Milan.svg.png")
as_monaco = blueprint.Team("Monaco", "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/LogoASMonacoFC2021.svg/1200px-LogoASMonacoFC2021.svg.png")
arsenal = blueprint.Team ("Arsenal", "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/1200px-Arsenal_FC.svg.png")
aston_villa = blueprint.Team ("Aston Villa", "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Aston_Villa_FC_new_crest.svg/250px-Aston_Villa_FC_new_crest.svg.png")
atalanta = blueprint.Team("Atalanta", "https://upload.wikimedia.org/wikipedia/en/thumb/6/66/AtalantaBC.svg/250px-AtalantaBC.svg.png")
atl_matrid = blueprint.Team ("Atletico Madrid", "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Atletico_Madrid_Logo_2024.svg/1200px-Atletico_Madrid_Logo_2024.svg.png")
barcelona = blueprint.Team ("Barcelona", "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/640px-FC_Barcelona_%28crest%29.svg.png")
b_leverkusen = blueprint.Team ("Bayer Leverkusen", "https://upload.wikimedia.org/wikipedia/en/thumb/5/59/Bayer_04_Leverkusen_logo.svg/1200px-Bayer_04_Leverkusen_logo.svg.png")
b_munich = blueprint.Team("Bayern Munich", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/FC_Bayern_München_logo_%282024%29.svg/250px-FC_Bayern_München_logo_%282024%29.svg.png")
benfica = blueprint.Team("Benfica", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/SL_Benfica_logo.svg/1200px-SL_Benfica_logo.svg.png")
bologna = blueprint.Team("Bologna", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Bologna_F.C._1909_logo.svg/1200px-Bologna_F.C._1909_logo.svg.png")
b_dortmund = blueprint.Team("Borussia Dortmund", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/1200px-Borussia_Dortmund_logo.svg.png")
brest = blueprint.Team ("Brest", "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Stade_Brestois_29_logo.svg/1200px-Stade_Brestois_29_logo.svg.png")
c_brugge = blueprint.Team ("Club Brugge", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Club_Brugge_KV_logo.svg/1200px-Club_Brugge_KV_logo.svg.png")
celtic = blueprint.Team ("Celtic", "https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Celtic_FC_crest.svg/1200px-Celtic_FC_crest.svg.png")
d_zagreb = blueprint.Team ("Dinamo Zagreb", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Club_Brugge_KV_logo.svg/1200px-Club_Brugge_KV_logo.svg.png")
feyenoord = blueprint.Team ("Feyenoord", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d0/Club_Brugge_KV_logo.svg/1200px-Club_Brugge_KV_logo.svg.png")
girona = blueprint.Team ("Girona", "https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/Girona_FC_Logo.svg/1200px-Girona_FC_Logo.svg.png")
inter = blueprint.Team ("Inter", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/1200px-FC_Internazionale_Milano_2021.svg.png")
juventus = blueprint.Team("Juventus", "https://upload.wikimedia.org/wikinews/en/d/d2/Juventus_Turin.svg")
lille = blueprint.Team("Lille", "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Lille_OSC_2018_logo.svg/800px-Lille_OSC_2018_logo.svg.png")
liverpool = blueprint.Team("Liverpool", "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/1200px-Liverpool_FC.svg.png")
man_city = blueprint.Team ("Manchester City", "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/1200px-Manchester_City_FC_badge.svg.png")
psv = blueprint.Team("PSV", "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/PSV_Eindhoven.svg/1200px-PSV_Eindhoven.svg.png")
paris = blueprint.Team ("Paris", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Paris_Saint-Germain_F.C..svg/1200px-Paris_Saint-Germain_F.C..svg.png")
rb_leipzig = blueprint.Team ("RB Leipzig", "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/RB_Leipzig_2014_logo.svg/1200px-RB_Leipzig_2014_logo.svg.png")
rb_salzburg = blueprint.Team ("RB Salzburg", "https://upload.wikimedia.org/wikipedia/en/thumb/7/77/FC_Red_Bull_Salzburg_logo.svg/1200px-FC_Red_Bull_Salzburg_logo.svg.png")
real_madrid = blueprint.Team ("Real Madrid", "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/1200px-Real_Madrid_CF.svg.png")
red_star = blueprint.Team ("Red Star", "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Red_Star_Belgrade_crest.svg/1200px-Red_Star_Belgrade_crest.svg.png")
sk_sturm = blueprint.Team ("Sturm Graz", "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/SK_Sturm_Graz_logo.svg/1200px-SK_Sturm_Graz_logo.svg.png")
shaktar = blueprint.Team ("Shakhtar", "https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/FC_Shakhtar_Donetsk.svg/1200px-FC_Shakhtar_Donetsk.svg.png")
slovan = blueprint.Team ("Slovan Bratislava", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/SK_Slovan_Bratislava_logo.svg/1200px-SK_Slovan_Bratislava_logo.svg.png")
sparta_praga = blueprint.Team ("Sparta Prague", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/AC-Sparta-LOGO2021.svg/1200px-AC-Sparta-LOGO2021.svg.png")
sporting = blueprint.Team  ("Sporting Lisbon", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Sporting_Clube_de_Portugal_%28Logo%29.svg/1200px-Sporting_Clube_de_Portugal_%28Logo%29.svg.png")
stuttgart = blueprint.Team ("Stuttgart", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Sporting_Clube_de_Portugal_%28Logo%29.svg/1200px-Sporting_Clube_de_Portugal_%28Logo%29.svg.png") 
young_boys = blueprint.Team ("Young Boys", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/BSC_Young_Boys.svg/800px-BSC_Young_Boys.svg.png")

teams = {1: ac_milan, 2: as_monaco, 3: arsenal, 4: aston_villa, 5: atalanta, 6: atl_matrid, 7: barcelona, 8: b_leverkusen, 9: b_munich,
        10: benfica, 11: bologna, 12: b_dortmund, 13: brest, 14: celtic, 15: c_brugge, 16: d_zagreb, 17: feyenoord, 18: girona, 19: inter,
        20: juventus, 21: lille, 22: liverpool, 23: man_city, 24: psv, 25: paris, 26: rb_leipzig, 27: rb_salzburg, 28:real_madrid,
        29: red_star, 30: sk_sturm, 31: shaktar, 32: slovan, 33: sparta_praga, 34: sporting, 35: stuttgart, 36: young_boys}


def main():
    clubs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    draw(18)
    for i in clubs:
        print(teams[i].opponents)
    



    

def draw (n_draws):
    for i in range (8):
        clubs_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        for _ in range (n_draws):
            team1 = random.choice(clubs_list)
            team2 = random.choice(clubs_list)
            while (team1 == team2) or (already_played(team1, team2)):
                team1 = random.choice(clubs_list)
                team2 = random.choice(clubs_list)
            teams[team1].opponents.append(team2)
            teams[team2].opponents.append(team1)
            clubs_list = remove_team(clubs_list, team1, team2)


def remove_team(temp, team1, team2):
    position = 0
    for i in temp:
        if i == team1:
            temp.pop(position)
            break
        else:
            position += 1
    position = 0
    for i in temp:
        if i == team2:
            temp.pop(position)
            break
        else:
            position += 1
    return temp

def already_played (team1, team2):
    for i in teams[team1].opponents:
        if team2 == i:
            return True
    return False



main()