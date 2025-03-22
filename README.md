# ShopScribe: AI Product Description Generator

![Logo](https://github.com/user-attachments/assets/15f31d0c-b7ea-4ee6-8b88-49d6cfa64a53)


A simple Flask web application that uses an LLM (OpenAI GPT) to generate compelling product descriptions based on user-provided inputs such as **Product Name**, **Keywords**, and a selectable **Tone**.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Tone Options](#tone-options)
- [Screenshots](#screenshots)
- [License](#license)

---

## Overview

ShopScribe is a demonstration of how Large Language Models (LLMs) can be integrated into retail and e-commerce solutions. By simply providing a **Product Name**, **Keywords**, and a desired **Tone**, you can instantly generate a custom product description suitable for various marketing channels.

---

## Features

1. **Easy Input**: Users can enter a product name and relevant keywords.
2. **Tone Selection**: Choose from multiple tones (Neutral, Formal, Casual, etc.) to tailor your description for different audiences.
3. **Real-Time Generation**: The application leverages OpenAI’s API to create product descriptions on the fly.
4. **Flask Framework**: A lightweight and efficient server-side environment.

---

## Setup and Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/yourusername/ShopScribe.git
   cd ShopScribe
   ```
2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > Alternatively, install Flask, openai, and python-dotenv manually:
   > ```bash
   > pip install flask openai python-dotenv
   > ```
4. **Add Your OpenAI API Key**:
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your-secret-key-here
     ```
   - Make sure `.env` is listed in your `.gitignore` to keep your key private.

---

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```
2. **Open Your Browser**:
   - Go to `http://127.0.0.1:5000/` (or the URL shown in your terminal).
3. **Enter Product Details**:
   - **Product Name**: e.g., *Shoes*
   - **Keywords**: e.g., *Leather*
   - **Tone**: e.g., *Neutral*
4. **Generate Description**:
   - Click the **Generate Description** button to see your AI-generated product description.

---

## Tone Options

- **Neutral**: Provides a straightforward, balanced description without strong emotional or stylistic elements.
- **Formal**: Uses professional language, suitable for business or academic contexts.
- **Casual**: Creates a friendly, conversational style ideal for everyday consumer products.
- **Humorous**: Injects light-hearted humor and a fun approach to engage readers in a more playful way.
- **For Young Adults**: Targets a younger demographic with more trendy language and style.
- **For Professionals**: Tailored to a business-minded audience, focusing on efficiency and expertise.

---

## Screenshots

1. **Screenshot: Inputting Product Name & Keywords**  
   ![Screenshot 2025-03-22 122355](https://github.com/user-attachments/assets/fc1a7184-a827-48e9-94f6-c5f2113236f6)

   *Description: Show how a user enters “Shoes” as the Product Name and “Leather” as the Keywords.*

2. **Screenshot: Tone Dropdown**  
   ![Screenshot 2025-03-22 122348](https://github.com/user-attachments/assets/bca693cf-bcfa-463d-bd07-5bc2831dc098)

   *Description: Highlight the dropdown menu with the available tone options (Neutral, Formal, Casual, etc.).*

3. **Screenshot: Generated Description**  
   ![Screenshot 2025-03-22 122355](https://github.com/user-attachments/assets/20442341-9282-4d7c-9308-8e639d256b22)

   *Description: Show the AI-generated product description displayed under “Generated Description.”*

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute this application as needed.

---

### Additional Notes

- If you encounter issues with `openai.Completion`, you may need to update your code to use `openai.ChatCompletion` or install a specific version of the `openai` package.
- Ensure you do not commit your `.env` file to version control.

Enjoy building your **ShopScribe** application! If you have any questions or suggestions, feel free to open an issue or submit a pull request.
