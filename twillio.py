from twilio.rest import Client
import psycopg2

account_sid = 'ACb59fc744019c4b49ec900c9fdb8a4fa9'
auth_token = '2bf9b951747e2747b0fc36ec00195bdf'
client = Client(account_sid, auth_token)


try:
    connection = psycopg2.connect(user = "dbAssignment",
                                 password = "test",
                                 host = "127.0.0.1",
                                 port = "5433",
                                 database = "assignment")
    cursor = connection.cursor()
    print ( connection.get_dsn_parameters(),"\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    message = client.messages.create(
        body='Kitida dakhavties?',
        from_='+12132773823',
        to='+12134763934')
except:
    print("Error")
#
# finally:
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")
print(message.sid)