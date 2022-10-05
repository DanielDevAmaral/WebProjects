with open("C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\txt\\hr_system.txt") as medical:
    for lines in medical:
        lines_separed = lines.split()
        name = lines_separed[0]
        id_number = lines_separed[1]
        job_title = lines_separed[2]
        salary = float(lines_separed[3])

        if lines_separed[2] == "Engineer":
            month_salary = salary/24
            new_salary = month_salary + 1000
            print(f"{name} (ID: {id_number}), {job_title} - ${new_salary}")
        else:
            print(f"{name} (ID: {id_number}), {job_title} - ${salary/24}")