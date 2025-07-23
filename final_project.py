import pandas as pd
import matplotlib.pyplot as plt


class DataAnalyzer:
    def __init__(self):
        self.data = None


    def load_dataset(self):
        self.data = pd.read_csv("test//final project//titanic_dataset (2).csv") 

        print("\nFile loaded successfully.........\n")

    def show_dataset(self):
        if self.data is not None :
            print(self.data.head())
            print("\n")
            print(self.data.tail())

        else:
            print("Please load dataset first........")

    def show_summary(self):
        if self.data is not None :
            print(self.data.info())

        else:
            print("Please load dataset first........")

    
    def drop_nullvalue(self):
        if self.data is not None :
            print("Null values are give below....")
            print(self.data.isna())

            print("\n")
            self.data.dropna()
            print("\nNull values are dropped successfully...........")

        else:
            print("Please load dataset first........")


    def visualizations(self):
        if self.data is not None :
            print("select an operations : \n")

            print("1. Bar plot")
            print("2. Histogram plot")
            print("3. Scatter plot")

            ch = int(input("Enter your choice : "))


            match ch :

                case 1 :
                    survival_counts = self.data['Survived'].value_counts()

                    plt.bar(['Not Survived', 'Survived'], survival_counts, color=['red', 'green'])

                    plt.title('Titanic Survival Count')
                    plt.xlabel('Survival')
                    plt.ylabel('Number of Passengers')
                    plt.show()



                case 2 :
                    plt.hist(self.data['Fare'], bins=30, color='lightgreen', edgecolor='black')
                    plt.title('Fare Distribution')
                    plt.xlabel('Fare')
                    plt.ylabel('Frequency')
                    plt.show()

                case 3 :
                    plt.scatter(self.data['Age'], self.data['Fare'], c="lightgreen", alpha=0.5)
                    plt.title('Age vs Fare (Colored by Survival)')
                    plt.xlabel('Age')
                    plt.ylabel('Fare')
                    plt.show()

                case _ :
                    print("Invalid choice Please try again..............")


        else:
            print("Please load dataset first........")



class main:

    da = DataAnalyzer()

    while True:
        print("====================================")

        print("Select an operations : ")

        print("====================================")

        print("1. Load dataset ")
        print("2. Show dataset ")
        print("3  Show dataset summary")
        print("4. Find and drop null vaues")
        print("5. Show data visualizations")
        print("6. Exit")
        
        choice = int(input("Enter your choice : "))


        match choice:

            case 1:
                da.load_dataset()

            case 2:
                da.show_dataset()

            case 3:
                da.show_summary()

            case 4:
                da.drop_nullvalue()

            case 5:
                da.visualizations()

            case 6:
                print("Exiting the program..........Goodbye.........")
                break

            case _:
                print("Invalid choice please try again...........")

main()