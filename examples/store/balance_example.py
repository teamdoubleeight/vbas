from vbaspy.vbasmian.store import *

# auth token (Change this to user's auth token)
authtoken = "Auth Token"
# entitlements token (Change this to user's entitlements token)
enttoken = "Ent Token"

# user region (Change this to user's region)
region = "rg"

# user puuid (Change this to user's puuid)
puuid = "puuid"

f = Store.checkbalance(region, puuid, enttoken, authtoken) # Main function, requeires 4 variables
# Returns 3 int obejcts to tuple, VP,RP,Unknwon currency(maybe KingdomPoint)

print("Result : " + str(f)) # Printing result

print("VP : " +  str(f[0]) + "\nRP : " + str(f[1]) + "\nFree Agents : " + str(f[2])) # VP,RP,and Unknwon point


