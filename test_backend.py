import requests
import time

def test_send_otp():
    url = "http://127.0.0.1:5000/send-otp"
    payload = {"email": "test@example.com"}
    headers = {"Content-Type": "application/json"}
    
    print(f"Testing {url}...")
    start_time = time.time()
    try:
        response = requests.post(url, json=payload, headers=headers)
        duration = time.time() - start_time
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.json()}")
        print(f"Time taken: {duration:.2f} seconds")
        
        if response.status_code == 200:
            print("SUCCESS: Endpoint responded correctly.")
        else:
            print(f"FAILED: Status {response.status_code}")
            
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_send_otp()
