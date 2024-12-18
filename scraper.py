import time
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION ---
CHROME_DRIVER_PATH = r"C:\Users\cepha\Downloads\chrome-win64\chrome.exe"  # Update with the path to ChromeDriver
CHROME_BINARY_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome browser
DATABASE_PATH = "jobs.db"  # SQLite database file
URL = "https://www.indeed.com/jobs?q=Data+Scientist&l="  # Target URL

# --- SETUP CHROME OPTIONS ---
options = Options()
options.binary_location = CHROME_BINARY_PATH
options.add_argument("--headless")  # Run in headless mode (remove for debugging)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

# --- DATABASE SETUP ---
def initialize_database():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# --- SCRAPE JOB LISTINGS ---
def scrape_jobs(url):
    """Scrape job listings from the given URL."""
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Opening URL...")
        driver.get(url)
        time.sleep(5)  # Allow time for the page to load

        print("Extracting job details...")
        job_cards = driver.find_elements("class name", "job_seen_beacon")
        jobs = []
        for card in job_cards:
            try:
                title = card.find_element("class name", "jobTitle").text
                company = card.find_element("class name", "companyName").text
                location = card.find_element("class name", "companyLocation").text
                jobs.append({"title": title, "company": company, "location": location})
            except Exception as e:
                print(f"Error extracting a job card: {e}")
        
        print(f"Extracted {len(jobs)} jobs.")
        return jobs

    except Exception as e:
        print(f"Error occurred while scraping: {e}")
        return []

    finally:
        driver.quit()

# --- STORE DATA IN DATABASE ---
def store_jobs_in_database(jobs):
    """Store the scraped jobs in the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location) VALUES (?, ?, ?)
        """, (job["title"], job["company"], job["location"]))
    conn.commit()
    conn.close()
    print(f"Stored {len(jobs)} jobs in the database.")

# --- MAIN FUNCTION ---
def main():
    """Main function to run the scraper."""
    print("Initializing database...")
    initialize_database()

    print("Starting web scraper...")
    jobs = scrape_jobs(URL)

    if jobs:
        print("Storing jobs in the database...")
        store_jobs_in_database(jobs)
    else:
        print("No jobs were scraped.")

    print("Scraper finished.")

# --- ENTRY POINT ---
if __name__ == "__main__":
    main()
