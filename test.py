from RequestModule.main import AppRequest
import unittest




class Test(unittest.TestCase):


    def test_RequestModule(self):

        app=AppRequest()
        result=app.RequestStockData("AAPL")
        print(result)
        self.assertTrue(result == True,"The response from the api request must return a dataclass object")


        result=app.SaveData("AAPL")
        print(result)
        self.assertTrue(result == True, "It is not possible to save the reponse data")

        result=app.GetCsvFilesList()
        print(result)
        self.assertTrue(type(result) is list,"It is not possible to get the files that containt the downloaded data")


        result=app.GetData("AAPL.txt")
        print(result)
        self.assertTrue(type(result) is list,"It is not possible to retrieve the data" )


if __name__ == "__main__":

    unittest.main()