# SEO Tools 🕵️‍♂

A collection of simple but useful SEO automation scripts written in Python.  
Created and maintained by **Gordon Nyona**, SEO Specialist & Freelancer.

---

##  Tools Included
- **Keyword Scraper** → Quickly collect keyword suggestions from search engines.  
- **Site Audit** → Run a lightweight SEO audit on any website (title tags, meta description, broken links).  

---

## Installation
```bash
## Usage

After installation, you can run the tools from the command line.

### Keyword Scraper
Run the script with a keyword phrase:
```bash
python keyword_scraper.py "best hotels in Nairobi" --limit 5
```

This will print out keyword suggestions from search results.

### Site Audit
Run the script with a website URL:
```bash
python site_audit.py https://example.com
```

This will output basic SEO audit information such as:
- Page Title  
- Meta Description  
- Total number of links  
- Broken links (if any)

git clone https://github.com/YOUR_USERNAME/seo-tools.git
cd seo-tools
pip install -r requirements.txt
