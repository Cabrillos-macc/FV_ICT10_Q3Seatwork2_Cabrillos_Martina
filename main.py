from pyscript import document

#This is a code that activates once the button named "team_info" has been clicked by the user. 
def team_info(e):
    regone = document.getElementById("reg_one").checked #The data for this variable comes from the registration of YES in my HTML.
    regtwo = document.getElementById("reg_two").checked #The data for this variable comes from the registration of NO in my HTML.
    medone = document.getElementById("med_one").checked #The data for this variable comes from the medical of YES in my HTML.
    medtwo = document.getElementById("med_two").checked #The data for this variable comes from the medical of NO in my HTML.

    grade = document.getElementById("grade").value #The data used for this variable is taken from the grade dropdown located in my HTML structure. 
    section = document.getElementById("section").value #The data used for this variable is taken from the section dropdown located in my HTML structure. 
    result = document.getElementById("result") #Data found here is in the div function with the id "result" found in my HTML structure. 

    #This allows pyscript to organize a specific grade and section to a specific intrams team. 
    team_mapping = {
        #Grade 7
        ("seven", "emerald"): "Red Bulldogs",
        ("seven", "ruby"): "Yellow Tigers",
        ("seven", "sapphire"): "Blue Bears",
        ("seven", "topaz"): "Green Hornets",

        #Grade 8
        ("eight", "emerald"): "Green Hornets",
        ("eight", "ruby"): "Blue Bears",
        ("eight", "sapphire"): "Red Bulldogs",
        ("eight", "topaz"): "Yellow Tigers",
        ("eight", "jade"): "Red Bulldogs",

        #Grade 9
        ("nine", "emerald"): "Red Bulldogs",
        ("nine", "ruby"): "Blue Bears",
        ("nine", "sapphire"): "Green Hornets",
        ("nine", "topaz"): "Yellow Tigers",
        ("nine", "jade"): "Red Bulldogs",

        #Grade 10
        ("ten", "emerald"): "Red Bulldogs",
        ("ten", "ruby"): "Green Hornets",
        ("ten", "sapphire"): "Yellow Tigers",
        ("ten", "topaz"): "Blue Bears",
    }

    #This connects the team name to the assigned/paired photo. 
    team_images = {
        "Yellow Tigers": "tiger.png",
        "Red Bulldogs": "bulldog.png",
        "Blue Bears": "bears.png",
        "Green Hornets": "hornet.png" }
    
    #This sets up the code to your assigned team and information based on your selection and data input on the form.
    team = team_mapping.get((grade, section)) 
    #This finds for the grade id and section id which holds the values needed to perform the code. 
    img_src = team_images.get(team, "schoollogo copy.png") 
    #This ensures that the assigned images to the teams will be done. 
    #Note: the "schoollogo copy.png" is for when the action "none" or when one area is not filled up by the user. This allows us to see the OBMC logo instead. 
    team_image_html = f"<br><img src='{img_src}' style='width:300px; margin-top:10px;'>"

    #if-elif-else
    #The conditions done by this code depends on the registration, medical, grade, and section. 
    #If ever user leaves all areas of the form as blank, this will proceed to the second elif condition. 
    #Once they have decided to fullfill what the second elif condition has given, this will still not give them their team as it will proceed to else condition IF first elif is not satisfied. 
    if regone and medone:
        result.innerHTML = f"You are part of <b>{team}</b>!!!!!! {team_image_html}" #This takes place when they have complied with all areas of the form.
    elif regtwo or medtwo:
        result.innerHTML = f""" ⚠️You are part of <b>{team}</b>. Sadly, you will not be permitted to join 
        the team fully until you comply with all requirements. Kindly double check what requirement/s you 
        lack and make the necessary appoitments to fullfill this. {team_image_html}""" #This takes place when they have placed "NO..." in one or both of the checkboxes.
    elif grade == "none" or section == "none":
        result.innerHTML = "🚨 Please select both grade and section. 🚨" #This takes place when they did not input the grade & section or if they left everything blank.
        return
    else:
        result.innerHTML = "Please answer all the requirements." #This takes place when they only answered grade & section and left the registration and medical as blank. 

#N-O-T-E:⬇︎
#If user fails to input the grade and sction BUT inputs in the registration and medical, 
#it would say "You are part of NONE" because this is meant to show you that you may have the requirements 
#but not having a class (grade & section) means you may not be part of OBMC (as an assumption). 
       