field = list(range(1,10))

# рисуем и нумеруем сетку игрового поля 3х3
def field_layout(field):
   print("-" * 13)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
      print("-" * 13)

# получаем ход игрока и проверяем его на правильность ввода
def game_step(mark_gamer):
   valid = False
   while not valid:
      step_gamer = input("Введите номер клетки куда поставим " + mark_gamer+"? ")
      if step_gamer.isdigit() == True:
            step_gamer = int(step_gamer)
            if step_gamer >= 1 and step_gamer <= 9:
               if(str(field[step_gamer-1]) not in "XO"):
                  field[step_gamer-1] = mark_gamer
                  valid = True
               else:
                  print("Эта клетка уже занята!")
            else:
              print("Неверный номер. Введите цифру от 1 до 9.")
      else:
          print("Неправильно. Вы уверены что ввели числовое значение?")
# заводим выигрышные комбинации и проверяем игровое поле для введенных значений
def test_victory(field):
   victory_combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for any in victory_combination:
       if field[any[0]] == field[any[1]] == field[any[2]]:
          return field[any[0]]
   return False
# заводим счетчик, определяем знак игрока (Х или О), циклируем ходы и с 5 хода проверяем выигрышные комбинации
def main(field):
    counter = 0
    victory = False
    while not victory:
        field_layout(field)
        if counter % 2 == 0:
           game_step("X")
        else:
           game_step("O")
        counter += 1
        if counter > 4:
           tmp = test_victory(field)
           if tmp:
              victory = True
              break
        if counter == 9:
            print("Ничья!")
            break
    field_layout(field)
main(field)
tmp = test_victory(field)
print(tmp, "выиграл!")
input("Нажмите Enter для выхода!")