from django.db import connection,connections
import os
def dictfetchall(cursor = ''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor = ''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))

def replace_null_with_empty_string_many(result):
    for dictionary in result:
        for i in dictionary:
            if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
                dictionary[i] = ''
            elif type(dictionary[i]) == int:
                dictionary[i] = str(dictionary[i])              
    return result

def replace_null_with_empty_string(dictionary):
    for i in dictionary:
        if dictionary[i] == 'NULL' or dictionary[i] == None or dictionary[i] == 'None' or dictionary[i] == 'null':
            dictionary[i] = ''
        elif type(dictionary[i]) == int:
                dictionary[i] = str(dictionary[i])
    return dictionary



def s3_content_type(file):
    try:
        result = os.path.splitext(file.name)
        print('Extension:', result[1])
        Extension = result[1].replace(".","")
        switcher = {
        'png': "image/png",
        'gif': "image/gif",
        'html': "text/html",
        'htmls': "text/html",
        'htm': "text/html",
        'jpg': "image/jpeg",
        'jpeg': "image/jpeg",
        'jfif': "image/jpeg",
        'pdf': "application/pdf",
        'webp': "image/webp"
        }
        return switcher.get(Extension, "nothing")
    except Exception as e:
        print(e)


def StudentList_q():
    with connections['Mydb'].cursor() as cursor:
        resp = cursor.execute(""" Select Id, StudentUUID, first_name, last_name, DOB, gender, email, phone, ProfileImage, 
        address, city, state, zip_code, country, nationality, guardian_name, guardian_relationship, guardian_phone, 
        admission_date, IsDeleted from LocalDb.Student where IsDeleted =0 """)
        if resp and cursor.rowcount:
            resp = dictfetchall(cursor)
        else:
            resp = None
    return resp

# def AdminClubAdvantagesList_q(pageNumber,content):
#     with connections["LucknowGolfClub"].cursor() as cursor:
#         resp = cursor.execute(f""" SELECT ID as KeyIndex, OurAdvantageUUID, Title, Description, Logo, IsDeleted, IsLive, 
#         CreatedAt, CreatedBy, UpdatedAt, UpdatedBy FROM LucknowGolfClub.ClubAdvantages 
#         WHERE IsDeleted = 0 order by ID desc limit {pageNumber}, {content} ; """)
#         if resp and cursor.rowcount:
#             resp = dictfetchall(cursor)
#         else:
#             resp = None
#     return resp