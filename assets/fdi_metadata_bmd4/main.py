from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_FDI@DF_FDI_BMD4")
    
    if data.num_rows > 0:
        upload_data(data, "fdi_metadata_bmd4")
        print(f"Uploaded {data.num_rows} rows to fdi_metadata_bmd4")
        
    save_state("fdi_metadata_bmd4", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
