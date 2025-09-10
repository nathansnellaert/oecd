from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FDI@DF_FDI_AGGR_SUMM")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_fdi_main_aggregates")
        print(f"Uploaded {data.num_rows} rows to fdi_main_aggregates")
        
    save_state("fdi_main_aggregates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
