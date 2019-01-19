import aqt
from aqt import mw

userOption = None
def getUserOption(key = None, default = None):
    print(f"getUserOption(key = {key}, default = {default})")
    global userOption
    if userOption is None:
        userOption = aqt.mw.addonManager.getConfig(__name__)
        print(f"userOption is {userOption}")
    if key is None:
        print(f"return {userOption}")
        return userOption
    if key in userOption:
        print(f"key in userOption. Returning {userOption[key]}")
        return userOption[key]
    else:
        print("key not in userOption. Returning default.")
        return default

def update(_):
    global userOption
    userOption = None
    
mw.addonManager.setConfigUpdatedAction(__name__,update)
