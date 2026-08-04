<font size="3"><b>

<div align = 'center'>

# Multimodel


### Описание работы


Multimodel представляет собой граф, который использует 4 разных LLM в зависимости от типа сообщения.

`
Ввод пользователя -> определение типа сообщения -> вызов соответствующей LLM -> Вывод LLM -> систематизация полученных результатов -> вывод систематизирующей LLM -> Ввод пользователя
`

### Быстрый старт
<div align = 'left'>

1) Клонирвоать репозиторий git clone https://github.com/s4lf3tk4/Multimodel.git

2) Установить окружение и зависимости: setup.sh
   
3) Запуск run.sh
   
</div>

### Настройка API-ключа

<div align = 'left'>

1) Получить ключ на [ChatAnywhere](https://chatanywhere.tech/), авторизируйтесь через GitHub и поставьте звезду для получения безлимитного ключа
2) Сохраните ключ, скопированный из .env.example в сздаваемый вами файл .env
   
</div>

### Структура проекта 

<div align = 'left'>

    ├──  core/   
    ├──  graph/   
    ├──  providers/
    ├──  main.py
    ├──  README.md              
    ├──  .env.example             
    ├──  setup.sh                 
    ├──  run.sh                   
    └──  docs/    


</div>


[Архитектура проекта](docs/general.md)

</div>

</b>
