# Web Scraping Project

This is a web scraping project in Python that uses BeautifulSoup for HTML parsing and requests for making HTTP requests.

## Description

The goal of this project is to provide a basic structure for web scraping HTML pages and collecting specific data. The main script (`main.py`) initializes a `WebScraper` object and calls the `scrape()` method to collect data from a specific URL.

## Features

- **Modular Structure:** The project is organized into modules, separating the main script from the scraping logic (`scraper.py`), allowing for easy extension and customization.

- **Dependency Management:** Dependencies are listed in the `requirements.txt` file, making it easy to install and manage project dependencies.

- **Gitignore Configuration:** The repository includes a `.gitignore` file to exclude unnecessary files and directories from version control.

- **Contributions Welcome:** Contributions are welcome through issues or pull requests, making it a collaborative project.

- **License:** The project is licensed under the MIT License, providing flexibility for use and modification.

## Prerequisites

Ensure you have Python installed on your machine. It is recommended to create a virtual environment before installing dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

How to Use

1. Clone this repository:

```bash
git clone https://github.com/DaveSimoes/web_scraping_project.git
cd web_scraping_project
```

2. Install dependencies:

```bash
pip install -r requirements.txt

```

3. Run the main script:

```bash
python src/main.py
```



### Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License.

Note: This project is just a basic example. Make sure to understand and respect the terms of service of the websites you are scraping.
