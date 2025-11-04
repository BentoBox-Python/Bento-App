# Core function to call other functions as needed
def main():
    # Call the notification_logic function
    try:
        notification_logic()
    except:
        print(Exception)


def notification_logic():
    try:
        # Test notifcation with two variables
        x = "foo"
        y = "bar"
        print(f"Notification: {x + y}")
        return
    except:
        print(Exception)

if __name__ == "__main__":
    main()
