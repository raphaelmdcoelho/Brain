Cron é um programa de utilidade para repetir tarefas numa data futura. Dar um comando que agenda uma tarefa, em um horário específico, repetidamente é um cron job

cron é a solução perfeita.

O Cron é um [[Daemon]]. Isso significa que ele trabalha em plano de fundo para executar tarefas não-interativas. No Windows, você pode estar mais familiarizados com processos em plano de fundo com os **Serviços**.

Um arquivo Cron é sempre um arquivo de texto que contém comandos para rodar em uma hora específica. O sistema padrão do arquivo contab é **/etc/crontab** e ele fica localizado dentro do diretório crontab, que é **/etc/cron.*/**. Apenas administradores podem editar um arquivo crontab do sistema.

### Editar arquivo cronjob
```bash
crontab -e
```

### Exibir conteúdo do arquivo atual
```bash
crontab -l
```

### Syntaxe do comando
```bash
* * * * * /bin/sh backup.sh
```

![[Pasted image 20230930214946.png]]

- **Minute** (Minuto) – é o minuto da hora em que o comando vai rodar, variando de 0 a 59.
- **Hour** (Hora) – é a hora em que o comando será executado, variando de 0 a 23.
- **Day of the month** (Dia do mês) – é o dia do mês em que o comando vai rodar, variando de 1 a 31.
- **Month** (Mês) – é o mês em que o comando será executado, variando de 1 a 12.
- **Day of the week** (Dia da semana) – é o dia da semana que você quer que o comando rode, variando de 0 a 7.

Junto a isso, você precisa usar caracteres apropriados em cada arquivo crontab.

- **Asterisco (*)** – define todos os parâmetros de agendamento.
- **Vírgula (,)** – mantém duas ou mais horas de execução em um único comando.
- **Hífen (-)** – determina o intervalo da hora ao definir vários tempos de execução de único comando.
- **Barra inclinada (/)** – cria intervalos pré-determinados de tempo dentro de um intervalo de tempo específico.
- **Last (L)** – tem o propósito específico de determinar o último dia da semana do mês respectivo. Por exemplo, **3L** significa a última quarta-feira.
- **Weekday (W)** – determina o dia da semana mais próximo de um tempo dado. Por exemplo, **1W** significa se o **1°** for um sábado, o comando vai ser executado na segunda-feira (**3°**).
- **Hash (#)** – para determinar o dia da semana, seguido por um número que varia de 1 a 5. Por exemplo, **1#2** significa a segunda segunda-feira.
- **Ponto de interrogação (?)** – serve para deixar um espaço.

#linux 