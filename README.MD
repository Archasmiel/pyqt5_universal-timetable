<i><font size="5"> KPI Timetable </font></i>

<details><summary >
<font size="4" color=#D3ECA7> Руководство по интерфейсу </font>
</summary>
<p>

Как окно отобразится если открыть программу:<br>
<img alt="alt text" src="https://github.com/Archasmiel/pyqt5_universal-timetable/blob/main/examples/example1.png?raw=true" width="450"/>

- Слева снизу область для выбора группы.<br>
- Справа снизу кнопка для смены цветовой темы с тёмной на светлую и со светлой на тёмную.<br>

<br>

- Выбираем группу, в итоге заполнятся две панели.<br> 
   1. Верхняя - расписание первой недели.<br>
   2. Нижняя - расписание второй недели.<br>

Пример результата:<br>
<img alt="alt text" src="https://github.com/Archasmiel/pyqt5_universal-timetable/blob/main/examples/example2.png?raw=true" width="450"/>

</p></details>

<details><summary>
<font size="4" color=#D3ECA7> Руководство по редактированию расписаний и добавлению новых </font>
</summary><p>

Необходимо:
   1. желательно иметь расписание перед глазами
   2. открыть в корне программы папку data<br><img alt="alt text" src="https://github.com/Archasmiel/pyqt5_universal-timetable/blob/main/examples/example3.png?raw=true" width="450"/>
   3. возпользуйтесь тестовым файлом freks.xlsx - c его помощью можно легко сделать своё расписание
   4. в файле расписания обязательно должна быть вкладка с распределением времени и хотя бы одна с расписанием
     <br><br>- что из себя представляет вкладка с распределением времени:<br><img alt="alt text" src="https://github.com/Archasmiel/pyqt5_universal-timetable/blob/main/examples/example4.png?raw=true" width="450"/><br>
     (1) поле для внесения данных в текстовом формате (не формат даты)
     <br>= в оранжевой области ничего менять не нужно, автоматически обсчитывается для обработки в программе 
     <br>= менять размер области с расписанием недели тоже не нужно
     <br><br>- что из себя представляет вкладка расписания:<br>
     <img alt="alt text" src="https://github.com/Archasmiel/pyqt5_universal-timetable/blob/main/examples/example5.png?raw=true" width="450"/><br>
     <img alt="alt text" src="https://github.com/Archasmiel/pyqt5_universal-timetable/blob/main/examples/example6.png?raw=true" width="450"/><br>
     (1) - поле с расписаниями знаменателя (1 неделя) - указаны ссылки в 3 пункте
     <br>
     (2) - поле с расписаниями знаменателя (2 неделя) - указаны ссылки в 3 пункте
     <br>
     (3) - область кратких ссылок для 1-2 недель по номеру в столбике
     <br>
     (4-7) - область для внесения текстовых данных по заголовку столбика
     <br>
     = можно добавлять ссылки в области 3 расширяя её, но при этом чтобы не было пустых названий предметов, остальные клетки после неё можно оставить пустыми 
    <br><br>
   5. добавить в файл files.txt название файла с таблицей в новую строчку без расширения .xlsx 
</p></details>

