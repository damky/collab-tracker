from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Sample data
data = {
    "names": ["John Doe", "Jane Smith", "Mike Johnson"],
    "platforms": ["Instagram", "TikTok", "YouTube"],
    "prices": [250, 450, 150],
    "engagement_rates": [3.5, 4.2, 2.8],
    "followers": [50000, 75000, 25000]
}

# HTML template
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Influencer Collaboration Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Influencer Collaboration Dashboard</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Platform</th>
                <th>Price</th>
                <th>Engagement Rate</th>
                <th>Followers</th>
            </tr>
            {% for i in range(data.names|length) %}
            <tr>
                <td>{{ data.names[i] }}</td>
                <td>{{ data.platforms[i] }}</td>
                <td>${{ data.prices[i] }}</td>
                <td>{{ data.engagement_rates[i] }}%</td>
                <td>{{ data.followers[i] }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 