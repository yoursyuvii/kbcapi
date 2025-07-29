# KBC Style Questions API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, easy-to-use Flask API that serves general knowledge questions in the style of the popular TV show 'Kaun Banega Crorepati' (KBC). This project is designed to be a straightforward backend for quiz applications, hackathons, or educational purposes.

## Live API Link

The API is deployed on Render and is publicly accessible.

**Base URL:** `https://kbc-api.onrender.com`

> **Note:** This API is hosted on Render's free tier. The first request after a period of inactivity may take 30-40 seconds to process as the server wakes up. Subsequent requests will be fast.

## Features

-   Serves random questions from a predefined list.
-   Allows fetching a specific question by its ID.
-   Easily extendable by adding more questions to the `questions.json` file.
-   Lightweight and built with Python and Flask.

## API Endpoints

Here are the available endpoints:

| Method | Endpoint                    | Description                                       |
| :----- | :-------------------------- | :------------------------------------------------ |
| `GET`  | `/`                         | Displays a simple welcome message for the API.    |
| `GET`  | `/api/questions/random`     | Fetches a single random question from the dataset. |
| `GET`  | `/api/questions/<int:id>`   | Fetches a specific question by its unique ID.     |

---

### Example Usage

#### Get a Random Question

**Request:**
`GET https://kbc-api.onrender.com/api/questions/random`

**Response:**
```json
{
  "answer": "c",
  "category": "Geography",
  "id": 1,
  "options": {
    "a": "Himachal Pradesh",
    "b": "Jammu and Kashmir",
    "c": "Uttarakhand",
    "d": "Sikkim"
  },
  "question": "In which Indian state would you find the Valley of Flowers National Park?"
}
````

#### Get a Question by ID

**Request:**
`GET https://kbc-api.onrender.com/api/questions/2`

**Response:**

```json
{
  "answer": "c",
  "category": "History",
  "id": 2,
  "options": {
    "a": "C. V. Raman",
    "b": "Mother Teresa",
    "c": "Rabindranath Tagore",
    "d": "Amartya Sen"
  },
  "question": "Who was the first Indian to win a Nobel Prize?"
}
```

-----

## Technology Stack

  - **Backend:** Python
  - **Framework:** Flask
  - **WSGI Server:** Gunicorn
  - **Deployment:** Render

## How to Set Up and Run Locally

To run this project on your own machine, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/kbc-api.git](https://github.com/your-username/kbc-api.git)
    cd kbc-api
    ```

2.  **Create and activate a virtual environment:**
    (This helps in managing project dependencies)

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**

    ```bash
    flask run
    ```

    The API will now be running at `http://127.0.0.1:5000`.

## How to Contribute

Contributions are welcome\! If you'd like to improve this API, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

Some ideas for contributions:

  - Add more questions to the `questions.json` file.
  - Create new endpoints (e.g., filter questions by category).
  - Improve the data structure.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

```
```
