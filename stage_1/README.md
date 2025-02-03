# HNG 12 Stage 1 - Mathematical Properties API

This project is part of the **HNG 12 Internship** Stage 1 task. The goal is to create an API that accepts a number and returns interesting mathematical properties about it, along with a fun fact using the [Numbers API](http://numbersapi.com/#42).

## Project Overview

The API takes a number as input and returns the following properties:
- Whether the number is **prime**
- Whether the number is **perfect**
- Whether the number is an **Armstrong number**
- Whether the number is **odd** or **even**
- The **digit sum** of the number
- A **fun fact** about the number

### API Endpoint

- **Endpoint**: `/api/classify-number?number={number}`
- **Method**: `GET`
- **Response Format**: JSON

### Example Request:
```
GET https://hng-internship-projects-1.onrender.com/api/classify-number?number=371
```

### Example Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

---

## Features

- **Prime Number Check**: Determines if the number is prime.
- **Perfect Number Check**: Determines if the number is perfect (sum of divisors equals the number).
- **Armstrong Number Check**: Determines if the number is an Armstrong number (sum of its digits raised to the power of the number of digits equals the number).
- **Odd or Even Check**: Identifies if the number is odd or even.
- **Digit Sum**: Computes the sum of the digits of the number.
- **Fun Fact**: Fetches a fun fact about the number from the Numbers API.

---

## Technologies Used

- **Flask**: Web framework used to build the API.
- **Requests**: Used to make HTTP requests to the Numbers API to fetch fun facts.
- **Python 3.x**: Programming language used for backend logic.

---

## Setup and Installation

### Prerequisites:
- Python 3.x installed
- `pip` package manager

### 1. Clone the repository:
```bash
git clone git@github.com:EmmanuelNiyonshuti/hng-internship-projects.git
cd hng-internship-projects && cd stage_1
```

### 2. Install dependencies:
```bash
create virtual environment # optional but recommended
pip install -r requirements.txt
```

### 3. Run the API locally:
```bash
python app.py
```
This will start the Flask development server on `http://127.0.0.1:5000`.

### 4. Access the API:
You can now test the API by sending a `GET` request to `http://127.0.0.1:5000/api/classify-number?number=371`.

---

## Error Handling

- **400 Bad Request**: If the input is not a valid integer or is missing, the API will respond with a `400` error and an error message.
    - Example:
    ```json
    {
        "number": "alphabet",
        "error": true
    }
    ```

---

## Deployment

The API is deployed to [Your Hosting Platform](https://your-deployment-link.com).

---

## Contribution

If you'd like to contribute to the project, feel free to fork the repository, create a branch, and submit a pull request.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

- **NIYONSHUTI Emmanuel**  
- HNG 12 Internship - Stage 1 Task

