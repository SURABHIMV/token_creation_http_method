from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.serializers import CompanySerializer
from myapp.serializers import userSerializer
# from myapp.serializers import userSerializer
from myapp.models import Company,reg_user
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
###################################
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from myapp.serializers import UserRegister
from rest_framework.views import APIView



# Create your views here.

class Register(APIView):

    def post(self,request,format=None):
        
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors

        return Response(data)



class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # Your authentication logic here
        user = authenticate(username=request.data['username'], password=request.data['password'],email=request.data['email'])
        cmp=reg_user.objects.create(username=request.data["username"],email=request.data["email"])
        print(cmp)
        serializer_class=userSerializer(cmp)
        print('$$$$$$$$$',user.password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            print('jjjjjjjjjjj',token)
            context={'data':serializer_class.data,'taken':token.key}

            return Response(context)
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

class companyapiview(APIView):
    permission_classes = [IsAuthenticated]
    ## to view only id data
    # def get(self,request,pk):
    #     pt=Company.objects.get(id=pk) 
    #     serializer_class=CompanySerializer(pt)
    #     return Response({"message":"company data","list":serializer_class.data})
    
    ## to view all the data in the database 

    def get(self,request):
        cmpy=  Company.objects.all()
        serializer_class=CompanySerializer(cmpy,many=True)
        print("sbdfb",serializer_class)
        print('bbbbbbbbbbbbbbb',request.user)
        return Response({"status":200,"message":"company list","list":serializer_class.data})
    
    def post(self,request):
        cmp=Company.objects.create(name=request.data["name"],location=request.data["location"],about=request.data["about"],type=request.data["type"])
        # allcompany=company.objects.filter(id=company.id).values()
        serializer_class=CompanySerializer(cmp)
        return Response({"message":"company list","list":serializer_class.data})
    
    def delete(self,request,pk):
        dlt=Company.objects.get(id=pk) 
        dlt.delete()
        return Response({"message":"company deleted succefuly"})
    
    def patch(self,request,pk):
        pt=Company.objects.get(id=pk) 
        serializer_class=CompanySerializer(pt, data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'partial data is updated'})
        return Response( serializer_class.errors)
    
    def put(self,request,pk):
        pt=Company.objects.get(id=pk) 
        serializer_class=CompanySerializer(pt, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'full data is updated'})
        return Response( serializer_class.errors)
    
    # def get(self,request,pk):
    #     pt=Company.objects.get(id=pk) 
    #     serializer_class=CompanySerializer(pt, data=request.data)
    #     return Response({"message":"company data","list":serializer_class.data})





    
    
                                                     


