# AI Vocabulary Web Scraping Application
### Overview
This project contains a web scraping application that collects AI-related terms and their definitions from the CNIL's AI glossary. It presents the information in a user-friendly interface using Streamlit, making it easier to navigate through the glossary and access definitions. The application allows users to select glossary entries alphabetically and view detailed definitions along with relevant hyperlinks for further reading.

## Features
Alphabetical Navigation: Users can select terms based on their starting letter.
Detailed Definitions: Each term includes a comprehensive definition sourced directly from the CNIL's AI glossary.
Hyperlinks to Original Source: Direct links to the CNIL's website for users who wish to explore further.
User-Friendly Interface: A simple and intuitive Streamlit interface for easy navigation.
## Installation
To set up the project, follow these steps:

1. Clone the repository:
``` bash
git clone https://github.com/All-Khwarizmi/glossaire_ia
```
   
3. Install the required dependencies:
``` bash
pip install -r requirements.txt
```

## Usage
To run the application:

1. Navigate to the project directory.
2. Run the Streamlit application:
``` bash
streamlit run app.py
```


## Technologies
- Python: Main programming language used for scripting and web scraping.
- Streamlit: Framework for building the web application.
- BeautifulSoup: Used for web scraping HTML content.
- Pandas: For data manipulation and structuring.
- Requests: For making HTTP requests to the CNIL website.

## Project Structure
- app.py: The main application script.
- ai_vocabulary_web_scraping.ipynb: The notebook containing all the application logic.
- requirements.txt: Lists all the necessary Python libraries.

## Contributing
Contributions to improve the application are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.
   
## License
Distributed under the Apache 2.0 License. See LICENSE for more information.

