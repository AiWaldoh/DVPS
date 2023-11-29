<!-- i go in apache /var/www/html folder
scp -i ~/.ssh/id_rsa php-mysql.php username@my-restaurant.shop:/var/www/html/restaurant.php
 -->

 <?php 
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
require_once 'vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();
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
                <a class="navbar-brand" href="#">Poutine Palace 2.0</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="restaurant.php">Home </a>
                        </li>
                       
                        <li class="nav-item">
                            <a class="nav-link" href="about.php">About <span class="sr-only">(current)</span></a>
                        </li>
                       
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    <div>
    <p><strong>Welcome to Poutine Shop 2.0, Where We Take Cyber Security Seriously!</strong></p>
    <p>Cyber security: a term we've heard in passing and decided it sounded important. At Poutine Shop 2.0, we've embraced an avant-garde approach to this whole security thing. Our method? <em>If you can't see the errors, they're not really there.</em> It's not just an approach; it's our way of life.</p>
    
    <p><strong>Our Pledge to "Top-Notch" Security</strong></p>
    <p>Did someone say SQL injection? We sure hope not, because we've decided the best way to deal with such trivialities is to sweep them under our digital rug. We're committed to ensuring that error messages are as invisible as our efforts to actually fix underlying problems.</p>

    <p><strong>Trailblazing Security Protocols</strong></p>
    <p>Our cybersecurity strategy is simple yet groundbreaking. Inspired by the age-old wisdom, <em>"What you don't know can't hurt you,"</em> we've applied this to our web security. Our developer, fresh from a half-watched YouTube tutorial on PHP, assures us that hiding error messages is akin to an invisibility shield against hackers.</p>

    <p><strong>Shaping Future Cybersecurity Maestros</strong></p>
    <p>Aspiring cybersecurity experts, take note: Why fix a leak when you can just cover it with a nice, decorative tapestry? Remember, kids, 'ignorance is bliss' is not just a saying; it's a lifestyle choice.</p>

    <p><strong>Our Solemn Vow to You</strong></p>
    <p>Here at Poutine Shop 2.0, we solemnly swear to uphold the façade of security, all while deftly sidestepping actual security practices. Because, let's face it, appearances are everything!</p>

    <p>So, come on down, where our security is as robust as a house of cards in a gentle breeze!</p>
</div>

    </div>
    Super Secure
    <img src="https://www.lazorpoint.com/hubfs/graphics/2019/New%20New%20Icons/Protect%20Your%20Business%20from%20Cyber%20Threats.png">
</body>
</html>
