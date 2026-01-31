import yagmail
import os
from datetime import datetime

# 从GitHub的保险箱读取邮箱信息
email_user = os.environ.get("EMAIL_USER")
email_pass = os.environ.get("EMAIL_PASS")

# 获取今天的日期
today = datetime.now().strftime("%m月%d日")

# 邮件内容（先用测试内容，成功后再换成真新闻）
html_content = f"""
<h2 style="color: #2c3e50;">🤖 {today} AI 新闻早报</h2>

<div style="margin: 20px 0; padding: 15px; border-left: 4px solid #3498db; background-color: #f8f9fa;">
    <h3 style="margin: 0 0 10px 0; color: #e74c3c;">📰 测试新闻：配置成功！</h3>
    <p style="margin: 0; color: #555;">如果你看到这封邮件，说明你的AI新闻机器人已经正常工作。</p>
    <p style="margin: 5px 0 0 0;"><a href="https://github.com" style="color: #3498db;">点击查看详情 →</a></p>
</div>

<div style="margin: 20px 0; padding: 15px; border-left: 4px solid #3498db; background-color: #f8f9fa;">
    <h3 style="margin: 0 0 10px 0; color: #e74c3c;">📰 AI技术每日更新</h3>
    <p style="margin: 0; color: #555;">这是系统每日自动推送的AI行业新闻汇总...</p>
    <p style="margin: 5px 0 0 0;"><a href="https://news.ycombinator.com" style="color: #3498db;">查看更多 →</a></p>
</div>

<hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
<p style="color: #999; font-size: 12px;">— 由你的私人 AI 机器人发送 🚀<br>发送时间：{today}</p>
"""

try:
    # 连接QQ邮箱服务器
    yag = yagmail.SMTP(user=email_user, password=email_pass, host='smtp.qq.com', port=465)
    
    # 发送邮件（发给自己）
    yag.send(
        to=email_user, 
        subject=f'📰 AI早报 {today}', 
        contents=[html_content]
    )
    print("✅ 邮件发送成功！请检查你的QQ邮箱")
except Exception as e:
    print(f"❌ 发送失败，错误信息：{e}")
    print("💡 提示：请检查EMAIL_USER和EMAIL_PASS是否正确设置")
