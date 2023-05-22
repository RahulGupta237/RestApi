data={
  "csv_file": {
    "columns": [
      "",
      "Employee Name",
      "Corporate Id",
      "Email Id",
      "Experience",
      "Designation",
      "Skills",
      "Technology",
      "Skype Id",
      "Contact No"
    ],
    "data_types": {
      "": [
        "empty"
      ],
      "Employee Name": [
        "string"
      ],
      "Corporate Id": [
        "numeric"
      ],
      "Email Id": [
        "string", "string"
      ],
      "Experience": [
        "string", "string"
      ],
      "Designation": [
        "string", "string"
      ],
      "Skills": [
        "string", "string", "string", "string"
      ],
      "Technology": [
        "string"
      ],
      "Skype Id": [
        "empty"
      ],
      "Contact No": [
        "numeric", "string"
      ]
    },
    "empty_count": 2,
    "null_count": 2,
    "rows_data": [
      {
        "": "",
        "Employee Name": "Rahul Gupta",
        "Corporate Id": "2498",
        "Email Id": "rahul.gupta1@kellton.com",
        "Experience": "1 years 6 months 1 days",
        "Designation": "Software Engineer",
        "Skills": "c, Django , Python, Python Programming, Django ORM, Python Django, DSA using C++, HTML, CSS , JAVASCRIPT , JQUERY , MYSQL, HTML,CSS,Bootstrap, Java,oops, Jira, Git, GitHub, Gitlab CI/CD",
        "Technology": "Python,Python",
        "Skype Id": "",
        "Contact No": "6302981453"
      }
    ],
    "column_data": {
      "": [
        ""
      ],
      "Employee Name": [
        "Rahul Gupta"
      ],
      "Corporate Id": [
        "2498"
      ],
      "Email Id": [
        "rahul.gupta1@kellton.com"
      ],
      "Experience": [
        "1 years 6 months 1 days"
      ],
      "Designation": [
        "Software Engineer"
      ],
      "Skills": [
        "c, Django , Python, Python Programming, Django ORM, Python Django, DSA using C++, HTML, CSS , JAVASCRIPT , JQUERY , MYSQL, HTML,CSS,Bootstrap, Java,oops, Jira, Git, GitHub, Gitlab CI/CD"
      ],
      "Technology": [
        "Python,Python"
      ],
      "Skype Id": [
        ""
      ],
      "Contact No": [
        "6302981453"
      ]
    }
  },
  "msg": "successfully read",
  "status": 200
}

for k,v in data["csv_file"]["data_types"].items():
    data["csv_file"]["data_types"][k]=data["csv_file"]["data_types"][k][0]
    print(k,v)
print("after modification")
for k,v in data["csv_file"].items():
   
    print(k,v)