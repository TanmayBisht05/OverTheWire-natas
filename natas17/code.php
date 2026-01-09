<?php

$name='$(passthru("pwd")';

$query = "SELECT * from users where username=\"".$name."\"";


$cmd="pwd";



passthru($cmd);

echo $query;


?>
