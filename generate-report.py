import pandas as pd
import os

def getUniqueTeachers(df:pd.DataFrame):
    teacher_li = []
    for index, row in df.iterrows():
        teacher_li.append(row['Teacher Name'].strip().lower())

    unique_teacher_li = list(dict.fromkeys(teacher_li))
    print(unique_teacher_li)
    return unique_teacher_li

def generateReports(df:pd.DataFrame, teacher_li:list):
    for teacher in teacher_li:
        teacher_details = {
            "Student Name": [],
            "Subject": [],
            "Year Group": [],
            "Reason for Report": [],
            "Comment": []
        }
        for index, row in df.iterrows():
            if row['Teacher Name'].strip().lower() == teacher:
                teacher_details["Student Name"].append(row["Student Name"])
                teacher_details["Subject"].append(row["Subject"])
                teacher_details["Year Group"].append(row["Year"])
                if row["Reason for Report"] == "Other (please specify)":
                    teacher_details["Reason for Report"].append(row["Other"])
                else:
                    teacher_details["Reason for Report"].append(row["Reason for Report"])
                teacher_details["Comment"].append(row["Any other comment"])
                
                if row["Finished?"] == "Enter Another Report":
                    for i in range(1, 10):
                        teacher_details["Student Name"].append(row[f"Student Name.{i}"])
                        teacher_details["Subject"].append(row[f"Subject.{i}"])
                        teacher_details["Year Group"].append(row[f"Year.{i}"])
                        if row[f"Reason for Report.{i}"] == "Other (please specify)":
                            teacher_details["Reason for Report"].append(row[f"Other.{i}"])
                        else:
                            teacher_details["Reason for Report"].append(row[f"Reason for Report.{i}"])
                        teacher_details["Comment"].append(row[f"Any other comment.{i}"])

                        if i != 9:
                            if row[f"Finished?.{i}"] == "Enter Another Report":
                                continue
                            else:
                                break
                        else:
                            break

        teacher_df = pd.DataFrame.from_dict(teacher_details)
        teacher_df.to_excel("./Results/"+teacher+".xlsx")

def main():
    df = pd.read_csv("./Data/jan.csv", header=0)
    os.makedirs("./Results/", exist_ok=True)
    print(df.head(5))

    teacher_li = getUniqueTeachers(df)

    generateReports(df, teacher_li)

if __name__ == "__main__":
    main()