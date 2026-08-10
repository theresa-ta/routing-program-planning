class Package:#this is a blueprint for all packages, each showing these specific attributes so there is minimal repition
    def __init__(self, package_id, address, city, zipcode, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight

        self.status = "At Hub"
        self.delivery_time = None

packages = [
Package(
    1,
    "195 W Oakland Ave",
    "Salt Lake City",
    "84115",
    "1030",
    21
),

Package(
    2,
    "2530 S 500 E",
    "Salt Lake City",
    "84106",
    "EOD",
    44
),
Package(
    3,
    "233 Canyon Rd",
    "Salt Lake City",
    "84103",
    "EOD",
    2
),

Package(
    4,
    "380 W 2880 S",
    "Salt Lake City",
    "84115",
    "EOD",
    4
),

Package(
    5,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "EOD",
    5
),

Package(
    6,
    "3060 Lester St",
    "West Valley City",
    "84119",
    "1030",
    88
),

Package(
    7,
    "1330 2100 S",
    "Salt Lake City",
    "84106",
    "EOD",
    8
),

Package(
    8,
    "300 State St",
    "Salt Lake City",
    "84103",
    "EOD",
    9
),

Package(
    9,
    "300 State St",
    "Salt Lake City",
    "84103",
    "EOD",
    2
),

Package(
    10,
    "600 E 900 S",
    "Salt Lake City",
    "84105",
    "EOD",
    1
),

Package(
    11,
    "2600 Taylorsville BLvd",
    "Salt Lake City",
    "84118",
    "EOD",
    1
),

Package(
    12,
    "3575 W Valley Central Station",
    "West Valley City",
    "84119",
    "EOD",
    1
),

Package(
    13,
    "2010 W 500 S",
    "Salt Lake City",
    "84104",
    "1030",
    1
),

Package(
    14,
    "4300 S 1300 E",
    "Millcreek",
    "84117",
    "1030",
    88
),

Package(
    15,
    "4580 S 2300 E",
    "Holladay",
    "84103",
    "0900",
    4
),

Package(
    16,
    "4580 S 2300 E",
    "Holladay",
    "84103",
    "1030",
    88
),

Package(
    17,
    "3148 S 1100 W",
    "Salt Lake City",
    "84119",
    "EOD",
    2
),

Package(
    18,
    "1488 4800 S",
    "Salt Lake City",
    "84123",
    "EOD",
    6
),

Package(
    19,
    "177 W Price Ave",
    "Salt Lake City",
    "84115",
    "EOD",
    37
),

Package(
    20,
    "3591 Main St",
    "Salt Lake City",
    "84115",
    "1030",
    37
),

Package(
    21,
    "3595 Main St",
    "Salt Lake City",
    "84115",
    "EOD",
    3
),

Package(
    22,
    "6351 South 900 East",
    "Murray",
    "84118",
    "EOD",
    2
),

Package(
    23,
    "5100 South 2700 West",
    "Salt Lake City",
    "84118",
    "EOD",
    5
),

Package(
    24,
    "5025 State St",
    "Murray",
    "84107",
    "EOD",
    7
),

Package(
    25,
    "5383 South 900 East #104",
    "Salt Lake City",
    "84117",
    "1030",
    7
),

Package(
    26,
    "5383 South 900 East #104",
    "Salt Lake City",
    "84117",
    "EOD",
    25
),

Package(
    27,
    "1060 Dalton Ave S",
    "Salt Lake City",
    "84104",
    "EOD",
    5
),

Package(
    28,
    "2835 Main St",
    "Salt Lake City",
    "84115",
    "EOD",
    7
),

Package(
    29,
    "1330 2100 S",
    "Salt Lake City",
    "84106",
    "1030",
    2
),

Package(
    30,
    "300 State St",
    "Salt Lake City",
    "84103",
    "1030",
    1
),

Package(
    31,
    "3365 S 900 W",
    "Salt Lake City",
    "84119",
    "1030",
    1
),

Package(
    32,
    "3365 S 900 W",
    "Salt Lake City",
    "84119",
    "EOD",
    1
),

Package(
    33,
    "2530 S 500 E",
    "Salt Lake City",
    "84106",
    "EOD",
    1
),

Package(
    34,
    "4580 S 2300 E",
    "Holladay",
    "84117",
    "1030",
    2
),

Package(
    35,
    "1060 Dalton Ave S",
    "Salt Lake City",
    "84104",
    "EOD",
    88
),

Package(
    36,
    "2300 Parkway Blvd",
    "West Valley City",
    "84119",
    "EOD",
    88
),

Package(
    37,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "1030",
    2
),

Package(
    38,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "EOD",
    9
),

Package(
    39,
    "2010 W 500 S",
    "Salt Lake City",
    "84104",
    "EOD",
    9
),

Package(
    40,
    "380 W 2880 S",
    "Salt Lake City",
    "84115",
    "1030",
    45
)

]
"""so far, i created a class (blueprint) for each package to follow. 
after that, i created an object for each individual package assigning 
a package to all of its attributes without having to repeatidly 
identify id, address, zip, etc.

then, i created an empty list to store all of the packages, like 
a hash table for lookup
"""

#package = packages[1]
#print("Package ID:", package.delivery_time)
#test case