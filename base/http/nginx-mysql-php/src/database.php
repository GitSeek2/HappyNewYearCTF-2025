<?php
$hostname = "localhost";
$username = "root";
$password = "123456";
$dbname = "cssec";

$conn = new mysqli($hostname, $username, $password, $dbname);

if ($conn->connect_error) {
    die("数据库连接失败: " . $conn->connect_error);
}