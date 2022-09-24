import requests
import re
import time
import os, errno

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    
    return fname[0]

url_pattern = 'http://www.domain.com/File_name_+COUNTER+_other_stuff.ext'
counter_pattern = '+COUNTER+'
counter_start = 2
counter_stop = 101

delay_seconds = 10
output_dir = "downloads"

try:
    os.makedirs(output_dir)
except FileExistsError:
    # directory already exists
    pass

os.system('clear')

print("Starting download {} files".format(counter_stop))

for item_index in range(counter_start, counter_stop + 1):
    if item_index < 10:
        item_str = str(item_index).zfill(2)
    else:
        item_str = str(item_index)

    url = url_pattern.replace(counter_pattern, item_str)
    r = requests.get(url, allow_redirects=True)
    filename = output_dir + "/" + get_filename_from_cd(r.headers.get('content-disposition'))
    print("Downloading from: {}, saving to: {}".format(url, filename))
    open(filename, 'wb').write(r.content)

    print("Waitinig {} seconds...".format(delay_seconds))
    print("---------------------------------------")
    time.sleep(delay_seconds)
