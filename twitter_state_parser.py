import regex as re

#----------------------------------------------------------------------------------------------------------------------#
# Alabama locations
def is_alabama(location):
    states_pattern = r'\bAlabama\b'
    abbrev_pattern = r'\bAL\b'
    cities_pattern = r'\b(Montgomery|Huntsville|Jefferson|Mobile|Birmingham|Tuscaloosa)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'AL'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Alaska locations
def is_alaska(location):
    states_pattern = r'\bAlaska\b'
    abbrev_pattern = r'\bAK\b'
    cities_pattern = r'\b(Anchorage|Fairbanks)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'AK'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Arizona locations
def is_arizona(location):
    states_pattern = r'\bArizona\b'
    abbrev_pattern = r'\bAZ\b'
    cities_pattern = r'\b(Phoenix|Tuscon|Mesa|Chandler|Maricopa)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'AZ'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Arkansas locations
def is_arkansas(location):
    states_pattern = r'\bArkansas\b'
    abbrev_pattern = r'\bAR\b'
    cities_pattern = r'\b(Little Rock|Fort Smith|Fayetteville)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'AR'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# California locations
def is_california(location):
    states_pattern = r'\bCalifornia\b'
    abbrev_pattern = r'\b(CA|OC|SF|LA)\b'
    cities_pattern = r'\b(Los Angeles|San Diego|San Jose|Santa Clara|San Francisco|Fresno|Sacramento|Long Beach|Oakland|Alameda|Bakersfield|Anaheim|Stockton|Santa Ana|Hollywood|Bay Area|Silicon Valley|Cali|So ?Cal)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'CA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Colorado locations
def is_colorado(location):
    states_pattern = r'\bColarado\b'
    abbrev_pattern = r'\bCO\b'
    cities_pattern = r'\b(Denver|Colorado Springs|Aurora|Fort Collins|Boulder)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'CO'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Connecticut locations
def is_connecticut(location):
    states_pattern = r'\bConnecticut\b'
    abbrev_pattern = r'\bCT\b'
    cities_pattern = r'\b(Bridgeport|Stamford|New Haven|Hartford|Fairfield)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'CT'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Delaware locations
def is_delaware(location):
    states_pattern = r'\bDelaware\b'
    abbrev_pattern = r'\bDE\b'
    cities_pattern = r'\b(Wilmington|Dover|New Castle)\b'
    area_code_pattern = r''

    if re.search(abbrev_pattern, location):
        if "RIO" not in location.upper() and "CIUDAD" not in location.upper():
            return 'DE'
    patterns = [states_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'DE'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Florida locations
def is_florida(location):
    states_pattern = r'\bFLorida\b'
    abbrev_pattern = r'\bFL\b'
    cities_pattern = r'\b(Jacksonville|Miami|Tampa|Orlando|Tallahassee|Fort Lauderdale|Duval|Orange|Broward)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'FL'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Georgia locations
def is_georgia(location):
    states_pattern = r'\bGeorgia\b'
    abbrev_pattern = r'\bGA\b|\bATL\b'
    cities_pattern = r'\b(Atlanta|Augusta|Athens|Savannah|Fulton|Muscogee|DeKalb)\b'
    area_code_pattern = r''

    if re.search(states_pattern, location):
        if "TBILISI" not in location.upper():
            return 'GA'

    patterns = [abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'GA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Hawaii locations
def is_hawaii(location):
    states_pattern = r'\bHawaii\b'
    abbrev_pattern = r'\bHI\b'
    cities_pattern = r'\b(Hawai\'i|Maui|O\'ahu|Kaua\'i|Moloka\'i|Honolulu)\b'
    islands_pattern = r'\b(The Big Island|The Valley Isle|The Gathering Place|The Garden Isle|The Friendly Isle)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern, islands_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'HI'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Idaho locations
def is_idaho(location):
    states_pattern = r'\bIdaho\b'
    abbrev_pattern = r'\bID\b'
    cities_pattern = r'\b(Boise|Meridian|Twin Falls|Idaho Falls|Pocatello)\b'
    area_code_pattern = r''

    if re.search(abbrev_pattern, location):
        if "JAKARTA" not in location.upper():
            return "ID"

    patterns = [states_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'ID'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Illinois locations
def is_illinois(location):
    states_pattern = r'\bIllinois\b'
    abbrev_pattern = r'\bIL\b'
    cities_pattern = r'\b(Chicago|Naperville|Peoria|Cook|Kane)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'IL'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Indiana locations
def is_indiana(location):
    states_pattern = r'\bIndiana\b'
    abbrev_pattern = r'\bIN\b'
    cities_pattern = r'\b(Indianapolis|Fort Wayne|Evansville|Gary)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'IN'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Iowa locations
def is_iowa(location):
    states_pattern = r'\bIowa\b'
    abbrev_pattern = r'\bIA\b'
    cities_pattern = r'\b(Des Moines|Cedar Rapids|Davenport|Sioux City|Iowa City|Cedar Falls)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'IA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Kansas locations
def is_kansas(location):
    states_pattern = r'\bKansas\b'
    abbrev_pattern = r'\bKS\b'
    cities_pattern = r'\b(Wichita|Overland Park|Olathe|Topeka)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'KS'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Kentucky locations
def is_kentucky(location):
    states_pattern = r'\bKentucky\b'
    abbrev_pattern = r'\bKY\b'
    cities_pattern = r'\b(Louisville|Lexington|Bowling Green|Fayette)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'KY'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Louisiana locations
def is_louisiana(location):
    states_pattern = r'\bLouisiana\b'
    abbrev_pattern = r'\b(NOLA)\b'
    cities_pattern = r'\b(New Orleans|Orleans|Baton Rouge|Shreveport|Lafayette)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'LA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Maine locations
def is_maine(location):
    states_pattern = r'\bMaine\b'
    abbrev_pattern = r'\bME\b'
    cities_pattern = r'\b(Lewiston|Bangor|South Portland|Auburn|Cumberland)\b'
    area_code_pattern = r''

    if re.search(abbrev_pattern, location):
        if "FOLLOW" not in location.upper() and "DM" not in location.upper():
            return 'ME'

    patterns = [states_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'ME'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Maryland locations
def is_maryland(location):
    states_pattern = r'\bMaryland\b'
    abbrev_pattern = r'\bMD\b'
    cities_pattern = r'\b(Baltimore|Germantown|Waldorf|Silver Spring)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'MD'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Massachusetts locations
def is_massachusetts(location):
    states_pattern = r'\bMassachusetts\b'
    abbrev_pattern = r'\bMA\b'
    cities_pattern = r'\b(Boston|Worcester|Springfield|Cambridge|Harvard|MIT)\b'
    area_code_pattern = r''

    if re.search(abbrev_pattern, location):
        if "LUIS" not in location.upper():
            return 'MA'

    patterns = [states_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'MA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Michigan locations
def is_michigan(location):
    states_pattern = r'\bMichigan\b'
    abbrev_pattern = r'\bMI\b'
    cities_pattern = r'\b(Detroit|Grand Rapids|Warren|Ann Arbor|Sterling Heights)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'MI'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Minnesota locations
def is_minnesota(location):
    states_pattern = r'\bMinnesota\b'
    abbrev_pattern = r'\bMN\b'
    cities_pattern = r'\b(Minneapolis|Saint Paul|Hennepin|Ramsey|Olmsted)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'MN'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Mississippi locations
def is_mississippi(location):
    states_pattern = r'\bMississippi\b'
    abbrev_pattern = r'\bMS\b'
    cities_pattern = r'\b(Jackson|Gulfport|Southaven)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'MS'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Missouri locations
def is_missouri(location):
    states_pattern = r'\bMissouri\b'
    abbrev_pattern = r'\b(MO|STL|KCMO)\b'
    cities_pattern = r'\b(Kansas City|St. Louis|Jefferson City)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'MO'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Montana locations
def is_montana(location):
    states_pattern = r'\bMontana\b'
    abbrev_pattern = r'\bMT\b'
    cities_pattern = r'\b(Billings|Missoula|Great Falls|Bozeman)\b'
    area_code_pattern = r''

    if re.search(abbrev_pattern, location):
        if "FOLLOW" not in location.upper() and "DM" not in location.upper():
            return 'MT'

    patterns = [states_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'MT'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Nebraska locations
def is_nebraska(location):
    states_pattern = r'\bNebraska\b'
    abbrev_pattern = r'\bNE\b'
    cities_pattern = r'\b(Omaha|Lincoln)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'NE'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Nevada locations
def is_nevada(location):
    states_pattern = r'\bNevada\b'
    abbrev_pattern = r'\bNV\b'
    cities_pattern = r'\b(Las Vegas|Vegas|Reno|Paradise|Carson City|Clark|Washoe)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'NV'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# New Hampshire locations
def is_new_hampshire(location):
    states_pattern = r'\bNew Hampshire\b'
    abbrev_pattern = r'\bNH\b'
    cities_pattern = r'\b(Concord|Manchester|Hillsborough)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'NH'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# New Jersey locations
def is_new_jersey(location):
    states_pattern = r'\bNew Jersey\b'
    abbrev_pattern = r'\bNJ\b'
    cities_pattern = r'\b(Newark|Jersey City|Paterson|Jersey|South Jersey)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'NJ'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# New Mexico locations
def is_new_mexico(location):
    states_pattern = r'\bNew Mexico\b'
    abbrev_pattern = r'\bNM\b'
    cities_pattern = r'\b(Albuquerque|Las Cruces|Rio Rancho|Santa Fe|Roswell)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'NM'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# New York locations
def is_new_york(location):
    states_pattern = r'\bNew York\b'
    abbrev_pattern = r'\bNY\b'
    cities_pattern = r'\b(New York City|NYC|Buffalo|Yonkers|Rochester|Syracuse|Albany|Brooklyn|Queens|Bronx|Staten Island|Manhattan|Long Island)\b'
    area_code_pattern = r'\b716\b|\b646\b|\b917\b|\b347\b|\b718\b|\b332\b|\b212\b|\b929\b'

    patterns = [states_pattern, abbrev_pattern, cities_pattern, area_code_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'NY'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# North Carolina locations
def is_north_carolina(location):
    states_pattern = r'\bNorth Carolina\b'
    abbrev_pattern = r'\bNC\b'
    cities_pattern = r'\b(Charlotte|Raleigh|Greensboro|Durham)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'NC'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# North Dakota locations
def is_north_dakota(location):
    states_pattern = r'\bNorth Dakota\b'
    abbrev_pattern = r'\bND\b'
    cities_pattern = r'\b(Bismarck|Fargo|Cass)\b'
    area_code_pattern = r''

    if re.search(abbrev_pattern, location):
        if "NSFW" not in location.upper() and "YES" not in location.upper():
            return 'ND'

    patterns = [states_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'ND'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Ohio locations
def is_ohio(location):
    states_pattern = r'\bOhio\b'
    abbrev_pattern = r'\b(OH|CLE)\b'
    cities_pattern = r'\b(Columbus|Cleveland|Cincinnati|Akron|Dayton)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'OH'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Oklahoma locations
def is_oklahoma(location):
    states_pattern = r'\bOklahoma\b'
    abbrev_pattern = r'\bOK\b'
    cities_pattern = r'\b(Oklahoma City|Tulsa|Norman|Broken Arrow)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'OK'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Oregon locations
def is_oregon(location):
    states_pattern = r'\bOregon\b'
    abbrev_pattern = r'\bOR\b'
    cities_pattern = r'\b(Portland|Salem|Eugene|Gresham|Marion)\b'
    area_code_pattern = r''

    if re.search(abbrev_pattern, location):
        if "UNFOLLOWED" not in location.upper():
            return 'OR'

    patterns = [states_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'OR'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Pennsylvania locations
def is_pennsylvania(location):
    states_pattern = r'\bPennsylvania\b'
    abbrev_pattern = r'\bPA\b'
    cities_pattern = r'\b(Philadelphia|Pittsburgh|Allentown|Reading|Erie|Scranton)\b'
    area_code_pattern = r''

    if re.search(states_pattern, location):
        if "1600" not in location.upper() and "AVENUE" not in location.upper():
            return 'PA'

    patterns = [abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'PA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Rhode Island locations
def is_rhode_island(location):
    states_pattern = r'\bRhode Island\b'
    abbrev_pattern = r'\bRI\b'
    cities_pattern = r'\b(Providence|Cranston|Warwick|Pawtucket)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'RI'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# South Carolina locations
def is_south_carolina(location):
    states_pattern = r'\bSouth Carolina\b'
    abbrev_pattern = r'\bSC\b'
    cities_pattern = r'\b(Charleston|Greenville)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'SC'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# South Dakota locations
def is_south_dakota(location):
    states_pattern = r'\bSouth Dakota\b'
    abbrev_pattern = r'\bSD\b'
    cities_pattern = r'\b(Sioux Falls|Rapid City)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'SD'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Tennessee locations
def is_tennessee(location):
    states_pattern = r'\bTennessee\b'
    abbrev_pattern = r'\bTN\b'
    cities_pattern = r'\b(Nashville|Memphis|Knoxville|Chattanooga|Clarksville|Murfreesboro)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'TN'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Texas locations
def is_texas(location):
    states_pattern = r'\bTexas\b'
    abbrev_pattern = r'\b(TX|HTX|DTX|ATX)\b'
    cities_pattern = r'\b(Houston|San Antonio|Dallas|Austin|Fort Worth|El Paso|Arlington|Corpus Christi|Plano|Lubbock|Laredo|Pasadena|Amarillo|Garland)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'TX'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Utah locations
def is_utah(location):
    states_pattern = r'\bUtah\b'
    abbrev_pattern = r'\bUT\b'
    cities_pattern = r'\b(Salt Lake City|West Valley City|West Jordan|Provo)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'UT'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Vermont locations
def is_vermont(location):
    states_pattern = r'\bVermont\b'
    abbrev_pattern = r'\bVT\b'
    cities_pattern = r'\b(Burlington|Rutland)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'VT'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Virginia locations
def is_virginia(location):
    states_pattern = r'\bVirginia\b'
    abbrev_pattern = r'\bVA\b'
    cities_pattern = r'\b(Richmond|Roanoke|Lynchburg|Charlottesville|Northern Virginia|NoVA|Harrisonburg|Winchester)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'VA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Washington locations
def is_washington(location):
    states_pattern = r'\bWashington\b'
    abbrev_pattern = r'\bWA\b'
    cities_pattern = r'\b(Seattle|Spokane|Tacoma|Vancouver|Bellevue|Everett)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'WA'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# West Virginia locations
def is_west_virginia(location):
    states_pattern = r'\bWest Virginia\b'
    abbrev_pattern = r'\bWV\b'
    cities_pattern = r'\b(Huntington|Morgantown|Parkersburg|Kanawha)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'WV'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Wisconsin locations
def is_wisconsin(location):
    states_pattern = r'\bWisconsin\b'
    abbrev_pattern = r'\bWI\b'
    cities_pattern = r'\b(Milwaukee|Madison|Green Bay|Kenosha|Waukesha|Oshkosh)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'WI'
    return None

#----------------------------------------------------------------------------------------------------------------------#
# Wyoming locations
def is_wyoming(location):
    states_pattern = r'\bWyoming\b'
    abbrev_pattern = r'\bWY\b'
    cities_pattern = r'\b(Cheyenne|Casper|Laramie|Gillette)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern, cities_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'WY'
    return None

# -------------------------------------------------------------------------------------------------------------------- #
# DC Locations
def is_dc(location):
    states_pattern = r'\b(Washington D.C.|District of Columbia)\b'
    abbrev_pattern = r'\b(DC|D.C.)\b'
    area_code_pattern = r''

    patterns = [states_pattern, abbrev_pattern]
    for pattern in patterns:
        if re.search(pattern, location):
            return 'DC'
    return None
#----------------------------------------------------------------------------------------------------------------------#


def parse_location(location):

    # 18. Louisiana
    state_code = is_louisiana(location)
    if state_code != None:
        return state_code

    # 1. Alabama
    state_code = is_alabama(location)
    if state_code != None:
        return state_code

    # 2. Alaska
    state_code = is_alaska(location)
    if state_code != None:
        return state_code

    # 3. Arizona
    state_code = is_arizona(location)
    if state_code != None:
        return state_code

    # 4. Arkansas
    state_code = is_arkansas(location)
    if state_code != None:
        return state_code

    # 5. California
    state_code = is_california(location)
    if state_code != None:
        return state_code

    # 6. Colorado
    state_code = is_colorado(location)
    if state_code != None:
        return state_code

    # 7. Connecticut
    state_code = is_connecticut(location)
    if state_code != None:
        return state_code

    # 8. Delaware
    state_code = is_delaware(location)
    if state_code != None:
        return state_code

    # 9. Florida
    state_code = is_florida(location)
    if state_code != None:
        return state_code

    # 10. Georgia
    state_code = is_georgia(location)
    if state_code != None:
        return state_code

    # 11. Hawaii
    state_code = is_hawaii(location)
    if state_code != None:
        return state_code

    # 12. Idaho
    state_code = is_idaho(location)
    if state_code != None:
        return state_code

    # 13. Illinois
    state_code = is_illinois(location)
    if state_code != None:
        return state_code

    # 14. Indiania
    state_code = is_indiana(location)
    if state_code != None:
        return state_code

    # 15. Iowa
    state_code = is_iowa(location)
    if state_code != None:
        return state_code

    # 16. Kansas
    state_code = is_kansas(location)
    if state_code != None:
        return state_code

    # 17. Kentucky
    state_code = is_kentucky(location)
    if state_code != None:
        return state_code

    # 19. Maine
    state_code = is_maine(location)
    if state_code != None:
        return state_code

    # 20. Maryland
    state_code = is_maryland(location)
    if state_code != None:
        return state_code

    # 21. Massachusetts
    state_code = is_massachusetts(location)
    if state_code != None:
        return state_code

    # 22. Michigan
    state_code = is_michigan(location)
    if state_code != None:
        return state_code

    # 23. Minnesota
    state_code = is_minnesota(location)
    if state_code != None:
        return state_code

    # 24. Mississippi
    state_code = is_mississippi(location)
    if state_code != None:
        return state_code

    # 25. Missouri
    state_code = is_missouri(location)
    if state_code != None:
        return state_code

    # 26. Montana
    state_code = is_montana(location)
    if state_code != None:
        return state_code

    # 28. Nevada
    state_code = is_nevada(location)
    if state_code != None:
        return state_code

    # 29. New Hampshire
    state_code = is_new_hampshire(location)
    if state_code != None:
        return state_code

    # 30. New Jersey
    state_code = is_new_jersey(location)
    if state_code != None:
        return state_code

    # 31. New Mexico
    state_code = is_new_mexico(location)
    if state_code != None:
        return state_code

    # 32. New York
    state_code = is_new_york(location)
    if state_code != None:
        return state_code

    # 33. North Carolina
    state_code = is_north_carolina(location)
    if state_code != None:
        return state_code

    # 34. North Dakota
    state_code = is_north_dakota(location)
    if state_code != None:
        return state_code

    # 35. Ohio
    state_code = is_ohio(location)
    if state_code != None:
        return state_code

    # 36. Oklahoma
    state_code = is_oklahoma(location)
    if state_code != None:
        return state_code

    # 37. Oregon
    state_code = is_oregon(location)
    if state_code != None:
        return state_code

    # 38. Pennsylvania
    state_code = is_pennsylvania(location)
    if state_code != None:
        return state_code

    # 39. Rhode Island
    state_code = is_rhode_island(location)
    if state_code != None:
        return state_code

    # 40. South Carolina
    state_code = is_south_carolina(location)
    if state_code != None:
        return state_code

    # 41. South Dakota
    state_code = is_south_dakota(location)
    if state_code != None:
        return state_code

    # 42. Tennessee
    state_code = is_tennessee(location)
    if state_code != None:
        return state_code

    # 43. Texas
    state_code = is_texas(location)
    if state_code != None:
        return state_code

    # 44. Utah
    state_code = is_utah(location)
    if state_code != None:
        return state_code

    # 45. Vermont
    state_code = is_vermont(location)
    if state_code != None:
        return state_code

    # 46. Virginia
    state_code = is_virginia(location)
    if state_code != None:
        return state_code

    # 46.5 DC
    state_code = is_dc(location)
    if state_code != None:
        return state_code

    # 47. Washington
    state_code = is_washington(location)
    if state_code != None:
        return state_code

    # 48. West Virginia
    state_code = is_west_virginia(location)
    if state_code != None:
        return state_code

    # 49. Wisconsin
    state_code = is_wisconsin(location)
    if state_code != None:
        return state_code

    # 50. Wyoming
    state_code = is_wyoming(location)
    if state_code != None:
        return state_code

    # 27. Nebraska
    state_code = is_nebraska(location)
    if state_code != None:
        return state_code

    return "--"

########################################################################################################################

if __name__ == '__main__':

    strings = ["Buffalo", "Long Island", "Charleston", "Uruguay", 'Ann Arbor', 'Cheyenne']
    for location in strings:
        result = parse_location(location)
        print(result)
