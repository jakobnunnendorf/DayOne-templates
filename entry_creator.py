def create_entry(entry_title, entry_date, entry_time, entry_path):
    # create template according to this format:
    #	Date:	28 January 2023 at 1:48:56 PM SGT
	#   Location:	Yale NUS College, Singapore

    # Example Header
    # Lorem ipsum
    first_line = "    Date:    " + entry_date + " at " + entry_time + "\n"
    second_line = "    Location:	" + "\n" + "\n"
    body = entry_title + "\n\nTLDR:\n\nResults:\n\nComments:\n\n"
    entry_template = first_line + second_line + body
    
    # create the txt file:
    text_file = open(entry_path+"/"+entry_title+".txt", "w")

    #write string to file
    text_file.write(entry_template)
    
    #close file
    text_file.close()

# test
#create_entry("TB1", "28 January 2023", "1:48:56 PM SGT", "/Users/jakobnunnendorf/Github/DayOne-templates/test")