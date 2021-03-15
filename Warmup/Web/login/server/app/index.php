<?php
    if (isset($_POST['password'])) {
        $password = $_POST['password'];
        $realPass = "anget_anget_pemanasan";

        if (strcmp($password, $realPass) == 0) {
            $flag = "LKS2021{".$realPass."}";
        } else {
            $flag = "Password salah";
        }
    }

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <p>Input password:</p>
        <input type="password" name="password">
        <input type="submit" value="Login">
    </form>

    <?php
        if (isset($_POST['password'])) {
            echo "<p>$flag</p>";
        }
    ?>
</body>
</html>