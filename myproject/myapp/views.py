from django.shortcuts import render
from .queries import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import  status as stus
from rest_framework.decorators import api_view
from rest_framework.exceptions import  APIException
import requests
import boto3
import secrets

s3 = boto3.client('s3',aws_access_key_id="tttttttttttttttttttttttttttt",
aws_secret_access_key= "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            


@api_view(['POST'])
def StudentList_f(requests):
    try:
        serializer = StudentList_s(data=requests.data)
        if serializer.is_valid():
            # bi=request.FILES.get("ProfileImage")
            # if bi:
            #     filee = request.FILES.get("ProfileImage")
            #     content_type = s3_content_type(filee)
            #     hex = secrets.token_hex(16)
            #     directory = 'zappas3bucket/Myfolder/{}{}'.format(hex,filee)
            #     s3.put_object(Bucket='zappas3bucket', Key=directory, Body=filee,ContentType=content_type)
            #     ProfileImagePath = "https://zappas3bucket.s3.ap-southeast-1.amazonaws.com/"+directory
            # else:
            #     ProfileImagePath= None
            Data = StudentList_q()
            if Data:
                    json_data = {
                        'status_code': 200,
                        'status': 'Success',
                        'data': replace_null_with_empty_string_many(Data),
                        'message': 'Data Found SuccessFully',
                    }
                    return Response(json_data, status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'count':'',
                    'data':[],
                    'message': 'Data Not Found',
                }
                return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
                }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
            }
        raise APIException(json_data, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)