import os,uuid,asyncio
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app=FastAPI(title="Windows VM Cloud API")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])
vms={}
class VMRequest(BaseModel): image:str="windows";cpu:int=2;memory_mb:int=4096;disk_gb:int=32
@app.post("/vms")
async def create_vm(req:VMRequest):
    if req.image!="windows":raise HTTPException(400,"Imagem não suportada")
    i=str(uuid.uuid4());vms[i]={"id":i,"state":"provisioning","progress":5,"console_url":None};asyncio.create_task(provision(i));return vms[i]
@app.get("/vms/{i}")
async def get_vm(i:str):
    if i not in vms:raise HTTPException(404,"VM não encontrada")
    return vms[i]
@app.post("/vms/{i}/stop")
async def stop_vm(i:str):
    if i not in vms:raise HTTPException(404,"VM não encontrada")
    vms[i]["state"]="stopped";vms[i]["progress"]=100
    return vms[i]
async def provision(i):
    for p in [15,30,50,70,90]:
        await asyncio.sleep(1)
        if i not in vms or vms[i]["state"]=="stopped":return
        vms[i]["progress"]=p
    vms[i]["state"]="running";vms[i]["console_url"]=os.getenv("CONSOLE_URL","http://localhost:6080/vnc.html")
