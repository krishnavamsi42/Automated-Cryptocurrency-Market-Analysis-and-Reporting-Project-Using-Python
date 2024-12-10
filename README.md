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

## Findings
The project identifies the top 10 cryptocurrencies with:

- Highest price increase: Cryptocurrencies that have had the largest price increase in the last 24 hours.
- Highest price decrease: Cryptocurrencies that have had the largest price decrease in the last 24 hours.

These insights can be valuable for investors looking to track market trends or identify potential investment opportunities.

Sample Output (CSV)
The CSV file contains the following columns:

- ID: The cryptocurrency identifier.
- Current Price: The current market price of the cryptocurrency.
- Market Cap: The total market capitalization of the cryptocurrency.
- Price Change Percentage (24h): The percentage change in the price over the last 24 hours.
- 24h High: The highest price reached in the last 24 hours.
- 24h Low: The lowest price reached in the last 24 hours.
- All-Time High (ATH): The highest price ever recorded for the cryptocurrency.
- All-Time Low (ATL): The lowest price ever recorded for the cryptocurrency.
- Timestamp: The date and time when the data was retrieved.

## Objectives Achieved
- Automated Data Collection: Real-time data is fetched from the CoinGecko API every day.
- Data Analysis: Analyzed and identified the top-performing and underperforming cryptocurrencies based on price changes.
- Email Automation: A report is automatically generated and sent via email every day, providing insights into the market's performance.
- Ease of Use: The script is easy to use and can be scheduled to run without manual intervention.

## Conclusion
This project demonstrates how automation can be applied to real-time cryptocurrency market analysis, helping investors or analysts stay informed without manually tracking market data. With the addition of scheduled tasks and automated email reports, this solution provides both convenience and actionable insights. The project can be extended to track additional metrics or support multiple users.
