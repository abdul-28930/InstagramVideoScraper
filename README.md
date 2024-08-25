# Instagram Video Scraper

Instagram Video Scraper is a Python-based tool designed to download videos from Instagram. This tool leverages the Instagram public API and web scraping techniques to collect videos from user profiles, hashtags, and locations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Video Scraping**: Download videos from any public Instagram user profile.
- **Configurable Output**: Choose the output directory and file naming conventions.
- **Automated Downloads**: Schedule downloads for batch processing.

## Installation

To install and run the Instagram Video Scraper, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/abdul-28930/InstagramVideoScraper.git
    cd InstagramVideoScraper
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Instagram Credentials**:

    Create a `.env` file in the root directory and add your Instagram credentials:

    ```
    INSTAGRAM_USERNAME=your_username
    INSTAGRAM_PASSWORD=your_password
    ```

    *Note: Use this tool responsibly and comply with Instagram's terms of service.*

## Usage

1. **Run the Scraper**:

    To start scraping videos, run the following command:

    ```bash
    python scraper.py --type <scrape_type> --target <target>
    ```

    - Replace `<scrape_type>` with `user`, `hashtag`, or `location`.
    - Replace `<target>` with the specific username, hashtag, or location you want to scrape.

    For example, to scrape videos from a user profile:

    ```bash
    python scraper.py --type user --target username
    ```

2. **Additional Options**:

    - `--output` specifies the directory where the videos will be saved.
    - `--limit` sets the maximum number of videos to download.

## Dependencies

- Python 3.6 or higher
- Requests
- BeautifulSoup
- Instaloader
- dotenv

To install these dependencies, run:

```bash
pip install requests beautifulsoup4 instaloader python-dotenv
```

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please reach out to the project maintainer at:

- Abdul - [GitHub Profile](https://github.com/abdul-28930)
