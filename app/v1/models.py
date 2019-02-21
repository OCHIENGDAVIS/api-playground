offices = []
parties = []

class Office:
    def __init__(self,_id, name, _type):
        self.id = _id
        self.name = name
        self.type = _type

    @classmethod
    def save_office(cls, _id, name, _type):
        office = Office(_id, name, _type)
        created_office ={
            "id": office.id,
            "name": office.name,
            "type": office.type
        }
        offices.append(created_office)
        return created_office


    @classmethod
    def get_all_offices(cls):
        return offices

    @classmethod
    def get_an_office_by_id(cls, _id):
        for office in offices:
            if office["id"] == _id:
                return office
        return False


    @classmethod
    def office_does_not_exists(csl,_id):
        for office in offices:
            if office["id"] == _id:
                return False
        return True




class Party:
    def __init__(self, _id, name, hqaddress, logourl):
        self.id = _id
        self.name = name
        self.hqaddress = hqaddress
        self.logourl = logourl

    @classmethod
    def save_party(cls, _id,name, hqaddress, logourl ):
        new_party = Party(_id, name, hqaddress, logourl)
        created_party = {
            "id":new_party.id,
            "name": new_party.name,
            "hqaddress": new_party.hqaddress,
            "logourl": new_party.logourl
        }
        parties.append(created_party)
        return created_party

    @classmethod
    def get_all_parties(cls):
        return parties

    @classmethod
    def party_does_not_exists(cls, _id):
        for party in parties:
            if party["id"] == _id:
                return False
        return True

    @classmethod
    def get_a_party_by_id(cls, _id):
        for party in parties:
            if party["id"] == _id:
                return party
        return False

    @classmethod
    def patch_a_party(cls, _id, name):
        for party in parties:
            if party["id"] == _id:
                party["name"] = name
                return party
        return False

    @classmethod
    def delete_a_party(cls, _id):
        for party in parties:
            if party["id"] == _id:
                party_index = parties.index(party)
                del parties[party_index]
                return party
        return False


