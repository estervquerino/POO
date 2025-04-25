<h1>Bem-vindo á aula de PHP</h1>
<?php
    // comentário de uma linha
    /**
     * Este é um bloco de comentário
     * 
     *
     */
    // Aula do dia 23.04.25

    echo "Olá mundo<br>";

    // Variáveis em PHP
    $nome = "João";
    $preco = 11.90;
    $soma = $preco * 4;
    $soma = number_format(num: $soma, decimal: 2);

    //mostrando resultado
    echo "O nome do cliente é $nome<br>";
    echo "O preço unitário da revista é R$ $preco<br>";
    echo "O total é R$ $soma<br>";

    date_default_timezone_set(timezoneId: 'America/Bahia'); // Set timezone
    $shora = (int)date(forma;: 'H');

    if ($shora < 12) {
        echo "Bom dia";
    } elseif ($shora >= 12 && $hora < 18){
        echo "Boa tarde";
    } else {
        echo "Boa noite";
    }
    
