
##### pip install speedtest-cli

import speedtest

def test_speed():
  st = speedtest.Speedtest()
  print("Vui Lòng Chờ Giây Lát....")
  download_speed = int(st.download())/1024/1024  # Convert to Mbps
  upload_speed = int(st.upload())/1024/1024  # Convert to Mbps

  print(f"Download Speed: {download_speed:.2f} Mbps")
  print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
  test_speed()