// daily_checkin js
const dailyLoginRewards = [100, 200, 400, 800, 1600, 3200, 5000];
async function dailyCheckIn() {
    const rewards_list = document.getElementsByClassName("reward");
    const claim_btn = document.getElementById("daily_claim");
    const rewards_div = document.getElementById("rewards");

    const response = await fetch(`${serverurl}/api/v2/dailyCheckin`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user_id })
    });

    const data = await response.json();
    const claimable = data.claimable;
    let checkinCount = data.dailyCheckin;
    if (checkinCount > 7) {
        const streak_img = document.createElement('img');
        streak_img.src = "../static/img/daily_reward.png";
        streak_img.classList.add("daily_reward");
        rewards_div.innerHTML = '';
        rewards_div.appendChild(streak_img);
        // console.log("--------->", rewards_div);
        // const rewards_streak = document.createElement('div');
        // rewards_streak.classList.add('rewards');
        
        // rewards_streak.appendChild(streak_img);
        
        // rewards_div.replaceWith = rewards_streak;
    }
    else {
        // delete the class
        for (let i = 0; i < rewards_list.length; i++) {
            rewards_list[i].classList.remove("current");
            rewards_list[i].classList.remove("past");
        }

        // add the class
        for (let i = 0; i < checkinCount; i++) {
            if (i == checkinCount - 1)
                rewards_list[i].classList.add("current");
            else
                rewards_list[i].classList.add("past");
        }
    }
    // disable the claimbutton
    if (claimable) {
        claim_btn.style.background = '#00FFCF';
        claim_btn.removeAttribute('disabled');
    } else {
        claim_btn.style.background = 'gray';
        claim_btn.setAttribute('disabled', 'disabled');
    }
}

async function dailyClaim() {
    const response = await fetch(`${serverurl}/api/v2/dailyClaim`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user_id })
    });

    await dailyCheckIn();
}

// function updateCheckinCount(count) {
//     document.getElementById('checkin-count').innerText = `Check-ins: ${count}`;
// }

function showModal() {
    document.getElementById('daily-checkin-modal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('daily-checkin-modal').style.display = 'none';
}