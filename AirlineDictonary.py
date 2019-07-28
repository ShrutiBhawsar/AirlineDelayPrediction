

carrier_dict={'9E': 0, 'AA': 1, 'AS': 2, 'B6': 3, 'DL': 4, 'EV': 5, 'F9': 6, 'G4': 7,
 'HA': 8, 'MQ': 9, 'NK': 10, 'OH': 11, 'OO': 12, 'UA': 13, 'VX': 14, 'WN': 15,
 'YV': 16, 'YX': 17}

carrier_code = {'9E':'9E - Endeavor Air', 'AA':'AA - American Airlines Inc.','AS': 'AS - Alaska Airlines Inc.',
                'B6': 'B6 - JetBlue Airways','DL':'DL - Delta Air Lines Inc.','EV': 'EV - Atlantic Southeast Airlines',
                'F9':'F9 - Frontier Airlines Inc.','G4':'G4 - Allegiant Air', 'HA':'HA - Hawaiian Airlines Inc.',
                'MQ': 'MQ - American Eagle Airlines Inc.','NK': 'NK - Spirit Air Lines','OH':'OH - Comair',
                'OO':'OO - Skywest Airlines Inc.', 'UA':'UA - United Air Lines Inc.', 'VX':'VX - Virgin America',
                'WN':'WN - Southwest Airlines Co.','YV': 'YV - Mesa Airlines', 'YX':'YX - Republic Airways'}


origin_dict={'ATL': 0, 'CLT': 1, 'DEN': 2, 'DFW': 3, 'IAH': 4, 'LAX': 5, 'LGA': 6, 'ORD': 7, 'PHX': 8, 'SFO': 9}

origin_code={'ATL': 'Hartsfield-Jackson Atlanta International Airport',
             'CLT': 'Charlotte Douglas International Airport',
             'DEN': 'Denver International Airport',
             'DFW': 'Dallas/Fort Worth International Airport',
             'IAH': 'George Bush Intercontinental Airport',
             'LAX': 'Los Angeles International Airport',
             'LGA': 'LaGuardia Airport (Marine Air Terminal)',
             'ORD': "Chicago O'Hare International Airport",
             'PHX': 'Phoenix Sky Harbor International Airport',
             'SFO': 'San Francisco International Airport'}


destination_dict={'ABE': 0, 'ABI': 1, 'ABQ': 2, 'ABY': 3, 'ACK': 4, 'ACT': 5, 'ACV': 6, 'ACY': 7,
                  'AEX': 8, 'AGS': 9, 'ALB': 10, 'ALO': 11, 'AMA': 12, 'ANC': 13, 'ASE': 14,
                  'ATL': 15, 'ATW': 16, 'AUS': 17, 'AVL': 18, 'AVP': 19, 'AZO': 20, 'BDL': 21,
                  'BFF': 22, 'BFL': 23, 'BGR': 24, 'BHM': 25, 'BIL': 26, 'BIS': 27, 'BKG': 28,
                  'BLI': 29, 'BMI': 30, 'BNA': 31, 'BOI': 32, 'BOS': 33, 'BPT': 34, 'BQK': 35,
                  'BRO': 36, 'BTR': 37, 'BTV': 38, 'BUF': 39, 'BUR': 40, 'BWI': 41, 'BZN': 42,
                  'CAE': 43, 'CAK': 44, 'CGI': 45, 'CHA': 46, 'CHO': 47, 'CHS': 48, 'CID': 49,
                  'CKB': 50, 'CLE': 51, 'CLL': 52, 'CLT': 53, 'CMH': 54, 'CMI': 55, 'CMX': 56,
                  'CNY': 57, 'COD': 58, 'COS': 59, 'COU': 60, 'CPR': 61, 'CRP': 62, 'CRW': 63,
                  'CSG': 64, 'CVG': 65, 'CWA': 66, 'CYS': 67, 'DAB': 68, 'DAL': 69, 'DAY': 70,
                  'DBQ': 71, 'DCA': 72, 'DEN': 73, 'DFW': 74, 'DHN': 75, 'DLH': 76, 'DRO': 77,
                  'DRT': 78, 'DSM': 79, 'DTW': 80, 'EAR': 81, 'EAU': 82, 'ECP': 83, 'EGE': 84,
                  'ELM': 85, 'ELP': 86, 'ERI': 87, 'EUG': 88, 'EVV': 89, 'EWN': 90, 'EWR': 91,
                  'EYW': 92, 'FAI': 93, 'FAR': 94, 'FAT': 95, 'FAY': 96, 'FCA': 97, 'FLG': 98,
                  'FLL': 99, 'FLO': 100, 'FNT': 101, 'FSD': 102, 'FSM': 103, 'FWA': 104, 'GCC': 105,
                  'GCK': 106, 'GEG': 107, 'GGG': 108, 'GJT': 109, 'GNV': 110, 'GPT': 111, 'GRB': 112,
                  'GRI': 113, 'GRK': 114, 'GRR': 115, 'GSO': 116, 'GSP': 117, 'GTF': 118, 'GTR': 119,
                  'GUC': 120, 'HDN': 121, 'HHH': 122, 'HLN': 123, 'HNL': 124, 'HOB': 125, 'HOU': 126,
                  'HPN': 127, 'HRL': 128, 'HSV': 129, 'HTS': 130, 'HVN': 131, 'HYS': 132, 'IAD': 133,
                  'IAH': 134, 'ICT': 135, 'IDA': 136, 'IFP': 137, 'ILM': 138, 'IND': 139, 'ISN': 140,
                  'ISP': 141, 'ITH': 142, 'ITO': 143, 'JAC': 144, 'JAN': 145, 'JAX': 146, 'JFK': 147,
                  'JLN': 148, 'JMS': 149, 'KOA': 150, 'LAN': 151, 'LAR': 152, 'LAS': 153, 'LAW': 154,
                  'LAX': 155, 'LBB': 156, 'LBF': 157, 'LBL': 158, 'LCH': 159, 'LEX': 160, 'LFT': 161,
                  'LGA': 162, 'LGB': 163, 'LIH': 164, 'LIT': 165, 'LNK': 166, 'LRD': 167, 'LSE': 168,
                  'LWB': 169, 'LYH': 170, 'MAF': 171, 'MBS': 172, 'MCI': 173, 'MCO': 174, 'MDT': 175,
                  'MDW': 176, 'MEI': 177, 'MEM': 178, 'MFE': 179, 'MFR': 180, 'MGM': 181, 'MHK': 182,
                  'MHT': 183, 'MIA': 184, 'MKE': 185, 'MKG': 186, 'MLB': 187, 'MLI': 188, 'MLU': 189,
                  'MMH': 190, 'MOB': 191, 'MOT': 192, 'MQT': 193, 'MRY': 194, 'MSN': 195, 'MSO': 196,
                  'MSP': 197, 'MSY': 198, 'MTJ': 199, 'MVY': 200, 'MYR': 201, 'OAJ': 202, 'OAK': 203,
                  'OGD': 204, 'OGG': 205, 'OKC': 206, 'OMA': 207, 'ONT': 208, 'ORD': 209, 'ORF': 210,
                  'OTH': 211, 'PAH': 212, 'PBI': 213, 'PDX': 214, 'PGV': 215, 'PHF': 216, 'PHL': 217,
                  'PHX': 218, 'PIA': 219, 'PIB': 220, 'PIT': 221, 'PNS': 222, 'PRC': 223, 'PSC': 224,
                  'PSP': 225, 'PUB': 226, 'PVD': 227, 'PVU': 228, 'PWM': 229, 'RAP': 230, 'RDD': 231,
                  'RDM': 232, 'RDU': 233, 'RIC': 234, 'RKS': 235, 'RNO': 236, 'ROA': 237, 'ROC': 238,
                  'ROW': 239, 'RST': 240, 'RSW': 241, 'SAF': 242, 'SAN': 243, 'SAT': 244, 'SAV': 245,
                  'SBA': 246, 'SBN': 247, 'SBP': 248, 'SCE': 249, 'SDF': 250, 'SEA': 251, 'SFO': 252,
                  'SGF': 253, 'SGU': 254, 'SHD': 255, 'SHV': 256, 'SJC': 257, 'SJT': 258, 'SJU': 259,
                  'SLC': 260, 'SLN': 261, 'SMF': 262, 'SNA': 263, 'SPI': 264, 'SPS': 265, 'SRQ': 266,
                  'STL': 267, 'STS': 268, 'STT': 269, 'STX': 270, 'SUN': 271, 'SUX': 272, 'SWO': 273,
                  'SYR': 274, 'TLH': 275, 'TOL': 276, 'TPA': 277, 'TRI': 278, 'TTN': 279, 'TUL': 280,
                  'TUS': 281, 'TVC': 282, 'TXK': 283, 'TYR': 284, 'TYS': 285, 'UIN': 286, 'VEL': 287,
                  'VLD': 288, 'VPS': 289, 'XNA': 290, 'YUM': 291}


destination_code={'ABE': 'Lehigh Valley International Airport', 'ABI': 'Abilene Regional Airport',
                  'ABQ': 'Albuquerque International Sunport', 'ABY': 'Southwest Georgia Regional Airport',
                  'ACK': 'Nantucket Memorial Airport', 'ACT': 'Waco Regional Airport', 'ACV': 'Arcata Airport',
                  'ACY': 'Atlantic City International Airport', 'AEX': 'Alexandria International Airport',
                  'AGS': 'Augusta Regional Airport\xa0(Bush Field)', 'ALB': 'Albany International Airport',
                  'ALO': 'Waterloo Regional Airport', 'AMA': 'Rick Husband Amarillo International Airport',
                  'ANC': 'Ted Stevens Anchorage International Airport', 'ASE': 'Aspen-Pitkin County Airport',
                  'ATL': 'Hartsfield-Jackson Atlanta International Airport', 'ATW': 'Appleton International Airport',
                  'AUS': 'Austin-Bergstrom International Airport', 'AVL': 'Asheville Regional Airport',
                  'AVP': 'Wilkes-Barre/Scranton International Airport',
                  'AZO': 'Kalamazoo/Battle Creek International Airport',
                  'BDL': 'Bradley International Airport', 'BFL': 'Meadows Field',
                  'BGR': 'Bangor International Airport',
                  'BHM': 'Birmingham-Shuttlesworth International Airport',
                  'BIL': 'Billings Logan International Airport',
                  'BIS': 'Bismarck Municipal Airport', 'BLI': 'Bellingham International Airport',
                  'BMI': 'Central Illinois Regional Airport at Bloomington-Normal',
                  'BNA': 'Nashville International Airport', 'BOI': 'Boise Airport\xa0(Boise Air Terminal)', 'BOS': 'Gen. Edward Lawrence Logan International Airport', 'BPT': 'Jack Brooks Regional Airport\xa0(Southeast Texas Regional)', 'BQK': 'Brunswick Golden Isles Airport', 'BRO': 'Brownsville/South Padre Island International Airport', 'BTR': 'Baton Rouge Metropolitan Airport', 'BTV': 'Burlington International Airport', 'BUF': 'Buffalo Niagara International Airport', 'BUR': 'Bob Hope Airport\xa0(Hollywood Burbank Airport)', 'BWI': 'Baltimore-Washington International Airport', 'BZN': 'Bozeman Yellowstone International Airport\xa0(Gallatin Field Airport)', 'CAE': 'Columbia Metropolitan Airport', 'CAK': 'Akron-Canton Regional Airport', 'CHA': 'Chattanooga Metropolitan Airport\xa0(Lovell Field)', 'CHO': 'Charlottesville-Albemarle Airport', 'CHS': 'Charleston International Airport/Charleston AFB', 'CID': 'The Eastern Iowa Airport', 'CLE': 'Cleveland Hopkins International Airport', 'CLL': 'Easterwood Airport', 'CLT': 'Charlotte Douglas International Airport', 'CMH': 'Port Columbus International Airport', 'CMI': 'University of Illinois - Willard Airport', 'CMX': 'Houghton County Memorial Airport', 'CNY': 'Canyonlands Field', 'COD': 'Yellowstone Regional Airport', 'COS': 'City of Colorado Springs Municipal Airport', 'COU': 'Columbia Regional Airport', 'CPR': 'Natrona County International Airport', 'CRP': 'Corpus Christi International Airport', 'CRW': 'Yeager Airport', 'CSG': 'Columbus Metropolitan Airport', 'CVG': 'Cincinnati/Northern Kentucky International Airport', 'CWA': 'Central Wisconsin Airport', 'DAB': 'Daytona Beach International Airport', 'DAL': 'Dallas Love Field', 'DAY': 'James M. Cox Dayton International Airport', 'DBQ': 'Dubuque Regional Airport', 'DCA': 'Ronald Reagan Washington National Airport', 'DEN': 'Denver International Airport', 'DFW': 'Dallas/Fort Worth International Airport', 'DHN': 'Dothan Regional Airport', 'DLH': 'Duluth International Airport', 'DRO': 'Durango-La Plata County Airport', 'DSM': 'Des Moines International Airport', 'DTW': 'Detroit Metropolitan Airport', 'EAU': 'Chippewa Valley Regional Airport', 'ECP': 'Northwest Florida Beaches International Airport', 'EGE': 'Eagle County Regional Airport', 'ELM': 'Elmira/Corning Regional Airport', 'ELP': 'El Paso International Airport', 'ERI': 'Erie International Airport', 'EUG': 'Eugene Airport\xa0(Mahlon Sweet Field)', 'EVV': 'Evansville Regional Airport', 'EWN': 'Coastal Carolina Regional Airport\xa0(Craven County Regional)', 'EWR': 'Newark Liberty International Airport', 'EYW': 'Key West International Airport', 'FAI': 'Fairbanks International Airport', 'FAR': 'Hector International Airport', 'FAT': 'Fresno Yosemite International Airport', 'FAY': 'Fayetteville Regional Airport', 'FCA': 'Glacier Park International Airport', 'FLG': 'Flagstaff Pulliam Airport', 'FLL': 'Fort Lauderdale-Hollywood International Airport', 'FNT': 'Bishop International Airport', 'FSD': 'Sioux Falls Regional Airport', 'FSM': 'Fort Smith Regional Airport', 'FWA': 'Fort Wayne International Airport', 'GCC': 'Gillette-Campbell County Airport', 'GCK': 'Garden City Regional Airport', 'GEG': 'Spokane International Airport', 'GGG': 'East Texas Regional Airport', 'GJT': 'Grand Junction Regional Airport\xa0(Walker Field)', 'GNV': 'Gainesville Regional Airport', 'GPT': 'Gulfport-Biloxi International Airport', 'GRB': 'Green Bay-Austin Straubel International Airport', 'GRI': 'Central Nebraska Regional Airport', 'GRK': 'Killeen-Fort Hood Regional Airport', 'GRR': 'Gerald R. Ford International Airport', 'GSO': 'Piedmont Triad International Airport', 'GSP': 'Greenville-Spartanburg International Airport', 'GTF': 'Great Falls International Airport', 'GTR': 'Golden Triangle Regional Airport', 'GUC': 'Gunnison-Crested Butte Regional Airport', 'HDN': 'Yampa Valley Airport\xa0(Yampa Valley Regional)', 'HLN': 'Helena Regional Airport', 'HNL': 'Honolulu International Airport', 'HOB': 'Lea County Regional Airport', 'HOU': 'William P. Hobby Airport', 'HPN': 'Westchester County Airport', 'HRL': 'Valley International Airport', 'HSV': 'Huntsville International Airport', 'HYS': 'Hays Regional Airport', 'IAD': 'Washington Dulles International Airport', 'IAH': 'George Bush Intercontinental Airport', 'ICT': 'Wichita Dwight D. Eisenhower National Airport\xa0(Wichita Mid-Continent Airport)', 'IDA': 'Idaho Falls Regional Airport', 'ILM': 'Wilmington International Airport', 'IND': 'Indianapolis International Airport', 'ISN': 'Sloulin Field International Airport', 'ISP': 'Long Island MacArthur Airport', 'ITH': 'Ithaca Tompkins Regional Airport', 'ITO': 'Hilo International Airport', 'JAC': 'Jackson Hole Airport', 'JAN': 'Jackson-Evers International Airport', 'JAX': 'Jacksonville International Airport', 'JFK': 'John F. Kennedy International Airport\xa0(New York International Airport)', 'JLN': 'Joplin Regional Airport', 'JMS': 'Jamestown Regional Airport', 'KOA': 'Kona International Airport at Keahole', 'LAN': 'Capital Region International Airport\xa0( Lansing Capital City)', 'LAR': 'Laramie Regional Airport', 'LAS': 'McCarran International Airport', 'LAW': 'Lawton-Fort Sill Regional Airport', 'LAX': 'Los Angeles International Airport', 'LBB': 'Lubbock Preston Smith International Airport', 'LCH': 'Lake Charles Regional Airport', 'LEX': 'Blue Grass Airport', 'LFT': 'Lafayette Regional Airport', 'LGA': 'LaGuardia Airport (Marine Air Terminal)', 'LGB': 'Long Beach Airport\xa0(Daugherty Field)', 'LIH': 'Lihue Airport', 'LIT': 'Bill and Hillary Clinton National Airport\xa0(Adams Field)', 'LNK': 'Lincoln Airport\xa0(Lincoln Municipal)', 'LRD': 'Laredo International Airport', 'LSE': 'La Crosse Regional Airport', 'MAF': 'Midland International Airport', 'MBS': 'MBS International Airport', 'MCI': 'Kansas City International Airport', 'MCO': 'Orlando International Airport', 'MDT': 'Harrisburg International Airport', 'MDW': 'Chicago Midway International Airport', 'MEI': 'Meridian Regional Airport', 'MEM': 'Memphis International Airport', 'MFE': 'McAllen-Miller International Airport\xa0(McAllen Miller International)', 'MFR': 'Rogue Valley International Airport', 'MGM': 'Montgomery Regional Airport', 'MHK': 'Manhattan Regional Airport', 'MHT': 'Manchester-Boston Regional Airport', 'MIA': 'Miami International Airport', 'MKE': 'General Mitchell International Airport', 'MKG': 'Muskegon County Airport', 'MLB': 'Melbourne International Airport', 'MLI': 'Quad City International Airport', 'MLU': 'Monroe Regional Airport', 'MMH': 'Mammoth Yosemite Airport', 'MOB': 'Mobile Regional Airport', 'MOT': 'Minot International Airport', 'MQT': 'Sawyer International Airport', 'MRY': 'Monterey Regional Airport\xa0(Monterey Peninsula Airport)', 'MSN': 'Dane County Regional Airport', 'MSO': 'Missoula International Airport', 'MSP': 'Minneapolis-Saint Paul International Airport', 'MSY': 'Louis Armstrong New Orleans International Airport', 'MTJ': 'Montrose Regional Airport', 'MVY': "Martha's Vineyard Airport", 'MYR': 'Myrtle Beach International Airport', 'OAJ': 'Albert J. Ellis Airport', 'OAK': 'Oakland International Airport', 'OGG': 'Kahului Airport', 'OKC': 'Will Rogers World Airport', 'OMA': 'Eppley Airfield', 'ONT': 'Ontario International Airport', 'ORD': "Chicago O'Hare International Airport", 'ORF': 'Norfolk International Airport', 'OTH': 'Southwest Oregon Regional Airport\xa0(North Bend Municipal)', 'PAH': 'Barkley Regional Airport', 'PBI': 'Palm Beach International Airport', 'PDX': 'Portland International Airport', 'PHF': 'Newport News/Williamsburg International Airport', 'PHL': 'Philadelphia International Airport', 'PHX': 'Phoenix Sky Harbor International Airport', 'PIA': 'General Wayne A. Downing Peoria International Airport', 'PIB': 'Hattiesburg-Laurel Regional Airport', 'PIT': 'Pittsburgh International Airport', 'PNS': 'Pensacola International Airport\xa0(Pensacola Gulf Coast Regional Airport)', 'PSC': 'Tri-Cities Airport', 'PSP': 'Palm Springs International Airport', 'PUB': 'Pueblo Memorial Airport', 'PVD': 'Theodore Francis Green State Airport', 'PWM': 'Portland International Jetport', 'RAP': 'Rapid City Regional Airport', 'RDD': 'Redding Municipal Airport', 'RDM': 'Redmond Municipal Airport\xa0(Roberts Field)', 'RDU': 'Raleigh-Durham International Airport', 'RIC': 'Richmond International Airport', 'RKS': 'Rock Springs-Sweetwater County Airport', 'RNO': 'Reno/Tahoe International Airport', 'ROA': 'Roanoke Regional Airport\xa0(Woodrum Field)', 'ROC': 'Greater Rochester International Airport', 'ROW': 'Roswell International Air Center', 'RST': 'Rochester International Airport', 'RSW': 'Southwest Florida International Airport', 'SAF': 'Santa Fe Municipal Airport', 'SAN': 'San Diego International Airport\xa0(Lindbergh Field)', 'SAT': 'San Antonio International Airport', 'SAV': 'Savannah/Hilton Head International Airport', 'SBA': 'Santa Barbara Municipal Airport\xa0(Santa Barbara Airport)', 'SBN': 'South Bend International Airport\xa0(South Bend Regional)', 'SBP': 'San Luis Obispo County Regional Airport\xa0(McChesney Field)', 'SCE': 'University Park Airport', 'SDF': 'Louisville International Airport\xa0(Standiford Field)', 'SEA': 'Seattle-Tacoma International Airport', 'SFO': 'San Francisco International Airport', 'SGF': 'Springfield-Branson National Airport', 'SGU': 'St. George Regional Airport', 'SHV': 'Shreveport Regional Airport', 'SJC': 'Norman Y. Mineta San José International Airport', 'SJT': 'San Angelo Regional Airport\xa0(Mathis Field)', 'SJU': 'Luis Muñoz Marín International Airport', 'SLC': 'Salt Lake City International Airport', 'SMF': 'Sacramento International Airport', 'SNA': 'John Wayne Airport\xa0(Orange County Airport)', 'SPI': 'Abraham Lincoln Capital Airport', 'SPS': 'Wichita Falls Municipal Airport/Sheppard AFB', 'SRQ': 'Sarasota-Bradenton International Airport', 'STL': 'St. Louis International Airport at Lambert Field', 'STT': 'Cyril E. King Airport', 'STX': 'Henry E. Rohlsen Airport', 'SUN': 'Friedman Memorial Airport', 'SUX': 'Sioux Gateway Airport', 'SYR': 'Syracuse Hancock International Airport', 'TLH': 'Tallahassee International Airport', 'TOL': 'Toledo Express Airport', 'TPA': 'Tampa International Airport', 'TRI': 'Tri-Cities Regional Airport', 'TTN': 'Trenton Mercer Airport', 'TUL': 'Tulsa International Airport', 'TUS': 'Tucson International Airport', 'TVC': 'Cherry Capital Airport', 'TXK': 'Texarkana Regional Airport\xa0(Webb Field)', 'TYR': 'Tyler Pounds Regional Airport', 'TYS': 'McGhee Tyson Airport', 'VEL': 'Valdez Airport', 'VLD': 'Valdosta Regional Airport', 'VPS': 'Destin-Fort Walton Beach Airport/Eglin AFB', 'XNA': 'Northwest Arkansas Regional Airport', 'YUM': 'Yuma International Airport'}




hour_list=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18',
           '19','20','21','22','23','24']

minute_list=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18',
             '19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37',
             '38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55',
             '56','57','58','59']