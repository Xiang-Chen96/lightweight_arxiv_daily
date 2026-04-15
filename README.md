# Lightweight arXiv Graber

自动获取 arXiv 上最新的 hep-ex 领域论文，并可通过邮件发送通知。

## 功能

- 📚 获取指定天数内的最新论文
- 📧 支持邮件通知（HTML 格式）
- ⏰ 支持 GitHub Actions 定时运行
- 🔧 支持本地运行和 CI/CD 部署

## 快速开始

### 本地运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置环境变量（二选一）：

   **方式一：使用 .env 文件**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件填入你的配置
   ```

   **方式二：使用系统环境变量**
   ```bash
   export SMTP_SERVER=smtp.163.com
   export SMTP_PORT=465
   export EMAIL_FROM=your_email@163.com
   export EMAIL_PASSWORD=your_auth_code
   export EMAIL_TO=recipient@example.com
   ```

3. 运行：
```bash
# 仅显示论文
python main.py

# 发送邮件通知
python main.py --email

# 自定义参数
python main.py --days 7 --max-results 50 --email
```

### GitHub Actions 部署

1. 在 GitHub 仓库的 Settings → Secrets and variables → Actions 中添加以下 Secrets：

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `SMTP_SERVER` | SMTP 服务器地址 | `smtp.163.com` |
| `SMTP_PORT` | SMTP 端口 | `465` |
| `EMAIL_FROM` | 发件人邮箱 | `your_email@163.com` |
| `EMAIL_PASSWORD` | 邮箱授权码 | `your_auth_code` |
| `EMAIL_TO` | 收件人邮箱 | `recipient@example.com` |

2. 工作流会自动运行：
   - 每天 UTC 0:00（北京时间 8:00）自动执行
   - 也可在 Actions 页面手动触发

## 配置说明

### 163 邮箱配置
```
SMTP_SERVER=smtp.163.com
SMTP_PORT=465
EMAIL_FROM=your_email@163.com
EMAIL_PASSWORD=your_auth_code  # 客户端授权码，不是登录密码
```

### Gmail 配置
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_FROM=your_email@gmail.com
EMAIL_PASSWORD=your_app_password  # 应用专用密码
```

## 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--days` | 搜索过去几天的论文 | 3 |
| `--max-results` | 最大结果数量 | 100 |
| `--email` | 发送邮件通知 | false |
| `--translate` | 启用英文到中文翻译 | false |

## 项目结构

```
.
├── main.py                 # 主程序
├── email_notifier.py       # 邮件通知模块
├── requirements.txt        # Python 依赖
├── .env.example           # 环境变量示例
├── .gitignore             # Git 忽略文件
└── .github/
    └── workflows/
        └── daily_arxiv.yml # GitHub Actions 工作流