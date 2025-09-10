from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DD_HCL@DF_DD_HCL_TEST")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_test_dd_hcl_order")
        print(f"Uploaded {data.num_rows} rows to test_dd_hcl_order")
        
    save_state("test_dd_hcl_order", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
