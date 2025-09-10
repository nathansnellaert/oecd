from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_TAD_EXP_RESTRIC@DF_QDD_TAD_EXP_RESTRIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_raw_material_export_restrictions")
        print(f"Uploaded {data.num_rows} rows to raw_material_export_restrictions")
        
    save_state("raw_material_export_restrictions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
