<?php

// $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

// $arr=json_encode($defaultdata);



// $data="HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=";

// $data_decrypted=base64_decode($data);


// echo strlen($data_decrypted);

// echo "\n";

// echo strlen($arr);

// echo "\n";

// echo $arr;

// echo "\n";
// echo "\n";


// for($i=0;$i<strlen($arr);$i++){
//     $out=$arr[$i]^$data_decrypted[$i];
//     echo "$out ";
// }






$requireddata= array("showpassword"=>"yes", "bgcolor"=>"#ffffff");




function xor_encrypt($in) {
    $key="eDWo";
    $text = $in;
    $outText = '';

    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}


function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}


$data = loadData($requireddata);

$ans=base64_encode(xor_encrypt(json_encode($data)));


echo "ans: $ans";




?>