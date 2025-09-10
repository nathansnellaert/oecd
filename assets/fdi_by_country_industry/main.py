from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FDI@DF_FDI_CTRY_IND_SUMM")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_fdi_by_country_industry")
        print(f"Uploaded {data.num_rows} rows to fdi_by_country_industry")
        
    save_state("fdi_by_country_industry", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
