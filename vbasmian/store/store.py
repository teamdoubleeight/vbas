import requests

from .store_exceptions import (
    EntTokenInvalidError,
    RegionInvalidError,
    RequestError,
)

__all__ = (
    "EntTokenInvalidError",
    "RegionInvalidError",
    "RequestError",
    "Store",
)

class Store():
    def storeskins(rg, puuid, ent, at):
        if rg != "kr" and rg != "eu" and rg != "ap" and rg != "pbe" and rg != "na":
            raise RegionInvalidError(
               "Region is invalid. kr/eu/ap/pbe/na are only valid regions." 
            )
        
        header = {"X-Riot-Entitlements-JWT" : ent, "Authorization" : "Bearer " + at}
        
        url = f"https://pd.{rg}.a.pvp.net/store/v2/storefront/{puuid}"
        response = requests.get(url=url, headers=header)

        if response.status_code == 200 : response = response.json()
        elif response.status_code == 403 :
            raise EntTokenInvalidError(
                "Entitlements token is invalid."
            )
        elif response.status_code == 400 :
                raise RequestError(
                "PUUID/Auth Token is invalid or unknwon error happened."
            )
        
        skinspuuid = response['SkinsPanelLayout']['SingleItemOffers']
        
        return skinspuuid[0], skinspuuid[1], skinspuuid[2], skinspuuid[3]
        
    
    def checkbalance(rg, puuid, ent, at):
        if rg != "kr" and rg != "eu" and rg != "ap" and rg != "pbe" and rg != "na":
            raise RegionInvalidError(
               "Region is invalid. kr/eu/ap/pbe/na are only valid regions." 
            )
        
        header = {"X-Riot-Entitlements-JWT" : ent, "Authorization" : "Bearer " + at}
        
        url = f"https://pd.{rg}.a.pvp.net/store/v1/wallet/{puuid}"
        response = requests.get(url=url, headers=header)

        if response.status_code == 200 : response = response.json()
        elif response.status_code == 403 :
            raise EntTokenInvalidError(
                "Entitlements token is invalid."
            )
        elif response.status_code == 400 :
                raise RequestError(
                "PUUID/Auth Token is invalid or unknwon error happened."
            )
        
        vp = response['Balances']['85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741']
        rp = response['Balances']['e59aa87c-4cbf-517a-5983-6e81511be9b7']
        
        return vp,rp
    
    def prices(rg, ent, at):
        if rg != "kr" and rg != "eu" and rg != "ap" and rg != "pbe" and rg != "na":
            raise RegionInvalidError(
               "Region is invalid. kr/eu/ap/pbe/na are only valid regions." 
            )
        
        header = {"X-Riot-Entitlements-JWT" : ent, "Authorization" : "Bearer " + at}
        
        url = f"https://pd.{rg}.a.pvp.net/store/v1/offers"
        response = requests.get(url=url, headers=header)

        if response.status_code == 200 : response = response.json()
        elif response.status_code == 403 :
            raise EntTokenInvalidError(
                "Entitlements token is invalid."
            )
        elif response.status_code == 400 :
                raise RequestError(
                "PUUID/Auth Token is invalid or unknwon error happened."
            )
        
        return response
    
