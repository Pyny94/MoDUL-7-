team1_num = int(input())
team2_num = int(input())
score_1 = int(input())
score_2 = int(input())
team1_time = float(input())
team2_time = float(input())
tasks_total = int(input())
time_avg = float(input())
challenge_result = str(input())


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"

print("В команде Мастера кода участников: %s" % team1_num)
print("В команде Мастера кода участников: %s, %s " % (team1_num,team2_num))

print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {result}!")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg } секунды на задачу!.")


