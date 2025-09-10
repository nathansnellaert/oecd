from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_MATERIAL_RESOURCES@DF_MATERIAL_RESOURCES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_material_flow_accounts")
        print(f"Uploaded {data.num_rows} rows to material_flow_accounts")
        
    save_state("material_flow_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
