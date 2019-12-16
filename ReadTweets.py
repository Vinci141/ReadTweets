# goal is to read the tweets
from requests import get
from bs4 import BeautifulSoup

#python function definition
def ReadTweets():
    t_user = str(input("Enter User Name: "))
    #Input from user
    url = 'https://twitter.com/' + t_user
    Tweeter page for the valid user
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    #Parsing the web page for suitable content.
    content = html_soup.find_all('div', class_='js-tweet-text-container')
    #filtering the content based on HTML Div tag
    print('*' * 10, "Tweets of {}".format(t_user), '*' * 10)
    #Header of output
    for count, data in enumerate(content):
        print(count, data.text)
        #Printing text format of the tweets 


ReadTweets()
#Calling funtion
