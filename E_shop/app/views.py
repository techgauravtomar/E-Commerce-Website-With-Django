from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from app.models import Product,Categories,Filter,Color,Brand,Contact_us
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 



# Create your views here.

def homeone(request):
    return render(request, 'index.html')
def hometwo(request):
    product = Product.objects.filter(status='Publish')
    
    context={
        'product':product,
    }
    return render(request, 'index-2.html',context)
def aboutus(request):
    return render(request, 'about.html')
def page404(request):
    return render(request, '404.html')
def ordertracking(request):
    return render(request,'order-tracking.html')
def faq(request):
    return render(request,'faq.html')
def comingsoon(request):
    return render(request,'coming-soon.html')
# def cart(request):
#     return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def compare(request):
    return render(request,'compare.html')
def wishlist(request):
    return render(request,'wishlist.html')
def accountpage(request):
    return render(request,'my-account.html')
def HandleRegister(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        customer = User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('register')
        
    return render(request,'login.html')

def HandleLogin(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
          username=form.cleaned_data.get('username')
          password=form.cleaned_data.get('password')
          user  = authenticate(username=username,password=password)
          if user is not None:
              login(request,user)
              messages.info(request, f"You are now logged in as {username}.")
              return redirect('hometwo')
          else:
             messages.error(request,"Invalid username or password.")
        else:
           messages.error(request,"Invalid username or password.")  
    form = AuthenticationForm()
    return render(request,'login.html', context={"login_form":form}) 

def HandleLogout(request):
    logout(request)

    return redirect('hometwo')
       
     
    

def emptycart(request):
    return render(request,'empty-cart.html')
def thankyoupage(request):
    return render(request,'thank-you-page.html')
def shop_3_column(request):
    return render(request,'shop-3-column.html')
def shop_4_column(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains=query)
    
    context = {
        'product':product
       }
    
    return render(request,'shop-4-column.html',context)


def shop_left_sidebar(request):
    # product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    filter = Filter.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    
    CATID = request.GET.get('categories')
    PRICEID = request.GET.get('filter_price')
    BRANDID = request.GET.get('brand')
    COLORID = request.GET.get('color')
    
    ATOZID= request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    
    NEW_PRODUCTID=request.GET.get('NEW_PRODUCT')
    OLD_PRODUCTID=request.GET.get('OLD_PRODUCT')
    if CATID:
        product = Product.objects.filter(categories= CATID,status='Publish')
    elif PRICEID:
        product = Product.objects.filter(filter_price= PRICEID,status='Publish')
    elif BRANDID:
        product= Product.objects.filter(brand=BRANDID,status='Publish')
    elif COLORID:
        product= Product.objects.filter(color=COLORID,status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif NEW_PRODUCTID:
        product=Product.objects.filter(status='Publish',condition='NEW').order_by('-id')
    elif OLD_PRODUCTID:
        product=Product.objects.filter(status='Publish',condition='OLD').order_by('-id')
    else:
        product = Product.objects.filter(status='Publish').order_by('-id')
        
        
    context={
        'product':product,
        'categories':categories,
        'filter':filter,
        'color' : color,
        'brand' : brand,
    }
    return render(request,'shop-left-sidebar.html',context)
def shop_right_sidebar(request):
    return render(request,'shop-right-sidebar.html')
def shop_list_left_sidebar(request):
    return render(request,'shop-list-left-sidebar.html')
def shop_list_right_sidebar(request):
    return render(request,'shop-list-right-sidebar.html')
def single_product(request,id):
    prode = Product.objects.filter(id=id).first()
    
    context={
      'prode':prode
    }
    
    return render(request,'single-product.html',context)
def product_variable(request):
    return render(request,'single-product-variable.html')

def product_affiliate(request):
    return render(request,'single-product-affiliate.html')

def product_group(request):
    return render(request,'single-product-group.html')

def single_product_tabstyle_2(request):
    return render(request,'single-product-tabstyle-2.html')

def single_product_tabstyle_3(request):
    return render(request,'single-product-tabstyle-3.html')

def single_product_slider(request):
    return render(request,'single-product-slider.html')

def single_product_gallery_left(request):
    return render(request,'single-product-gallery-left.html')

def single_product_gallery_right(request):
    return render(request,'single-product-gallery-right.html')

def single_product_sticky_left(request):
    return render(request,'single-product-sticky-left.html')

def single_product_sticky_right(request):
    return render(request,'single-product-sticky-right.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        con=Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        # con.save()
        # return redirect('hometwo')
        
        subject = subject
        message = message
        eamil_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,eamil_from,['itsnew012gmail.com'])
            con.save()
            return redirect('hometwo')
        except:
            return redirect('contact')
    
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')

@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("hometwo")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")




@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")

@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")
    
@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'cart.html')

# @property
# def get_cart_deal_total(self):
#     orderitem = self.orderitem_set.all()
#     total = sum(item.get_deal_total for item in orderitem)
#     return total

# def get_deal_total(self):
#         price = self.product.deal_price
#         quantity = self.quantity
#         total = price*quantity
#         print(total)

#         return total
    
    

@property
def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total

@property
def get_cart_item(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total

