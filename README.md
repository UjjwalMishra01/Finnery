# Finnery Project

## Introduction

**Finnery** is a financial chatbot designed to provide real-time financial information, answer investment-related queries, and deliver insights based on user input. The bot leverages APIs, document retrieval, and AI models to deliver accurate, personalized financial news and data.

## Features

- **Financial News & Updates**: Fetches real-time financial news and updates from APIs like NewsAPI, Yahoo Finance API, and FRED API.
- **Investment Guidance**: Answers questions related to stocks, economic indicators, and financial trends.
- **Document Retrieval**: Integrates with ChromaDB for storing and retrieving relevant financial documents.
- **Contextual Responses**: Utilizes embeddings and vector storage to improve the accuracy and relevance of responses.
- **Multi-API Integration**: Supports APIs for financial data, ensuring comprehensive and accurate answers.

## Prerequisites

- Python 3.x installed on your machine.
- API keys for NewsAPI, Yahoo Finance API, and FRED API.
- Basic understanding of Python and working with APIs.
- A GitHub account to access the repository.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/UjjwalMishra01/Finnery.git
   cd Finnery
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file and add your API keys:
     ```bash
     API_KEY_NEWSAPI=your_newsapi_key
     API_KEY_YAHOO_FINANCE=your_yahoo_finance_api_key
     API_KEY_FRED=your_fred_api_key
     ```

4. **Run the Bot**:
   ```bash
   python app.py
   ```

   This will start the chatbot and expose the service at `http://localhost:8000`.

## Configuration

- The `config.py` file contains configurable settings such as API endpoints and other parameters.
- You can update the `config.py` to customize the behavior of the chatbot, including API endpoints and other configurations.

## Contribution

Contributions to Finnery are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a pull request.

## License

Finnery is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute.
