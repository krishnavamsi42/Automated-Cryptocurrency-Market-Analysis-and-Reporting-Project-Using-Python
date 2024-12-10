# Task
# 1. Download the datasets from the coingeko
# 2. send mail.
# 3. schedule task  everyday at 8AM.

# importing dependencies
import smtplib       # sending email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders

import requests
import schedule
from datetime import datetime
import time
import pandas as pd

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def send_mail(subject,body,filename):
    #setup email configaration
    # smtp_server = "smtp.google.com"
    smtp_server='smtp.gmail.com'
    smtp_port=587
    
    sender_mail = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    receiver_mail = os.getenv("RECEIVER_EMAIL")

    #compose the mail
    message=MIMEMultipart()
    message['From']=sender_mail
    message['To']=receiver_mail
    message['Subject']= subject

    #attaching body of the mail
    message.attach(MIMEText(body,'plain'))

    #attach the csv file
    with open(filename, "rb") as file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())
        email.encoders.encode_base64(part)  
        part.add_header("Content-Disposition", f"attachment; filename=\"{filename}\"")
        message.attach(part)
            
    #start server
    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls()
            server.login(sender_mail,email_password)
            server.sendmail(sender_mail,receiver_mail,message.as_string())
            print("Email sent Sucessful")



    except Exception as e:
        print(f"unable to send mail {e}")     


def get_crypto_data():
    # API information
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    param = {
        'vs_currency' : 'usd',       #It allows you to customize the data based on the currency you want.
        'order' : 'market_cap_desc',
        'per_page': 250,
        'page': 1
    }

    # sending the request
    response = requests.get(url, params=param)

    if response.status_code == 200:
        print('Connection Successfull! \nGetting the data...')
        # 200: Indicates the request was successful, and the data was retrieved.
        # Other codes: Indicate various errors, such as 404 (not found) or 500 (server error).
        
        # storing the response into data
        data = response.json()
        
        # creating df dataframe
        df = pd.DataFrame(data)

        #Selecting only columns we need
        df = df[[
            'id','current_price', 'market_cap', 'price_change_percentage_24h',
            'high_24h', 'low_24h','ath', 'atl'
        ]]

        #creating new columns
        today=datetime.now().strftime('%d-%m-%Y %H-%M-%S')
        df['time_stamp']=today

        # Getting negative top 10
        top_negative_10 = df.nsmallest(10,'price_change_percentage_24h')
        
        # Getting positive top
        top_positive_10 = df.nlargest(10,'price_change_percentage_24h')
        
        # saving the data
        file_name = f'crypto_data {today}.csv'
        df.to_csv(file_name,index=False)

        print(f"Data saved successfull! as {file_name}!")

        #call email function to send the reports
        
        subject=f"Top 10 crypto currency data to invest for {today}"
        body=body = f"""
        Good Morning!\n\n

        Your crypt reports is here!\n\n

        Top 10 crypto with highest price increase in last 24 hour!\n
        {top_positive_10}\n\n\n

        Top 10 crypto with highest price decrease in last 24 hour!\n
        {top_negative_10}\n\n\n

        Attached 250 plus crypto currency latest reports\n

        Regards!\n
        See you tomorrow!\n
        Your crypto python application
        """

        #sending the mail
        send_mail(subject,body,file_name)


    else:
        print(f"Connection Failed Error Code {response.status_code}")   


# This gets executed only if we run this function
if __name__=='__main__':
    
    #get_crypto_data()
    #sheduling the task at every 8AM
    schedule.every().day.at('12:42').do(get_crypto_data)

    while True:
        schedule.run_pending()