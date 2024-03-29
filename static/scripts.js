const affirmations = [
    "You got this",
    "You'll figure it out",
    "You're a smart cookie",
    "I believe in you",
    "Sucking at something is the first step towards being good at something",
    "Struggling is part of learning",
    "Everything has cracks - that's how the light gets in",
    "Mistakes don't make you less capable",
    "We are all works in progress",
    "You are a capable human",
    "You know more than you think",
    "10x engineers are a myth",
    "If everything was easy you'd be bored",
    "I admire you for taking this on",
    "You're resourceful and clever",
    "You'll find a way",
    "I know you'll sort it out",
    "Struggling means you're learning",
    "You're doing a great job",
    "It'll feel magical when it's working",
    "I'm rooting for you",
    "Your mind is full of brilliant ideas",
    "You make a difference in the world by simply existing in it",
    "You are learning valuable lessons from yourself every day",
    "You are worthy and deserving of respect",
    "You know more than you knew yesterday",
    "You're an inspiration",
    "Your life is already a miracle of chance waiting for you to shape its destiny",
    "Your life is about to be incredible",
    "Nothing is impossible. The word itself says 'I’m possible!'",
    "Failure is just another way to learn how to do something right",
    "I give myself permission to do what is right for me",
    "You can do it",
    "It is not a sprint, it is a marathon. One step at a time",
    "Success is the progressive realization of a worthy goal",
    "People with goals succeed because they know where they’re going",
    "All you need is the plan, the roadmap, and the courage to press on to your destination",
    "The opposite of courage in our society is not cowardice... it is conformity",
    "Whenever we’re afraid, it’s because we don’t know enough. If we understood enough, we would never be afraid",
    "The past does not equal the future",
    "The path to success is to take massive, determined action",
    "It’s what you practice in private that you will be rewarded for in public",
    "Small progress is still progress",
    "Don't worry if you find flaws in your past creations, it's because you've evolved",
    "Starting is the most difficult step - but you can do it",
    "Don't forget to enjoy the journey",
    "It's not a mistake, it's a learning opportunity",
];

var isDay = false;
var darkMode = false;

function goDark(setInMemory = false) {
    var bodyElement = document.body;
    bodyElement.classList.toggle("dark-mode");

    var footerElement = document.getElementById("mainBodyDiv");
    footerElement.classList.toggle("dark-mode");

    var footerElement = document.getElementById("footerMaster");
    footerElement.classList.toggle("dark-mode");

    var affirmationElement = document.getElementById("affirmationBox");
    affirmationElement.classList.toggle("dark-mode");

    var siteNavElement = document.getElementById("siteNav");
    siteNavElement.classList.toggle("dark-mode");

    if (setInMemory == true) {
        if (affirmationElement.classList.contains("dark-mode")) {
            darkMode = true;
        } else {
            darkMode = false;
        }
        localStorage.setItem("darkMode", JSON.stringify(darkMode));
        localStorage.setItem("manualSetting", JSON.stringify(true));
    }
}

// alright so I've forgotten a major amount of the work I did here
// so, I might try to document it once I go through all the code
// (and get it working too, obvsly)

function checkStorageForConfig() {
    if (typeof (Storage) !== "undefined") {
        // Code for checking localStorage/sessionStorage availability.
        var configDarkMode = JSON.parse(localStorage.getItem("darkMode"));
        var configManualSetting = JSON.parse(localStorage.getItem("manualSetting"));

        // logging it here
        console.table(
            {
                'configDarkMode': configDarkMode,
                'configManualSetting': configManualSetting,
                'darkMode': darkMode
            }
        )

        if (configManualSetting == true) {
            if (configDarkMode != darkMode) {
                goDark();
                toggleButton = document.getElementById("goDarkToggle");
                toggleButton.checked = true;
                localStorage.setItem("darkMode", true);
                localStorage.setItem("lastCheckAtDay", true);
                localStorage.setItem("manualSetting", true);
            }
        } else {
            // Sorry! No Web Storage support..
            darkModeCheck();
        }

    } else {
        // Sorry! No Web Storage support..
        darkModeCheck();
    }
}

function darkModeCheck() {
    var now = new Date();
    hours = now.getHours();
    if (hours < 7 || hours > 19) {
        goDark();
        isDay = false
        toggleButton = document.getElementById("goDarkToggle");
        toggleButton.checked = true;
        localStorage.setItem("darkMode", true);
        localStorage.setItem("lastCheckAtDay", false);
        localStorage.setItem("manualSetting", false);
    } else {
        localStorage.setItem("darkMode", false);
        localStorage.setItem("lastCheckAtDay", true);
        localStorage.setItem("manualSetting", false);
    }
}

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

function setAffirmation() {
    affirmationIndex = affirmations.length;
    affirmationText = affirmations[getRandomInt(affirmationIndex)];
    // console.log(affirmationText);
    document.getElementById("affirmationBox").innerText = affirmationText
}

function initPage() {
    checkStorageForConfig();
    setAffirmation();
    // darkModeCheck();
}