# SkyHoundz Classic Google Drive share link
SHClass_orig_url = 'https://drive.google.com/file/d/1KiBVDmnbsZcYx2ltx-DK2edbLo4iBJTb/view?usp=sharing'

# DiscDogathon Google Drive share link
DDT_orig_url = 'https://drive.google.com/file/d/1LHVI57ePPoegt7oaUWClMaK_tC2o7Dj3/view?usp=sharing'

# Xtreme Distance Google Drive share link
XD_orig_url = 'https://drive.google.com/file/d/1w_8bGc1IcAj4B1ntGmzkuYLGF8PGOGia/view?usp=sharing'

# Toss and Fetch league scores Google Drive share link
k9tf_orig_url = 'https://drive.google.com/file/d/1qQcclnrSAh1pXwS4mN2VvMKVnXwOW881/view?usp=sharing'


# get CSV from Google Drive and return pandas df
def getGoogleDriveCSV(orig_url):
    file_id = orig_url.split('/')[-2]
    dwn_url = 'https://drive.google.com/uc?export=download&id=' + file_id
    url = requests.get(dwn_url).text
    csv_raw = StringIO(url)
    return pd.read_csv(csv_raw)
