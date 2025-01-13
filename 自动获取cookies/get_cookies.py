import requests

def get_cookies(url):
    """
    获取指定网址的cookies
    """
    # 发送GET请求
    response = requests.get(url)
    
    # 获取cookies
    cookies = response.cookies
    
    # 转换成字典形式
    cookies_dict = requests.utils.dict_from_cookiejar(cookies)
    
    return cookies_dict

def make_request_with_cookies(url, cookies):
    """
    使用cookies发送请求
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, cookies=cookies, headers=headers)
    return response

# 使用示例
if __name__ == "__main__":
    target_url = "https://example.com"  # 替换成你要访问的网站
    
    # 获取cookies
    cookies = get_cookies(target_url)
    print("获取到的cookies:", cookies)
    
    # 使用cookies发送请求
    response = make_request_with_cookies(target_url, cookies)
    print("响应状态码:", response.status_code) 