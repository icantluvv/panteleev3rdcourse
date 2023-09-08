from import_this import RACE_DATA
def gon(key):
    print("")
    print(f"гонщик на {racer_info['FinishedPlace']} месте")
    print("")
    print("\t" + "Имя: " + racer_info['RacerName'])
    print("\t" + "Команда: " + racer_info['RacerTeam'])
    print("\t" + "Время: " + str(racer_info['FinishedTimeSeconds']))
    print("")


for key, racer_info in RACE_DATA.items():
    if racer_info['FinishedPlace'] == 1:
        finish = (f"выиграл {racer_info['RacerName']} поздравляем!")
        print(finish)
        print('_' * len(finish))
        print("")
        print('первые три места: ')
        gon(key)
    if racer_info['FinishedPlace'] == 2:
        gon(key)
    if racer_info['FinishedPlace'] == 3:
        gon(key)

