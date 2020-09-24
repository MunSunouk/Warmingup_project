from django.shortcuts import render

# Create your views here.



def about(request):
    
    return render(request, 'app1/about.html')

def contact(request):
    
    return render(request, 'app1/contact.html')

def foods(request):
    
    ingredient = request.GET.get('ingredient')
    
    ingredient_data = {'ingredient':ingredient}
    
    return render(request, 'app1/foods.html', ingredient_data)


def index(request):
    
    return render(request, 'app1/index.html')

def lifestyle(request):
    
    return render(request, 'app1/lifestyle.html')

def single(request):
    
    return render(request, 'app1/single.html')

def test(request):#테스트용
    
    return render(request, 'app1/test.html')














#def index(request):
#    context = {'post':'testtesttest'}
#    return render(request, 'app1/index.html', context)
    

#def index(request):
#    context = {
#            'post':{
#                'author':'_person1',
#                'bodt':'kkkkkkk'
#            },
#            'numbers':[1,2,3],
#            'user':user('user',25)
#    }
#    return render(request, 'app1/index.html', context)
