from ipapi import location

def get_location(ip):
    res = location(ip)
    return res.get('country_name') + ', ' + res.get('region_name') + ', ' + res.get('city')