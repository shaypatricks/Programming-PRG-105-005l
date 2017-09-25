calories_burned_per_minute = 4.2

for minutes_treadmill in range(10, 60, 5):
    calories_burned = (minutes_treadmill / 1) * calories_burned_per_minute
    print('you will burn', calories_burned, "calories in", minutes_treadmill, 'minutes')
