from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_SBE@DF_SBE")
    
    if data.num_rows > 0:
        upload_data(data, "activation_requirements_strictness")
        print(f"Uploaded {data.num_rows} rows to activation_requirements_strictness")
        
    save_state("activation_requirements_strictness", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
