<?php

class Database
{
    private $pdo;

    public function getConnection() {
        if ($this->pdo == null) {
            $this->pdo = new PDO("sqlite:" . __DIR__ . "/bestwaifu.db");
        }
        return $this->pdo;
    }
}