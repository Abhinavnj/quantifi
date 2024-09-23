# Quantifi

Quantifi is a financial analysis platform designed to simplify investment knowledge and empower users to make informed financial decisions. With a focus on intuitive design and comprehensive data insights, Quantifi caters to both beginners and experienced traders. The platform provides users with real-time market data, financial trends, and personalized investment insights, helping users understand their financial options better.

## Vision

At Quantifi, our mission is to make investment knowledge and financial analysis accessible to everyone. Whether you're an experienced trader or just starting out, we believe that understanding the world of finance should be intuitive and user-friendly. Our goal is to empower individuals by offering data-driven insights that enable smarter investment choices.

### Key Features

- **Comprehensive financial analysis tools**: Users can perform in-depth stock analysis, access historical data, and visualize financial trends.
- **Real-time market data and trends**: Powered by the Polygon.io API, users receive live updates and data insights on the stocks they follow.
- **User-friendly interface**: Designed for ease of use, with a sleek interface that caters to both beginner and expert investors.

## Table of Contents
- [Quantifi](#quantifi)
  - [Vision](#vision)
    - [Key Features](#key-features)
  - [Table of Contents](#table-of-contents)
  - [Technical Stack](#technical-stack)
  - [FastAPI Backend](#fastapi-backend)
    - [Key Backend Features:](#key-backend-features)
  - [Polygon.io API Integration](#polygonio-api-integration)
  - [Vue.js Frontend](#vuejs-frontend)
    - [Key Frontend Features:](#key-frontend-features)
  - [DynamoDB Integration](#dynamodb-integration)
    - [Blog API:](#blog-api)
  - [AWS EC2 \& NGINX Hosting](#aws-ec2--nginx-hosting)
    - [AWS Components:](#aws-components)
  - [Dockerization](#dockerization)
  - [Setup Instructions](#setup-instructions)
    - [Prerequisites:](#prerequisites)
    - [Backend Setup:](#backend-setup)

## Technical Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Vue.js (JavaScript), TailwindCSS, DaisyUI
- **Database**: AWS DynamoDB
- **Hosting**: AWS EC2 with NGINX
- **Data Provider**: Polygon.io API

## FastAPI Backend

The backend is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework for building APIs with Python. FastAPI powers the financial data endpoints and integrates with the Polygon.io API for real-time stock data.

### Key Backend Features:
- **Financial Data Retrieval**: Handles requests to retrieve stock data, market trends, and financial metrics.
- **Data Caching**: Efficiently caches API responses to minimize redundant calls to the Polygon.io API.
- **API Endpoints**: 
  - `/api/analysis`: Provides detailed analysis for a specific stock, including financial data, trends, and news.
  - `/api/blogs`: Fetches blog posts from DynamoDB and populates the blog section of the app.
  - `/api/ticker/news`: Retrieves recent news for a particular stock ticker.

## Polygon.io API Integration

Quantifi relies on the [Polygon.io API](https://polygon.io/) for real-time and historical stock data. The API integration allows the platform to fetch:
- Stock price history
- Real-time price updates
- Daily open, close, high, low, and volume data
- Aggregate stock data for the past 5 years

The FastAPI backend communicates with Polygon.io using secure API keys, ensuring smooth data flow between the two systems.

## Vue.js Frontend

The frontend is built using [Vue.js](https://vuejs.org/), a progressive JavaScript framework known for its flexibility and simplicity. The Vue.js frontend interacts with the FastAPI backend to display financial data, charts, and user insights.

### Key Frontend Features:
- **Stock Analysis Dashboard**: Users can view real-time stock performance, historical data, and financial statistics on the Analysis page.
- **Responsive UI**: TailwindCSS and DaisyUI are used to create a responsive and modern user interface, optimized for different screen sizes and devices.
- **Charts**: Financial trends are displayed using Chart.js, offering users interactive visualizations of stock performance over time.

## DynamoDB Integration

AWS DynamoDB is used to store blog content and any future user-related data. DynamoDB allows the platform to serve dynamic content, such as blog posts, to users without traditional SQL overhead.

### Blog API:
- **Blogs Endpoint**: The API `/api/blogs` fetches blog data from DynamoDB, dynamically rendering blog content on the front end.
- **Blog Structure**: Each blog post contains a title, description, content, and a timestamp.

## AWS EC2 & NGINX Hosting

Quantifi is hosted on an AWS EC2 instance, which provides the backend infrastructure for the FastAPI application. NGINX is configured as a reverse proxy, ensuring that traffic is efficiently routed between the frontend and backend services.

### AWS Components:
- **EC2**: Virtual servers to host the application and handle HTTP requests.
- **NGINX**: Configured as a reverse proxy to manage requests between FastAPI, Vue.js, and other external APIs.

## Dockerization

Quantifi is fully dockerized for ease of deployment. Both the FastAPI backend and Vue.js frontend are containerized using Docker, simplifying the setup and deployment process on AWS EC2.

The app is packaged with `docker-compose`, allowing you to deploy both the backend and frontend in a single command.

## Setup Instructions

### Prerequisites:
- Python 3.8+
- Node.js and npm
- AWS credentials for DynamoDB and EC2 (if deploying)

### Backend Setup:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/quantifi.git
   cd quantifi/backend
