import requests

def main():
    requestdata = requests.get('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2018-02-10&'
       'sortBy=popularity&'
       'apiKey=f5f6bcd710b04091bab2fa73f226d1e5')
    jsonrequestdata = requestdata.json()
    print(jsonrequestdata)

main()
