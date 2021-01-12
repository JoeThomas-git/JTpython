import speedtest

st = speedtest.Speedtest()
option = int(input('''What speed do you want to test?

1) Download
2) Upload
3) Ping

Your Choice: '''))

if option == 1:
    dl = (st.download()/1000000)
    print('Your download speed is %.2f mb/s' % dl)
    if dl <= 20:
        print("Pretty slow internet bud.")
    elif dl >= 20:
        print("Not bad!")

elif option == 2:
    ul = (st.upload()/1000000)
    print('Your upload speed is %.2f mb/s' % ul)
    if ul <= 10:
        print("Sucks bud.")
    elif ul >= 10:
        print("You're killing it!")

elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)

else:
    print("Not a valid answer, please enter a value 1-3.")
