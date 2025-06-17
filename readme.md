# Proxy Scraper Tool

## 🌟 Features
- **Multi-Source Scraping** - Aggregates proxies from 6+ public sources
- **Smart Validation** - Cleans and filters invalid proxies
- **Concurrent Fetching** - Uses threading for faster scraping
- **Duplicate Removal** - Ensures unique proxies only
- **Rich Output** - Beautiful console interface

## 🛠️ Installation
```bash
# Run setup (auto-installs dependencies)
python setup.py 
```

## 🚀 Usage
```bash
python main.py
```
Output will be saved to `proxies.txt`


## 📂 File Structure
```
/
├── main.py   # Main scraping tool
├── setup.py           # Installation script
```

## 📊 Performance
- Typically scrapes 5000-15000 proxies
- Execution time: 15-30 seconds
- Output format: `IP:PORT` (one per line)

## ⚠️ Important Notes
- Free proxies often have low reliability
- Always verify proxies before production use
- Respect source websites' terms of service
- Not responsible for misuse of scraped proxies

## 📜 License
MIT License - Free for educational and personal use

## 👨💻 Author
**Rayzer** - [@exsarorrayzer](https://github.com/exsarorrayzer)

---

### 🔧 Troubleshooting
**Problem**: Connection errors  
**Solution**: Check your internet connection and firewall settings

**Problem**: Empty output file  
**Solution**: Sources may be temporarily down - try again later

**Problem**: Rate limiting  
**Solution**: Wait 1-2 minutes between scrapes

---
