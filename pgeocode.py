# Checking for country "India"
import pgeocode
nomi = pgeocode.Nominatim('In')

# Getting geo information by passing the postcodes

nomi.query_postal_code(["620018", "620017", "620012"])