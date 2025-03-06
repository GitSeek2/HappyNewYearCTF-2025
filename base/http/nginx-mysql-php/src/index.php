<!DOCTYPE html>
<html>

<head>
    <link href="https://cdn.jsdelivr.net/npm/jetbrains-mono@1.0.6/css/jetbrains-mono.min.css"
          rel="stylesheet" />
    <style>
        body {
            font-family: "JetBrains Mono", monospace;
            background: #fff;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            overflow: hidden;
        }

        .title {
            position: relative;
            font-size: 6rem;
            font-style: italic;
            text-transform: uppercase;
            background: linear-gradient(90deg, #ff0000, #00ff00, #0000ff, #ff0000);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: flow 12s linear infinite;
            width: 100%;
            text-align: center;
            margin-bottom: 2rem;
        }

        @keyframes flow {
            0% {
                background-position: 0% 50%;
            }

            100% {
                background-position: 400% 50%;
            }
        }

        pre {
            font-family: "JetBrains Mono", monospace;
            background: #f5f5f5;
            padding: 1rem;
            border-radius: 8px;
            width: 48rem;
            max-height: calc(100vh - 30rem);
            overflow-y: auto;
            margin-top: 2rem;
            text-align: center;
        }

        @media (max-width: 768px) {
            .title {
                font-size: 4rem;
            }

            pre {
                font-size: 1rem;
            }
        }
    </style>
</head>

<body>
    <h1 class="title"
        data-text="CSSEC">CSSEC</h1>
    <a href="phpinfo.php">phpinfo</a>
    <pre>
        <?php
        include_once("database.php");
        global $conn;

        $sql = "SELECT flag FROM flag LIMIT 1";
        $result = $conn->query($sql);

        if ($result && $result->num_rows > 0) {
            $row = $result->fetch_assoc();
            echo $row['flag'];
        } else {
            echo "flag 查询失败";
        }

        $conn->close();
        ?>
    </pre>
</body>

</html>