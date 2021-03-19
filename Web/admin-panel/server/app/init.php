<?php

require_once 'db.php';

$db = new Database();
$conn = $db->getConnection();
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$sql = "CREATE TABLE IF NOT EXISTS users (
	id integer PRIMARY KEY,
	username text NOT NULL,
	password text NOT NULL,
	role text NOT NULL
);";
$conn->exec($sql);

$sql = "INSERT INTO users (username, password, role) VALUES ('adm00n', 'beneran_adm00n', 'admin')";
$conn->exec($sql);