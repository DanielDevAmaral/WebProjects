with open("C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\txt\\books_and_chapters.txt") as scriptures:
    
    larger = 0
    larger_name = ""
    
    for parts in scriptures:
       
        separed = parts.split(":")

        book = separed[0]
        chapter = int(separed[1])
        scripture = separed[2]    

        if scripture == "Book of Mormon":
            if larger < chapter:
                larger = chapter
                larger_name = book


        #if larger < chapter:
         #   larger = chapter
          #  larger_name = book

    print(f"{larger} --- {larger_name}")