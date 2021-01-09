from firebase import firebase as fb
import datetime
import pytz
from creds import cred
firebase = fb.FirebaseApplication(cred.DB_URL)


def datefind():
    date = datetime.datetime.utcnow()
    date2 = date.replace(tzinfo=pytz.UTC)
    date = date2.astimezone(pytz.timezone("Asia/Kolkata"))
    date = str(date)
    date = date[0:10]
    today_date = int(date.replace("-", ""))
    return today_date


today_date = datefind()
date = datetime.datetime.utcnow()
date2 = date.replace(tzinfo=pytz.UTC)
date = date2.astimezone(pytz.timezone("Asia/Kolkata"))
date = str(date)
date = date[0:10]


def check(chatids):
    data = firebase.get("/users", chatids)
    rslt = data["status"]
    return rslt


def count(chatids):
    data = firebase.get("/users", chatids)
    rslt = data["count"]
    return rslt


def update(id, count, status):
    update_data = {"user_id": id, "status": status, "count": count, "date": today_date}
    firebase.put("/users", id, update_data)


def dt(chatids):
    rslt = ""
    try:
        data = firebase.get("/users", chatids)
        rslt = data["date"]
    except Exception:
        pass
    return rslt


def format_time(elapsed):
    """Formats elapsed seconds into a human readable format."""
    hours = int(elapsed / (60 * 60))
    minutes = int((elapsed % (60 * 60)) / 60)
    seconds = int(elapsed % 60)
    rval = ""
    if hours:
        rval += "{0}h".format(hours)
    if elapsed > 60:
        rval += "{0}m".format(minutes)
    rval += "{0}s".format(seconds)
    return rval


def updateFile():
    filess = firebase.get("/", "files")
    filess = filess["files"]
    filess += 1
    firebase.put("/", "files", {"files": filess})


def insertlog():
    subtrans_users = firebase.get("/users", "")
    files = firebase.get("/", "files")
    lst1 = []
    act = []
    for _, v in subtrans_users.items():
        lst1.append("u")
        if v["date"] == today_date:
            act.append("d")
    total_files = f"{files['files']}"
    total_users = f"{lst1.count('u')}"
    active_today = f"{act.count('d')}"

    data = {
        "active_users": active_today,
        "translated_files": total_files,
        "total_users": total_users,
    }
    firebase.put("/stats", date, data)


def logreturn():
    subtrans_users = firebase.get("/users", "")
    files = firebase.get("/", "files")
    total_files = f"{files['files']}"
    lst1 = []
    act = []
    for _, v in subtrans_users.items():
        lst1.append("u")
        if v["date"] == today_date:
            act.append("d")
    total_files = f"`Total subtitles translated` : **{total_files}**"
    total_users = f"`Total bot users`                          : **{lst1.count('u')}**"
    active_today = f"`Active users today`                   : **{act.count('d')}**"
    stato = f"\n{total_files}\n{total_users}\n{active_today}"
    return stato
