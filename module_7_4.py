team1_num = 5 # командa Мастер кода
team2_num = 6 # команда Волшебники данных
score1 = 40
score2 = 40
team1_time = 1552.512
team2_time = 2153.31451
task_total = 82
time_avg = (team1_time + team2_time) / task_total


print()
print('    *****')
print()

print(' "%"')
print('в команде Мастера кода участников: %d!' % team1_num)
print('итого сегодня участников %d и %d!' % (team1_num, team2_num))
print(' "format"')
print('команда Мастера кода решила задач: {}'.format(score1))
print('команда Волшебники данных решила задач: {}'.format(score2))
print('всего было задач: {}'.format(task_total))
print(' "f-строка"')
print(f'команды решили {score1} и {score2} задач')
print(f'среднее время выполнения задачи = {time_avg}')
if score1 > score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'победа команды Мастера кода'
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'победа команды Волшебники данных'
else:
    challenge_result = 'ничья'
print()
print(f' команда Мастера кода решила {score1} задач за время в {team1_time} секунд')
print(f' команда Волшебники данных решила {score2} задач за время в {team2_time} секунд')
print()
print(' в итоге - ', challenge_result)

print()
print('End of lesson')
print('   --------')
