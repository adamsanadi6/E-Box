from utility import *
from domain import *
from dao import *
from bo import *

def menu_details(ch):
    if(ch==1):
        productType = ProductType()
        print("Enter Name:")
        productType.set_name(input())
        print("Enter Description:")
        productType.set_description(input())
        i = ProductTypeDAO().add_product_type(productType)
        if(i!=False):
            print("Product Type Added Successfully")
        else:
            print("Product type already exists.")
    elif(ch==2):
        productCategory=ProductCategory()
        print("Enter Name:")
        productCategory.set_name(input())
        print("Enter Description:")
        productCategory.set_description(input());
        i = ProductCategoryDAO().add_product_category(productCategory);
        if(i):
            print("Product Category Added Successfully")
        else:
            print("Product category already exists.")
    elif(ch==3):
        brand=Brand()
        print("Enter Name:")
        brand.set_name(input())
        i = BrandDAO().add_brand(brand)
        if(i):
            print("Brand Added Successfully")
        else:
            print("Brand already exists.")
    elif(ch==4):
        product =Product()
        print("Enter Product Name:")
        product.set_name(input())
        print("Enter Product Color:")
        product.set_color(input())
        print("Enter Product Material:")
        product.set_material(input())
        print("Enter Product Price:")
        product.set_price(float(input()))
        print("Enter Product Quantity:")
        product.set_quantity(int(input()))
        print("Choose (Id) Brand:")
        BrandDAO().display_brand()
        brandId = int(input())
        product.set_brand(BrandDAO().obtain_brand_by_id(brandId))
        print("Choose (Id) from below product types:")
        ProductTypeDAO().display_product_type()
        productTypeId = int(input())
        product.set_product_type(ProductTypeDAO().obtain_product_type_by_id(productTypeId))
        print("Choose (Id) from below product category:")
        ProductCategoryDAO().display_product_category()
        productCategoryId = int(input())
        product.set_product_category(ProductCategoryDAO().obtain_product_category_by_id(productCategoryId))
        product.set_active(1)
        prodadd = ProductDAO().add_product(product)
        if(prodadd):
            print("Product Added Successfully")
        else:
            print("Product with the entered specification already exists. Product could not be added.")
    elif(ch==5):
        print("Enter Product Id:");
        product =(pdao.obtain_product_by_id(int(input())))
        if(product!=None):
            print("Enter Product Details:")
            print("Enter Name:")
            product.set_name(input())
            print("Enter Color:")
            product.set_color(input())
            print("Enter Material:")
            product.set_material(input())
            print("Enter price:")
            product.set_price(float(input()))
            print("Enter Quantity:")
            product.set_quantity(int(input()))
            print("Is the product active?(yes/no)")
            ans=input()
            if(ans.lower()==("yes")):
                product.set_active(1)
            else:
                product.set_active(0)
            if(pdao.update_product(product)):
                print("Product details updated successfully.")
        else:
            print("Product not found.")
    elif(ch==6):
        pdao.display_all_products();
    elif(ch==7):
        print("Enter Product Name:");
        product =(pdao.obtain_product_by_name(input()))
        if product!=None:
            pdao.display_product(product)
        else:
            print("Product not found.")
    elif(ch==8):
        print("Enter Quantity of order:")
        quantity=int(input())
        print("Available sales order items:")
        print("%-20s %-20s %-20s %-20s\n"%( "Id", "Product Name", "Quantity", "Unit Price"))
        for soi in (SalesOrderItemDAO().obtain_all_sales_order_items()):
            print(soi)
        taxAmount=0
        totalPrice=0
        sList=[]
        ans='yes'
        while(ans.lower()==("yes")):
            print("Enter sales Order id:")
            soiId=int(input())
            soi=SalesOrderItemDAO().obtain_sales_order_item_by_id(soiId);
            if(soi!=None):
                sList.append(soi)
                taxAmount=taxAmount+(0.18*quantity*float(soi.get_quantity())*float(soi.get_unit_price()))
                totalPrice=totalPrice+taxAmount+quantity*float(soi.get_quantity())*float(soi.get_unit_price())
            else:
                print("Invalid Sales Order Item Id.")
            print("Do you want to add another item details?(yes/no)")
            ans=input()
        print("Available Customer Details:")
        print("%-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id" , "Name", "Username", "Mobile Number", "Email-id", "Address"))
        for u in (UserDAO().obtain_users_by_role("Customer")):
            print(u)
        print("Choose customer id:")
        cid=int(input())
        cust=(UserDAO().obtain_users_by_id(cid))
        if(cust==None):
            print("Invalid Customer id.")
            return
        salesLead=None
        if(user.get_role().get_name().lower()==("store manager")):
            print("Available Sales lead Details:")
            print("%-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id" , "Name", "Username", "Mobile Number", "Email-id", "Address"))
            for u in (UserDAO().obtain_users_by_role("Sales Lead")):
                print(u)
            print("Choose Sales lead id:")
            sid=int(input())
            salesLead=(UserDAO().obtain_users_by_id(sid))
        else:
            salesLead=user
        if(salesLead==None):
            print("Invalid Sales lead id.")
            return
        print("Enter Sales Date(dd/MM/yyyy):")
        salesDate=datetime.datetime.strptime(input(),"%d/%m/%Y")
        so=SalesOrder(None, cust, quantity, totalPrice, taxAmount, salesLead, salesDate, sList)
        b=(SalesOrderDAO().add_sales_order(so))
        if(b):
            print("Sales Order details added successfully.")
    elif(ch==9):
        print("Sales Order Details:")
        SalesOrderDAO().display_sales_order()
    elif(ch==10):
        print("Enter Quantity of order:")
        pquantity=int(input())
        print("Available Purchase order items:")
        print("%-20s %-20s %-20s %-20s\n"%("Id", "Product Name", "Quantity", "Unit Price"));
        for poi in PurchaseOrderItemDAO().obtain_all_purchase_order_items():
            print(poi)
        ptaxAmount=(0)
        ptotalPrice=(0)
        pList=[]
        ans='yes'
        while(ans.lower()==("yes")):
            print("Enter Product Order id:")
            poiId=int(input())
            poi=PurchaseOrderItemDAO().obtain_purchase_order_item_by_id(poiId)
            if(poi!=None):
                pList.append(poi)
                ptaxAmount=ptaxAmount+0.18*pquantity*float(poi.get_quantity())*float(poi.get_unit_price())
                ptotalPrice=ptotalPrice+ptaxAmount+pquantity*float(poi.get_quantity())*float(poi.get_unit_price())
            else:
                print("Invalid Product Order Item Id.")
            print("Do you want to add another item details?(yes/no)")
            ans=input()
        print("Available Supplier Details:")
        print("%-20s %-20s %-20s %-20s %-20s\n"%("Id" , "Name", "Mobile Number", "Email-id", "Address"))
        for s in SupplierDAO().obtain_all_suppliers():
            print(s)
        print("Choose Supplier id:")
        sid=int(input())
        supplier=(SupplierDAO().obtain_supplier_by_id(sid))
        if(supplier==None):
            print("Invalid Supplier id.")
            return
        print("Available Product lead Details:")
        print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s\n"%("Id" , "Name", "Username", "Mobile Number", "Email-id", "Address","Role"))
        for u in UserDAO().obtain_users_by_role("Product Lead"):
            print(u)
        print("Choose Product lead id:")
        productLeadid=int(input())
        prodLead=(UserDAO().obtain_users_by_id(productLeadid))
        if(prodLead==None):
            print("Invalid Product lead id.")
            return
        print("Enter Purchase Date(dd/MM/yyyy):")
        purchaseDate=datetime.datetime.strptime(input(),"%d/%m/%Y")
        po=PurchaseOrder(sid, supplier, pquantity, ptotalPrice, ptaxAmount, prodLead, purchaseDate, pList);
        b=(PurchaseOrderDAO().add_purchase_order(po))
        if(b):
            print("Purchase Order details added successfully.")
    


print("Welcome to Best Buy Electronix!")
choice = 0
userDAO=UserDAO()
roleDAO =RoleDAO()
pdao=ProductDAO()
while(True):
    print("1.Login\n2.Exit\nChoose from the above menu")
    choice=int(input())
    if(choice==1):
        print("Enter Username")
        username = input()
        print("Enter Password")
        password = input()
        user = userDAO.validate_login(username,password)
        if(user == None):
            print("Invalid username or password")
        elif(user.get_role().get_name().lower()=="store manager" or user.get_role().get_name().lower()=="product lead" or user.get_role().get_name()=="sales lead"):
            ch = 0
            while(True):
                print("Menu\n1.Add Product Type\n2.Add Product Category\n3.Add Brand\n4.Add Product\n5.Edit Product\n6.Display Products\n7.Search Product\n8.Create Sales Order\n9.Display Sales Order\n10.Create Purchase Order\n11.Logout")
                ch=int(input())
                if ch>=1 and ch <=10:
                    menu_details(ch)
                elif(ch==11):
                    print("Successfully logged out!")
                    break
                else:
                    print("Invalid Choice")
                    break
        else:
            print("Sorry. You don't have permission to access.")
    elif(choice==2):
        print("Thank you!")
        break
    else:
        print("Invalid Choice")

