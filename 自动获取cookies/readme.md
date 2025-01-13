

```markdown:README.md
# Bilibili Cookies 获取工具

这是一个用于获取和使用 Bilibili cookies 的 Python 工具。

## 功能特点

1. 自动获取浏览器中的 Bilibili cookies
2. 过滤并保存重要的 cookies
3. 支持使用已保存的 cookies 发送请求
4. 支持无 cookies 时的备用请求方式

## 使用前准备

1. 安装必要的 Python 包：
```bash
pip install selenium webdriver-manager requests
```

2. 确保已安装 Chrome 浏览器

3、低版本chrome需要安装chrome driver

## 使用方法

### 方法一：自动获取 Cookies

1. 运行脚本获取 cookies：
```python
python browser_cookies.py
```
脚本会自动访问 Bilibili 并获取 cookies，保存到 `useful_cookies.json` 文件中。

### 方法二：手动设置 Cookies

1. 从浏览器开发者工具中复制 cookies
2. 创建 `useful_cookies.json` 文件，格式如下：
```json
{
    "SESSDATA": "your_sessdata_here",
    "bili_jct": "your_bili_jct_here",
    "buvid3": "your_buvid3_here",
    "DedeUserID": "your_dedeuserid_here"
}
```

## 重要 Cookies 说明

Bilibili 主要使用的 cookies 包括：
- SESSDATA：登录凭证
- bili_jct：CSRF 令牌
- buvid3：设备标识
- DedeUserID：用户 ID
- DedeUserID__ckMd5：用户 ID 的 MD5 值
- sid：会话 ID
- _uuid：用户唯一标识
- b_ut：用户类型
- b_lsid：本地会话 ID
- buvid_fp：浏览器指纹

## 注意事项

1. 请勿分享你的 cookies 信息
2. cookies 有效期有限，过期需要重新获取
3. 使用 cookies 时需遵守 Bilibili 的使用条款
4. 建议定期更新 cookies

## 文件说明

- `browser_cookies.py`：主程序文件
- `useful_cookies.json`：保存过滤后的有效 cookies
- `response.html`：保存请求响应的内容

## 错误处理

如果遇到以下情况：
1. cookies 获取失败：检查浏览器是否正常运行
2. 请求失败：检查网络连接和 cookies 是否有效
3. ChromeDriver 错误：尝试更新 webdriver-manager
```

