#gathering user data and generatinga  text file with  all the data 
from pywebio.input import *
from pywebio.output import *
def main():
    name=input("Enter your name here : ",type=TEXT)
    age=input("Enter age here : ",type=NUMBER)
    select_language=select("Select prefrered language",options=['Hindi','English','Marathi'])
    select_gender=radio("Select Gender",options=['Male','Female','Dont want to disclsoe'])
    terms=checkbox("Do you agree to our terms and conditions",options=['Yes I agree',"No i don't agree"])
    toast("Successfuly registered data")
    put_text("Thank you for your time for the survey")
    with open('data.txt','a') as file1:
        file1.write(f'Your name : {name}\n')
        file1.write(f'Your age : {age}\n')
        file1.write(f'Prefered Language : {select_language}\n')
        file1.write(f'Gender : {select_gender}')
        file1.write(f'Terms : {terms}')
if __name__=='__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("--http", action="store_true", default=False, help='Whether to enable http protocol for communicates')
    args = parser.parse_args()

    if args.http:
        start_http_server(main, port=args.port)
    else:
        # Since some cloud server may close idle connections (such as heroku),
        # use `websocket_ping_interval` to  keep the connection alive
        start_ws_server(main, port=args.port, websocket_ping_interval=30)
