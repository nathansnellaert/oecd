from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INDUSTRIAL_POLICY@DF_FIN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quis_policy_financial_instruments")
        print(f"Uploaded {data.num_rows} rows to quis_policy_financial_instruments")
        
    save_state("quis_policy_financial_instruments", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
