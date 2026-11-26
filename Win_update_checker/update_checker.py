import win32com.client

session = win32com.client.Dispatch("Microsoft.Update.Session")
searcher = session.CreateUpdateSearcher()

print("Searching for updates that are not installed...")


results = searcher.Search("IsInstalled=0") 
print("Available updates: ", results.Updates.Count)


for Update in results.Updates:
    print(Update.Title)
