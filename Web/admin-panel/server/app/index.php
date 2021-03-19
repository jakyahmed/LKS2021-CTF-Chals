<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>Admin Panel</title>
</head>
<body>
    <div class="w3-container w3-center">
        <h1>Admin Panel Login</h1>
        <h5>Hanya admin yang boleh login</h5>
        <form action="admin.php" method="POST">
            <p>Username:</p><input type="text" name="username">
            <p>Password:</p><input type="password" name="password">
            <p></p>
            <input type="submit" value="login">
        </form>
    </div>
</body>
</html>