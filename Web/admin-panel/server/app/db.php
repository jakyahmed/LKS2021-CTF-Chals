<?php

class Database
{
    private $pdo;

    public function getConnection() {
        if ($this->pdo == null) {
            $this->pdo = new PDO("sqlite:" . __DIR__ . "/databaseadmin1337.db");
        }
        return $this->pdo;
    }
}