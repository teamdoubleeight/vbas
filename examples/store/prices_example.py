from vbaspy.vbasmian.store import *

# auth token (Change this to user's auth token)
authtoken = "Auth Token"
# entitlements token (Change this to user's entitlements token)
enttoken = "Ent Token"

# user region (Change this to user's region)
region = "rg"


f = Store.prices(region, enttoken, authtoken) # Main function, requeires 4 variables
# Returns 3 int obejcts to tuple, VP,RP,Unknwon currency(maybe KingdomPoint)
