from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    # Use beautiful soup to prettify data
    # Set an instance of beautiful soup
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # Scrapping of specific data
    all_tickets = soup.find_all('div', class_='container3-item')
    for ticket in all_tickets:
        ticket_name = ticket.p.text
        ticket_price = ticket.a.text.split()[-1]
        print(f'The ticket {ticket_name} is estimated to cost you {ticket_price}')