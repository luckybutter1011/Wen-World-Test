import os
from datetime import datetime
from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": ["https://telegram-1-Triend.replit.app"]}})

# Firebase credentials and initialization
firebase_creds = {
    "type": "service_account",
    "project_id": "wen-world",
    "private_key_id": "b68e2d114e709af3e47027261095f1f47d90e34f",
    "private_key":
    "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDAP2fa/QjzYcwM\nG7NqBPhKzNVQFleCWg/wBEjRBB7fp40Ge0ZOReQX9iZmMQ4amns7V7Z8nTiP1OFV\ncjam6wcJd1e5h9jphd1SCaLSFh0XV0OqrKOtT0wQ4f/WoiH6bT0/K5bQy5nUeHM0\n6gdxHuc6kHP7sIwVhgZXvo1bSZam8dAjCh5lf00h2kOb39p2U32XYX6djLVCPagf\nXln4ryuJb5QrWUe6lPQqZTlVi8CAbYLK9maQZNTDqUWwbisR58hg/3NL6tlEbcZc\n2SkBRB9lZ4ucoRYAf025XhuKwEXCn47C3jeAFWPNSFJP1iZDUVc51kDon+1mqwSn\nMisWeu3BAgMBAAECggEAEpuQf9USCAylOrQhBNf/owMkenX5zmIikhwNYuhqh0H+\nbRbYJ+dX5oHVbFAUig/9xtv8i8nj7vgElMf98OC6yPhw2JevhRrciyjnm5IMYB/6\n1WA/D3KnbX2Sd8HbAWmQDgyNXR731WWQhm9IfR3Sn7aE+Lg5Nt7Gv7jFPIVo5uDs\npAjZioYHa3/p2NszcrF7vZjRp0IVsjCx7nMecHhT1b42bqEw1Rkkj5c1xrhxDNd4\nqd820j2KIXnoTlZVZCW3KhxYuu+feEkglxhBODsoB/+yLdXq0wrBERGtX1YLEIiq\nV0JWuaH8JdXR080e/nSQ3XJ4O0s8pNsJEtL3fX7MyQKBgQDfktzPzHJhb8B2eUkD\nzz5tajOsjGkB0t6to7FvjJpNjiy+aiYCctfS8J/A7u5O1dHUlhm3XBq54cZf5NLA\nDin3PK2TYxunaV5571hs3Sx/EP/GS7kuitQng0YqgtNoN9IwzQIpWsu3bKGtfMjV\n0a98jBjrTMIwL3jI+uaSJ4qG/wKBgQDcIW4ccg5EqYuHGPgBtGqabItYZmJ8PfU1\n3quB95RNokjhqp2KLAca5nurOhsEtCNooUsug2b1f1UJdhq+L2PtuMz8AAp6C5Jz\nkL23MqH1690tMBP5gEJZr/8XKwhmW28A0ZdeIpGSctAlEYOHdF4N7pSPP6hcwgLv\n6h8A2SlLPwKBgDyiafx5aDQAyOPYtPKxjC7EdMtBMWFrPTU+herI6ThLbNsfkrtr\nRhlRZSJAKqV62/OZ2dOeySjMkK6FMpsfvEXvUOv+HwviSdssDIFJ4r17cMLo2opC\n4JLuyWLSJF/Jc9oEX6ezljhi395bT2Sd/8f5fvCh2rCSz2FCmrHcw3clAoGAb+rv\nOLckWfR5Y+5l6Tf5GxoknoUvfUti6EiVmjZtyCrCMzmzbxSDaEHWjm+0XOfZONEI\nkFVue1KJwY2yew9NFwfl8Bl1Oie4BdmJGyM7BPUuNlNDVI7JLSA16WmPk7rY7Omi\ns9GPgY2uFaqZ3LxlNWAfV9VdnAtnwuKdcKj4PbECgYByQt3npIHVUSiFwlCJ/1Ke\nE9xduDqH5vkgKgI1+FD2uNFSk4vNhwVgNrk0Tm3ajXmhuKz1EXxy7GHldDGmhXrZ\n9d0hZ/lXJT+48Po9sZR2vdML9ZoOfx7c97/RrN3M0D8h5rQydpyJtMmF5POTiSg2\nHIyWf/Hk58W4onQzIg9Lmw==\n-----END PRIVATE KEY-----\n",
    "client_email":
    "firebase-adminsdk-2kzlg@wen-world.iam.gserviceaccount.com",
    "client_id": "117463761929069557825",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":
    "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url":
    "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2kzlg@wen-world.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com",
}

cred = credentials.Certificate(firebase_creds)
firebase_admin.initialize_app(cred)
db = firestore.client()


# Serve the game HTML
@app.route("/")
def index():
    return render_template("index.html")


# Serve the leaderboard HTML
@app.route("/leaderboard")
def leaderboard_page():
    return render_template("leaderboard.html")


# Serve the tasks HTML
@app.route("/tasks")
def tasks_page():
    return render_template("tasks.html")


# Test route
@app.route("/profile")
def profile_page():
    return render_template("profile.html")


# Get the User info
@app.route("/api/v1/getUserInfo", methods=["POST"])
def getUserInfo():
    currentTime = datetime.utcnow().strftime("%m-%d-%y")
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_doc = user_ref.get().to_dict()
    high_ref = user_ref.collection("scores").document(currentTime)
    high_score = 0
    
    # Get Scores
    scores_ref = db.collection("users").document(user_id)
    current_score_doc = scores_ref.get()
    user_ref = db.collection("users").document(user_id).get()

    if current_score_doc.exists:
        score_data = current_score_doc.to_dict()
        high_score = score_data.get("highscore", 0)

    user_name = user_doc.get("nickname", "Player")
    total_score = user_doc.get("totals", 0)
    dailyCheckin = user_doc.get("dailyCheckin", 0)

    return jsonify({
        "message": "Success",
        "data": {
            "total_score": total_score,
            "user_name": user_name,
            "high_score": high_score,
            "dailyCheckin": dailyCheckin,
            "picture": user_doc.get("picture", "")
        },
    })


# Init the Task Page
@app.route("/api/v1/getTaskStatus", methods=["POST"])
def getTaskStatus():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    task_ref = user_ref.collection("totals").document(
        "taskscore").get().to_dict()

    return jsonify({"message": "Success", "data": task_ref})


# Endpoint to get the leaderboard
@app.route("/api/v1/highscore_data", methods=["GET"])
def highscore_data():
    currentTime = datetime.utcnow().strftime("%m-%d-%y")
    highscoredata = []
    users_ref = db.collection("users")
    users = users_ref.get()

    for user in users:
        user_ref = user.to_dict()
        # Get Scores
        scores_ref = db.collection("users").document(
            user.id)
        current_score_doc = scores_ref.get()
        if current_score_doc.exists:
            score_data = current_score_doc.to_dict()
            highscoredata.append({
                "name": user_ref.get("nickname", "Player"),
                "user_id": user.id,
                "points": score_data.get("highscore", 0),
                "picture": user_ref.get("picture", "")
            })

    highscoredata = sorted(highscoredata,
                            key=lambda x: x["points"],
                            reverse=True)
    return jsonify(highscoredata)


# Endpoint to get the leaderboard
@app.route("/api/v1/totalscore_data", methods=["GET"])
def totalscore_data():

    if request.args.get("user_id"):
        user_id = request.args.get("user_id")
        user_ref = db.collection("users").document(user_id)
        user_data = user_ref.get().to_dict()
        total_data = user_data.get("totals", '')

        return {
            "name": user_data.get("nickname", "Player"),
            "total": total_data,
        }

    else:
        users_ref = db.collection("users")
        users = users_ref.get()
        totalScoredata = []

        for user in users:
            user_ref = user.to_dict()
            total_data = user_ref.get("totals", '')

            totalScoredata.append({
                "name": user_ref.get("nickname", "Player"),
                "user_id": user.id,
                "total": total_data,
                "picture": user_ref.get("picture", ""),
            })

        totalScoredata = sorted(totalScoredata,
                                key=lambda x: x["total"],
                                reverse=True)
        return jsonify(totalScoredata)


# Get FarmingTime
@app.route("/api/v1/farmingTime", methods=["GET"])
def farmingTime():
    if request.args.get("user_id"):
        user_id = str(request.args.get("user_id"))
        user_ref = db.collection("users").document(user_id)
        user_data = user_ref.get().to_dict()
        farmingTime = user_data.get("startFarming", '')

        if farmingTime == '':
            farmingTime = 0

    return (jsonify({"farmingTime": farmingTime}), 200)


# Get CurrentTime
@app.route("/api/v1/currentTime", methods=["GET"])
def currentTime():
    currentTime = int(datetime.utcnow().timestamp() * 1000)
    return (jsonify({"currentTime": currentTime}), 200)


# Invite the User
@app.route("/api/v2/invite", methods=["POST"])
def invite():
    try:
        user_id = str(request.json.get("user_id"))
        inviter_id = str(request.json.get("inviter_id"))

        # Get Scores
        user_ref = db.collection("users").document(inviter_id)
        user_doc = user_ref.get().to_dict()
        nick_name = user_doc.get("nickname", "")
        total_score = user_doc.get("totals", "")

        if nick_name == "":
            nick_name = user_doc.get("name", "")

        if db.collection("user").document(user_id) and inviter_id != user_id:
            task_ref = user_ref.collection("totals").document("taskscore")
            task_data = task_ref.get().to_dict()

            task_score = task_data.get("score", 0)
            inviteFriend = task_data.get("inviteFriend", 0)
            friendList = task_data.get("friendList", [])
    
            if inviteFriend < 10:
                if user_id not in friendList:
                    friendList.append(user_id)
                    inviteFriend += 1
                    task_score += 4000
                    total_score += 4000
 
                    task_ref.update({"inviteFriend": inviteFriend})
                    task_ref.update({"friendList": friendList})
                    task_ref.update({"score": task_score})

                    task_data.update({"totals": total_score})

                    return (jsonify({"message": "success", "nickname": nick_name}), 200)
                else: 
                    return (jsonify({"message": "Already added into the friendList"}), 201)
            else:
                return (jsonify({"message": "Already invited over 10 users."}), 201)
    except Exception as e:
        return (jsonify({"message": "failed"}), 400)


# Init the User Database
@app.route("/api/v2/initUser", methods=["POST"])
def initUser():
    current_time = datetime.utcnow().strftime("%m-%d-%y")
    user_id = request.json.get("user_id")
    user_name = request.json.get("user_name")
    picture = request.json.get("picture")

    if not user_id or not user_name or not picture:
        return jsonify({"message": "Missing required fields"}), 400

    user_id = str(user_id)
    user_name = str(user_name)

    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    if user_data is None:
        user_ref.set(
            {
                "name": user_name,
                "nickname": user_name,
                "picture": picture,
                "totals": 0,
                "dailyCheckin": 0,
                "last_reward": "",
                "startFarming": "",
                "highscore": 0,
            },
            merge=True,
        )

        total_ref = user_ref.collection("totals")
        score_ref = user_ref.collection("scores")
        highscore_doc = total_ref.document("highscore")
        dailyscore_doc = total_ref.document("dailyscore")
        farmingscore_doc = total_ref.document("farmingscore")

        taskscore_doc = total_ref.document("taskscore")
        score_doc = score_ref.document(current_time)

        score_doc.set({"score": 0}, merge=True)
        highscore_doc.set({"score": 0}, merge=True)
        dailyscore_doc.set({"score": 0}, merge=True)
        farmingscore_doc.set({"score": 0}, merge=True)
        taskscore_doc.set(
            {
                "learnAbout": False,
                "joinDiscord": False,
                "joinInstagram": False,
                "joinTikTok": False,
                "joinX": False,
                "followTelegram": False,
                "inviteFriend": 0,
                "score": 0,
                "friendList": [],
            },
            merge=True,
        )
    
    else:
        user_ref.update({"picture": picture})
        
    return jsonify({"message": "Success"})

# Learn about the triend app
@app.route("/api/v2/learnAbout", methods=["POST"])
def learnAbout():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    task_ref = user_ref.collection("totals").document("taskscore")
    task_data = task_ref.get().to_dict()
    learnAbout = task_data.get("learnAbout", False)

    if learnAbout != True:
        task_ref.update({"learnAbout": True})
        totals = user_data.get("totals", 0)
        task_total = task_data.get("score", 0)
        totals += 3500
        task_total += 3500

        user_ref.update({"totals": totals})
        task_ref.update({"score": task_total})

        return jsonify({"message": "Success"})
    return jsonify({"message": "Failed"})


# Learn about the triend app
@app.route("/api/v2/followTelegram", methods=["POST"])
def followTelegram():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    task_ref = user_ref.collection("totals").document("taskscore")
    task_data = task_ref.get().to_dict()
    followTelegram = task_data.get("followTelegram", False)

    if followTelegram != True:
        task_ref.update({"followTelegram": True})
        totals = user_data.get("totals", 0)
        task_total = task_data.get("score", 0)
        totals += 4000
        task_total += 4000

        user_ref.update({"totals": totals})
        task_ref.update({"score": task_total})

        return jsonify({"message": "Success"})
    return jsonify({"message": "Failed"})


# Learn about the followTeam
@app.route("/api/v2/joinDiscord", methods=["POST"])
def joinDiscord():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    task_ref = user_ref.collection("totals").document("taskscore")
    task_data = task_ref.get().to_dict()
    joinDiscord = task_data.get("joinDiscord", False)

    if joinDiscord != True:
        task_ref.update({"joinDiscord": True})
        totals = user_data.get("totals", 0)
        task_total = task_data.get("score", 0)
        totals += 3500
        task_total += 3500

        user_ref.update({"totals": totals})
        task_ref.update({"score": task_total})
        return jsonify({"message": "Success"})
    return jsonify({"message": "Failed"})


# Learn about the joinInstagram
@app.route("/api/v2/joinInstagram", methods=["POST"])
def joinInstagram():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    task_ref = user_ref.collection("totals").document("taskscore")
    task_data = task_ref.get().to_dict()
    joinInstagram = task_data.get("joinInstagram", False)

    if joinInstagram != True:
        task_ref.update({"joinInstagram": True})
        totals = user_data.get("totals", 0)
        task_total = task_data.get("score", 0)
        totals += 3500
        task_total += 3500

        user_ref.update({"totals": totals})
        task_ref.update({"score": task_total})
        return jsonify({"message": "Success"})
    return jsonify({"message": "Failed"})


# Learn about the joinInstagram
@app.route("/api/v2/joinTikTok", methods=["POST"])
def joinTikTok():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    task_ref = user_ref.collection("totals").document("taskscore")
    task_data = task_ref.get().to_dict()
    joinTikTok = task_data.get("joinTikTok", False)

    if joinTikTok != True:
        task_ref.update({"joinTikTok": True})
        totals = user_data.get("totals", 0)
        task_total = task_data.get("score", 0)
        totals += 3500
        task_total += 3500

        user_ref.update({"totals": totals})
        task_ref.update({"score": task_total})
        return jsonify({"message": "Success"})
    return jsonify({"message": "Failed"})


# Learn about the joinInstagram
@app.route("/api/v2/joinX", methods=["POST"])
def joinX():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    task_ref = user_ref.collection("totals").document("taskscore")
    task_data = task_ref.get().to_dict()
    joinX = task_data.get("joinX", False)

    if joinX != True:
        task_ref.update({"joinX": True})
        totals = user_data.get("totals", 0)
        task_total = task_data.get("score", 0)
        totals += 3500
        task_total += 3500

        user_ref.update({"totals": totals})
        task_ref.update({"score": task_total})
        return jsonify({"message": "Success"})
    return jsonify({"message": "Failed"})


# Daily Checkin
@app.route("/api/v2/dailyCheckin", methods=["POST"])
def dailyCheckin():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()
    dailyCheckin = user_data.get("dailyCheckin", 0)
    last_reward = user_data.get("last_reward", "")
    current_date = datetime.utcnow().date()
    claimable = False

    if last_reward != "":
        # Assuming last_reward is stored as a string in 'YYYY-MM-DD' format
        last_reward_date = convert_to_unix_timestamp(last_reward)
        date_diff = (current_date - last_reward_date.date()).days

        if date_diff == 1:
            dailyCheckin += 1
            claimable = True
        elif date_diff >= 2:
            dailyCheckin = 1
            claimable = True
            user_ref.update({"dailyCheckin": dailyCheckin})
    else:
        claimable = True

    return jsonify({
        "dailyCheckin": int(dailyCheckin),
        "claimable": claimable,
    })


# Daily CheckinClaim
@app.route("/api/v2/dailyClaim", methods=["POST"])
def dailyClaim():
    reward_array = [100, 200, 400, 800, 1600, 3200, 5000]
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()
    dailyCheckin = user_data.get("dailyCheckin", 0)
    last_reward = user_data.get("last_reward", "")

    total_ref = user_ref.collection("totals")
    total_score_doc = total_ref.document("dailyscore")
    total_data = total_score_doc.get().to_dict()
    daily_total_value = total_data.get("score", 0)
    current_date = datetime.utcnow().date()

    if last_reward != "":
        last_reward_date = convert_to_unix_timestamp(last_reward)
        date_diff = (current_date - last_reward_date.date()).days

        if date_diff < 1:
            return (jsonify({"message":
                             "failed to claim the daily checkin"}), 400)

        if date_diff > 6:
            dailyReward = 5000
    else:
        dailyReward = reward_array[dailyCheckin]

    dailyCheckin += 1
    user_ref.update({"dailyCheckin": dailyCheckin})
    user_ref.update(
        {"last_reward": datetime.utcnow().strftime("%m/%d/%y:%H-%M-%S")})

    daily_total_value += dailyReward
    total_score_doc.update({"score": daily_total_value})

    totals = user_data.get("totals", 0)
    totals += dailyReward
    user_ref.update({"totals": totals})
    return (jsonify({"message": "successfully checked for dailyReward"}), 200)


# farmingpoint start api
@app.route("/api/v2/farmingStart", methods=["POST"])
def farmingStart():
    currentTime = datetime.utcnow().strftime("%m/%d/%y:%H-%M-%S")
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_ref.set({"startFarming": currentTime}, merge=True)

    return (jsonify({"message": "start the farming!"}), 200)


# farmingClaim api
@app.route("/api/v2/farmingClaim", methods=["POST"])
def farmingClaim():
    user_id = str(request.json.get("user_id"))
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get().to_dict()

    total_ref = user_ref.collection("totals")
    total_score_doc = total_ref.document("farmingscore")
    total_data = total_score_doc.get().to_dict()
    farming_total_value = total_data.get("score", 0)
    startFarming = user_data.get("startFarming", '')

    # get the time difference
    currentTime = int(datetime.utcnow().timestamp() * 1000)
    oldTime = convert_to_unix_timestamp(startFarming)
    print("--------->oldTime", oldTime)

    if oldTime != 0:
        oldTime_timestamp = int(oldTime.timestamp() * 1000)
        time_diff = currentTime - oldTime_timestamp

        if time_diff > (6 * 3600 * 1000):
            # get total value & set the total value
            total_value = user_data.get("totals", 0)
            total_value += 1000
            farming_total_value += 1000
            total_score_doc.update({"score": farming_total_value})
            user_ref.update({"totals": total_value})
            user_ref.update({"startFarming": ''})

            return jsonify({"message": "Added the farming reward!", "total_val": total_value}), 200

    return jsonify({"message": "failed to add the farming reward!"}), 400


# farmingpoint API
@app.route("/api/v2/farmingPoint", methods=["POST"])
def farmingPoint():
    user_id = str(request.json.get("user_id"))
    name = request.json.get("name")
    add_point = request.json.get("point")

    # userlist creation
    user_ref = db.collection("users").document(user_id)
    user_ref.set({"name": name}, merge=True)

    farming_ref = user_ref.collection("farming")
    farming_ref.document().set({"point": add_point, "timestamp": currentTime})
    return (
        jsonify({
            "status": "success",
            "message": "Point updated",
        }),
        200,
    )


# Endpoint to update the score
@app.route("/api/v2/update_score", methods=["POST"])
def update_score():
    try:
        # get User data
        user_id = str(request.json.get("user_id"))
        score = request.json.get("score")
        currentTime = datetime.utcnow().strftime("%m-%d-%y")

        if not all([user_id, score]):
            return (
                jsonify({
                    "status": "error",
                    "message": "Missing required fields"
                }),
                400,
            )
        # userlist creation
        user_ref = db.collection("users").document(user_id)
        # get total score & scores data
        scores_ref = user_ref.collection("scores")
        user_data = user_ref.get().to_dict()

        total_ref = user_ref.collection("totals")
        total_score_doc = total_ref.document("highscore")
        total_data = total_score_doc.get().to_dict()
        highscore_current = user_ref.get().to_dict()
        highscore_total_value = total_data.get("score", 0)

        highscore_current_value = highscore_current.get("highscore", 0)
        total_value = user_data.get("totals", 0)
        current_score_doc = scores_ref.document(currentTime).get()

        # companre the score with high score
        if highscore_current_value < score:
            user_ref.update({"highscore": score})

        # update total score & scores data
        if not current_score_doc.exists:
            scores_ref.document(currentTime).set({"score": score})
            total_value += score
            highscore_total_value += score
            user_ref.update({"totals": total_value})
            total_score_doc.update({"score": highscore_total_value})
            # user_ref.set({"totals": total_value}, merge=True)
        else:
            current_score = current_score_doc.to_dict().get("score", 0)
            if score > current_score:
                scores_ref.document(currentTime).set({"score": score})
                total_value += score - current_score
                highscore_total_value += score - current_score
                user_ref.update({"totals": total_value})
                total_score_doc.update({"score": highscore_total_value})

        return (
            jsonify({
                "status": "success",
                "message": "Score updated and user data saved",
            }),
            200,
        )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Get the User info
@app.route("/api/v2/updateName", methods=["POST"])
def updateName():
    user_id = str(request.json.get("user_id"))
    name = request.json.get("name")
    user_ref = db.collection("users").document(user_id)
    user_ref.update({"nickname": name})

    return jsonify({"message": "Success"})


def convert_to_unix_timestamp(date_string):
    if date_string != '':
        date_part, time_part = date_string.split(':')
        month, day, year = map(int, date_part.split('/'))
        hours, minutes, seconds = map(int, time_part.split('-'))
    
        # Construct the datetime object
        date = datetime(year + 2000, month, day, hours, minutes, seconds)
    
        # Convert to Unix timestamp
        # unix_timestamp = int(date.timestamp()*1000)
    else:
        date = 0
    return date

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host="0.0.0.0", port=port)
