from import_this import RACE_DATA

if __name__ == '__main__':
    a = 1
    min_finished_time = float('inf')
    top_racers = {}


    for racer_id, racer_info in RACE_DATA.items():
        finished_time = racer_info['FinishedTimeSeconds']
        if finished_time < min_finished_time:
            min_finished_time = finished_time
            top_racers[a] = racer_info
            a += 1
        if a > 3:
            break
        
    first_place = max(top_racers)
    last_place = min(top_racers)

    for place, racer_info in top_racers.items():
        if place == first_place:
            time_seconds = racer_info['FinishedTimeSeconds']
            time_hours = time_seconds // 3600
            time_minutes = time_seconds % 3600 // 60
            time_seconds = time_seconds % 60
            time_formatted = f"{time_hours:02d}:{time_minutes:02d}:{time_seconds:02d}"
            print("\n\n\n\n\n\n")
            res = (f"Выиграл - {racer_info['RacerName']} ! Поздравляем ! \n")            
            print(res)
            print('_' * ( len(res)) + "\n\n\n")
            print("Первые три места: \n\n\n")
            print("Гонщик на 1 месте:\n")
            print(f"\t Имя: {racer_info['RacerName']} \n")
            print(f"\t Команда: {racer_info['RacerTeam']} \n")
            print("\t Время:", time_formatted + "\n\n")

    for place, racer_info in top_racers.items():
        if place < first_place and place > last_place:
            time_seconds = racer_info['FinishedTimeSeconds']
            time_hours = time_seconds // 3600
            time_minutes = (time_seconds % 3600) // 60
            time_seconds = time_seconds % 60
            time_formatted = f"{time_hours:02d}:{time_minutes:02d}:{time_seconds:02d}"
            print("Гонщик на 2 месте:\n")
            print(f"\t Имя: {racer_info['RacerName']}")
            print(f"\t Команда: {racer_info['RacerTeam']}")
            print("\t Время:", time_formatted + "\n\n")

    for place, racer_info in top_racers.items():
        if place == last_place:
            time_seconds = racer_info['FinishedTimeSeconds']
            time_hours = time_seconds // 3600
            time_minutes = (time_seconds % 3600) // 60
            time_seconds = time_seconds % 60
            time_formatted = f"{time_hours:02d}:{time_minutes:02d}:{time_seconds:02d}"
            print("Гонщик на 3 месте:\n")
            print(f"\t Имя: {racer_info['RacerName']}")
            print(f"\t Команда: {racer_info['RacerTeam']}")
            print("\t Время:", time_formatted + "\n\n")
        