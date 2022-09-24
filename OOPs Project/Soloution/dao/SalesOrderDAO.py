from bo import *
from domain import *
from utility import *
from dao import UserDAO,SalesOrderItemDAO

class SalesOrderDAO:

    def obtain_all_salesOrder(self):
        itemList = []
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from sales_order")
        data=mycursor.fetchall()
        userDAO = UserDAO.UserDAO()
        soidao = SalesOrderItemDAO.SalesOrderItemDAO()
        for x in data:
            customer=userDAO.obtain_users_by_id(x[1])
            salesLead=userDAO.obtain_users_by_id(x[5])
            sList=[]
            mycursor.execute("select * from sales_order_item where sales_order_id='"+str(x[0])+"'")
            for y in mycursor:
                sList.append(soidao.obtain_sales_order_item_by_id(x[0]))
            itemList.append(SalesOrder(x[0],customer,x[2],x[3],x[4],salesLead,x[6],sList))
        return itemList
         

    def add_sales_order(self,salesOrder):
        dbObj = DBConnection()
        mydb = dbObj.get_connection()
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("insert into sales_order(customer_id,quantity,total_price,tax_amount,sales_lead_id,sale_date) values('"+str(salesOrder.get_customer().get_id())+"','"+str(salesOrder.get_quantity())+"','"+str(salesOrder.get_total_price())+"','"+str(salesOrder.get_tax_amount())+"','"+str(salesOrder.get_sales_lead().get_id())+"','"+str(salesOrder.get_sale_date())+"')")
        mydb.commit()
        mycursor.execute("select max(id) from sales_order")
        sid=-1
        for x in mycursor:
            sid=x
        for i in salesOrder.get_item_list():
            mycursor.execute("update sales_order_item set sales_order_id='"+str(sid[0])+"' where id='"+str(i.get_id())+"'")
            #mycursor.execute("insert into sales_order_item(product_id,quantity,unit_price,sales_order_id) values('"+str(i.get_id())+"','"+str(i.get_quantity())+"','"+str(i.get_unit_price())+"','"+str(sid[0])+"')")
        mydb.commit()
        return True
        
    def display_sales_order(self):
        sList = self.obtain_all_salesOrder()
        print("%-20s %-20s %-20s %-20s %-20s %-20s\n"%("User Name", "Order Quantity","Total Price","Tax Amount","Sales Lead","Sale Date"))
        for s in sList:
            print(s)
