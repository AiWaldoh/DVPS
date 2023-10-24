import MySQLdb

# Database config
HOST = "localhost"
USER = "kevinadmin"
PASSWORD = "password"  # replace with your MySQL password
DB_NAME = "poutine_shop"

# Connect to MySQL
connection = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD)
cursor = connection.cursor()

# Create database if it doesn't exist
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")

# Create users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    home_address VARCHAR(255),
    city VARCHAR(255),
    province VARCHAR(50),
    postal_code VARCHAR(10),
    password VARCHAR(255) NOT NULL,
    about_me TEXT,
    date_of_birth DATE,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    favorite_poutine VARCHAR(255),
    profile_picture TEXT
)
""")

# Insert dummy users data
users_data = [
    ("John", "Doe", "john.doe@example.com", "123 Maple St", "Montreal", "QC", "H2Y 1Z7", "johndoe123", "I love poutines!", "1985-05-15", "Galactic Gravy Galaxy", "https://via.placeholder.com/200x150.png?text=Galactic+Gravy+Galaxy"),
    ("Jane", "Smith", "jane.smith@example.com", "456 Birch Ave", "Toronto", "ON", "M4B 1B7", "janesmith456", "Poutine enthusiast!", "1990-03-10", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Cheese+Curd+Comet"),
    ("Kevin", "Bacon", "kevin.bacon@example.com", "789 Pine Rd", "Vancouver", "BC", "V5Z 2T9", "kevinbacon789", "Poutine is life!", "1980-07-20", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Fry+Nebula+Supernova"),
    ("Évangeline", "Star", "evangeline.star@example.com", "101 Acadia Ave", "Moncton", "NB", "E1C 5Y7", "evastar101", "J'adore le tintamarre!", "1975-08-15", "Pépère’s Poutine Party", "https://via.placeholder.com/200x150.png?text=Pépère’s+Poutine"),
    ("Louis", "Tintamarre", "louis.tint@example.com", "102 Noise St", "Dieppe", "NB", "E1A 3Z9", "loudlouis789", "Ça barde, hein?", "1982-04-05", "Lobster Trap Lattice", "https://via.placeholder.com/200x150.png?text=Lobster+Poutine"),
    ("Cécile", "Rebelle", "cecile.rebel@example.com", "103 Rebel Rd", "Bathurst", "NB", "E2A 6T8", "rebelcecile567", "Je suis pure laine!", "1989-11-20", "Bonhomme Grits Gravy", "https://via.placeholder.com/200x150.png?text=Bonhomme+Grits"),
    ("Jacques", "Dory", "jacques.dory@example.com", "104 Fisherman Way", "Shediac", "NB", "E4P 2W6", "fisherjack123", "À la bonne franquette!", "1972-02-18", "Dulse Dive Delight", "https://via.placeholder.com/200x150.png?text=Dulse+Delight"),
    ("Marie", "Beausoleil", "marie.beau@example.com", "105 Sunshine St", "Bouctouche", "NB", "E4S 3H5", "sunnymarie890", "Tant qu'à moi!", "1995-07-30", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Beachside+Bechamel"),
    ("Henri", "LeBlanc", "henri.leblanc@example.com", "106 Blanc Blvd", "Edmundston", "NB", "E3V 1J8", "whitehenry456", "C'est right d'fun!", "1968-12-10", "Fiddlehead Fry Festival", "https://via.placeholder.com/200x150.png?text=Fiddlehead+Fry"),
    ("Josette", "Bouctouche", "josette.bouch@example.com", "107 Dune Dr", "Campbellton", "NB", "E3N 1T7", "dunejose111", "Ça vaut la peine!", "1992-09-03", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Musical+Maudite"),
    ("René", "Arseneau", "rene.arseneau@acadie.com", "10 Rue d'Acadie", "Moncton", "NB", "E1C 8W4", "arseneaurene", "Le bon temps rouler!", "1978-06-15", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Tarte+Tariflette"),
    ("Lucie", "Thériault", "lucie.theriault@maritimes.ca", "25 Baie Crescent", "Dieppe", "NB", "E1A 4P7", "lucielouise", "Chiac and proud!", "1987-10-10", "Chiac Cheese Chunk", "https://via.placeholder.com/200x150.png?text=Chiac+Cheese"),
    ("Marc", "Boudreau", "marc.boudreau@nouvelle.ca", "45 Rivière Road", "Bathurst", "NB", "E2A 5R8", "boudreauboy", "À la prochaine!", "1982-09-22", "Galactic Gravy Galaxy", "https://via.placeholder.com/200x150.png?text=Rappie+Pie"),
    ("Élise", "Landry", "elise.landry@miramichi.net", "128 Coastal Court", "Miramichi", "NB", "E1V 6N5", "miramichimuse", "Mer et montagnes!", "1990-11-11", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Maritime+Melt"),
    ("Guy", "Robichaud", "guy.robichaud@lamer.ca", "64 Océan Avenue", "Shediac", "NB", "E4P 2L3", "robichaudrocks", "Vive le vent!", "1975-03-05", "Codiac Curd Clash", "https://via.placeholder.com/200x150.png?text=Codiac+Curd"),
    ("Nicole", "Melanson", "nicole.melanson@lobster.love", "512 Crustacean Close", "Bouctouche", "NB", "E4S 3J6", "nicolenovelle", "Bercé par les vagues.", "1988-05-19", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Lobster+Layers"),
    ("Antoine", "Belliveau", "antoine.belliveau@acadien.org", "238 History Heights", "Church Point", "NS", "B0W 1M0", "belliveaubeat", "Avec un accent!", "1977-02-02", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Nova+Nectar"),
    ("Madeleine", "LeBlanc", "madeleine.leblanc@cape.coast", "18 Cape Court", "Chéticamp", "NS", "B0E 1H0", "capeclanqueen", "Dances with the tide.", "1992-12-25", "Chéticamp Cheese Chase", "https://via.placeholder.com/200x150.png?text=Chéticamp+Cheese"),
    ("Clément", "Cormier", "clement.cormier@bay.beauty", "92 Bay Breeze Blvd", "Tracadie", "NB", "E1X 1A4", "tracadietrend", "Belle baie, belles gens!", "1983-04-15", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Belle+Baie"),
    ("Sophie", "Girouard", "sophie.girouard@fiddle.fest", "56 Fiddlehead Forest", "Saint-Quentin", "NB", "E8A 2K7", "fiddlefestfan", "Nature and notes.", "1985-01-30", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Forest+Fry"),
    ("Mathieu", "Comeau", "mathieu.comeau@tidalwave.net", "5 Marée Rise", "Petit-Rocher", "NB", "E8J 1A5", "tidechaser789", "Where the tide meets time.", "1974-07-17", "Tidal Turnover Twist", "https://via.placeholder.com/200x150.png?text=Tidal+Turnover"),
    ("Nathalie", "Dupuis", "nathalie.dupuis@foggyfun.ca", "48 Brume Lane", "Campobello", "NB", "E5E 1Z5", "mistymirth", "Island in the mist.", "1987-06-06", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Foggy+Fry"),
    ("Philippe", "Daigle", "philippe.daigle@maplemagic.com", "92 Érable St", "Memramcook", "NB", "E4K 3P5", "maplemaven", "Where syrup sings.", "1980-11-28", "Galactic Gravy Galaxy", "https://via.placeholder.com/200x150.png?text=Maple+Medley"),
    ("Caroline", "Forest", "caroline.forest@pinepride.ca", "18 Pin Place", "Kedgwick", "NB", "E8B 1W7", "pineprincess", "Where pines whisper.", "1986-03-14", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Pine+Platter"),
    ("Gilles", "Léger", "gilles.leger@lighthouselove.net", "72 Phare Point", "Miscou Island", "NB", "E8T 2J3", "beaconbuff", "Guided by the light.", "1978-02-21", "Cheese Curd Comet", "https://via.placeholder.com/200x150.png?text=Lighthouse+Lunch"),
    ("Denise", "Savoie", "denise.savoie@starfishsea.org", "34 Étoile Shore", "Neguac", "NB", "E9G 1A8", "seastarshine", "Stars above and below.", "1990-09-09", "Galactic Gravy Galaxy", "https://via.placeholder.com/200x150.png?text=Starfish+Sauce"),
    ("Bernard", "Allain", "bernard.allain@bluenosebounce.ca", "89 Bluenose Boulevard", "Dalhousie", "NB", "E8C 2X2", "bluenosebooster", "Where the nose knows!", "1976-05-05", "Galactic Gravy Galaxy", "https://via.placeholder.com/200x150.png?text=Bluenose+Brunch"),
    ("Céline", "Bourque", "celine.bourque@whalewonder.net", "55 Baleine Beach", "St. Martins", "NB", "E5R 1A7", "whalewatcher", "Majesty of the deep.", "1988-12-12", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Whale+Whimsy"),
    ("Rémi", "Gautreau", "remi.gautreau@rockyridge.org", "128 Roche Ridge", "Saint-Isidore", "NB", "E8M 1E5", "rockyroadrunner", "Strength in stones.", "1983-01-20", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Rocky+Rumble"),
    ("Florence", "Gagnon", "florence.gagnon@butterflybreeze.com", "66 Papillon Path", "Saint-Léonard", "NB", "E7E 2L7", "butterflybliss", "Wings of wonder.", "1991-04-18", "Fry Nebula Supernova", "https://via.placeholder.com/200x150.png?text=Butterfly+Bounty"),
    ("pmm", "pmm", "NONE", "NONE", "NONE", "NONE", "pmm", "pmmpassword", "NONE", "NONE", "NONE", "NONE"),




]

# Prepare the INSERT INTO statement
insert_query = """
INSERT INTO users 
(first_name, last_name, username, home_address, city, province, postal_code, password, about_me, date_of_birth, favorite_poutine, profile_picture) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""



# Use the cursor's executemany() method to insert all records at once
cursor.executemany(insert_query, users_data)
# Create menu table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(5, 2) NOT NULL,
    description TEXT,
    ingredients TEXT,
    image TEXT
)
""")
# Insert dummy menu data
menu_data = [
    ("Classic Poutine", 6.99, "Traditional poutine with cheese and gravy", "Fries, Cheese curds, Gravy", "path/to/image1.jpg"),
    ("Bacon Poutine", 8.99, "Poutine topped with crispy bacon", "Fries, Cheese curds, Gravy, Bacon", "path/to/image2.jpg"),
    ("Veggie Poutine", 7.49, "Poutine with sauteed vegetables", "Fries, Cheese curds, Gravy, Mixed vegetables", "path/to/image3.jpg"),
    ("Healthy Poutine", 9.99, "Poutine with no fries, cheese, or gravy", "Nothing", "path/to/image4.jpg")
]
cursor.executemany("INSERT INTO menu (name, price, description, ingredients, image) VALUES (%s, %s, %s, %s, %s)", menu_data)

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()

print("Database populated successfully!")
