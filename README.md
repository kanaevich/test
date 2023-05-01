# test
Файл graph.py содержит скрипт с реализацией класса graph

Метод __init__ переписан так, что конструктор создает граф по словарю вершин и ребер, присваивая каждой вершине значение 0

Метод random(n) генерирует случайный граф с n вершинами, проходясь циклом по упорядоченным парам занумерованных 
вершин (i<=j), случайно выбирая (rand(0,1)) инициировать ли между i и j ребро или нет

Вспомогательный метод gr.complement() из графа gr делает граф, где различные вершины соединены тогда и только тогда, когда они НЕ соединены в gr
(вершина gr.complement() по прежнему остается соединенной с самой собой)

Функция shashlyk(gr) по графу, в словаре(dict2 переменная экземпляра класса) ребер которого вершины упорядочены по возрастанию 
(это обязательно для того, чтобы функция выдавала нужный результат) осуществляет цикл по всем различным упорядоченным наборам вершин gr.complement(), которые 
попарно соединены между собой. Это осуществляется по индукции, начиная с множества наборов, состоящих из одной вершины (которая считается соединенной с самой собой) 
далее добавляя на каждом шаге к уже имеющемуся набору вершин вершину, чей номер больше максимального номера вершины в наборе и которая соединена со всеми 
вершинами этого набора. То есть, на следующем шаге работы цикла из множества всех наборов k-1 соединенных попарно вершин получается множество всех наборов k
попарно соединенных вершин. Для проверки, что вершина соединена со всеми вершинами набора используется вспомогательная функция intersect, пересекающая 
упорядоченные подмножества в range(0,n). 

Папка dracula содержит баш скрипты для последнего задания.
