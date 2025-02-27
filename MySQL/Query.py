import subprocess, mysql.connector

config : dict = {
    "user" : "root",
    "password" : "root",
    "host" : "localhost",
    "port" : 3306
}

if __name__ == "__main__":
    with mysql.connector.connect(**config) as cnx:
        with cnx.cursor() as cursor:
            print(f"\n")
            query = input("Please enter your query! : ")
            print("Enter the password for the 'root' user when prompted! : ")
            subprocess.run(f"mysql -u root -p --execute '{query}';", shell = True)
            print(f"\n")

            while True:
                still = input("Do you want to do another query? (Y/N): ")

                match still:
                    case "Y":
                        print("\nContinuing! ...\n")
                        query = input("Please enter your query! : ")
                        print("Enter the password for the 'root' user when prompted! : ")
                        subprocess.run(f"mysql -u root -p --execute '{query}';", shell = True)
                        print(f"\n")
                    case "N":
                        print(f"\nGoodbye!\n")
                        break

    


