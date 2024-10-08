let serverurl = "https://triend-wenworldgame-05ef17649d0d.herokuapp.com";
const user = window.Telegram.WebApp.initDataUnsafe.user;
const user_id = user?.id;

async function init() {
  await fetch(`${serverurl}/api/v1/getTaskStatus`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user_id: user_id }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.data) {
        if (data.data.followTelegram) {
          document.getElementById("followTelegram").classList.remove("claim");
          document.getElementById("followTelegram").classList.add("claimed");
          document.getElementById("followTelegram").innerHTML = "claimed";
          // document.getElementById("followTelegram").onclick = "";
        }

        if (data.data.inviteFriend != null) {
          if (data.data.inviteFriend > 9) {
            document.getElementById("inviteFriend").classList.remove("claim");
            document.getElementById("inviteFriend").classList.add("claimed");
            document.getElementById("inviteFriend").innerHTML = "claimed";
            // document.getElementById("inviteFriend").onclick = "";
          }

          document.getElementById("inviteText").innerHTML = `${
            10 - data.data.inviteFriend
          } / 10`;
        }

        if (data.data.joinDiscord) {
          document.getElementById("joinDiscord").classList.remove("claim");
          document.getElementById("joinDiscord").classList.add("claimed");
          document.getElementById("joinDiscord").innerHTML = "claimed";
          // document.getElementById("joinDiscord").onclick = "";
        }

        if (data.data.joinInstagram) {
          document.getElementById("joinInstagram").classList.remove("claim");
          document.getElementById("joinInstagram").classList.add("claimed");
          document.getElementById("joinInstagram").innerHTML = "claimed";
          // document.getElementById("joinInstagram").onclick = "";
        }

        if (data.data.joinTikTok) {
          document.getElementById("joinTikTok").classList.remove("claim");
          document.getElementById("joinTikTok").classList.add("claimed");
          document.getElementById("joinTikTok").innerHTML = "claimed";
          // document.getElementById("joinTikTok").onclick = "";
        }

        if (data.data.joinX) {
          document.getElementById("joinX").classList.remove("claim");
          document.getElementById("joinX").classList.add("claimed");
          document.getElementById("joinX").innerHTML = "claimed";
          // document.getElementById("joinX").onclick = "";
        }

        if (data.data.learnAbout) {
          document.getElementById("learnAbout").classList.remove("claim");
          document.getElementById("learnAbout").classList.add("claimed");
          document.getElementById("learnAbout").innerHTML = "claimed";
          // document.getElementById("learnAbout").onclick = "";
        }
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

async function inviteFriend() {
  const text = `🚀 Get in on This! 🚀

I'm hooked on this WenWorld game! Navigate the market, grab Wen Coins, and dodge Sammy and the Bear. Verified coins keep it legit, but the risky ones are where the thrill’s at.

Every coin is Triend-verified for trust. High scores and airdrop points up for grabs!

Join the community and let’s see who can top the leaderboard! 🎮💰`;

  const encodedText = encodeURIComponent(text);
  window.open(
    `https://t.me/share/url?url=https://t.me/wen_worldbot?start=${user_id}&text=${encodedText}`
  );
}

async function learnClick() {
  window.open("https://triend.gitbook.io/triend-docs-and-litepaper", "_blank");
  if (document.getElementById("learnAbout").classList.contains("claimed")) {
    document.getElementById("learnAbout").innerHTML = "claim";
    document.getElementById("learnAbout").classList.add("claim");
    document.getElementById("learnAbout").onclick = init;

    await fetch(`${serverurl}/api/v2/learnAbout`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: user_id }),
    });
  }
}

async function followTelegram() {
  window.open("https://t.me/triendapp", "_blank");
  if (
    !document.getElementById("followTelegram").classList.contains("claimed")
  ) {
    document.getElementById("followTelegram").innerHTML = "claim";
    document.getElementById("followTelegram").classList.add("claim");
    document.getElementById("followTelegram").onclick = init;
    await fetch(`${serverurl}/api/v2/followTelegram`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: user_id }),
    });
  }
}

async function joinX() {
  window.open("https://x.com/triendapp", "_blank");
  if (!document.getElementById("joinX").classList.contains("claimed")) {
    document.getElementById("joinX").innerHTML = "claim";
    document.getElementById("joinX").classList.add("claim");
    document.getElementById("joinX").onclick = init;

    await fetch(`${serverurl}/api/v2/joinX`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: user_id }),
    });
  }
}

async function joinTikTok() {
  window.open("https://www.tiktok.com/@triendapp", "_blank");
  if (!document.getElementById("joinTikTok").classList.contains("claimed")) {
    document.getElementById("joinTikTok").innerHTML = "claim";
    document.getElementById("joinTikTok").classList.add("claim");
    document.getElementById("joinTikTok").onclick = init;

    await fetch(`${serverurl}/api/v2/joinTikTok`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: user_id }),
    });
  }
}

async function joinInstagram() {
  window.open("https://www.instagram.com/triend.app/?hl=en", "_blank");
  if (!document.getElementById("joinInstagram").classList.contains("claimed")) {
    document.getElementById("joinInstagram").innerHTML = "claim";
    document.getElementById("joinInstagram").classList.add("claim");
    document.getElementById("joinInstagram").onclick = init;

    await fetch(`${serverurl}/api/v2/joinInstagram`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: user_id }),
    });
  }
}

async function joinDiscord() {
  window.open("https://discord.gg/XZPwtfZjWq", "_blank");
  if (!document.getElementById("joinDiscord").classList.contains("claimed")) {
    document.getElementById("joinDiscord").innerHTML = "claim";
    document.getElementById("joinDiscord").classList.add("claim");
    document.getElementById("joinDiscord").onclick = init;

    await fetch(`${serverurl}/api/v2/joinDiscord`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: user_id }),
    });
  }
}

document.addEventListener("DOMContentLoaded", async (event) => {
  if (window.Telegram.WebApp) {
    Telegram.WebApp.ready();
    init();
  }

  const taskCards = document.querySelectorAll(".task");

  taskCards.forEach(function (taskCard) {
    taskCard.addEventListener("touchstart", function () {
      taskCard.classList.add("selected");
    });

    taskCard.addEventListener("touchend", function () {
      taskCard.classList.remove("selected");
    });
  });
});
