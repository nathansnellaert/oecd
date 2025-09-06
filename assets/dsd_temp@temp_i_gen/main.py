from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TEMP@DF_TEMP_I_GEN")
    
    if data.num_rows > 0:
        upload_data(data, "dsd_temp@temp_i_gen")
        print(f"Uploaded {data.num_rows} rows to dsd_temp@temp_i_gen")
        
    save_state("dsd_temp@temp_i_gen", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
