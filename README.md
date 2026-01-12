# Customer Support Bot System with RAG

A powerful customer support bot system built using FastAPI and LangChain, implementing Retrieval-Augmented Generation (RAG) for intelligent customer query responses based on product reviews.

## Features

- FastAPI-based web application
- RAG implementation for context-aware responses
- Google's Generative AI integration
- Interactive chat interface
- Document retrieval system using product review data
- Customizable prompt templates
- Docker support for easy deployment

## Project Structure

```
├── config/             # Configuration files and YAML settings
├── data/              # Product review datasets
├── data_ingestion/    # Data processing and ingestion pipeline
├── notebook/          # Jupyter notebooks for development
├── prompt_library/    # Custom prompt templates
├── retriever/         # Document retrieval system
├── static/           # Static files (CSS)
├── templates/        # HTML templates
├── utils/            # Utility functions and model loaders
├── main.py           # FastAPI application
├── requirements.txt  # Project dependencies
├── setup.py          # Package setup configuration
├── test.py           # Test suite
└── Dockerfile        # Docker configuration
```

## Prerequisites

- Python 3.10
- Conda (for environment management)
- Google API credentials (for Gemini integration)
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/siddharthgupta5/YouBot.git
cd YouBot
```

2. Create and activate the conda environment:
```bash
conda create -p venv python=3.10 -y
conda activate venv
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add your Google API credentials:
```
GOOGLE_API_KEY=your_api_key_here
```

## Running the Application

### Using Python

Start the FastAPI server:
```bash
uvicorn main:app --reload --port 8001
```

### Using Docker

Build and run the Docker container:
```bash
docker build -t customer-support-system .
docker run -p 8001:8001 customer-support-system
```

The application will be available at `http://localhost:8001`

## Usage

1. Open your web browser and navigate to `http://localhost:8001`
2. Use the chat interface to interact with the customer support system
3. Ask questions about products or customer concerns
4. The system will retrieve relevant information from product reviews and generate context-aware responses

## Development

- The main application logic is in `main.py`
- Configuration settings can be modified in `config/config.yaml`
- Custom prompts can be modified in the `prompt_library/` directory
- Document retrieval system is implemented in the `retriever/` directory
- Model loading utilities are in the `utils/` directory
- Frontend templates are located in the `templates/` directory
- Data ingestion pipeline is in the `data_ingestion/` directory

## Testing

Run the test suite:
```bash
python test.py
```

## Contributing

Contributions to the Customer Support System are welcome! If you have suggestions, enhancements, or bug fixes, please follow the steps below:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or feedback, please open an issue on the GitHub repository.
