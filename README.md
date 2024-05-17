# Shree MCQ Generator: Transforming PDFs into Interactive Quizzes 🚀

The MCQ Generator is a powerful web application that allows users to generate multiple-choice questions (MCQs) from PDF files. This application leverages the power of Google's Generative AI and Streamlit to create an interactive and user-friendly experience.

## Features

- **Generate MCQs from PDF files**: Easily convert your PDF documents into interactive quizzes.
- **Select Difficulty Level**: Choose from three difficulty levels (Easy, Medium, or Hard) to suit your needs.
- **Customizable Question Count**: Specify the desired number of questions to generate.
- **Interactive Quiz Interface**: Engage with the generated questions in a sleek and intuitive interface.
- **Question Tracking**: Keep track of the questions you've attempted and those you haven't.
- **Results and Answer Key**: Upon submission, view your score and the answer key for further analysis.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Shree2604/Shree-MCQ-Wizard.git
```

2. Navigate to the project directory:

```bash
cd Shree-MCQ-Wizard
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the Google API key:
   - Create a `.env` file in the project root directory.
   - Add your Google API key to the file: `GOOGLE_API_KEY=your_api_key_here`

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Upload a PDF file through the file uploader.
3. Select the difficulty level and the number of questions to generate.
4. Click the "Start Quiz" button to generate the MCQs.
5. Answer the questions and click the "Submit" button to view your results and the answer key.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. We appreciate your feedback and contributions to make this project even better.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Google Generative AI](https://cloud.google.com/generative-ai) - Powerful generative AI models for generating MCQs.
- [Streamlit](https://streamlit.io/) - A modern and interactive data visualization library.
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) - A lightweight and robust PDF parsing library.

## Support

If you have any questions, issues, or need further assistance, please feel free to reach out to us at [shreeraj.m22@iiits.in](mailto:shreeraj.m22@iiits.in).

## Roadmap

We have an exciting roadmap planned for the MCQ Generator, including:

- Support for additional document formats (e.g., Word, PowerPoint)
- Improved question generation algorithms for higher accuracy
- Collaborative quiz-taking and real-time leaderboards
- Integration with learning management systems (LMS)

Stay tuned for more updates and enhancements!
