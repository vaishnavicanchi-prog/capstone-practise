from fastapi import FastAPI
proj=FastAPI()
@proj.get("/")
def prac():
    return("Hi.....")
