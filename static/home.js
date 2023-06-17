function functionabout(){
    window.location.href = "About.html";
}

function functionhome(){
    window.location.href = "Home.html";
}

function functiontest(){
    window.location.href = "Test.html";
}
function functionupload(){
    if ( fever_and_sweating.checked  || shivering_and_chills.checked  || discomfort.checked  || muscle_or_joint_pain.checked  || rapid_breathing.checked  || chest_and_abdominal_pain.checked  || rapid_heart_rate.checked  || cough.checked  || fatigue.checked  || headache.checked  || body_ache.checked  || nausea.checked  || vomiting.checked  || convulsion.checked  || jaundice.checked  || stooling.checked  || sore_throat.checked  || sneezing.checked  || earache.checked  || facial_pain.checked  || mouth_sore.checked  || stiff_neck.checked  || weakness.checked  || no_appetite.checked  ||  difficulty_breathing.checked  || rash.checked  || none.checked ){
        var vals = `fever_and_sweating=${ fever_and_sweating.checked}&shivering_and_chills=${ shivering_and_chills.checked}&discomfort=${ discomfort.checked}&muscle_or_joint_pain=${ muscle_or_joint_pain.checked}&rapid_breathing=${ rapid_breathing.checked}&chest_and_abdominal_pain=${ chest_and_abdominal_pain.checked}&rapid_heart_rate=${ rapid_heart_rate.checked}&cough=${ cough.checked}&fatigue=${ fatigue.checked}&headache=${ headache.checked}&body_ache=${ body_ache.checked}&nausea=${ nausea.checked}&vomiting=${ vomiting.checked}&convulsion=${ convulsion.checked}&jaundice=${ jaundice.checked}&stooling=${ stooling.checked}&sore_throat=${ sore_throat.checked}&sneezing=${ sneezing.checked}&earache=${ earache.checked}&facial_pain=${ facial_pain.checked}&mouth_sore=${ mouth_sore.checked}&stiff_neck=${ stiff_neck.checked}&weakness=${ weakness.checked}&no_appetite=${ no_appetite.checked}&difficulty_breathing=${ difficulty_breathing.checked}&rash=${ rash.checked}&none=${ none.checked}`.replaceAll("=", ":");
        document.cookie = `choices=${vals}`;
        var clickEvent = new MouseEvent("click", {
            "view": window,
            "bubbles": true,
            "cancelable": false
        });
        submit.dispatchEvent(clickEvent);
    } else {
        alert("Please select a symptom, or the 'none of the above' option.");
    }
 
}

