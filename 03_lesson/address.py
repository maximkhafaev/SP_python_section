class Address:

    def __init__(self, zip, city, street, build, ap):
        self.zip_code = zip
        self.city = city
        self.street = street
        self.building = build
        self.apartment = ap

    def getAddress(self):
        str = self.zip_code + ', ' + self.city + ', ' + self.street + ', ' + self.building + ' — ' + self.apartment
        return str