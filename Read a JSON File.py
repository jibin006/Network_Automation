#Create a Function to Read a JSON File
import json

def get_api_keys(filename):
    
    try:
        with open(filename, "r") as file: #open the file
            data = json.load(file) #read and parsh to python directory
            return data.get("aws_access_key","key not found")
    except FileNotFoundError:
        return "file not found"
    except json.JSONDecodeError:
        return "invalid json format" 


api_keys = get_api_keys("config.json")
print("AWS API KEY: ", api_keys)   
