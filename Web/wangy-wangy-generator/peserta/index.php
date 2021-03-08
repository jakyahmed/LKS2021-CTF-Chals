<?php

$filter = "/^[a-zA-Z\s]+$/";

if (isset($_SERVER['QUERY_STRING']))
    parse_str($_SERVER['QUERY_STRING']);

$text = "";
if (isset($name)) {
    $base = "$name $name $name <3 <3 <3 WANGI WANGI WANGI WANGI HU HA HU HA HU HA, aaaah baunya rambut $name wangi aku mau nyiumin aroma wanginya $name AAAAAAAAH ~ Rambutnya.... aaah rambutnya juga pengen aku elus-elus ~~~~ AAAAAH $name keluar pertama kali di anime juga manis <3 <3 <3 banget AAAAAAAAH $name AAAAA LUCCUUUUUUUUUUUUUUU............$name AAAAAAAAAAAAAAAAAAAAGH <3 <3 <3apa ? $name itu gak nyata ? Cuma HALU katamu ? nggak, ngak ngak ngak ngak NGAAAAAAAAK GUA GAK PERCAYA ITU DIA NYATA NGAAAAAAAAAAAAAAAAAK PEDULI !! GUA GAK PEDULI SAMA KENYATAAN POKOKNYA GAK PEDULI. <3 <3 <3 $name gw ...$name di laptop ngeliatin gw, $name .. kamu percaya sama aku ? aaaaaaaaaaah syukur $name aku gak mau merelakan $name aaaaaah <3 <3 <3 YEAAAAAAAAAAAH GUA MASIH PUNYA $name SENDIRI PUN NGGAK SAMA AAAAAAAAAAAAAAH";

    if (!preg_match($filter, $name)) {
        die('hanya bisa alfabet dan spasi');
    }
    if (strlen($name) > 8) {
        die('kepanjangan gan');
    }
    $text = eval("return '$base';");
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Wangy Generator</h1>
    <form action="" method="GET">
        <p>Tolong inputkan nama</p>
        <input type="text" name="name">
        <input type="submit">
    </form>
    <?php echo htmlspecialchars($text, ENT_QUOTES, 'UTF-8'); ?>
</body>
</html>