# Your imports
import calendar
import datetime as dt
import pandas as pd

def months_interval(start_date, end_date):
    """
    returns the names of the months that are present between them (inclusive)
    """
    if isinstance(start_date, dt.date):
        d1 = start_date
    else:
        d1 = dt.datetime.strptime(start_date,"%Y-%m-%d")
    
    if isinstance(end_date, dt.date):
        d2 = end_date
    else:
        d2 = dt.datetime.strptime(end_date,"%Y-%m-%d")
    
    mnts = []
    dts = pd.date_range(d1, d2, freq='MS')
    mnts = [d.month for d in dts]
    mnts = sorted(list(set(mnts)))
    mnts_nm = [calendar.month_name[nr] for nr in mnts]
    
    return mnts_nm
