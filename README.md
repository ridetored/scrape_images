# Web Scraper for Image SRCs

This Python script scrapes a list of product pages based on provided IDs and extracts the `src` URLs of images within specified desktop and mobile classes. The results are saved in a CSV file.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Add your list of product IDs**:  
   Create a file named `id_list.txt` in the project directory and add one product ID per line. You can use the `example_id_list.txt` as a reference.

2. **Replace URL and Class Keywords**:
   - In `scrape_images.py`, replace `url_template` with your actual URL format.
   - Update `desktop_class_keyword` and `mobile_class_keyword` with the actual class names or keywords present on your website.

3. **Run the script**:
    ```bash
    python scrape_images.py
    ```

4. **Output**:
    The script will create a `results.csv` file containing:
    - Product ID
    - Desktop image `src` URLs (if available)
    - Mobile image `src` URLs (if available)

## Example

An example `id_list.txt` is provided as `example_id_list.txt` in this repository.

### Note
Ensure that you update the class keywords (`example-desktop-class` and `example-mobile-class`) and URL format in `scrape_images.py` before running the script.

## License
This project is licensed under the MIT License.
