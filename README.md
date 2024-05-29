Реализован типичный [клеточный автомат](https://github.com/facebook/react/wiki/Sites-Using-React) в котором применяется обход [окрестности Мура](https://ru.wikipedia.org/wiki/Окрестность_Мура).

### Изначальные условия:
1. Необходимо ввести в ручную нужный паттерн.
2. Исходя из поле будет проверятся по правилу B3/S23 (клетка выживает, если вокргу нее 2 или 3 соседа живых, клетка создается если вокруг нее 3 соседа живых).
3. Клетка проверяет 8 соседей вокруг нее.



## Управление:
1. При запуске игры выставляем изначальный паттерн.
2. Нажатие клавиши `space` включает и выключает анимацию.
3. Нажатие клавиши `escape` очищает поле.

## Настройки:
1. Для того, чтобы изменить размер поля в файле `main.py` нужно изменить параметр `self.screen = pygame.display.set_mode((x, y))`, где `x` и `y` необходимы размер окна, но ширина и высота должны быть равны между собой.
2. Для того, чтобы изменить размер клетки в файле `main.py` нужно изменить параметр `gamefield.set_cell_size(x)`, где `x` размер клетки в `px` (всегда квадратная).
3. Для того, чтобы изменить скорость воспроизведения в файле `main.py` нужно изменить параметр `gamefield.set_game_speed(x)`, где `x` кратность обычной скорости, по умолчанию стоит 1.
4. Для того, чтобы изменить правила обходя ячеек в файле `main.py` нужно изменить параметр `gamefield.set_rules([x], [y])`, где под `x` нужно указать количество соседних клеток, необходимых для создания новых, под `y` количество клеток, при которых живая клетка продолжает жить.

<details>
  <summary>Примитивные клеточные конструкции:</summary>

  
  Глайдер (B3/S23)
  
![Глайдер](https://github.com/whynot00/CellularAutomaton/assets/26331860/ee9e63e0-0d6b-41d4-8969-b93635a3a863)


  Жаба (B3/S23)
  
![Жаба](https://github.com/whynot00/CellularAutomaton/assets/26331860/abcd567c-a6eb-4564-86a5-ef584819d799)

  Пульсар (B3/S23)

![Пульсар](https://github.com/whynot00/CellularAutomaton/assets/26331860/b4ce086f-a299-4759-ab07-512601dc870a)

</details>

<details>
  <summary>Конструкции (корабли, ружья):</summary>
  
  Космический корабль (B3/S23)
  
![Корабль](https://github.com/whynot00/CellularAutomaton/assets/26331860/113e3cd7-41a4-42f1-95ba-46d495c7d538)


  Ружье (B3/S23) - формирует глайдер и отправляет его в полет.
  
![Ружье](https://github.com/whynot00/CellularAutomaton/assets/26331860/5dccab29-4b0a-4313-b1ed-1d3f80c5c417)


</details>

<details>
  <summary>Лабиринты:</summary>
  
  Обычный лабиринт (B3/S12345), заполнение ~90%
  
![Лабиринт](https://github.com/whynot00/CellularAutomaton/assets/26331860/aca1bdd7-6141-4c0d-ad8a-fbebdd6b6df5)

  Лабиринт с мышами (мигалками) (B37/S1234)
  
![Лабиринт с мышами](https://github.com/whynot00/CellularAutomaton/assets/26331860/f136acff-74a1-43db-a35d-a55561f36872)

</details>

</details>

<details>
  <summary>Ковер:</summary>
  
  Одна и разновидностей ковров (B234678/S8)
  
![Ковер](https://github.com/whynot00/CellularAutomaton/assets/26331860/26e4e33b-182f-4a50-9c74-f8db206d206b)

</details>

<details>
  <summary>Фрактал:</summary>
  
  Простейшая разновидность фрактала, который можно сгенерировать (B1/S012345678)
  
![Фрактал](https://github.com/whynot00/CellularAutomaton/assets/26331860/a89da39c-1af4-4189-80b8-2d89a2ce10b9)


</details>
