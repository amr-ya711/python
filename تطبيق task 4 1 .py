Contacts = {
    "Amr" : "01224596090" ,
    "Yasser" : "01220924712",
    "Ahmed" : " 01282929281"
}
Search = input ("Enter The Name That You Want To Search : ")

found = False

for Contact in Contacts:
    if Contact.title() ==  Search.title() :
        print ("Number" , Contact , "is" , Contacts [Contact] )
        found = True 
        break 
else :
    print (f"{Search} isn't there") 