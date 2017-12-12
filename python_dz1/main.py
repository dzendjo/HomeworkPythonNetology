# Задача №1
#
# На лекции мы приступили к написанию калькулятора для Шенгенской визы. Вам нужно дополнить его функционал следующим образом:
#
# Выводить текущий курс евро к рублю (считаем, что он не меняется).
# Вывести стоимость проживания не только в евро, но и в рублях.
# Допустим у нас есть бюджет на поездку, выяснить, не выходим ли мы за него, если выходим, то вывести предупреждение.
# Предположим, что каждый из нас начал вести список расходов. Вывести сумму, которую потратил каждый и сколько осталось в общем бюджете.

day_cost = 50

trip_length_1 = 5
trip_length_2 = 7
trip_length_3 = 7
trip_length = trip_length_1 + trip_length_2 + trip_length_3

flight_cost = 50
number_flights = 6

total_trip_cost_eur = trip_length * day_cost + flight_cost * number_flights
print('Сумарная стоимость путешествия в евро: {} евро'.format(total_trip_cost_eur))

eur_rur_rate = 70
print('Текущий курс евро к рублю: {}'. format(eur_rur_rate))

total_trip_cost_rur = total_trip_cost_eur * eur_rur_rate
print('Сумарная стоимость путешествия в рублях: {} рублей'.format(total_trip_cost_rur))

trip_budget = 1200
print('Бюджет путешествий {} евро'.format(trip_budget))

if trip_budget > total_trip_cost_eur:
    print('В бюджет вписываемся!')
else:
    print('Мы не вписываемся в бюджет :(')

#Начинаем записывать свои расходы
anton_spent = [20, 10, 30]
anna_spent = [10, 12, 15, 40, 8]

resoult_money_stayed = trip_budget - sum(anton_spent) - sum(anna_spent)
print('\nОстатки бюджета: {} евро'.format(resoult_money_stayed))
