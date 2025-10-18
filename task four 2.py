Students = [ 
    {"Name" : "Amr" , "Grades" :[ 90 , 95 , 90] },
    {"Name" : "Yasser" , "Grades" :[ 80 , 85 , 90]} ,
    {"Name" : "Ahmed" , "Grades" :[ 85 , 90 , 95]}
]
for Student in Students : 
    Average = sum ( Student["Grades"]) / 3
    print(f"{Student ['Name']}  : {Average : .2f}")