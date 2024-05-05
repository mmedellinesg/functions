#%%
import os.path
import configparser
import time
# %%
def getConfigParameters():
    config = configparser.ConfigParser()
    retval = {}
    if os.path.exists('CONFIG.ini'):
        config.read('CONFIG.ini')
        for key in config['DEFAULT'].keys():
            retval[key] = config['DEFAULT'][key]
    elif os.path.exists('../CONFIG.ini'):
        config.read('../CONFIG.ini')
        for key in config['DEFAULT'].keys():
            retval[key] = config['DEFAULT'][key]
    else:
        print('No configuration file found')
    return retval
# %%
