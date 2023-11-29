<?php 
ini_set('display_errors', 0); // Turn off error reporting
ini_set('display_startup_errors', 0);
error_reporting(0);

require_once 'vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();


$dbHost = $_ENV['MYSQL_HOST'];
$dbUser = $_ENV['MYSQL_USER'];
$dbPass = $_ENV['MYSQL_PASSWORD'];
$dbName = $_ENV['MYSQL_DATABASE'];

$conn = new mysqli($dbHost, $dbUser, $dbPass, $dbName);

if ($conn->connect_error) {
    die("Unable to connect to database"); // Or handle the error as appropriate
}

$id = $_GET['id']; // Directly taking user input without sanitization
$sql = "SELECT name, price, description, ingredients FROM menu WHERE id = $id";
$result = $conn->query($sql);


if ($result === false) {
    //die("Error executing query"); // Or handle the error as appropriate
}


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poutine Restaurant</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="style.css" rel="stylesheet">
</head>
<body>
 

    <style>
        body {
    margin: 0;
    font-family: Arial, sans-serif;
}

/* Header Styles */
header {
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-brand {
    font-size: 1.5em;
    font-weight: bold;
    color: #ea5455; /* Poutine-themed color */
}

.nav-link {
    font-weight: bold;
    color: #333;
}

.nav-link:hover {
    color: #ea5455;
}

/* Responsive adjustments */
@media (max-width: 992px) {
    .navbar-brand {
        font-size: 1.2em;
    }
}


    body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; }
    .container {
        width: 80%;
        margin: 20px auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start; /* align items to the start */
        gap: 20px; /* space between columns */
    }
    .poutine {
        flex: 0 1 calc(33.333% - 20px); /* maintain the size */
        border: 1px solid #ddd;
        padding: 15px;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-decoration: none; /* remove underline from links */
        color: #333; /* text color */
        transition: transform 0.2s, box-shadow 0.2s; /* smooth transition for hover effect */
    }
    .poutine:hover {
        transform: translateY(-5px); /* subtle lift effect on hover */
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
    }
    .poutine img {
        width: 100%;
        height: auto;
        border-bottom: 1px solid #ddd;
    }
    .poutine h2 {
        color: #ea5455; /* title color */
        margin-top: 10px;
    }
    .price {
        font-weight: bold;
        margin-top: 5px;
    }
    .description {
        margin-top: 10px;
        font-size: 14px;
    }
    a:hover {
    color: #333;
    text-decoration: none; /* Remove underline */
}
</style>

</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <a class="navbar-brand" href="#">Poutine Palace</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="restaurant.php">Home</a>
                        </li>
                        
                        <li class="nav-item">
                            <a class="nav-link" href="about.php">About</a>
                        </li>
                        
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    <div class="container">
        <?php
        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            echo "<div class='poutine'>";
            
            echo "<div class='details'>";
            echo "<h2>" . htmlspecialchars($row["name"]) . "</h2>";
            echo "<p class='price'>$" . htmlspecialchars($row["price"]) . "</p>";
            echo "<p class='description'>" . htmlspecialchars($row["description"]) . "</p>";
            echo "<p class='ingredients'><strong>Ingredients:</strong> " . htmlspecialchars($row["ingredients"]) . "</p>";
            echo "</div>";
            echo "</div>";
        } else {
            echo "<p>Poutine not found!</p>";
        }
        $conn->close();
        ?>
        <a href="restaurant.php" class="back-link">&larr; Back to Menu</a>
    </div>
</body>
</html>
