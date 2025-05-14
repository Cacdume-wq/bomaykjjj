import requests
import time
import os,sys
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;20m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;20m"
lam="\033[1;20m"
tim="\033[1;20m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;20m"
lam = "\033[1;36m"
tim = "\033[35m"
hong = "\033[1;95m"
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

os.system('clear')
# Thông tin cần thiết
access_token = input("\033[1;94mNHẬP TOKEN FB: ")  # Token người dùng
cookie = input("\033[1;94mNHẬP COOKIE FB: ")              # Cookie từ trình duyệt
comment_id = input("\033[1;94mNHẬP ID BÌNH LUẬN TĂNG LIKE: ")    
time_sec=int(input('\033[1;94mNhập delay tăng :'))# ID bình luận muốn thích
api_version = "v22.0"

# Headers chứa cookie
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        while(p>1):
            p=p-1
            print(f'[ 🌸\033[1;20mPHUOCAN🌸][|][\033[1;20mLO......][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mPHUOCAN🌸][/][\033[1;20mLOA.....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mPHUOCAN🌸][-][\033[1;20mLOAD....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mPHUOCAN🌸][+][\033[1;20mLOADI...][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20mPHUOCAN🌸][\][\033[1;20mLOADIN..][{p}]','     ',end='\r');sleep(1/6)
            print(f'[ 🌸\033[1;20MPHUOCAN🌸][|][\033[1;20mLOADING.][{p}]','     ',end='\r');sleep(1/6)
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ", end="\r")
# Hàm lấy danh sách token của tất cả các Trang
def get_page_tokens():
    url = f"https://graph.facebook.com/{api_version}/me/accounts"
    params = {"access_token": access_token}
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        pages = data.get("data", [])
        if not pages:
            print("Không tìm thấy Trang nào.")
            return []
        print(f"Tìm thấy {len(pages)} Trang.")
        return [{"page_name": page["name"], "access_token": page["access_token"]} for page in pages]
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy danh sách Trang: {e}")
        print(f"Phản hồi: {response.text}")
        return []

# Hàm thích bình luận bằng token của Trang
def like_comment_with_page(page_access_token, page_name):
    url = f"https://graph.facebook.com/{api_version}/{comment_id}/likes?access_token={page_access_token}"
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Thích bình luận {comment_id} thành công bằng Trang '{page_name}'!")
            return True
        else:
            print(f"Thích bình luận {comment_id} thất bại bằng Trang '{page_name}': {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi thích bình luận bằng Trang '{page_name}': {e}")
        print(f"Phản hồi: {response.text}")
        return False

# Thực thi chính
if __name__ == "__main__":
    pages = get_page_tokens()
    if pages:
        # Hiển thị danh sách các Trang
        print("Danh sách các Trang Đang Có:")
        for i, page in enumerate(pages, start=1):
            print(f"[{i}]|{page['page_name']}")
        
        # Tiếp tục với hành động thích bình luận
        successful_likes = 0
        for page in pages:
            countdown(time_sec)
            print(f"Đang xử lý Trang: {page['page_name']}")
            if like_comment_with_page(page["access_token"], page["page_name"]):
                successful_likes += 1
            time.sleep(2)  # Độ trễ 2 giây để tránh giới hạn API
        print(f"Hoàn tất! Đã thích bình luận {comment_id} bằng {successful_likes}/{len(pages)} Trang.")
    else:
        print("Không có Trang nào để thực hiện hành động.")
