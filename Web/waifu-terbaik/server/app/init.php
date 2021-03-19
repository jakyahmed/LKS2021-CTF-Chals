<?php

require_once 'db.php';

$db = new Database();
$conn = $db->getConnection();

$sql = "CREATE TABLE IF NOT EXISTS characters (
	id integer PRIMARY KEY,
	name text NOT NULL
);";
$conn->exec($sql);

$sql = "CREATE TABLE IF NOT EXISTS flags (
	id integer PRIMARY KEY,
	value text NOT NULL
);";
$conn->exec($sql);

$sql = "INSERT INTO flags (value) VALUES ('LKS2021{waifumu_integral_satu_per_t_dt_mas}')";
$conn->exec($sql);