Contacts = {
    "Amr" : "01224596090" ,
    "Yasser" : "01220924712",
    "Ahmed" : " 01282929281"
}
Search = input ("Enter The Name That You Want To Search : ").title()
if Search in Contacts :
    print ("Number" , Search , "is" , Contacts [Search] )
else :
    print (f"{Search} isn't there")    