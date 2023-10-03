from vbaspy.vbasmian.store import *

# auth token (Change this to user's auth token)
authtoken = "Auth Token"
# entitlements token (Change this to user's entitlements token)
enttoken = "Ent Token"

# user region (Change this to user's region)
region = "rg"

# user puuid (Change this to user's puuid)
puuid = "puuid"

print(str(Store.storeskins(region, puuid, enttoken, authtoken))) # Main function, requeires 4 variables
# Returns 4 str obejcts to tuple, each skin's puuid
