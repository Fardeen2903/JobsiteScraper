# JobsiteScraper
simple job website scraper in python

### `README.md`

JobsiteScraper is a Python-based GUI application for scraping job details from job sites. It allows users to input a URL, extract job details such as titles, categories, number of applicants, and requirements, and display them in a user-friendly interface. The results can also be saved to a file for further analysis.

---

## Features

- **User-friendly GUI**: Built with Tkinter for easy interaction.
- **Dynamic Job Scraping**: Extracts job details from a provided URL.
- **Categorized Job Information**:
  - **Title**: The job title.
  - **Category**: Job designation or category.
  - **Applicants**: Number of applicants for the job.
  - **Requirements**: Key job requirements.
- **Save Results**: Export scraped job details to a text file.

---

## How to Use

### Prerequisites

1. **Python**: Install Python 3.8 or higher.
2. **Dependencies**:
   - Install the required Python libraries:
     ```bash
     pip install selenium beautifulsoup4
     ```
3. **Chromedriver**:
   - Download [Chromedriver](https://chromedriver.chromium.org/downloads) matching your Chrome browser version.
   - Place the `chromedriver` executable in the project directory.

---

### Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/Fardeen2903/JobsiteScraper.git
   cd JobsiteScraper
   ```

2. Run the application:
   ```bash
   python contentscraper.py
   ```

3. Enter the job site URL in the provided field and click **Scrape Jobs**.

4. View categorized job details in the application.

5. Optionally, save the results to a text file by clicking **Save Results**.

---

## Code Structure

- **`contentscraper.py`**: Main application script with the scraping and GUI logic.
- **`requirements.txt`**: List of dependencies for the project (optional for packaging).

---

## Sample Screenshot

![image](https://github.com/user-attachments/assets/55c0a41d-8efa-4741-bb4a-6f3d95276793)

---

## Technical Details

- **Libraries Used**:
  - `selenium`: For web automation and scraping dynamic content.
  - `beautifulsoup4`: For parsing and extracting HTML content.
  - `tkinter`: For building the graphical user interface.

- **Dynamic Content Handling**:
  - Uses Selenium to load JavaScript-rendered content before parsing.

---

## Notes

- Ensure the target website structure matches the selectors used in the script. Update the `find` and `find_all` calls if the website layout changes.
- Respect the website's terms of service while scraping.

---

## Future Enhancements

- Add support for other job sites with modular scraping functions.
- Implement CSV/JSON export options for more flexible data handling.
- Add pagination support for scraping multiple pages.

---

## License

This project is licensed under the **BSD 2-Clause License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---
