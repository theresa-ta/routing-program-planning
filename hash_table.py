#no import needed even though im referencing package_id?

class HashTable:
    def __init__(self): #first we make a hash table. 40 rows filled with none so it can be inserted w packages
        self.table = [None] * 40

    def hashkey(self, key): #create key, hash table need unique ID to access/hash
        return key - 1 #since list start at 0, key - 1 will place package # to index #. ex: package 1 = 1 - 1 = 0, package 1 is the first package so it should go to list[0].
    
    def insert(self, package): #create insert to be able to insert package into hash table self.table
        bucket = self.hashkey(package.package_id) #how you are storing the package in the bucket, through hashkey
        self.table[bucket] = package #replaces None with package

    def lookup(self, package_id):
        bucket = self.hashkey(package_id)
        return self.table[bucket]