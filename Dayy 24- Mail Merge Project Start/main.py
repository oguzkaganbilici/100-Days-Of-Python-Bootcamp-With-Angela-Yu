        
with open("C:\\Users\\061885\\Desktop\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as f:
    text = f.read()
    
    
with open("C:\\Users\\061885\\Desktop\\Mail Merge Project Start\\Input\\Names\invited_names.txt") as f:
    names = f.read()
    
    
names = list(names.split("\n"))
for i in names:
    text2 = text.replace("[name]", i)
    with open(f"C:\\Users\\061885\\Desktop\\Mail Merge Project Start\\Output\\ReadyToSend\\{i}'s invate.txt", "w") as f:
        f.write(text2)
    