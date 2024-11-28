import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

# Path to chromedriver (ensure the correct version for your Chrome browser is installed)
service = Service('./chromedriver')  # Provide the relative or absolute path to chromedriver


def scrape_jobs():
    """Scrape job details from the provided URL."""
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        # Initialize the Chrome WebDriver with the service
        driver = webdriver.Chrome(service=service)

        # Open the URL
        results_text.delete("1.0", tk.END)
        results_text.insert(tk.END, f"Opening URL: {url}\n")
        driver.get(url)

        # Ensure the page is fully loaded
        time.sleep(5)

        # Get the page source
        html = driver.page_source

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        job_cards = soup.find_all('div', class_='job-card')  # Update this to the actual class used for job postings

        if job_cards:
            jobs = []
            results_text.insert(tk.END, "Categorized Job Details:\n\n")
            for job_card in job_cards:
                title = job_card.find('a', class_='title').text.strip() if job_card.find('a', class_='title') else "N/A"
                category = job_card.find('div', class_='category').text.strip() if job_card.find('div',
                                                                                                 class_='category') else "N/A"
                applicants = job_card.find('div', class_='applicants').text.strip() if job_card.find('div',
                                                                                                     class_='applicants') else "N/A"
                requirements = job_card.find('div', class_='requirements').text.strip() if job_card.find('div',
                                                                                                         class_='requirements') else "N/A"

                job_info = {
                    "Title": title,
                    "Category": category,
                    "Applicants": applicants,
                    "Requirements": requirements
                }
                jobs.append(job_info)

                # Display in the GUI
                results_text.insert(tk.END, f"Title: {title}\n")
                results_text.insert(tk.END, f"Category: {category}\n")
                results_text.insert(tk.END, f"Applicants: {applicants}\n")
                results_text.insert(tk.END, f"Requirements: {requirements}\n")
                results_text.insert(tk.END, "-" * 50 + "\n")

            save_button.config(state=tk.NORMAL)
            global scraped_data
            scraped_data = jobs
        else:
            results_text.insert(tk.END, "No job profiles found on the page.\n")

    except Exception as e:
        results_text.insert(tk.END, f"An error occurred: {e}\n")

    finally:
        # Close the WebDriver
        if 'driver' in locals():
            driver.quit()


def save_results():
    """Save the scraped results to a file."""
    if not scraped_data:
        messagebox.showwarning("Warning", "No data to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            for job in scraped_data:
                file.write(f"Title: {job['Title']}\n")
                file.write(f"Category: {job['Category']}\n")
                file.write(f"Applicants: {job['Applicants']}\n")
                file.write(f"Requirements: {job['Requirements']}\n")
                file.write("-" * 50 + "\n")
        messagebox.showinfo("Success", f"Results saved to {file_path}.")


# Create the GUI
root = tk.Tk()
root.title("Job Scraper")

# URL Entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Scrape Button
scrape_button = tk.Button(root, text="Scrape Jobs", command=scrape_jobs)
scrape_button.pack(pady=5)

# Results Text Area
results_text = tk.Text(root, height=20, width=60, wrap=tk.WORD)
results_text.pack(pady=5)

# Save Button
save_button = tk.Button(root, text="Save Results", command=save_results, state=tk.DISABLED)
save_button.pack(pady=5)

# Run the application
root.mainloop()
