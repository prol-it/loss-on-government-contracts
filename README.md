## Loss on government contracts

### Краткое описание:

Расчет предполагаемого ущерба в сфере госзакупок.
Сайт госзакупок: https://zakupki.gov.ru

### Стек:

Python, PostgreSQL

### Полное описание:

Рассчитывает возможный ущерб на основе входных данных о закупках:
1. Конкретного контрагента, по которому необходимо провести анализ.
2. Других контрагентов, которые в этот же период закупали такие-же (либо схожие) позиции товаров.

Для начала необходимо собрать и подготовить (очистить) данные для расчета - завершить работу с проектом https://github.com/prol-it/analysis-of-government-contracts. Далее создаем в текущей директории проекта папку `data`. И выполняем шаги:

1. Создаем таблицу с данными о закупках заказчика (`greate_table_customer.py`). На вход в папку `data` нужно подать ods файл, содержащий исходные данные в виде:

| find_text| sname | name | name_dop | qty | unit | price | total | сontract | year | customer |
|----------| ------|------|----------|-----|------|-------|-------|----------|------|----------|
| абрикос | абрикосы сушеные| Абрикосы сушёные | Фрукты косточковые сушеные (10.39.25.132) | 930 | кг | 374,39 | 348182,7 | 2782001254220000004 | 2020 | SPB-PNI-4 |
| ветчин | ветчина индейка | Ветчина из индейки | Изделия колбасные мясосодержащие (10.13.14.529) | 505 | кг | 448,25 | 226366,25 | 2782001254217000093 | 2018 | SPB-PNI-4 |

данные будут импортированы из файла.

2. Создаем таблицу с данными о закупках аналогичных позиций другими участниками (`greate_table_products.py`). На вход в папку `data` нужно подать ods файлы, содержащие очищенные данные по каждому продукту в виде :

| sname | name | name_dop | qty | unit | price | total | contract | year | customer | find_text |
|-------|------|----------|-----|------|-------|-------|----------|------|----------|-----------|
| печень говяжья | Печень говяжья замороженная |Субпродукты пищевые крупного рогатого скота замороженные (10.11.31.140) | 1864 | кг	| 316 | 589024 | 2780702227718000013 | 2018 | САНКТ-ПЕТЕРБУРГСКОЕ ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ СТАЦИОНАРНОЕ УЧРЕЖДЕНИЕ СОЦИАЛЬНОГО ОБСЛУЖИВАНИЯ ПСИХОНЕВРОЛОГИЧЕСКИЙ ИНТЕРНАТ № 9 | печень |
| печень говяжья | Печень говяжья замороженная | Субпродукты пищевые крупного рогатого скота замороженные (10.11.31.140) | 2700 | кг | 231,4 | 624780 | 2782506561118000012 | 2018 | САНКТ-ПЕТЕРБУРГСКОЕ ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ СТАЦИОНАРНОЕ УЧРЕЖДЕНИЕ СОЦИАЛЬНОГО ОБСЛУЖИВАНИЯ ПСИХОНЕВРОЛОГИЧЕСКИЙ ИНТЕРНАТ №1 | печень |

данные будут импортированы из файла.

3. Анализируем закупочные цены аналогичных позиций из этих двух таблиц и рассчитывает предполагаемый ущерб (lost.py).  На выходе получаем таблицу (lost.ods) с расчетом справедливой цены, обоснованием этой цены (контракты с закупочными ценами других контрагентов за этот же период) и сумму предполагаемого ущерба.

| Наименование | Наименование доп. | Кол-во | Единица изм. | Цена | Сумма | Номер контракта | Год | Заказчик | Справедливая цена | Обоснование | Убыток |
|--------------|-------------------|--------|--------------|------|-------|-----------------|-----|----------|------------|-------------|--------|
| Батон обогащенный витаминными и минеральными веществами | Хлеб недлительного хранения из пшеничной муки (10.71.11.111) | 17 745 | шт | 110,15 | 1 954 612 | 2782001254217000002 | 2017 | SPB-PNI-4 | 59,81 | 30.53 - 1780404195516000103 / 32.0 - 2782666724917000149 / ... | 893 283 |
| Говядина задние части замороженные Тип На кости | Говядина замороженная (10.11.31.110) | 6 336 | кг | 604,2 | 3 828 211 | 2782001254216000095 | 2017 | SPB-PNI-4 | 418,43 | 297.0 - 2781901284417000003 / 301.27 - 2781304702217000012 / ... | 1 177 039 |


### Инструкция по запуску:

Создать папку для проекта. Создать в ней папку `data`.
Выполнить в папке проекта последовательно скрипты:

>greate_table_customer.py

>greate_table_products.py

>lost.py

