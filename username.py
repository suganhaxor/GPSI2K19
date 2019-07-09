
#importing libraries
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq


def NameUser():

    #username is input through user and search string is formed
    print('''1. Facebook \n2. Twitter''')
    choice = input(">>")
    if choice == '1':
        pass
    elif choice == '2':
        ScrapTweets()
        exit()
    else:
        exit()
    username= input("Enter the Username : ")
    search_string = "https://en-gb.facebook.com/" + username

    #response is stored after request is made
    response = requests.get(search_string)

    #Response is stored and parsed to implement beautifulsoup
    soup = BeautifulSoup(response.text, 'html.parser')

    #List that will store the data that is to be fetched
    data = {'Name': "null",
            'Photo_link': "null",
            'Work':{'Company': "null", 'Position': "null", 'time_period': "null", 'Location': "null"},
            'Education': {'Institute': "null", 'time_period': "null", 'Location': "null"},
            'Address': {'Current_city': "null", 'Home_town': "null"},
            'Favouriate': {},
            'Contact_info': {}
            }





    ###Finding Name of the user
    #Min div element is found which contains all the information
    main_div = soup.div.find(id="globalContainer")

    #finding name of the user
    def find_name():
        name = main_div.find(id="fb-timeline-cover-name").get_text()
        print(name)

    #finding profile pic of the user
    #link = main_div.find_all(name="img")





    ###Finding About the user details
    #finding work details of the user
    def find_eduwork_details():
        education = soup.find(id="pagelet_eduwork")
        apple=education.find(attrs={"class":"_4qm1"})
        if (apple.get_text() != " "):
            for category in education.find_all(attrs={"class":"_4qm1"}):
                print(category.find('span').get_text() + " : ")
                for company in category.find_all(attrs={"class":"_2tdc"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
            print("No work details found")

    #finding home details of the user
    def find_home_details():
        if(soup.find(id="pagelet_hometown") !=" "):
                home = soup.find(id="pagelet_hometown")
                for category in home.find_all(attrs={"class":"_4qm1"}):
                    print(category.find('span').get_text() + " : ")
                    for company in category.find_all(attrs={"class":"_42ef"}):
                        if (company.get_text() != " "):
                            print(company.get_text())
                        else:
                            continue
        else:
            print("No Home details found")

    #finding contact details of the user
    def find_contact_details():
        contact = soup.find(id="pagelet_contact")
        orange = contact.find(attrs={"class":"_4qm1"})
        if (orange.get_text() !=" "):
            for category in contact.find_all(attrs={"class":"_4qm1"}):
                print(category.find('span').get_text() + " : ")
                for company in category.find_all(attrs={"class":"_2iem"}):
                    if (company.get_text() != " "):
                        print(company.get_text())
                    else:
                        continue
        else:
             print("No Contact details found")






    ###Logic for finding the status of the response
    if ("200" in str(response)):
        find_name()
        find_eduwork_details()
        find_home_details()

    elif ("404" in str(response)):
        print("profile not found")
    else:
        print("some other response")


def ScrapTweets():
    username = input("Enter the user_id of the person -->   ")
    link = "https://twitter.com/" + username
    the_client = uReq(link)
    page_html = the_client.read()
    the_client.close()

    # print(link)

    soup = BeautifulSoup(page_html, 'html.parser')

    ######################################################################
    try:
        full_name = soup.find('a', attrs={"class": "ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
        print("User Name --> " + full_name.text)
    except:
        print("User Name --> Not Found")
    print()

    try:
        user_id = soup.find('b', attrs={"class": "u-linkComplex-target"})
        print("User Id --> " + user_id.text)
    except:
        print("User Id --> Not Found")
    print()

    try:
        decription = soup.find('p', attrs={"class": "ProfileHeaderCard-bio u-dir"})
        print("Description --> " + decription.text)
    except:
        print("Decription not provided by the user")
    print()

    try:
        user_location = soup.find('span', attrs={"class": "ProfileHeaderCard-locationText u-dir"})
        print("Location -->  " + user_location.text.strip())
    except:
        print("Location not provided by the user")
    print()

    try:
        connectivity = soup.find('span', attrs={"class": "ProfileHeaderCard-urlText u-dir"})
        tittle = connectivity.a["title"]
        print("Link provided by the user --> " + tittle)
    except:
        print("No contact link is provided by the user")
    print()

    try:
        join_date = soup.find('span', attrs={"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
        print("The user joined twitter on --> " + join_date.text)
    except:
        print("The joined date is not provided by the user")
    print()

    try:
        birth = soup.find('span', attrs={"class": "ProfileHeaderCard-birthdateText u-dir"})
        birth_date = birth.span.text
        print(birth_date.strip())
    except:
        print("Birth Date not provided by the user")
    print()

    ###########################################################################
    try:
        span_box = soup.findAll('span', attrs={"class": "ProfileNav-value"})
        print("Total tweets --> " + span_box[0].text)
    except:
        print("Total Tweets --> Zero")
    print()

    try:
        print("Following --> " + span_box[1].text)
    except:
        print("Following --> Zero")
    print()

    try:
        print("Followers --> " + span_box[2].text)
    except:
        print("Followers --> Zero")
    print()

    try:
        print("Likes send by him --> " + span_box[3].text)
    except:
        print("Likes send by him --> Zero")
    print()

    try:
        if span_box[4].text != "More ":
            print("No. of parties he is Subscribed to --> " + span_box[4].text)
        else:
            print("No. of parties he is Subscribed to --> Zero")
    except:
        print("No. of parties he is Subscribed to --> Zero")
    print()

    spana = soup.findAll('span', attrs={"class": "ProfileNav-value"})

    ###########################################################################
    print("Tweets by " + username + " are --> ")
    # TweetTextSize TweetTextSize--normal js-tweet-text tweet-text
    for tweets in soup.findAll('p', attrs={"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
        print(tweets.text)
        print()


