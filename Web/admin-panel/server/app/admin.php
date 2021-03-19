<?php
require_once 'db.php';
$db = new Database();
$conn = $db->getConnection();
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

if (isset($_POST['username']) && isset($_POST['password'])) {

    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT * FROM users WHERE username = '$username'";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    $users = $stmt->fetchAll();

    if (count($users) == 1) {
        $user = $users[0];
        if ($password == $user['password'] && $user['role'] == 'admin') {
            echo 'Selamat datang admin, flag anda LKS2021{sql_injection_adalah_jalan_hekelku_xixixi}';
        } else {
            'username/password salah';
        }
    } else {
        echo 'username/password salah';
    }

} else {
    echo 'username/password tidak boleh kosong';
}
?>