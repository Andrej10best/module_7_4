team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print('В команде Мастеров кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

challenge_result = result
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / 2

print(challenge_result)
