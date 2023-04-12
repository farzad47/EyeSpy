# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, Query, Request, status, Response, Header, Body
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from loguru import logger
from dotenv import load_dotenv
from os.path import join, dirname

import traceback
import os

logger.add(".\API Backend\log\EveSpy_API.log", rotation="100MB", retention="1 year")

dot_env_path = join(dirname(__file__), '.env')
load_dotenv(dot_env_path)
APP_ENV = os.environ.get("APP_ENV")

app = FastAPI(
    title='EyeSpy',
    description='Control API',
    version='0.1.1'
    #docs_url=None, 
    #redoc_url=None
)


class rt_building(BaseModel):
    building_id : int = Field(..., title="building_id", description="building id for new building", example= 123)

class rt_resident(BaseModel):
    resident_id : int = Field(..., title="resident_id", description="resident id for new resident", example= 123)

class rt_session(BaseModel):
    session_token : str = Field(..., title="session_token", description="session token", example= "ABC123")

class ACK(BaseModel):
    status : str = Field(..., title="status", description="status of request", example= "Failure")

class BuildingInfo(BaseModel):
    name : str = Field(...,  title="name", description="name of person", example= "farzad")
    isalert : bool = Field(..., title="isalert", description="alert on/off", example= True)
    alerttype : str = Field(..., title="alerttype", description="type of alert", example= "all alert")
    alertEmail : str = Field(...,  title="alertEmail", description="Email for alerts", example= "farzad@gmail.com")

class ResidentInfo(BaseModel):
    name : str = Field(...,  title="name", description="name of person", example= "farzad")
    building_id : int = Field(..., title="building_id", description="Id of Building", example= 123456)
    appartment_no : int = Field(..., title="appartment_no", description="no of appartment", example= 420)
    images : list[str]

class rt_BuildingInfo(BaseModel):
    list_building : list[BuildingInfo]

class rt_ResidentInfo(BaseModel):
    list_resident : list[ResidentInfo]

@app.post('/api/SecurityCheck', summary="Security Check Endpoint", response_model=ACK)
def SecurityCheck(
        building_id: str = Header(..., description= "Id of Building"),
        face_image: str = Header(..., description= "image of the face")     
        ):
    return JSONResponse(status_code=200,content={"Access Granted"})
    
@app.get('/api/get_session', summary="get the access token for the admin functions",response_model=rt_session)
def get_session(       
        admin_user: str = Header(..., description= "Id of Building"),
        adminm_password: str = Header(..., description= "API Access Token")
        ):
    return JSONResponse(status_code=200,content={"session_token":"ABC123"})

@app.put('/admin/Add_resident', summary="add new people to an building", response_model=rt_resident)
def Add_resident(
        User: ResidentInfo,
        session_token: str = Header(..., description= "token for the admin functions")
        ):
    return JSONResponse(status_code=200,content={"resident_id":123})

@app.delete("/admin/remove_resident", summary="remove people from building", response_model=ACK)
def remove_resident(
        session_token: str = Header(..., description= "token for the admin functions"),
        building_id : int = Header(..., description= "Id of Building"),
        resident_id : int = Header(..., description= "Id of Resident")
        ):
    return JSONResponse(status_code=200,content={"ACK":"Deleted"})

@app.put('/admin/Add_building', summary="add new building", response_model=rt_building)
def Add_resident(
        BuildingInfo: BuildingInfo ,
        session_token: str = Header(..., description= "token for the admin functions")
        ):
    return JSONResponse(status_code=200,content={"building id":123})

@app.get('/admin/list_building', summary="list of all building",response_model=rt_BuildingInfo)
def list_building(
        session_token: str = Header(..., description= "token for the admin functions"),
        ):
    return JSONResponse(status_code=200,content= {"list_building":[{'name':'abc','id':123},{'name':'xyz','id':456}]} )

@app.get('/admin/list_resident', summary="list of all resident",response_model=rt_ResidentInfo)
def list_resident(
        session_token: str = Header(..., description= "token for the admin functions"),
        building_id : int = Header(..., description= "Id of Building")
        ):
    return JSONResponse(status_code=200,content= {"list_resident":[{'name':'abc','build_id':123,'appart_id':69},{'name':'xyz','build_id':456,'appart_id':96}]} )

@app.get('/my-endpoint')
@app.head('/my-endpoint')
async def my_endpoint(request: Request):
    return {'status': 1, 'message': request.client.host}


if __name__ == "__main__":

    if APP_ENV == 'local' :
        uvicorn.run(app, host="127.0.0.1", port=8000)
    elif APP_ENV == 'testing' :
        uvicorn.run(app, host="0.0.0.0", port=8001)
    else:
        uvicorn.run(app, host="0.0.0.0", port=80)
