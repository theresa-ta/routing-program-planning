class Package:#this is a blueprint for all packages, each showing these specific attributes so there is minimal repition
    def __init__(self, package_id, address, city, zipcode, deadline):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline

packages = {}

packages[1] = Package(
    1,
    "195 W Oakland Ave",
    "Salt Lake City",
    "84115",
    "1030"
)

packages[2] = Package(
    2,
    "2530 S 500 E",
    "Salt Lake City",
    "84106",
    "EOD"
)

packages[3] = Package(
    3,
    "233 Canyon Rd",
    "Salt Lake City",
    "84103",
    "EOD"
)

packages[4] = Package(
    4,
    "380 W 2880 S",
    "Salt Lake City",
    "84115",
    "EOD"
)

packages[5] = Package(
    5,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "EOD"
)

packages[6] = Package(
    6,
    "3060 Lester St",
    "West Valley City",
    "84119",
    "1030"
)

packages[7] = Package(
    7,
    "1330 2100 S",
    "Salt Lake City",
    "84106",
    "EOD"
)

packages[8] = Package(
    8,
    "300 State St",
    "Salt Lake City",
    "84103",
    "EOD"
)

packages[9] = Package(
    9,
    "300 State St",
    "Salt Lake City",
    "84103",
    "EOD"
)

packages[10] = Package(
    10,
    "600 E 900 S",
    "Salt Lake City",
    "84105",
    "EOD"
)

packages[11] = Package(
    11,
    "2600 Taylorsville BLvd",
    "Salt Lake City",
    "84118",
    "EOD"
)

packages[12] = Package(
    12,
    "3575 W Valley Central Station",
    "West Valley City",
    "84119",
    "EOD"
)

packages[13] = Package(
    13,
    "2010 W 500 S",
    "Salt Lake City",
    "84104",
    "1030"
)

packages[14] = Package(
    14,
    "4300 S 1300 E",
    "Millcreek",
    "84117",
    "1030"
)

packages[15] = Package(
    15,
    "4580 S 2300 E",
    "Holladay",
    "84103",
    "0900"
)

packages[16] = Package(
    16,
    "4580 S 2300 E",
    "Holladay",
    "84103",
    "1030"
)

packages[17] = Package(
    17,
    "3148 S 1100 W",
    "Salt Lake City",
    "84119",
    "EOD"
)

packages[18] = Package(
    18,
    "1488 4800 S",
    "Salt Lake City",
    "84123",
    "EOD"
)

packages[19] = Package(
    19,
    "177 W Price Ave",
    "Salt Lake City",
    "84115",
    "EOD"
)

packages[20] = Package(
    20,
    "3591 Main St",
    "Salt Lake City",
    "84115",
    "1030"
)

packages[21] = Package(
    21,
    "3595 Main St",
    "Salt Lake City",
    "84115",
    "EOD"
)

packages[22] = Package(
    22,
    "6351 South 900 East",
    "Murray",
    "84118",
    "EOD"
)

packages[23] = Package(
    23,
    "5100 South 2700 West",
    "Salt Lake City",
    "84118",
    "EOD"
)

packages[24] = Package(
    24,
    "5025 State St",
    "Murray",
    "84107",
    "EOD"
)

packages[25] = Package(
    25,
    "5383 South 900 East #104",
    "Salt Lake City",
    "84117",
    "1030"
)

packages[26] = Package(
    26,
    "5383 South 900 East #104",
    "Salt Lake City",
    "84117",
    "EOD"
)

packages[27] = Package(
    27,
    "1060 Dalton Ave S",
    "Salt Lake City",
    "84104",
    "EOD"
)

packages[28] = Package(
    28,
    "2835 Main St",
    "Salt Lake City",
    "84115",
    "EOD"
)

packages[29] = Package(
    29,
    "1330 2100 S",
    "Salt Lake City",
    "84106",
    "1030"
)

packages[30] = Package(
    30,
    "300 State St",
    "Salt Lake City",
    "84103",
    "1030"
)

packages[31] = Package(
    31,
    "3365 S 900 W",
    "Salt Lake City",
    "84119",
    "1030"
)

packages[32] = Package(
    32,
    "3365 S 900 W",
    "Salt Lake City",
    "84119",
    "EOD"
)

packages[33] = Package(
    33,
    "2530 S 500 E",
    "Salt Lake City",
    "84106",
    "EOD"
)

packages[34] = Package(
    34,
    "4580 S 2300 E",
    "Holladay",
    "84117",
    "1030"
)

packages[35] = Package(
    35,
    "1060 Dalton Ave S",
    "Salt Lake City",
    "84104",
    "EOD"
)

packages[36] = Package(
    36,
    "2300 Parkway Blvd",
    "West Valley City",
    "84119",
    "EOD"
)

packages[37] = Package(
    37,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "1030"
)

packages[38] = Package(
    38,
    "410 S State St",
    "Salt Lake City",
    "84111",
    "EOD"
)

packages[39] = Package(
    39,
    "2010 W 500 S",
    "Salt Lake City",
    "84104",
    "EOD"
)

packages[40] = Package(
    40,
    "380 W 2880 S",
    "Salt Lake City",
    "84115",
    "1030"
)