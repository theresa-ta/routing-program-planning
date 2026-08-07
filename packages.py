class Package:#this is a blueprint for all packages, each showing these specific attributes so there is minimal repition
    def __init__(self, package_id, address, city, zipcode, deadline):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline

packages = [
Package(
    1,
    "195 W Oakland Ave",
    "Salt Lake City",
    "84115",
    "1030"
),

Package(
    2,
    "2530 S 500 E",
    "Salt Lake City",
    "84106",
    "EOD"
),
Package(
    3,
    "233 Canyon Rd",
    "Salt Lake City",
    "84103",
    "EOD"
),

Package(
    4,
    "380 W 2880 S",
    "Salt Lake City",
    "84115",
    "EOD"
),

Package(
    5,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "EOD"
),

Package(
    6,
    "3060 Lester St",
    "West Valley City",
    "84119",
    "1030"
),

Package(
    7,
    "1330 2100 S",
    "Salt Lake City",
    "84106",
    "EOD"
),

Package(
    8,
    "300 State St",
    "Salt Lake City",
    "84103",
    "EOD"
),

Package(
    9,
    "300 State St",
    "Salt Lake City",
    "84103",
    "EOD"
),

Package(
    10,
    "600 E 900 S",
    "Salt Lake City",
    "84105",
    "EOD"
),

Package(
    11,
    "2600 Taylorsville BLvd",
    "Salt Lake City",
    "84118",
    "EOD"
),

Package(
    12,
    "3575 W Valley Central Station",
    "West Valley City",
    "84119",
    "EOD"
),

Package(
    13,
    "2010 W 500 S",
    "Salt Lake City",
    "84104",
    "1030"
),

Package(
    14,
    "4300 S 1300 E",
    "Millcreek",
    "84117",
    "1030"
),

Package(
    15,
    "4580 S 2300 E",
    "Holladay",
    "84103",
    "0900"
),

Package(
    16,
    "4580 S 2300 E",
    "Holladay",
    "84103",
    "1030"
),

Package(
    17,
    "3148 S 1100 W",
    "Salt Lake City",
    "84119",
    "EOD"
),

Package(
    18,
    "1488 4800 S",
    "Salt Lake City",
    "84123",
    "EOD"
),

Package(
    19,
    "177 W Price Ave",
    "Salt Lake City",
    "84115",
    "EOD"
),

Package(
    20,
    "3591 Main St",
    "Salt Lake City",
    "84115",
    "1030"
),

Package(
    21,
    "3595 Main St",
    "Salt Lake City",
    "84115",
    "EOD"
),

Package(
    22,
    "6351 South 900 East",
    "Murray",
    "84118",
    "EOD"
),

Package(
    23,
    "5100 South 2700 West",
    "Salt Lake City",
    "84118",
    "EOD"
),

Package(
    24,
    "5025 State St",
    "Murray",
    "84107",
    "EOD"
),

Package(
    25,
    "5383 South 900 East #104",
    "Salt Lake City",
    "84117",
    "1030"
),

Package(
    26,
    "5383 South 900 East #104",
    "Salt Lake City",
    "84117",
    "EOD"
),

Package(
    27,
    "1060 Dalton Ave S",
    "Salt Lake City",
    "84104",
    "EOD"
),

Package(
    28,
    "2835 Main St",
    "Salt Lake City",
    "84115",
    "EOD"
),

Package(
    29,
    "1330 2100 S",
    "Salt Lake City",
    "84106",
    "1030"
),

Package(
    30,
    "300 State St",
    "Salt Lake City",
    "84103",
    "1030"
),

Package(
    31,
    "3365 S 900 W",
    "Salt Lake City",
    "84119",
    "1030"
),

Package(
    32,
    "3365 S 900 W",
    "Salt Lake City",
    "84119",
    "EOD"
),

Package(
    33,
    "2530 S 500 E",
    "Salt Lake City",
    "84106",
    "EOD"
),

Package(
    34,
    "4580 S 2300 E",
    "Holladay",
    "84117",
    "1030"
),

Package(
    35,
    "1060 Dalton Ave S",
    "Salt Lake City",
    "84104",
    "EOD"
),

Package(
    36,
    "2300 Parkway Blvd",
    "West Valley City",
    "84119",
    "EOD"
),

Package(
    37,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "1030"
),

Package(
    38,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "EOD"
),

Package(
    39,
    "2010 W 500 S",
    "Salt Lake City",
    "84104",
    "EOD"
),

Package(
    40,
    "380 W 2880 S",
    "Salt Lake City",
    "84115",
    "1030"
)

]
"""so far, i created a class (blueprint) for each package to follow. 
after that, i created an object for each individual package assigning 
a package to all of its attributes without having to repeatidly 
identify id, address, zip, etc.

then, i created an empty dictionary to store all of the packages, like 
a hash table for lookup
"""

#package = packages[1]
#print("Package ID:", package.package_id)
#test case