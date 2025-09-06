from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_WAGES_DECOMP@DF_TW_DECOMP")
    
    if data.num_rows > 0:
        upload_data(data, "tax_wedge_decompositions")
        print(f"Uploaded {data.num_rows} rows to tax_wedge_decompositions")
        
    save_state("tax_wedge_decompositions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
