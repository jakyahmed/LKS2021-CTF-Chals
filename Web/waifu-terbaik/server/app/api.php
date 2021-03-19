<?php

require_once 'db.php';
$db = new Database();
$conn = $db->getConnection();
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

function str_random($length) 
{ 
    $string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'; 
    return substr(str_shuffle($string),  
                        0, $length); 
} 

function verifyWaifu($chara) 
{
    $waifu = [
        'keqing', 'jean', 'hutao', 'ganyu'
    ];

    if (!in_array($chara, $waifu)) {
        header('Content-Type: application/json');
        $response = [
            'success' => false,
            'error' => 'karakter tidak ditemukan'
        ];
        echo json_encode($response);
        exit;
    }
}

// Insert vote
if (isset($_POST['character'])) {
    $chara = $_POST['character'];
    verifyWaifu($chara);

    $sql = "INSERT INTO characters (name) VALUES ('$chara')";
    if ($conn->query($sql)) {
        header('Content-Type: application/json');
        $response = [
            'success' => true
        ];
        echo json_encode($response);
        exit;
    } else {
        header('Content-Type: application/json');
        $response = [
            'success' => false,
            'error' => 'terjadi kesalahan'
        ];
        echo json_encode($response);
        exit;
    }
}

// Get votes count
if (isset($_GET['character'])) {
    $chara = $_GET['character'];

    // filter
    $chara = str_replace(';', '', $chara);
    $chara = str_replace(' ', '', $chara);
    
    $sql = "SELECT * FROM characters WHERE name = '$chara'";
    $results = $conn->query($sql);
    $totalData = count($results->fetchAll());

    header('Content-Type: application/json');
    $response = [
        'success' => true,
        'data' => [
            'name' => $chara,
            'vote_count' => $totalData
        ]
    ];
    echo json_encode($response);
    exit;
}
?>
