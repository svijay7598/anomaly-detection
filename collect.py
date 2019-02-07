from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import urllib

tweet_count=10

class listener(StreamListener):
      def on_data(self,data):
        file=open("twitter.csv","a") 
        file.write(data)
        file.close()
        print("Record Saved")
        return(True)
      def on_error(self,status):
          print(status)

auth = OAuthHandler("kbLi2diVgTFK2VAsyykH1IA78","HCEuFlmfLTZabsPyYpeIklcdBMiODftuTPXtKSYtlxZWmbZgV7")
auth.set_access_token("729897675353640964-lJtTXp671caNJdU4CTpGOdXhplF5dhg","hpydBsWeDUeyOUIzNji5eI7mpJPnGW917ZKSPO7Jbf124")
stream=Stream(auth,listener())
stream.filter(track = ["Corruption","Panama","nawaz shreef","Nab"])
