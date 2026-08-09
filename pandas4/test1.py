#Level Two

import pandas as pd

data = {
    "server_name" : ["server1","server2","server3"],
    "cpu" : [45, 89, 94],
    "memory" : [50,70,80],
    "status" : ["running", "failed", "active"],
    "location" : ["us-east-1", "Banglore", "us-west-2"]
}


df = pd.DataFrame(data)

print(df[(df["cpu"]>70) & (df["memory"]>60)])

print(df[(df["cpu"]>80) | (df["cpu"]>80)])

print(df[(df["status"]=="running")& (df["location"]=="us-east-1")])