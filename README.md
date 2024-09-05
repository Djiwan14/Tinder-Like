# Tinder Automation with Selenium

This project demonstrates automating the Tinder login and liking process using Selenium. The script handles login through Facebook, navigates Tinder's interface, and performs actions like liking profiles.

## Technologies Used

- **[Selenium](https://www.selenium.dev/)**: A browser automation tool that enables the interaction with web elements and automates repetitive tasks.
- **[Python](https://www.python.org/)**: The programming language used to write the automation script.
- **[Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/)**: The WebDriver used to interface with the Google Chrome browser.

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Install the required packages:**

    ```bash
    pip install selenium
    ```

3. **Download ChromeDriver:**

   Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/) and place it in a directory that is included in your system's PATH.

## Usage

1. **Setup Credentials:**

   Replace the placeholders `#` in the script with your actual Facebook email and password.

    ```python
    EMAIL = 'your-email@example.com'
    PWD = 'your-facebook-password'
    ```

2. **Run the script:**

   Execute the script using Python:

    ```bash
    python <script-name>.py
    ```

## Script Overview

- **Initialize WebDriver**: Starts a Chrome browser session.

    ```python
    driver = webdriver.Chrome()
    ```

- **Navigate to Tinder Login**: Opens the Tinder login page.

    ```python
    driver.get("https://tinder.com/app/profile")
    ```

- **Login via Facebook**: Clicks the Facebook login button and switches to the Facebook login window.

- **Enter Facebook Credentials**: Inputs email and password, and logs in.

- **Handle Tinder Permissions**: Interacts with Tinder's location, notifications, and cookie permissions pop-ups.

- **Like Profiles**: Clicks the "Like" button on profiles repeatedly.

- **Handle Pop-ups**: Manages "Matched" pop-ups and retries clicking the "Like" button if necessary.

## Notes

- Ensure that your Chrome browser version matches the ChromeDriver version.
- Be cautious when automating social media platforms; they may have terms of service that prohibit such automation.

