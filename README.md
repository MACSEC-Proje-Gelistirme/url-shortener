# URL Shortener API Documentation

## Project Overview
This project is a RESTful API that takes long URLs from users, shortens them, and returns an easy-to-use short URL. When accessed, the short URL redirects the user to the original URL.

---

## Technologies and Tools
- **Programming Language:** Python
- **Framework:** Flask
- **Database:** SQLite
- **Server:** Flask local development server
- **JSON Format:** Used for API requests and responses.
- **Tools:** Postman (for testing)

---

## Installation Instructions

### 1. Install Required Packages
Install the following dependencies:
```bash
pip install flask sqlite3
```

### 2. Project Structure
The project directory should look like this:
```
url_shortener/
|-- app.py          # API application
|-- db.sqlite       # SQLite database file
```

### 3. Start the Server
Run the following command to start the project locally:
```bash
python app.py
```
The server will run at **http://localhost:5000**.

---

## API Endpoints

### 1. **Shorten URL**

- **Method:** POST  
- **URL:** `/shorten`  
- **Description:** Accepts a long URL, generates a unique short ID, saves it to the database, and returns the shortened URL.

#### Request
- **Header:** `Content-Type: application/json`
- **Body:**
```json
{
  "url": "https://www.example.com/long-url"
}
```

#### Response
- **Status Code:** 201
- **Body:**
```json
{
  "short_url": "http://localhost:5000/abc123"
}
```

#### Error Cases
- **Missing URL:**
```json
{
  "error": "URL is required"
}
```
- **Status Code:** 400

---

### 2. **Redirect to Original URL**

- **Method:** GET  
- **URL:** `/<short_id>`  
- **Description:** Redirects the user to the original URL based on the provided short ID.

#### Example
**Request:**
```
GET http://localhost:5000/abc123
```

**Result:** The user is redirected to the original URL in their browser.

#### Error Cases
- **Invalid Short ID:**
```json
{
  "error": "Short URL not found"
}
```
- **Status Code:** 404

---

## Database Design
**Table Name:** `urls`
| Column Name       | Data Type   | Description                      |
|------------------ |------------|----------------------------------|
| id                | INTEGER    | Auto-incrementing primary key    |
| short_id          | TEXT UNIQUE| Unique short identifier          |
| original_url      | TEXT       | Original long URL                |

---

## Workflow
1. The user sends a long URL to the **POST /shorten** endpoint.
2. The system generates a random **short_id** (6 characters).
3. The **short_id** and original URL are saved in the database.
4. The shortened URL is returned to the user.
5. When the user accesses **GET /<short_id>**, the system redirects them to the original URL.

---

## API Testing
You can test the API using Postman or cURL.

### 1. **Test Shorten URL**
```bash
curl -X POST http://localhost:5000/shorten \
-H "Content-Type: application/json" \
-d '{"url": "https://www.example.com/long-url"}'
```

### 2. **Test Redirect**
```bash
curl -i http://localhost:5000/abc123
```

---

## Development Suggestions
- **Validation:** Check the format of the submitted URL using regex.
- **Short ID Collision Handling:** Ensure that the same ID is not generated twice.
- **Rate Limiting:** Limit the number of requests per user per second.
- **Database:** Use PostgreSQL for better performance instead of SQLite.
- **Caching:** Use Redis to speed up the redirection process.

---

## Contact
For questions or further development, feel free to reach out. 😊

