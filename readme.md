
---

# **Web Scraper Project**

## **Overview**
This project is a web scraping tool built using Python and Selenium to extract job listings from online job portals such as **Indeed.com**. The data, including job titles, company names, and locations, is automatically stored in a SQLite database for further analysis.

---

## **Features**
- Scrapes job postings dynamically from **Indeed** or similar platforms.
- Extracts information such as:
  - **Job Title**
  - **Company Name**
  - **Location**
- Stores scraped data into a **SQLite database**.
- Designed to run in **headless mode** for performance and automation.
- Includes error handling to manage scraping interruptions.

---

## **Tech Stack**
- **Python 3.x**: Core programming language.
- **Selenium**: Used for web scraping and automation.
- **SQLite3**: Lightweight database for storing job listings.
- **ChromeDriver**: WebDriver for Chrome browser automation.
- **Flask**: (Optional) Can serve data extracted by the scraper.

---

## **Project Structure**
```
web_scraper_project/
│-- app.py               # Main script for running the web scraper
│-- requirements.txt     # Dependencies for the project
│-- jobs.db              # SQLite database to store job data
│-- README.md            # Documentation for the project
│-- /screenshots         # Screenshots or sample outputs (optional)
```

---

## **Installation**

### **Prerequisites**
- Python 3.x installed
- Google Chrome installed
- ChromeDriver (compatible version) downloaded
- Required Python packages: Selenium and SQLite3

### **Steps**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/web_scraper_project.git
   cd web_scraper_project
   ```

2. **Install dependencies:**
   Use `pip` to install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver:**
   - Download from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
   - Place it in your project folder or add it to your PATH.

---

## **Usage**

1. **Update Configuration:**
   Open the `app.py` file and configure these variables:
   ```python
   CHROME_DRIVER_PATH = "path/to/chromedriver"  # Path to ChromeDriver
   CHROME_BINARY_PATH = "path/to/chrome"        # Path to Chrome browser
   DATABASE_PATH = "jobs.db"                    # Path for SQLite database
   URL = "https://www.indeed.com/jobs?q=Data+Scientist&l="  # Target URL
   ```

2. **Run the Web Scraper:**
   Execute the script:
   ```bash
   python app.py
   ```

3. **View the Data:**
   After running, the scraped job listings are stored in `jobs.db`. Use SQLite tools or Python to view the database content:
   ```python
   import sqlite3

   conn = sqlite3.connect("jobs.db")
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM jobs")
   print(cursor.fetchall())
   conn.close()
   ```

---

## **Example Output**
Sample job data stored in the SQLite database:

| ID  | Job Title           | Company Name          | Location           |
|-----|---------------------|-----------------------|--------------------|
| 1   | Data Scientist      | ABC Tech Solutions    | New York, NY       |
| 2   | Machine Learning Eng| XYZ Innovations       | San Francisco, CA  |

---

## **Error Handling**
- Automatically skips invalid job cards.
- Gracefully handles page loading or scraping issues with appropriate error messages.

---

## **Future Enhancements**
- Add support for other job portals (e.g., LinkedIn, Glassdoor).
- Integrate Flask or FastAPI to display scraped data via a web dashboard.
- Export scraped data to CSV, Excel, or JSON format.
- Add multi-threading to speed up scraping.

---

## **Dependencies**
- **Selenium**: Web scraping automation.
- **SQLite3**: Database management.
- **ChromeDriver**: WebDriver for Chrome browser.

Install all dependencies via:
```bash
pip install selenium sqlite3
```

---

## **Contributions**
Feel free to fork the repository, make changes, and submit pull requests. All contributions are welcome.

---

## **License**
This project is licensed under the **MIT License**.

---

## **Contact**
**Cephas Acquah Forson**  
Email: [cephas@example.com](mailto:cephasfn@gmail.com)  
GitHub: [@cephas2bn](https://github.com/cephas2bn)  
LinkedIn: [Cephas Acquah Forson](https://www.linkedin.com/in/cephasaforson/)

---
