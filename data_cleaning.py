import pandas as pd

def replace_accents(series):
    series = series.replace('Á','A', regex=True) \
                    .replace('É','E', regex=True) \
                    .replace('Í','I', regex=True) \
                    .replace('Ó','O', regex=True) \
                    .replace('Ú','U', regex=True) \
                    .replace('Ñ','N', regex=True) \
                    .replace('Ü','U', regex=True)
    return series