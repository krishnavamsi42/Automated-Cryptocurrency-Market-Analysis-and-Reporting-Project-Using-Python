# Automated Cryptocurrency Market Analysis and Reporting 

<img src="https://github.com/krishnavamsi42/Automated-Cryptocurrency-Market-Analysis-and-Reporting-Project-Using-Python/blob/main/image.webp" width="800"/>

## Project Overview
This project leverages Python to automate the process of fetching real-time cryptocurrency market data from the CoinGecko API. It analyzes the top 10 cryptocurrencies with the highest and lowest price changes over the last 24 hours, compiles the data into a CSV file, and sends daily email reports with the findings attached. The task is scheduled to run every day at 8:00 AM, making it a fully automated solution for tracking market trends in cryptocurrency.

## Objective
The primary goal of this project is to:
- Provide insights into the cryptocurrency market by identifying top-performing and underperforming cryptocurrencies based on price change.
- Automate data retrieval, processing, and reporting to save time for analysts or investors.
- Generate a daily email report that includes a CSV file with the latest market data and analysis, ensuring stakeholders can make informed decisions.

  
## Technologies Used
- Python
- Pandas
- Requests
- SMTP
- Schedule
- Dotenv (for environment variables)

### Purpose
- Python: The main programming language used to develop the application.
- Requests: To fetch real-time cryptocurrency data from the CoinGecko API.
- Pandas: For data manipulation and creating structured reports in CSV format.
- SMTP: For sending emails with attachments.
- Schedule: For automating the task to run daily at 8:00 AM.
- Dotenv: For securely managing environment variables like email credentials.
