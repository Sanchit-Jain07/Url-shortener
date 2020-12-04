from hashids import Hashids

hashids=Hashids(salt='9d30d9e3fe2a02c5dba90a4fa9c1cd649e60eac2', min_length=6)

def generate_hash(link_id):
    return hashids.encode(link_id)

def decode_hash(hash):
    return hashids.decode(hash)