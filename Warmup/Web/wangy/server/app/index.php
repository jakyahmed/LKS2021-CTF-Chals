<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wangy</title>
</head>
<body>
    <h1>Wangy wangy</h1>
    <form method="POST">
        <p>Input name:</p>
        <input type="text" name="name">
        <input type="submit" value="Submit">
    </form>

    <?php
        if (isset($_POST['name'])) {
            $name = $_POST['name'];
            passthru("echo '$name wangy wangy wangy'");
        }
    ?>
</body>
</html>