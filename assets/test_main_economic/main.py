from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DF_TEST_MEI")
    
    if data.num_rows > 0:
        upload_data(data, "test_main_economic")
        print(f"Uploaded {data.num_rows} rows to test_main_economic")
        
    save_state("test_main_economic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
