"# -Intelligence_Task_Manager" 


רקע הפרויקט ומטרתו:
הפרויקט הוא בעצם מערכת לניהול משימות לחיילים.
מה שאנחנו עושים זה לבנות טבלאות אחת agents והשנייה היא missions.
בתוך הטבלות היו הנתונים שאנחנו צרכים.
אנחנו נצטרך גם לבנות classes שהם יעבדו עם הטבלות.
וכמובן אנחנו נצטרך גם לבנות endpoints , בשביל שהמשתמש יכול להזין את הפרטים שהוא רוצה.




מבנה תיקיות:
intelligence-task-manager/
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore





מבנה הטבלאות:
agents:
id | name | specialty | is_active | completed_missions | failed_missions | agent_rank



missions:
id | title | description | location | difficulty | importance | status | level_risk | assigned_agent_id




הסבר על מחלקות:
DB_connection:
המחלקה הזאת מחברת אותנו ל mysql.
connection_get() -> המתודה הזאת מחזירה חיבור פעיל ל MySQL.

database_create() -> המתודה הזאת יוצרת database במידה ולא קיים.

tables_create() -> המתודה הזאת יוצרת את הטבלאות agents, missions במידה ולא קיים.



AgentDB:
במחלקה הזאת אנחנו יוצרים מתדות לטבלה של agents.
agent_create(data) -> המתודה יוצרת סוכן חדש מחזירה את האובייקט של הסוכן.

agents_all_get() -> המתודה מחזירה את כל החיילים שבטבלה.

get_agent_by_id(id) -> המתודה מחזירה סוכן לפי id במידה וה id לא קיים המערכת תחזיר None.

update_agent(id, data) -> המתודה מעדכנת את כל החייל חוץ מ id.

agent_deactivate(id) -> המתודה מגדירה מצב סוכן לא פעיל.

completed_increment(id) -> המתודה מעדכנת את כמות המשימות שהשלמו.

failed_increment(id) -> המתודה מעדכנת את כמות המשימות שלא השלמו.

get_agent_performance(id) -> המתודה מחזירה מילון עם המפתחות: completed, failed, total, success_rate.

count_agents_actice() -> המתודה מחזירה את כמות הסוכנים הפעילים.






MissionDB:
במחלקה הזאת אנחנו יוצרים מתדות לטבלה של missions.
create_mission(data) -> המתודה יוצרת משימה חדשה ומחזירה את אובייקט.

get_all_missions() -> המתודה מחזירה את כל המשימות.

get_mission_by_id(id) -> המתודה מחזירה משימה אחת לפי id, במידה ואין היא מחזירה None.

assign_mission(m_id, a_id) -> המתודה משייכת משימה לסוכן.

update_mission_status(id, status) -> המתודה משנה סטטוס לאותו id שהמשתמש רצה.

get_open_missions_by_agent(id) -> המתודה מחזירה לי רשימה של משימות שהם ASSIGNED/IN_PROGRESS של אותו סוכן.

count_all_mission() -> סופרת כמה משימות יש בסך הכל.

count_by_status(status) -> המתודה סופרת לפי סטטוס מסויים.

count_open_missions() -> המתודה סופרת כמה משימות פתוחות יש.

count_critical_missions() -> המתודה סופרת כמה משימות במצב קריטי.

get_top_agent() -> המתודה מחזירה את הסוכן עם completed_missions הכי גבוה.






חוקי המערכת:

1. agent_rank mast to be one of Junior/Senior/Commander. else error.

2. difficulty and importance חייבים להיות בין 1-10 אירת יזרק שגיאה.

3. level_risk מחשב אוטומטית את בעת יצירת המשימה. זה שדה שהמשתמש לא מכניס.

4. סוכן שהשדה is_active=False הוא לא יכול לקבל משימה.

5. סוכן לא יכול לקבל יותר מ 3 משימות פתחות במקביל .

6. level_risk=CRITICAL רק סוכן בדרגת Commander יכול לקבל משימה כזאת.

7. ניתן לשייך משימה רק אם השדה status=NEW ולאחר שיוך status=ASSIGNED.

8. ניתן להתחיל את המשימה רק השדה status=ASSIGNED ולאחר מכן status=PROGRESS_IN.

9. ניתן לסיים רק משימה PROGRESS_IN ולשנות ל completed or failed.

10. ניתן לבטל משימה רק אם היא NEW or ASSIGNED, אחרת שגיאה.




הוראות הרצה:
בשיבל להפעיל את הדוקר יש להריץ
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234  -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0

ואחרי זה הSQL צריך להתחבר אליו