# Лабораторная работа №1

## Цель: 
1. Изучить основные возможности языка Python для разработки программных систем с интерфейсом командной строки (CLI)
2. Разработать программную систему на языке Python согласно описанию предметной области
## Задача:
Разработать программную систему на языке Python. Модель проверки качества продукции.

<em>
Предметная область: контроль и обеспечение качества товаров.<br>
Важные сущности: продукция, контролеры, стандарты качества, сертификаты, отзывы.
<br>
Операции: операция проверки продукции по стандартам, операция анализа отзывов и рекомендаций, операция выдачи сертификатов качества, операция контроля продукции на всех этапах производства, операция внесения улучшений.
</em>

## Сущности:
Были выделены следующие сущности:

Контролёр - Controller <br>
Сертификат - Certificate <br>
Продукт - Product <br>
Отзыв - Review <br>
Стандарт - Standart <br>


## Описание работы программы:
- При запуске программы пользовотелю даётся меню операций. <br>

![[image](\images\01.png)](https://github.com/MoonF1re/ppois-2-2024/blob/new_branch/Lab_1/images/01.png?raw=true)

- После выбора операции пользователь вводит нужные данные и операция завершается.

![[image](\images\03.png)](https://github.com/MoonF1re/ppois-2-2024/blob/new_branch/Lab_1/images/03.png?raw=true)

- После выполнения всех нужных операций пользователь выходит из программы.

![[image](\images\04.png)](https://github.com/MoonF1re/ppois-2-2024/blob/new_branch/Lab_1/images/04.png?raw=true)


## Тестирование:
Программа успешно прошла unit-тестирование:

![[image](\images\02.png)](https://github.com/MoonF1re/ppois-2-2024/blob/new_branch/Lab_1/images/02.png?raw=true)

## Вывод:
В результате выполнения лабораторной работы были изучены ключевые возможности языка Python для создания программ с интерфейсом командной строки. Затем была успешно разработана программная система на Python, моделирующая функциональность милиции. Это позволило понять применимость Python для разработки эффективных и удобных CLI-приложений и создать работоспособную систему для управления задачами и данными в рамках модели милиции.